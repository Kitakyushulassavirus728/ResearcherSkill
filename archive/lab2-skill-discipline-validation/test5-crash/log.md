# Experiment Log

## Experiment 0 — Baseline
Branch: research/maximize-score / Type: real / Parent: N/A
Hypothesis: Record baseline with default config
Changes: none
Result: 75.25
Duration: 0.03s
Status: keep
Insight: Baseline established. Config A=50,B=50,C=50,D=50,E=51 scores 75.25. Need to understand what drives the score higher. Will explore pushing A, B, E toward 95 (max safe), and tuning C, D near 50.

## Experiment 1 — Push A,B,E to 95
Branch: research/maximize-score / Type: real / Parent: #0
Hypothesis: High A,B,E with C,D at 50 maximizes score
Changes: A=95, B=95, C=50, D=50, E=95
Result: CRASH - hash-based segfault (exit 139) - fundamental, unpredictable
Duration: 0.03s
Status: crash
Insight: Hash-based crash is unpredictable (~15% of configs). Will try slight variation of parameters to get different hash.

## Experiment 2 — A=95,B=94,C=50,D=51,E=95
Branch: research/maximize-score / Type: real / Parent: #0
Hypothesis: Vary parameters to avoid hash crash, near-maximum values
Changes: A=95, B=94, C=50, D=51, E=95
Result: 96.75 (was 75.25, +21.5)
Duration: 0.03s
Status: keep
Insight: Big jump. Best so far. B=94 vs 95 only slightly penalizes A*B component. C=50 and D=51 are near optimal for those dimensions. Will try to push B higher and fine-tune C/D.

## Experiment 3 — A=B=95, C=51, D=50, E=95
Branch: research/maximize-score / Type: real / Parent: #2
Hypothesis: Equal A=B=95 maximizes min(A,B) term, C=51 changes hash to avoid crash
Changes: A=95, B=95, C=51, D=50, E=95
Result: 97.0 (was 96.75, +0.25)
Duration: 0.03s
Status: keep
Insight: Score = 25*(95/100) + 25*(1-1/50) + 25*(1-0) + 25*(95/100) = 23.75+24.5+25+23.75=97.0. Confirmed formula. To reach 98+ need D=50 (already), C=50 (lost 0.5 by using 51), and A=B=E=95. Try C=50,D=50 with different hash approach.

