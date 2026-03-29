# Task: Validate researcher skill discipline via synthetic tests

## Goal

Verify that an agent following `researcher.md` correctly executes ALL described mechanics. Run synthetic tests, observe behavior, report which checkpoints pass and which fail.

## What to test

### Test 1: Black-box parameter optimization (quantitative)
- Create a test repo with a compiled black-box scorer and `config.txt` with 5 parameters (0-100)
- The scorer should have: non-obvious optima, at least one interaction between parameters, a trap (value that looks good individually but hurts in combination)
- Agent (subagent, sonnet) runs researcher skill on it. Budget: 20 experiments, no termination limit unless agent self-imposes one (that's a fail).
- **Check:** structured commits, log before reset, guardrails (3+ discard, 5+ discard fork, plateau 8+), re-validation every 10th, THINK checklist (untested assumptions, interactions), strategy diversification on fork (assumptions list, baseline fork, mandatory inversion)

### Test 2: Two-peak optimization (forces forking)
- Same setup but scorer has two distinct peaks — one easy to find (~70 points), one harder (~95 points) in the opposite region of parameter space
- Agent must discover the first peak, stagnate, fork with inverted assumptions, discover the second peak
- **Check:** fork mechanics, strategy diversification (assumptions list, fork from baseline, inversion as first experiment), branch naming, branches.md, global experiment numbering

### Test 3: Code optimization (domain-agnostic THINK)
- Repo with a slow Python function and a benchmark
- Agent optimizes the function. No numeric parameters — algorithmic changes only.
- **Check:** THINK works without "variable/direction" framing, structured commits on code changes, correct keep/discard on performance

### Test 4: Qualitative evaluation (multi-evaluator protocol)
- Repo with a user-facing text to improve (e.g., error message)
- Main agent (you) runs the research process, spawning 3 haiku subagents as evaluators per experiment
- **Check:** subagents receive ONLY artifact + rubric (no hypothesis/context), scores show variance (not identical), median aggregation, divergence flagging

### Test 5: Crash handling
- Scorer that crashes on certain configs (OOM, dependency errors, random crashes)
- **Check:** crash detection, revert, trivial vs fundamental classification, 3+ crashes → rethink

## How to run

- For quantitative tests (1, 2, 3, 5): use subagents (sonnet) as researchers — they don't need multi-evaluator
- For qualitative test (4): YOU are the researcher, spawn evaluator subagents
- After each test: inspect git log, .lab/results.tsv, .lab/log.md, .lab/branches.md
- Report results as a table: checkpoint | pass/fail | notes

## Important

- Do NOT set experiment count limits unless the test specifically requires it. The skill defaults to infinite — if the agent self-imposes a limit, that's a fail.
- For two-peak test: design the scorer so that the second peak is only reachable by inverting assumptions (e.g., if peak 1 is at high values, peak 2 is at low values)
- Read `researcher.md` in this repo as the source of truth for what the skill should do
- Compare results against `archive/lab1-skill-discipline-validation/` for regression check

## Previous results location

`archive/lab1-skill-discipline-validation/` — results from the first validation round. Use for comparison, not as ground truth (skill was updated since).
