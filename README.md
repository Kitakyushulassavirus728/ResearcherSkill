# researcher-skill

An autonomous experimentation skill for AI coding agents. The agent interviews you, sets up a lab, then researches freely — thinking, testing, reflecting — until it hits a target or you tell it to stop.

Works for optimization, exploration, and everything in between. You observe, it researches.

## What it does

```
Resume ──→ Discovery ──→ Lab Setup ──→ Autonomous Research ──→ Summary
(pick up    (interview)   (branch,       ┌─────────────────┐    (best result,
 where                     .lab/,        │ THINK → TEST →  │     insights,
 left off)                 baseline)     │ REFLECT → loop  │     failed paths)
                                         └─────────────────┘
```

**Phase 0 — Resume.** If a `.lab/` directory exists, the agent reads the state, presents a summary, and asks whether to resume or start fresh.

**Phase 1 — Discovery.** The agent asks what you're exploring, how to measure progress (quantitative or qualitative), what's in scope, wall-clock budget per experiment, and when to stop. Sensible defaults reduce friction.

**Phase 2 — Lab Setup.** Creates a git branch, a `.lab/` directory with config, results log, iteration log, branch registry, and parking lot. Runs a baseline. `.lab/` is untracked and sacred — it survives all git operations.

**Phase 3 — Autonomous Research.** The core. The agent works freely in a think → test → reflect rhythm, deciding how long to stay in each phase and when to transition. It can fork branches to explore divergent approaches, learn across branches, and combine wins. Execution discipline is enforced (commit before, measure after, log always) but navigation is completely free. The agent has full autonomy — it doesn't come back to you unless a scope violation is unavoidable or it has truly exhausted all directions.

**Phase 4 — Wrap-up.** Summary of what worked, what didn't, branch history, and experiment genealogy. Code reflects the global best.

## Key features

- **Complete autonomy** — agent doesn't interrupt you; logs everything, you observe when you want
- **Free-form exploration** — think → test → reflect rhythm, not a rigid step-by-step loop
- **Execution discipline** — commit before, measure after, log always, revert on discard — non-negotiable
- **Non-linear branching** — fork branches to explore divergent approaches, learn across branches, combine wins
- **Sacred `.lab/`** — untracked local directory survives all git operations, holds complete history across all branches
- **Session resume** — interrupted conversations pick up where they left off
- **Multi-metric** — primary metric drives decisions, secondary metrics provide context
- **Quantitative and qualitative** — works with hard metrics or agent-judged rubrics
- **`interesting` status** — not everything is keep/discard; results that open new directions get their own status
- **10 hypothesis strategies** — reference tools when stuck, not a menu you must pick from
- **Convergence signals** — patterns that suggest something needs to change, without dictating what
- **Parking lot** — ideas captured mid-experiment, picked up when stuck
- **Re-validation** — periodic drift detection
- **Noise threshold** — 0.1% floor distinguishes signal from noise
- **Persistence by design** — agent is explicitly instructed to keep going when stuck, with concrete recovery actions
- **LLM compliance design** — critical rules at start/end (primacy/recency), semantic XML hierarchy (`<critical>` for mandatory rules, `<reference>` for consult-when-needed material), positive framing, drift re-injection in THINK phase

## How it differs from autoresearch

