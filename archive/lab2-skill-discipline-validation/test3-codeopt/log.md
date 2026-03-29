# Experiment Log

## Experiment 15 — Module-level zero bytearray
Branch: research/sieve-optimization / Type: real / Parent: #5
Hypothesis: Preallocated bytearray at module level avoids b'\x00'*count alloc each iteration
Changes: _SIEVE_ZEROS = bytearray(5001) at module level; zeros[:count] replaces b'\x00'*count
Result: score=10000.0 (min=10.3µs vs 12µs — 14% faster, new best)
Duration: 0.025s wall
Status: keep (NEW BEST)
Insight: Avoiding per-iteration heap allocation in inner loop saves ~1.7µs total across 25 prime markings.

## Experiment 14 — Two-phase sieve (precompute small primes)
Branch: research/sieve-optimization / Type: real / Parent: #5
Hypothesis: Precomputing small primes up to sqrt(n) then using them in a for-loop avoids if-checks
Changes: Two-phase: small sieve to sqrt(n), then mark large sieve
Result: 16.8µs vs 12µs — 40% slower due to double allocation
Status: discard (not committed, restored)
Insight: Double allocation overhead dominates. Single-pass is better for small n.

## Experiment 13 — Local variable caching
Branch: research/sieve-optimization / Type: real / Parent: #5
Hypothesis: Caching b'\x00' as local _zeros avoids repeated bytes literal lookup
Changes: _zeros = b'\x00' local, use _zeros * count
Result: min=12.6µs vs 12µs — slight regression
Status: discard (not committed, restored)
Insight: Python bytecode for b'\x00' literal is already fast. Extra local lookup adds overhead.

## Experiment 12 — Trial division 6k±1 wheel (no allocation)
Branch: research/sieve-optimization / Type: real / Parent: #5
Hypothesis: Inverted: avoid sieve allocation, use O(n*sqrt(n)/3) trial division
Changes: _is_prime helper with 6k±1 wheel, iterate candidates of form 6k±1
Result: 1228µs — 100x slower than sieve. Not committed.
Status: discard
Insight: Even optimized trial division is fundamentally O(n*sqrt(n)) vs O(n log log n) sieve. Sieve wins.

## Experiment 11 — array.array('b') sieve
Branch: research/sieve-optimization / Type: real / Parent: #5
Hypothesis: array.array might have lower overhead than bytearray
Changes: from array import array; use array('b', ...) instead of bytearray
Result: 56.7µs — 4.7x SLOWER than bytearray (12µs). Not committed.
Status: discard
Insight: bytearray has better C-level optimizations for slice assignment than array.array.