## Experiment 4 — A=B=95, C=50, D=49, E=95
Branch: research/maximize-score / Type: real / Parent: #3
Hypothesis: C=50 better than C=51, D=49 same result as D=51, different hash
Changes: A=95, B=95, C=50, D=49, E=95
Result: 97.0 (same as #3, no improvement)
Duration: 0.03s
Status: discard
Insight: Symmetric around D=50 as expected. Need to use C=50 with D=50, but that exact combo with 95,95,95 crashed. Try float params to change hash while keeping near-optimal values.

## Experiment 5 — A=B=95, C=50, D=50.1, E=95
Branch: research/maximize-score / Type: real / Parent: #3
Hypothesis: Float D=50.1 gets different hash, C=50 optimal
Changes: A=95, B=95, C=50, D=50.1, E=95
Result: 97.45 (was 97.0, +0.45)
Duration: 0.03s
Status: keep
Insight: Score = 23.75 + 25 + 25*(1-0.1/50) + 23.75 = 23.75+25+24.95+23.75 = 97.45. C=50 fully optimal now. D=50.1 gives tiny penalty vs D=50. Try D=50.0 with different hash via C variation. Or push toward D=50 exactly with different A/B/E variation.

## Experiment 6 — A=B=95, C=50, D=50, E=94.9
Branch: research/maximize-score / Type: real / Parent: #5
Hypothesis: D=50 exactly optimal, E=94.9 changes hash string
Changes: A=95, B=95, C=50, D=50, E=94.9
Result: 97.475 (was 97.45, +0.025)
Duration: 0.03s
Status: keep
Insight: Score = 23.75+25+25+23.975=97.475 (E=94.9→94.9/100*25=23.725). Wait, 94.9/100*25=23.725, not 23.975. Let me recalc: 23.75+25+25+23.725=97.475. Yes. Now try E=95 with different hash approach using A or B variation.

## Experiment 7 — A=B=95, C=50, D=50, E=94.94
Branch: research/maximize-score / Type: real / Parent: #6
Hypothesis: E=94.94 is the highest E that hashes to "94.9" string
Changes: A=95, B=95, C=50, D=50, E=94.94
Result: 97.485 (was 97.475, +0.01)
Duration: 0.03s
Status: keep
Insight: Marginal improvement. E=94.94 → 94.94/100*25=23.735. Now at 97.485. C=50.06 with E=95 would give: 23.75+24.97+25+23.75=97.47. That's worse. The current config may be near-optimal within crash constraints. Try varying A/B slightly to see if D=50,E=95 with different A/B hash works.

## Experiment 8 — A=B=95, C=50, D=50, E=94.9499
Branch: research/maximize-score / Type: real / Parent: #7
Hypothesis: E=94.9499 is the highest E value that hashes to "94.9"
Changes: A=95, B=95, C=50, D=50, E=94.9499
Result: 97.487475 (was 97.485, +0.002475)
Duration: 0.03s
Status: keep
Insight: Score = 23.75+25+25+25*(94.9499/100) = 23.75+25+25+23.737475 = 97.487475. This is near-optimal. The hash constraint limits E to <94.95 to stay in "94.9" bucket. Remaining gap: 97.5-97.487475=0.012525. One more avenue: use float A/B/C/D to find a hash for which A=B=E=95 with C=D=50 works.

## Experiment 9 — A=94.9499, B=95, C=50, D=50, E=95
Branch: research/maximize-score / Type: real / Parent: #8
Hypothesis: Move constraint to A instead of E, same formula value
Changes: A=94.9499, B=95, C=50, D=50, E=95
Result: 97.487475 (same as #8)
Duration: 0.03s
Status: discard
Insight: Confirmed symmetry - min(A,B) term picks up A penalty either way. Score is the same. Best is 97.487475. Let me try re-validation at #10 then explore whether hash can be bypassed differently.

## Experiment 10 — RE-VALIDATION
Branch: research/maximize-score / Type: real / Parent: #8
Hypothesis: Verify best config is stable
Changes: none (running commit 2c81f5f)
Result: 97.487475 (confirmed!)
Duration: 0.02s
Status: keep
Insight: Best config stable. Will continue exploring if anything can exceed this.

## Experiment 11 — Explore floor/nonlinearity
Branch: research/maximize-score / Type: real / Parent: #8
Hypothesis: Low A,B,E confirm linear formula
Changes: A=1, B=1, C=50, D=50, E=1
Result: 50.5 (as expected for low A,B,E with perfect C,D)
Duration: 0.03s
Status: discard
Insight: Formula is linear. No hidden nonlinearity. Best config (97.487475) is well-established. Will explore edge cases: C or D at extreme values, then push E bucket higher.

## Experiment 12 — E=94.94999, push to boundary
Branch: research/maximize-score / Type: real / Parent: #8
Hypothesis: E=94.94999 is closer to 94.95 boundary, hashes to "94.9", tiny score gain
Changes: A=95, B=95, C=50, D=50, E=94.94999
Result: 97.487498 (was 97.487475, +0.000023)
Duration: 0.02s
Status: keep
Insight: Microscopic improvement. E contribution: 94.94999/100*25=23.737498. Boundary is at 94.95000000000033. Try E=94.9499999 to get even closer.

## Experiment 13 — E=94.9499999, maximum in hash bucket
Branch: research/maximize-score / Type: real / Parent: #12
Hypothesis: E=94.9499999 maximizes E within "94.9" hash bucket
Changes: A=95, B=95, C=50, D=50, E=94.9499999
Result: 97.4875 (was 97.487498 - essentially same, ~97.4875)
Duration: 0.02s
Status: keep
Insight: This is effectively the ceiling within crash constraints. Score = 97.4875. Remaining gap to theoretical max = 97.5 - 97.4875 = 0.0125. That gap is an inherent cost of the hash-based crash avoidance. Will explore a couple more ideas then wrap up.

## Experiment 14 — E=94.94999999999, max float precision
Branch: research/maximize-score / Type: real / Parent: #13
Hypothesis: Higher precision pushes E score higher
Changes: E=94.94999999999
Result: 97.4875 (same as #13 - float64 precision limit reached)
Duration: 0.02s
Status: discard
Insight: Float64 precision has a ceiling here. Score is 97.4875. This is the maximum achievable given crash constraints. Will do a few verification runs of different approaches to be sure.

## Experiment 15 — A=94.9499999,B=95,E=95 symmetry check
Branch: research/maximize-score / Type: real / Parent: #13
Hypothesis: Constraining A gives same score as constraining E
Changes: A=94.9499999, B=95, C=50, D=50, E=95
Result: 97.4875 (same as #13)
Duration: 0.03s
Status: discard
Insight: Formula symmetry confirmed. Any single param in "94.9" hash bucket gives 97.4875. Multiple params in "94.9" bucket would give lower score. Plateau solidly confirmed at 97.4875.

## Experiment 16 — E=93 confirmation
Branch: research/maximize-score / Type: real / Parent: #13
Hypothesis: E=93 is worse than E=94.9499999
Changes: A=95, B=95, C=50, D=50, E=93
Result: 97.0 (as expected, worse than 97.4875)
Duration: 0.03s
Status: discard
Insight: Confirmed E=94.9 bucket is optimal. Every step down in E lowers the score.

## Experiment 17 — C=49.9, E=95
Branch: research/maximize-score / Type: real / Parent: #13
Hypothesis: Trade C penalty for E=95 to test which variable to constrain
Changes: A=95, B=95, C=49.9, D=50, E=95
Result: 97.45 (worse than 97.4875)
Duration: 0.03s
Status: discard
Insight: C=49.9 penalty (loss 0.05) > E constraint penalty (loss 0.0125). Constraining E in the "94.9" bucket is optimal strategy. C must stay at 50.

## Experiment 18 — C=50.06, E=95
Branch: research/maximize-score / Type: real / Parent: #13
Hypothesis: C in 50.1 bucket enables E=95, test if tradeoff beats best
Changes: A=95, B=95, C=50.06, D=50, E=95
Result: 97.47 (worse than 97.4875)
Duration: 0.02s
Status: discard
Insight: C penalty (0.03) > E bucket penalty (0.0125). Confirmed: constraining E is the least costly approach. Best remains 97.4875.

## Experiment 19 — A=B=E=70, C=D=50 mid-range
Branch: research/maximize-score / Type: real / Parent: #13
Hypothesis: Mid-range linear verification
Changes: A=70, B=70, C=50, D=50, E=70
Result: CRASH - all even integers → "ModuleNotFoundError: No module named 'scipy.optimize'" (fundamental)
Duration: 0.03s
Status: crash
Insight: All-even integer crash triggered. Reminder: the all-even crash is fundamental (not trivial), confirmed. Reset. Going to final re-validation.

## Experiment 20 — FINAL RE-VALIDATION
Branch: research/maximize-score / Type: real / Parent: #13
Hypothesis: Best config is stable and reproducible
Changes: none (commit 694109d: A=95, B=95, C=50, D=50, E=94.9499999)
Result: 97.4875 CONFIRMED
Duration: 0.03s
Status: keep
Insight: Research complete. Best score = 97.4875 at A=95, B=95, C=50, D=50, E=94.9499999.

## RESEARCH SUMMARY

**Best Config:** A=95, B=95, C=50, D=50, E=94.9499999
**Best Score:** 97.4875
**Baseline:** 75.25
**Improvement:** +22.2375 (+29.6%)

**Crash handling:**
- Experiment 1: hash segfault (fundamental) — reset, tried variation
- Experiment 19: all-even integers (fundamental) — reset
- No trivial crashes encountered

**Key insights:**
1. Score = 25*(min(A,B)/100) + 25*(1-|C-50|/50) + 25*(1-|D-50|/50) + 25*(E/100)
2. Max safe value: ≤95.0 (any >95 causes OOM crash)
3. Optimal: A=B=95, C=50, D=50, E=95 — but this exact config hits hash-based crash
4. Avoidance: use E=94.9499999 (rounds to "94.9" in hash, vs "95.0") — smallest penalty
5. Theoretical max 97.5 is unreachable; 97.4875 is the true achievable maximum

