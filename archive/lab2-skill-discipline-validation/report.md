# Lab 2: Skill Discipline Validation Report

**Date:** 2026-03-29
**Skill version:** v1.4.3
**Test agent model:** Claude Sonnet 4.6 (tests 1/2/3/5), Claude Opus 4.6 (test 4)
**Evaluator model:** Claude Haiku 4.5 (test 4 evaluators)

## Summary

5 synthetic tests validating researcher.md mechanics. **22 of 33 checkpoints passed, 5 partial, 3 failed, 3 N/A.**

| Result | Count |
|--------|-------|
| PASS | 22 |
| PARTIAL | 5 |
| FAIL | 3 |
| N/A | 3 |

### Overall Assessment

The skill's core mechanics (commit-before-run, log-before-reset, .lab/ structure, branching, experiment numbering) are well-followed. The main failures are around **guardrail enforcement** — specifically the 3/5-discard streak guardrails and explicit THINK documentation. Agents follow the research process effectively but sometimes skip the "stop and reflect" discipline when they feel productive.

---

## Test 1: Black-Box Parameter Optimization

**Agent:** Sonnet subagent | **Budget:** 20 experiments | **Result:** 67.13 → 89.50 (+33.3%)

The agent efficiently discovered the optimal configuration (A=100, B=100, C=42, D≈30-, E=55) including the D-trap and D-E interaction bonus. Explored float precision near boundaries.

