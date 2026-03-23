<img width="1376" height="768" alt="Gemini_Generated_Image_5z6cxx5z6cxx5z6c" src="https://github.com/user-attachments/assets/02c3c4cd-fe2a-4fcd-b414-29bd84f5a741" />

# Researcher Skill

**One file. Your AI coding agent becomes a scientist.**

Drop `researcher.md` into Claude Code, Codex, or any agent. It will design experiments, test hypotheses, discard what fails, keep what works — 30+ experiments overnight while you sleep.

## What it looks like running

> ### Experiment 5 — Parallelize independent test suites
> **Branch:** research/faster-tests · **Parent:** #3 · **Type:** real
>
> **Hypothesis:** Unit and integration suites don't share state. Running them in parallel should cut total time.
> **Changes:** split test config into two parallel jobs in `test.config.ts`
> **Result:** 38s (was 94s baseline, 52s best) — **new best**
> **Status:** keep
>
> **Insight:** Most of the remaining time is in integration tests. Unit tests finish in 6s. Focus on integration from here.

| # | branch | metric | status | description |
|---|--------|--------|--------|-------------|
| 0 | research/faster-tests | 94s | keep | Baseline |
| 1 | research/faster-tests | 71s | keep | Remove redundant setup/teardown |
| 2 | research/faster-tests | 74s | discard | Shared test fixtures |
| 3 | research/faster-tests | 52s | keep | Mock external HTTP calls |
| 4 | research/faster-tests | - | thought | DB reset is slow but tests need clean state, skip for now |
| 5 | research/faster-tests | **38s** | **keep** | Parallelize independent test suites |

*Example is simulated. The skill works on any codebase — run it and share your real results.*

**Same loop, different problems:**
- `npm run build` takes 40s → agent gets it to 18s
- prompt returns wrong format 30% of the time → agent gets it to 3%
- API p99 is 200ms → agent finds the bottleneck and cuts it to 80ms
- document parser misses edge cases → agent improves match rate from 74% to 91%

## How it works

The agent interviews you about what to optimize, sets up a lab on a git branch, and works autonomously. Thinks, tests, reflects. Commits before every experiment, reverts on failure, logs everything.

It forks branches to explore divergent approaches. Detects when it's stuck and changes strategy. Keeps going until you stop it or it hits a target.

Generalizes [autoresearch](https://github.com/karpathy/autoresearch) beyond ML. Supports thought experiments, non-linear branching, qualitative metrics, convergence signals, and session resume.

All experiment history lives in an untracked `.lab/` directory. Git manages code. `.lab/` manages knowledge.

**Want the full walkthrough?** Read the [guide](GUIDE.md). It walks through a complete example from start to finish.

## License

MIT

## See also

**[Yggdrasil](https://github.com/krzysztofdudek/Yggdrasil)** — the agent experiments on your code. But does it understand what it's working on? Semantic memory for repositories.
