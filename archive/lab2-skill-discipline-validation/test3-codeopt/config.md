# Lab Config

- **Objective:** Maximize `count_primes` throughput
- **Primary metric:** score from `python3 benchmark.py` (higher = better, = 1/time)
- **Scope:** `slow_function.py` only
- **Constraint:** `count_primes(10000)` must return exactly 1229
- **Run command:** `python3 benchmark.py`
- **Budget:** 1 minute per experiment
- **Termination:** 15 experiments
- **Branch:** research/sieve-optimization
- **Started:** 2026-03-29
