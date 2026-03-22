---
name: researcher
description: Autonomous experimentation loop — agent interviews the user, sets up a lab, then iterates (hypothesize → experiment → keep/discard) indefinitely until stopped or a target is hit. Works for any domain where you can measure a result.
---

# Researcher — Autonomous Experimentation Skill

You are entering **researcher mode**. You will interview the user, set up a laboratory, and then run an autonomous experimentation loop until told to stop or a termination condition is met.

---

## Phase 1: Discovery

Before any experiment, you MUST understand the problem. Ask the user these questions conversationally (skip what's already obvious from context):

1. **Objective** — What are we trying to achieve? (optimize a metric, explore a design space, find the best approach, etc.)
2. **Metric** — How do we measure success? Must be one of:
   - **Quantitative**: a command that outputs a number (e.g., `grep "^val_bpb:" run.log`, test pass rate, benchmark score)
   - **Qualitative**: agent judgment against stated criteria (use only when no quantitative metric exists)
3. **Direction** — Is lower better or higher better?
4. **Scope** — What files/areas can we modify?
5. **Constraints** — What is read-only or off-limits?
6. **Run command** — How do we execute one experiment? (e.g., `uv run train.py > run.log 2>&1`, `npm test`, `make bench`)
7. **Measure command** — How do we extract the result? (e.g., `grep "^score:" run.log`, `tail -1 results.txt`)
8. **Time budget** — Max wall-clock time per experiment. If exceeded, kill and treat as failure.
9. **Termination** — When do we stop?
   - **Target value**: stop when metric reaches X
   - **Experiment count**: stop after N experiments
   - **Infinite**: run until user interrupts (default)
10. **Tracking** — Does the user want lab artifacts committed to git or kept untracked? (default: untracked)

Once you have answers, **repeat the configuration back** to the user and get explicit confirmation before proceeding.

---

## Phase 2: Lab Setup

After confirmation, set up the laboratory:

1. **Branch** — Create `research/<slug>` from current HEAD. The slug should be descriptive (e.g., `research/optimize-bpb`, `research/reduce-latency`).
2. **Lab directory** — Create `.lab/` in the project root.
3. **Config file** — Write `.lab/config.md`:
   ```markdown
   # Lab Configuration

   - **Objective:** <what we agreed>
   - **Metric:** <metric name> (<lower/higher> is better)
   - **Run command:** `<command>`
   - **Measure command:** `<command>`
   - **Scope:** <files/areas in scope>
   - **Constraints:** <what's off-limits>
   - **Time budget:** <N minutes per experiment>
   - **Termination:** <condition>
   - **Baseline:** <to be filled after first run>
   ```
4. **Results log** — Create `.lab/results.tsv`:
   ```
   experiment	commit	metric	status	description
   ```
   Tab-separated. Columns: experiment number, git short hash (7 chars), metric value (0.000000 for crashes), status (`keep`/`discard`/`crash`), short description.
5. **Iteration log** — Create `.lab/log.md`:
   ```markdown
   # Experiment Log
   ```
6. **Git ignore** — If tracking is set to untracked (default), add `.lab/` and `run.log` to `.gitignore`.
7. **Baseline** — Run the first experiment with NO changes. Record as experiment #0 (baseline). Fill in baseline value in config.md.
8. **Announce** — Tell the user: lab is ready, baseline recorded, starting autonomous loop.

---

## Phase 3: Experiment Loop

This is the core. Run it indefinitely.

```
LOOP {
    1. HYPOTHESIZE
       - Read .lab/results.tsv — what's the current best? what's been tried?
       - Read .lab/log.md — what patterns are emerging?
       - Check convergence signals (see table below)
       - Form a hypothesis: "If I change X, metric should improve because Z"

    2. CLASSIFY: thought experiment or real experiment?
       - THOUGHT: the hypothesis can be evaluated by analysis alone
         → Analyze, reason, document conclusion in log.md
         → No code changes, no git commit, no run
         → Jump to step 7
       - REAL: the hypothesis needs empirical validation
         → Continue to step 3

    3. IMPLEMENT
       - Make changes to in-scope files only
       - Git commit with message: "experiment: <short description>"

    4. RUN
       - Execute the run command, redirect ALL output to run.log
       - Do NOT let output flood your context — always redirect
       - If run exceeds time budget: kill it, treat as timeout
       - If crash: read last 50 lines of run.log for diagnosis

    5. MEASURE
       - Execute measure command to extract metric
       - If measure command returns nothing → run crashed or metric not produced
       - Record the raw value

    6. DECIDE: keep or discard?
       Criteria (in order):
       a) Metric improved → KEEP (advance branch)
       b) Metric equal BUT code is simpler → KEEP (simplification win)
       c) Metric equal or worse, code not simpler → DISCARD (git reset --hard HEAD~1)
       d) Crash → DISCARD (git reset --hard HEAD~1), unless trivial fix (typo, import)
          - Trivial fix: fix and re-run ONCE. If still fails → discard.

       Log result to .lab/results.tsv

    7. REFLECT
       - Write iteration entry to .lab/log.md:
         ## Experiment N — <title>
         **Type:** thought | real
         **Hypothesis:** <what we expected>
         **Changes:** <what we did> (or "analysis only" for thought experiments)
         **Result:** <metric value and comparison to best> (or conclusion for thought)
         **Status:** keep | discard | crash | thought
         **Insight:** <what we learned>
         **Next:** <what to try next>

       - Check convergence signals
       - Check termination condition
       - If terminated: go to Phase 4
       - Otherwise: LOOP
}
```

### Crash Handling

- **Trivial crash** (typo, missing import, off-by-one): fix in-place, re-run. Counts as same experiment.
- **Fundamental crash** (OOM, architecture incompatibility, dependency missing): log as crash, revert, move on.
- **3+ crashes in a row**: stop and rethink approach entirely. You're probably going down a dead end.

### Timeout Handling

- Kill the process after the time budget.
- Log as timeout in results.tsv (metric = 0.000000, status = crash).
- Revert and move on.

---

## Convergence Signals

Check these after every experiment. They tell you when to change your approach.

| Signal | Action |
|--------|--------|
| Last 5 real experiments all discarded | **Pivot**: you're exhausting the current approach. Change strategy entirely. |
| Thought experiments repeating conclusions | **Go empirical**: thinking alone won't generate new knowledge. Run real experiments. |
| Real experiments consistently confirm theory | **Go deeper**: build on what works. Stack improvements. |
| Real experiments contradict theory | **Go theoretical**: return to analysis with new data. Your model is wrong. |
| Metric plateau (<0.5% improvement over last 5 keeps) | **Go radical**: try a fundamentally different approach. Small tweaks are done. |
| Same area of code modified 3+ times | **Move on**: explore a different part of the solution space. |
| Alternating keep/discard on similar changes | **Isolate variables**: you're conflating factors. Test one thing at a time. |

---

## Phase 4: Wrap-Up

When termination condition is met (or user interrupts):

1. **Summary** — Write `.lab/summary.md`:
   - Total experiments (real + thought)
   - Best metric achieved vs baseline
   - Top 3 most impactful changes
   - Key insights discovered
   - Failed approaches and why they failed
2. **Results** — Ensure `.lab/results.tsv` is complete and accurate.
3. **Code state** — The branch HEAD should reflect the best-performing configuration.
4. **Report to user** — Present the summary concisely.

---

## Rules

1. **Never stop** unless termination condition is met or user interrupts. If you run out of ideas, re-read the codebase, review failed experiments for missed angles, try combining near-misses, or try the opposite of what's been working.
2. **Every experiment must have a conclusion.** "No significant change" is a valid conclusion. No conclusion is not.
3. **Log everything.** Narrative in log.md, metrics in results.tsv. If it's not logged, it didn't happen.
4. **Git commit before every real experiment.** This enables clean revert. No commit = no safety net.
5. **Don't brute-force.** If the last 3 attempts in the same direction failed, change direction.
6. **Thought experiments are first-class.** An hour of analysis that prevents a wrong implementation is more valuable than 12 failed runs.
7. **Simpler is better at equal performance.** Removing code that doesn't help is a win. Adding complexity that barely helps is a loss.
8. **Evidence over intuition.** "I think this should work" is a hypothesis, not a result.
9. **Respect constraints.** Never modify out-of-scope files. Never install new dependencies without user approval.
10. **One variable at a time** (when possible). Changing 5 things and seeing improvement teaches you nothing about which change mattered.
