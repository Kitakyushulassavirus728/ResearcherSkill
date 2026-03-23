<img width="1376" height="768" alt="Gemini_Generated_Image_5z6cxx5z6cxx5z6c" src="https://github.com/user-attachments/assets/02c3c4cd-fe2a-4fcd-b414-29bd84f5a741" />

# Researcher Skill

**One file. Your AI coding agent becomes a scientist.**

Drop `researcher.md` into Claude Code, Codex, or any agent. It will design experiments, test hypotheses, discard what fails, keep what works — 30+ experiments overnight while you sleep.

## What it looks like running

> ### Experiment 7 — Replace O(n^2) neighbor search with KD-tree
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
| 0 | research/reduce-latency | 142.00 | keep | Baseline measurement |
| 1 | research/reduce-latency | 139.20 | discard | Add response caching |
| 2 | research/reduce-latency | 141.50 | discard | Connection pooling tuning |
| 3 | research/reduce-latency | 135.80 | discard | LRU cache on hot path |
| 5 | research/reduce-latency | 118.00 | keep | Batch DB queries |
| 7 | research/reduce-latency | **89.00** | **keep** | KD-tree neighbor search |

*Example is simulated. The skill works on any codebase — run it and share your real results.*

**Same loop, different problems:**
- `npm run build` takes 40s → agent gets it to 18s
- prompt returns wrong format 30% of the time → agent gets it to 3%
- API p99 is 200ms → agent finds the bottleneck and cuts it to 80ms
- document parser misses edge cases → agent improves match rate from 74% to 91%

## What can I research?

Anything where you can measure or evaluate a result:

- **API latency** — p50, p99, throughput
- **Test speed** — suite runtime, parallelization strategies
- **Bundle size** — tree-shaking, code splitting, dependency swaps
- **Prompt engineering** — accuracy, cost, token usage
- **Algorithm tuning** — runtime complexity, memory usage
- **Configuration optimization** — DB settings, cache sizes, thread pools

The agent interviews you about what to optimize, sets up a lab on a git branch, then works autonomously — thinking, testing, reflecting — committing before every experiment, reverting on failure, logging everything. It forks branches to explore divergent approaches, detects when it's stuck, and keeps going until you stop it or it hits a target.

Generalizes [autoresearch](https://github.com/karpathy/autoresearch) beyond ML: supports thought experiments, non-linear branching, qualitative metrics, convergence signals, and session resume.

All experiment history lives in an untracked `.lab/` directory that survives all git operations — git manages code, `.lab/` manages knowledge.

**Want the full walkthrough?** Read the [guide](GUIDE.md). It walks through a complete example from start to finish.

## License

MIT

---

If this is useful, star the repo and share what you discovered.

## See also

[Yggdrasil](https://github.com/krzysztofdudek/Yggdrasil) – your agent keeps forgetting your architecture, constraints, and past decisions. Yggdrasil gives your repository persistent semantic memory, so each task starts with the right context instead of another giant prompt.