## Re-Validation after Experiment 9 (Experiment 10)
Branch: research/sieve-optimization / Type: thought / Parent: #5
Hypothesis: Confirm current best (exp #5) is stable and correct
Changes: None
Result: 5/5 runs = 10000.0, count_primes(10000) = 1229 ✓
Status: keep (best confirmed)
Insight: Score is permanently maxed. Benchmark cap at 1/0.0001 = 10000 is reached. Actual function at ~12µs — 8.3x below cap. Further Python-level optimization cannot improve benchmark score.

## Experiment 9 — math.isqrt bound + for-loop + b'\x01' init
Branch: research/sieve-optimization / Type: real / Parent: #5
Hypothesis: isqrt, for-loop, and b'\x01' init would be marginally faster
Changes: from math import isqrt; bytearray(b'\x01'*size); for i in range(...)
Result: score=10000.0 (min=12.8µs vs 12µs — slight regression)
Duration: 0.027s wall
Status: discard (reset HEAD~1)
Insight: Import overhead and range() object creation slightly worse than while+manual counter.

## Experiment 8 — 2/3 Wheel sieve (CRASH)
Branch: research/sieve-optimization / Type: real / Parent: #5
Hypothesis: 6k±1 wheel sieve would process only 1/3 candidates vs odd-only's 1/2
Changes: Track only 6k+1 and 6k+5 forms in flat bytearray
Result: count_primes(10000) = 1232, wrong (expected 1229)
Duration: -
Status: crash (not committed, file restored)
Insight: Wheel sieve marking logic complex and error-prone. Python overhead of complex indexing negates gains. Keep odd-only.

## Experiment 7 — Bitfield sieve (Python int)
Branch: research/sieve-optimization / Type: real / Parent: #5
Hypothesis: Python int as bitfield + bin().count('1') for tally avoids bytearray alloc
Changes: Sieve stored as int, bit manipulation loop to clear composites
Result: 1112µs — 90x SLOWER. Tested, not committed.
Duration: -
Status: discard (not committed, file restored)
Insight: Python-level bit operations inside a loop are catastrophically slow. bytearray slice is vectorized C.

## Experiment 6 — Preallocated zeros buffer
Branch: research/sieve-optimization / Type: real / Parent: #5
Hypothesis: Slicing pre-built bytes obj faster than b'\x00'*count each time
Changes: Module-level _ZEROS = b'\x00' * 5001, use _ZEROS[:count]
Result: score=10000.0 (min=13.7µs vs 12µs — slight regression)
Duration: 0.021s wall
Status: discard (reset HEAD~1)
Insight: Slice of large bytes not faster than small allocation. Python allocator fast for small objects.

## Experiment 5 — Avoid temp slice for len
Branch: research/sieve-optimization / Type: real / Parent: #4
Hypothesis: Avoid len(sieve[start::p]) allocation by computing count mathematically
Changes: count = (size - start + p - 1) // p instead of len(sieve[start::p])
Result: score=10000.0 (min=12µs vs 16µs — ~25% faster)
Duration: 0.022s wall
Status: keep
Insight: Allocation reduction helps. At 12µs, getting close to Python overhead floor.

## Experiment 4 — sieve.count(1) instead of sum()
Branch: research/sieve-optimization / Type: real / Parent: #3
Hypothesis: bytearray.count() is C-level, should beat Python-level sum()
Changes: Changed `sum(sieve)` to `sieve.count(1)`
Result: score=10000.0 (min=16µs vs 37µs — 2.3x faster!)
Duration: 0.026s wall
Status: keep
Insight: Major win. C-level count op dominates. Total: ~16µs for n=10000. Now push allocation.

## Experiment 3 — Odd-only sieve
Branch: research/sieve-optimization / Type: real / Parent: #2
Hypothesis: Odd-only sieve halves memory and iteration count
Changes: Track only odd numbers, index i = number 2i+3
Result: score=10000.0 (min=37µs vs 55µs — 33% faster)
Duration: 0.021s wall
Status: keep
Insight: Half-memory sieve meaningfully faster. Try 2/3 wheel or precomputed count.

## Experiment 2 — Sieve with b'\x00' slice assignment
Branch: research/sieve-optimization / Type: real / Parent: #1
Hypothesis: b'\x00' * len avoids bytearray object creation overhead
Changes: Changed inner sieve fill to b'\x00' * len(range(...)), while loop instead of for
Result: score=10000.0 (min=55µs, same as #1)
Duration: 0.022s wall
Status: keep
Insight: Score already maxed. Need to find approaches that reduce actual µs. Try odd-only sieve.

## Experiment 1 — Sieve of Eratosthenes
Branch: research/sieve-optimization / Type: real / Parent: #0
Hypothesis: Sieve of Eratosthenes O(n log log n) will dominate O(n²) trial division
Changes: Replaced trial division with sieve using bytearray
Result: score=10000.0 (capped at 1/0.0001, elapsed < 0.0001s)
Duration: 0.025s wall
Status: keep
Insight: Massive 1300x speedup. Score is hitting the cap (1/max(elapsed, 0.0001)). Need finer measurement or the benchmark is saturated.

## Experiment 0 — Baseline
Branch: research/sieve-optimization / Type: real / Parent: -
Hypothesis: Measure baseline performance of naive trial division
Changes: None
Result: score=7.683339 (elapsed ~0.130s)
Duration: 0.157s wall
Status: keep
Insight: O(n²) trial division is very slow. Clear room for massive improvement with sieve.

