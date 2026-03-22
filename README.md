<img width="1376" height="768" alt="Gemini_Generated_Image_5z6cxx5z6cxx5z6c" src="https://github.com/user-attachments/assets/02c3c4cd-fe2a-4fcd-b414-29bd84f5a741" />

# Researcher Skill

**One file. Your AI coding agent becomes a scientist.**

Drop `researcher.md` into Claude Code, Cursor, or any agent that reads markdown. It will design experiments, test hypotheses, discard what fails, keep what works — 30+ experiments overnight while you sleep.

<!-- TODO: replace with a GIF showing the agent running 3-4 experiments autonomously -->

## What it looks like running

> ### Experiment 7 — Replace O(n²) neighbor search with KD-tree
> **Branch:** research/reduce-latency · **Parent:** #5 · **Type:** real
>
> **Hypothesis:** KD-tree lookup should reduce p99 from 142ms to under 100ms
> **Changes:** swapped brute-force loop in `spatial_index.py` with `scipy.spatial.KDTree`
> **Result:** p99 = 89ms (was 142ms baseline, 118ms best) — **new best**
> **Status:** keep
>
> **Insight:** The bottleneck was always the neighbor search, not the scoring. Experiment #3 (caching) was treating the symptom.

| # | branch | metric | status | description |
|---|--------|--------|--------|-------------|
| 0 | research/reduce-latency | 142.00 | keep | Baseline |
| 1 | research/reduce-latency | 139.20 | discard | Add response caching |
| … | | | | |
| 7 | research/reduce-latency | **89.00** | **keep** | KD-tree neighbor search |

The agent interviews you about what to optimize, sets up a lab on a git branch, then works autonomously — thinking, testing, reflecting — committing before every experiment, reverting on failure, logging everything. It forks branches to explore divergent approaches, detects when it's stuck, and keeps going until you stop it or it hits a target.

Generalizes [autoresearch](https://github.com/karpathy/autoresearch) beyond ML: works for any domain (API latency, test speed, bundle size, prompt engineering), supports thought experiments, non-linear branching, qualitative metrics, convergence signals, and session resume.

All experiment history lives in an untracked `.lab/` directory that survives all git operations — git manages code, `.lab/` manages knowledge.

## License

MIT