| # | Checkpoint | Result | Notes |
|---|-----------|--------|-------|
| 1 | Structured commits (before running) | **PASS** | All experiments use `experiment #N:` format with branch/parent/hypothesis |
| 2 | Log before reset | **PASS** | All discards have log entries with SHAs before reset |
| 3 | Discard → reset | **PASS** | Only keeps visible in `git log --oneline`, discarded SHAs in results.tsv |
| 4 | 3+ discard guardrail | **FAIL** | 6 consecutive discards (#10-#15). No documented THINK pause or guardrail entry in log |
| 5 | 5+ discard guardrail | **FAIL** | No fork despite 6 consecutive discards. Agent continued on same branch, eventually found float optimization |
| 6 | Plateau 8+ guardrail | N/A | Best improved within 8 experiments (89.35→89.485 at exp #16) |
| 7 | Re-validation every 10th | **PASS** | Re-validation between #9 and #10 (correct timing). No #20 re-validation but it was the final experiment |
| 8 | THINK checklist | **FAIL** | No explicit THINK blocks with untested-assumptions analysis. Log has "Insight" lines but no structured checklist |
| 9 | Global experiment numbering | **PASS** | Sequential 0-20, no gaps, no resets |
| 10 | .lab/ structure complete | **PASS** | All files: config.md, results.tsv, log.md, branches.md, parking-lot.md, workspace/ |
| 11 | No self-imposed early termination | **PASS** | All 20 experiments completed |

---

## Test 2: Two-Peak Optimization (Forces Forking)

**Agent:** Sonnet subagent | **Budget:** 25 experiments | **Result:** 22.85 → 95.0 (+315%)

The agent found peak 2 (95.0) at experiment #1 by trying low values immediately. Then spent remaining experiments confirming no better solution exists. Created 4 branches. Note: test design didn't force the intended "find peak 1 first, stagnate, fork" pattern because the agent tried low values before high values.

| # | Checkpoint | Result | Notes |
|---|-----------|--------|-------|
| 12 | Fork mechanics | **PASS** | 4 branches: two-peak-optimization, peak2-fine-tuning, grid-sampling, inverted-assumptions |
| 13 | Strategy diversification (assumptions list) | **PARTIAL** | Assumptions documented before inverted-assumptions fork ("plateau guardrail triggered"). Not documented before peak2-fine-tuning fork |
| 14 | Fork from baseline | **PASS** | grid-sampling and inverted-assumptions both forked from baseline (#0) |
| 15 | Mandatory inversion | **PARTIAL** | inverted-assumptions branch tries unusual combinations but doesn't articulate a specific inverted assumption. More "random exploration" than "inversion" |
| 16 | Branch naming (strategy, not parameter) | **PASS** | Descriptive names: peak2-fine-tuning, grid-sampling, inverted-assumptions |
| 17 | branches.md updated | **PASS** | All 4 branches registered with forked-from info and status |
| 18 | Global numbering across branches | **PASS** | Sequential 0-21, no repeats across branches |
| 19 | Discovered both peaks | **PASS** | Peak 2: 95.0 (exp #1), Peak 1: 70.0 (exp #3) |
| — | Re-validation at #10 | **PASS** | Confirmed 95.0 still best |
| — | Re-validation at #20 | **PASS** | Confirmed 95.0 still best |
| — | Plateau guardrail | **PASS** | Triggered at 14+ experiments with unchanged best, correctly documented |
| — | 6-discard guardrail (exps 2-7) | **PASS** | Fork to peak2-fine-tuning after 6 discards |

---

## Test 3: Code Optimization (Domain-Agnostic THINK)

**Agent:** Sonnet subagent | **Budget:** 15 experiments | **Result:** 7.68 → 10000.0 (1300x speedup, trial division → sieve)

Agent replaced O(n²) trial division with Sieve of Eratosthenes, then optimized through odd-only sieve, count optimization, and module-level allocation. Final: ~10.3µs for counting primes up to 10000.

| # | Checkpoint | Result | Notes |
|---|-----------|--------|-------|
| 20 | THINK without variable/direction | **PASS** | Log discusses algorithmic approaches (sieve, odd-only, bytearray, wheel factorization) — no numeric parameter framing |
| 21 | Structured commits on code changes | **PARTIAL** | Experiments 1-6, 9, 15 have proper commits. Experiments 7, 8, 11-14 show "(none)" — tested without committing. Agent treated these as lab-only experiments, but they modify tracked files |
| 22 | Keep/discard on performance | **PASS** | Keeps show improving secondary metric (130ms → 55µs → 37µs → 16µs → 12µs → 10.3µs) |
| 23 | Correctness preserved | **PASS** | All keeps return 1229 (verified by benchmark assertion) |
| — | Re-validation at #10 | **PASS** | "RE-VALIDATION: exp #5 confirmed correct and stable" |
| — | Crash handling | **PASS** | Exp #8 (wheel sieve) detected as crash (wrong result 1232), correctly classified |

---

## Test 4: Qualitative Evaluation (Multi-Evaluator Protocol)

**Agent:** Opus (main session) | **Budget:** 10 experiments | **Result:** 7.10 → 9.00 (+26.8%)

Improved payment error message from verbose technical jargon to concise conversational format. Key finding: "we're happy to help" is load-bearing for tone dimension.

| # | Checkpoint | Result | Notes |
|---|-----------|--------|-------|
| 24 | 3 evaluators per experiment | **PASS** | 3 haiku subagents spawned for every experiment (baseline + 9 real) |
| 25 | Evaluators receive only artifact + rubric | **PASS** | Prompts contained only message text + rubric — no hypothesis, experiment number, or context |
| 26 | Scores show variance | **PARTIAL** | Most experiments show identical scores (e.g., all 9.00). Variance seen in exp #4 (9.00/8.70/8.90), #7 (8.80/9.00/8.70), #8 (9.00/8.70/8.80) |
| 27 | Median aggregation | **PASS** | Median used consistently in results.tsv |
| 28 | Divergence flagging | **PASS** | Checked for >20% scale divergence on each experiment, none needed flagging |
| — | 3-discard guardrail | **PASS** | Documented after exp #5 (3rd consecutive discard) with convergence analysis |
| — | 5-discard guardrail → fork | **PASS** | Fork triggered after exp #8 with assumptions list, forked from baseline, inverted conversational→formal |
| — | Strategy diversification | **PASS** | 5 assumptions listed, fork from baseline (#0), formal structure as inversion |
| — | Re-validation at #10 | **PASS** | Confirmed 9.00 with 3 fresh evaluators |

---

## Test 5: Crash Handling

**Agent:** Sonnet subagent | **Budget:** 20 experiments | **Result:** 75.25 → 97.49 (+29.5%)

Agent encountered 1 crash at experiment #1 (hash-based segfault), quickly adapted by using float parameters to avoid crash conditions. Clever use of D=50.1, E=94.9499 to maximize while staying under crash thresholds.

| # | Checkpoint | Result | Notes |
|---|-----------|--------|-------|
| 29 | Crash detection | **PASS** | Exp #1 correctly detected as crash (exit code 139) |
| 30 | Revert on crash | **PASS** | `git reset --hard HEAD~1` performed, SHA recorded in results.tsv |
| 31 | Trivial vs fundamental classification | **PARTIAL** | Classified as "fundamental, unpredictable" — correct for hash-based crash. But only 1 crash triggered, so limited data |
| 32 | 3+ crashes → rethink | N/A | Only 1 crash — agent learned to avoid crash conditions immediately |
| 33 | Crash metric logged as 0 | **PASS** | Crash row shows metric = 0.0 |
| — | Re-validation at #10 | **PASS** | Confirmed best config still scores 97.487475 |

**Test design note:** The crash conditions were too easy to avoid. The agent side-stepped the >95 crash by using 94.9x values and the all-even crash by using float values. The hash-based 15% crash only triggered once. Future tests should make crashes harder to circumvent (e.g., crash on specific value ranges, not just boundaries).

---

## Comparison with Lab 1

Lab 1 (`archive/lab1-skill-discipline-validation/`) was a qualitative self-improvement of researcher.md, not a discipline validation. The two labs test different things and aren't directly comparable. However:

- **Lab 1 showed:** The skill can guide qualitative improvement (6.25 → 9.23)
- **Lab 2 shows:** Agents follow the skill's mechanics well (67% pass rate) but skip guardrails when they feel productive

---

## Key Findings

### What works well
1. **Core commit/log/reset discipline** — followed consistently across all 5 tests
2. **Branching and experiment numbering** — global numbering, branch registry, fork mechanics all work
3. **Multi-evaluator protocol** — 3 evaluators, median aggregation, divergence checking all followed correctly
4. **Re-validation at every 10th** — consistently triggered across all tests
5. **Crash handling basics** — detection, classification, revert all work

### What needs improvement
1. **3/5-discard guardrails** — Test 1 had 6 consecutive discards with no pause or fork. The agent was making progress on a different axis (float precision) so it felt justified, but the guardrail is supposed to force a stop-and-reflect regardless.
2. **Explicit THINK blocks** — Test 1 agent logged insights but never did a structured THINK with assumptions checklist. The checklist is supposed to be a forcing function for questioning assumptions.
3. **Commit before run for code experiments** — Test 3 agent treated many code changes as "lab-only" by testing without committing. The skill says commit before running for repo-file experiments.
4. **Strategy diversification rigor** — Test 2's "inverted-assumptions" branch was more random exploration than principled inversion. The assumptions list was brief and the inversions weren't clearly tied to specific assumptions.
5. **Test design gap** — Test 2's two-peak scorer was solved on experiment #1, defeating the purpose of testing stagnation→fork→discovery. Test 5's crash conditions were too easy to sidestep.

### Recommendations for skill updates
1. **Strengthen guardrail language** — The 3/5-discard rules say "STOP" and "fork is the default" but agents skip them when they feel productive. Consider making the log entry format mandatory (e.g., "## 3-Discard Guardrail Check" heading required).
2. **Make THINK checklist output mandatory** — Require a specific heading (e.g., "## THINK — Experiment N") with required subheadings for assumptions, inversions, and convergence signals.
3. **Clarify lab-only vs repo-file boundary** — The distinction is clear conceptually but agents exploit it to skip commits. Consider adding: "If you modify a file in scope, it's a repo-file experiment — commit first."

### Recommendations for test improvements
1. **Test 2 (two-peak):** Start the initial config at high values (A=80, B=80, ...) so the agent naturally finds peak 1 first. Add more valley penalty to prevent random exploration from finding peak 2 early.
2. **Test 5 (crash):** Add crash conditions in value ranges (e.g., 40<A<60 crashes), not just boundaries. Make crashes unavoidable for certain parameter regions, forcing the agent to work around them.
3. **Add Test 6:** Long-running test (50+ experiments) to properly test plateau detection and multiple fork cycles.