[autoresearch](https://github.com/karpathy/autoresearch) by Karpathy is a brilliant setup for ML training optimization: one file, one metric, fixed time budget. This skill generalizes that idea:

| | autoresearch | researcher-skill |
|---|---|---|
| Domain | ML training (val_bpb) | Anything measurable or evaluable |
| Autonomy | Agent follows rigid loop | Agent navigates freely, discipline on execution only |
| Setup | Pre-built harness (prepare.py) | Agent builds the lab from conversation |
| Metrics | Single, quantitative | Primary + secondary, quantitative or qualitative |
| Experimentation | Code-only (modify → train → measure) | Thought + real experiments, free-form rhythm |
| Hypothesis generation | Unstructured | 10 named strategies as reference tools |
| Convergence | None | Signals that suggest change, without dictating response |
| Branching | Linear only | Non-linear — fork, switch, cross-branch learning |
| Session continuity | None | Resume from `.lab/` state |
| Drift detection | None | Re-validation every 10 experiments |
| User interaction | None | Complete autonomy; user observes, intervenes when they want |
| Logging | TSV only | TSV + narrative + branch registry + parking lot |
| Scope | Single file (train.py) | Any files, defined in discovery |

The key additions:
- **Free navigation with disciplined execution.** The agent decides what to explore and when. But commit-before-measure-after-log-always is non-negotiable.
- **Thought experiments as first-class.** Analysis that prevents 5 wasted runs is more valuable than running them.
- **Convergence signals as advisors, not commands.** Patterns suggest change is needed; the agent decides what change.
- **Domain-agnostic.** Works for ML, performance optimization, API design, algorithm exploration, prompt engineering — anything with a feedback loop.

## Usage

### As a Claude Code skill

Drop `researcher.md` into your skills directory. Invoke it when you want autonomous experimentation:

```
Use the researcher skill — I want to optimize the inference latency of this service.
```

### As a CLAUDE.md

Copy the content of `researcher.md` (without the frontmatter) into your project's `CLAUDE.md` or reference it:

```markdown
When I say "research" or "experiment", follow the methodology in researcher.md.
```

### As a prompt

Paste the content of `researcher.md` into any AI coding agent's context. The instructions are self-contained.

## Example use cases

**ML training optimization** (the autoresearch case)
- Primary metric: `val_bpb` (lower is better)
- Run: `uv run train.py > run.log 2>&1`
- Measure: `grep "^val_bpb:" run.log`
- Scope: `train.py`

**API latency reduction**
- Primary metric: p99 latency in ms (lower is better)
- Secondary: throughput (requests/sec, higher is better)
- Run: `make bench > run.log 2>&1`
- Measure: `grep "p99_ms:" run.log`, `grep "rps:" run.log`
- Scope: `src/handlers/`, `src/middleware/`

**Test suite speed**
- Primary metric: total test time in seconds (lower is better)
- Secondary: test count (higher is better — don't speed up by deleting tests)
- Run: `npm test 2>&1 | tee run.log`
- Measure: `grep "Time:" run.log`, `grep "Tests:" run.log`
- Scope: test configuration, parallelization, fixtures

**Algorithm exploration**
- Primary metric: accuracy % on validation set (higher is better)
- Secondary: inference time (lower is better)
- Run: `python evaluate.py > run.log 2>&1`
- Measure: `grep "accuracy:" run.log`, `grep "time_ms:" run.log`
- Scope: `src/algorithm.py`

**Prompt engineering**
- Primary metric: qualitative rubric (agent-judged, 1–10 scale)
- Run: `python run_eval.py > run.log 2>&1`
- Measure: agent evaluates output against rubric criteria
- Scope: `prompts/`, `system_messages/`

**Architecture design exploration**
- Primary metric: qualitative rubric (clarity, extensibility, simplicity — weighted)
- Run: N/A (qualitative research)
- Measure: agent judgment against rubric
- Scope: `docs/`, `src/core/`

## What the agent creates

```
.lab/
├── config.md         # Experiment parameters (agreed in discovery)
├── results.tsv       # Metrics log — ALL experiments, ALL branches, with lineage
├── log.md            # Narrative log — hypothesis → result → insight
├── branches.md       # Branch registry — status, results, relationships
├── parking-lot.md    # Deferred ideas — picked up when stuck
└── summary.md        # Final summary (created at wrap-up)
```

`.lab/` is **untracked** (in `.gitignore`) and **sacred** — the agent uses only git commands that preserve untracked directories. This is the single source of truth. Git manages code state on `research/*` branches. `.lab/` manages knowledge independently — it survives all checkouts, resets, and branch switches.

## Design principles

1. **Interview first, experiment second.** Understand the problem before touching code.
2. **Freedom in navigation, discipline in execution.** Agent decides what to explore; commit/measure/log rules are non-negotiable.
3. **Complete autonomy by default.** Agent logs, user observes. Only two reasons to interrupt: unavoidable scope violation or true dead end.
4. **Thinking counts.** A thought experiment that eliminates a dead end is as valuable as a successful code change.
5. **Simplicity wins.** At equal performance, less code beats more code.
6. **Track everything.** Lineage, branch, duration — if it's not logged, it didn't happen.
7. **Survive interruptions.** Sessions resume cleanly from `.lab/` state.
8. **Branch freely.** Exploration doesn't mean abandoning progress. Fork, diverge, recombine.

## License

MIT
