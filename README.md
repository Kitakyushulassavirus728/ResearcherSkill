# researcher-skill

**Autonomous experimentation for your AI coding agent.**

Drop a single file into Claude Code, Cursor, or any agent that reads markdown — your agent will design experiments, test hypotheses, discard what fails, and keep what works. You sleep, it researches.

<!-- TODO: replace with a GIF/screen recording showing the agent running 3-4 experiments autonomously -->
<!-- The demo should show: agent proposes hypothesis → runs experiment → evaluates → keeps or discards → moves to next -->

## Install

Copy `researcher.md` to your skills directory and invoke it:

```
Use the researcher skill — I want to optimize the inference latency of this service.
```

Or paste the content of `researcher.md` into any AI agent's context. The instructions are self-contained.

## How it works

1. **Discovery** — the agent interviews you: what to optimize, how to measure it, what's in scope, when to stop
2. **Lab setup** — creates a `research/` git branch and a `.lab/` directory that tracks all experiment history across branches
3. **Autonomous research** — the agent loops through THINK (analyze, hypothesize) → TEST (implement, run, measure) → REFLECT (log, update direction) — with full freedom to fork branches, combine wins, and change strategy
4. **Wrap-up** — summary of what worked, what didn't, and why. Code reflects the global best.

The agent commits before every experiment, measures after, logs always, and reverts on discard. Navigation is free; execution discipline is non-negotiable.

## What it looks like running

```
## Experiment 7 — Replace O(n^2) neighbor search with KD-tree
Branch: research/reduce-latency
Type: real | Parent: #5
Hypothesis: KD-tree lookup should reduce p99 from 142ms to under 100ms
Changes: swapped brute-force loop in spatial_index.py with scipy.spatial.KDTree
Result: p99 = 89ms (was 142ms baseline, 118ms best) — new best
Status: keep
Insight: The bottleneck was always the neighbor search, not the scoring.
         Experiment #3 (caching) was treating the symptom.
```

```
experiment  branch                parent  commit   metric  status   description
0           research/reduce-lat   0       a1b2c3d  142.00  keep     Baseline
1           research/reduce-lat   0       e4f5g6h  139.20  discard  Add response caching
...
7           research/reduce-lat   5       k8l9m0n   89.00  keep     KD-tree neighbor search
```

## How it differs from autoresearch

[autoresearch](https://github.com/karpathy/autoresearch) is a brilliant setup for ML training: one file, one metric, rigid loop. This skill generalizes that:

- **Any domain** — ML, API latency, test speed, bundle size, algorithm design, prompt engineering
- **Thought experiments** — analysis that prevents 5 wasted runs is more valuable than running them
- **Non-linear branching** — fork hypotheses, explore in parallel, combine wins across branches
- **Convergence signals** — detects when you're stuck and suggests strategy changes
- **Session resume** — pick up where you left off from `.lab/` state
- **Qualitative metrics** — works with agent-judged rubrics, not just numbers

## What the agent creates

```
.lab/
├── config.md         # Experiment parameters
├── results.tsv       # All experiments, all branches, with lineage
├── log.md            # Narrative: hypothesis → result → insight
├── branches.md       # Branch registry
├── parking-lot.md    # Ideas for later
└── summary.md        # Final report (wrap-up)
```

`.lab/` is untracked and survives all git operations. Git manages code; `.lab/` manages knowledge.

## License

MIT
