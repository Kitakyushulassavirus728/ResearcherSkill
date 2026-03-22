# researcher-skill

An autonomous experimentation skill for AI coding agents. The agent interviews you, sets up a lab, then runs experiments in a loop — keeping what works, discarding what doesn't — until it hits a target or you tell it to stop.

Works with any codebase, any metric, any domain. You sleep, it researches.

## What it does

```
Discovery ──→ Lab Setup ──→ Experiment Loop ──→ Summary
(interview)   (branch,       (hypothesize →      (best result,
               logs,          implement →          insights,
               baseline)      measure →            failed paths)
                              keep/discard)
```

**Phase 1 — Discovery.** The agent asks what you're optimizing, how to measure it, what's in scope, and when to stop. No assumptions. Everything is explicit.

**Phase 2 — Lab Setup.** Creates a git branch, a `.lab/` directory with config, a results TSV, and an iteration log. Runs a baseline. Everything is reproducible.

**Phase 3 — Experiment Loop.** The core. Each iteration: form a hypothesis, decide if it needs code or just analysis, implement, run, measure, keep or discard. Convergence signals detect when the agent is spinning and force a strategy change.

**Phase 4 — Wrap-up.** Summary of what worked, what didn't, and why. Branch HEAD reflects the best result.

## How it differs from autoresearch

[autoresearch](https://github.com/karpathy/autoresearch) by Karpathy is a brilliant setup for ML training optimization: one file, one metric, fixed time budget. This skill generalizes that idea:

| | autoresearch | researcher-skill |
|---|---|---|
| Domain | ML training (val_bpb) | Anything measurable |
| Setup | Pre-built harness (prepare.py) | Agent builds the lab from conversation |
| Experimentation | Code-only (modify → train → measure) | Thought experiments + real experiments |
| Convergence | None (agent "thinks harder") | Explicit signals with prescribed actions |
| Logging | TSV only | TSV (metrics) + narrative (reasoning) |
| Scope | Single file (train.py) | Any files, defined in discovery |

The key additions:
- **Thought experiments as first-class.** Analysis that prevents 5 wasted runs is more valuable than running them.
- **Convergence detection.** When the last 5 experiments are all discards, the skill forces a strategy pivot instead of more hill-climbing.
- **Domain-agnostic.** Works for ML, performance optimization, API design, algorithm exploration, test coverage — anything with a feedback loop.

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
- Metric: `val_bpb` (lower is better)
- Run: `uv run train.py > run.log 2>&1`
- Measure: `grep "^val_bpb:" run.log`
- Scope: `train.py`

**API latency reduction**
- Metric: p99 latency in ms (lower is better)
- Run: `make bench > run.log 2>&1`
- Measure: `grep "p99_ms:" run.log`
- Scope: `src/handlers/`, `src/middleware/`

**Test suite speed**
- Metric: total test time in seconds (lower is better)
- Run: `npm test 2>&1 | tee run.log`
- Measure: `grep "Time:" run.log`
- Scope: test configuration, parallelization, fixtures

**Algorithm exploration**
- Metric: accuracy % on validation set (higher is better)
- Run: `python evaluate.py > run.log 2>&1`
- Measure: `grep "accuracy:" run.log`
- Scope: `src/algorithm.py`

**Bundle size reduction**
- Metric: bundle size in KB (lower is better)
- Run: `npm run build > run.log 2>&1`
- Measure: `grep "total_kb:" run.log`
- Scope: webpack config, imports, dependencies

## What the agent creates

```
.lab/
├── config.md       # Experiment parameters (agreed in discovery)
├── results.tsv     # Tab-separated metrics log
├── log.md          # Narrative iteration log (hypothesis, result, insight)
└── summary.md      # Final summary (created at wrap-up)
```

By default, `.lab/` is added to `.gitignore` — lab artifacts are for you, not for the repo. The actual code improvements live in git commits on the `research/<slug>` branch.

## Design principles

1. **Interview first, experiment second.** The agent must understand the problem before touching code.
2. **Mechanical rigor.** Keep/discard is binary. Git commit before every experiment. Revert on failure. No ambiguity.
3. **Thinking counts.** A thought experiment that eliminates a dead end is as valuable as a successful code change.
4. **Convergence awareness.** Detect when you're spinning and change strategy automatically.
5. **Simplicity wins.** At equal performance, less code beats more code. Removing something that doesn't help is a positive result.

## License

MIT
