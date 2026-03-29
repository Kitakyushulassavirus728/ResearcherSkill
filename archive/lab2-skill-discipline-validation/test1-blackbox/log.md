# Experiment Log

## Experiment 20 — D=29.9999 (final)
Branch: research/blackbox-optimization / Type: real / Parent: #18
Hypothesis: D=29.9999 squeezes final marginal gain at boundary
Changes: D=29.9999 (was 29.999)
Result: 89.499985 (was 89.49985, +0.000135)
Duration: <1s
Status: keep
Insight: Still improving. Theoretical maximum for D approaching 30 from below. Score converging to ~89.5.

## Experiment 19 — A=99 sensitivity test
Branch: research/blackbox-optimization / Type: real / Parent: #18
Hypothesis: A=99 tests A-B synergy sensitivity — confirms A=100 is optimal
Changes: A=99 (was 100)
Result: 89.349473 (was 89.49985, -0.150377)
Duration: <1s
Status: discard
Insight: A=100 confirmed optimal. min(A,B) component needs both at max.

## Experiment 18 — D=29.999
Branch: research/blackbox-optimization / Type: real / Parent: #17
Hypothesis: D=29.999 safely below threshold for maximum D contribution
Changes: D=29.999 (was 29.99)
Result: 89.49985 (was 89.4985, +0.00135)
Duration: <1s
Status: keep
Insight: Marginal gains. Approaching asymptote. Try E float fine-tuning too — E=55.0 is integer, maybe E=55 is already exact peak.

## Experiment 17 — D=29.99
Branch: research/blackbox-optimization / Type: real / Parent: #16
Hypothesis: D=29.99 even closer to boundary gives more D contribution
Changes: D=29.99 (was 29.9)
Result: 89.4985 (was 89.485, +0.0135)
Duration: <1s
Status: keep
Insight: D=29.99 better. Pushing D toward 30 limit is working. Try D=29.999.

## Experiment 16 — D=29.9 (float)
Branch: research/blackbox-optimization / Type: real / Parent: #9
Hypothesis: D=29.9 is higher than 29 while still satisfying D<30 for interaction bonus
Changes: D=29.9 (was 29)
Result: 89.485 (was 89.35, +0.135)
Duration: <1s
Status: keep
Insight: Float values work! D=29.9 better than D=29. Try D=29.99 next.

## Experiment 15 — D=25
Branch: research/blackbox-optimization / Type: real / Parent: #9
Hypothesis: D=25 tests if optimal D is not exactly at boundary 29
Changes: D=25 (was 29)
Result: 88.75 (was 89.35, -0.6)
Duration: <1s
Status: discard
Insight: D=29 still better. Higher D (while staying below 30) is optimal.

## Experiment 14 — E=53
Branch: research/blackbox-optimization / Type: real / Parent: #9
Hypothesis: E=53 may be better than E=55
Changes: E=53 (was 55)
Result: 88.622727 (was 89.35, -0.727273)
Duration: <1s
Status: discard
Insight: E=55 confirmed optimal. E=53 worse.

## Experiment 13 — C=43
Branch: research/blackbox-optimization / Type: real / Parent: #9
Hypothesis: C=43 may be slightly better than C=42
Changes: C=43 (was 42)
Result: 88.754762 (was 89.35, -0.595238)
Duration: <1s
Status: discard
Insight: C=42 confirmed as optimal. C=43 is worse.

## Experiment 12 — B=80 asymmetry
Branch: research/blackbox-optimization / Type: real / Parent: #9
Hypothesis: A and B synergy may be best when both maximized equally
Changes: B=80 (was 100)
Result: 86.182816 (was 89.35, -3.167184)
Duration: <1s
Status: discard
Insight: Symmetric A=B=100 is better. A-B synergy requires both to be maximal.

## Experiment 11 — E=45
Branch: research/blackbox-optimization / Type: real / Parent: #9
Hypothesis: E=45 may be better or equivalent to E=55 but closer to lower bound
Changes: E=45 (was 55)
Result: 85.713636 (was 89.35, -3.636364)
Duration: <1s
Status: discard
Insight: E=55 is better. E peak is around 55, not 45. E=55 optimal.

## Experiment 10 — D=30 (boundary test)
Branch: research/blackbox-optimization / Type: real / Parent: #9
Hypothesis: D=30 crosses boundary — test if losing D-E interaction bonus hurts more than D contribution gains
Changes: D=30 (was 29)
Result: 79.5 (was 89.35, -9.85)
Duration: <1s
Status: discard
Insight: CRITICAL finding. D=30 drops by 9.85! D<30 constraint is essential for the D-E interaction bonus. D=29 is optimal boundary. D must stay below 30.

## Re-Validation after Experiment 9
Current HEAD score: 89.35 (recorded best: 89.35). No drift. Continuing.

## Experiment 9 — D=29
Branch: research/blackbox-optimization / Type: real / Parent: #8
Hypothesis: D=29 maximizes D contribution while maintaining D-E interaction bonus (D<30)
Changes: D=29 (was 20)
Result: 89.35 (was 88.0, +1.35)
Duration: <1s
Status: keep
Insight: D=29 better. The D-E interaction bonus (D<30, 40<E<70) appears active. Next: test D=30 to see if crossing threshold hurts.

## Experiment 8 — D=20
Branch: research/blackbox-optimization / Type: real / Parent: #7
Hypothesis: D=20 still in low-D range and adds D contribution
Changes: D=20 (was 10)
Result: 88.0 (was 86.5, +1.5)
Duration: <1s
Status: keep
Insight: D=20 better still. D is still contributing positively. The cutoff for penalty might be higher. Need to test D=29 (boundary before interaction bonus).

## Experiment 7 — D=10
Branch: research/blackbox-optimization / Type: real / Parent: #4
Hypothesis: D=10 gives more D component while still staying low enough for D-E interaction bonus
Changes: D=10 (was 0)
Result: 86.5 (was 85.0, +1.5)
Duration: <1s
Status: keep
Insight: D=10 is better than D=0. D contributes positively at low values. Need to find optimal D — balance between D component and interaction penalty.

## Experiment 6 — C=40
Branch: research/blackbox-optimization / Type: real / Parent: #4
Hypothesis: C peak may not be exactly 42 — test C=40
Changes: C=40 (was 42)
Result: 83.809524 (was 85.0, -1.190476)
Duration: <1s
Status: discard
Insight: C=42 confirmed better than C=40. C=42 appears to be the optimal value.

## Experiment 5 — E=60
Branch: research/blackbox-optimization / Type: real / Parent: #4
Hypothesis: E may improve beyond 55
Changes: E=60 (was 55)
Result: 83.181818 (was 85.0, -1.818182)
Duration: <1s
Status: discard
Insight: E=60 worse than E=55. E=55 appears to be near optimal. The peak is not monotonically higher.

## Experiment 4 — E=55
Branch: research/blackbox-optimization / Type: real / Parent: #3
Hypothesis: E may have a peak value near 55
Changes: E=55 (was 50)
Result: 85.0 (was 83.181818, +1.818182)
Duration: <1s
Status: keep
Insight: E=55 gives improvement. D=0 + E=55 may trigger a hidden interaction bonus (D<30 and 40<E<70). The combo looks powerful.

## Experiment 3 — D=0 (low D)
Branch: research/blackbox-optimization / Type: real / Parent: #2
Hypothesis: D may have a negative interaction with A when both are high; lowering D may help
Changes: D=0 (was 50)
Result: 83.181818 (was 80.681818, +2.5)
Duration: <1s
Status: keep
Insight: D=0 gives +2.5. Since A=100, having high D too may hurt. Low D seems preferred with high A.

## Experiment 2 — C=42 sweet spot
Branch: research/blackbox-optimization / Type: real / Parent: #1
Hypothesis: C may have a sweet spot near 42
Changes: C=42 (was 50)
Result: 80.681818 (was 75.919913, +4.761905)
Duration: <1s
Status: keep
Insight: C=42 gives +4.76 improvement. Strong indication that C has a sweet spot around 42.

## Experiment 1 — High A and B
Branch: research/blackbox-optimization / Type: real / Parent: #0
Hypothesis: High A and B together may produce synergy bonus
Changes: A=100, B=100 (was 50, 50)
Result: 75.919913 (was 67.133117, +8.786796)
Duration: <1s
Status: keep
Insight: A and B both being high significantly boosts score. Strong positive interaction between A and B confirmed.

## Experiment 0 — Baseline
Branch: research/blackbox-optimization / Type: real / Parent: -
Hypothesis: Record initial score with default parameters
Changes: None
Result: 67.133117
Duration: <1s
Status: keep
Insight: Baseline established. A=50, B=50, C=50, D=50, E=50 gives 67.133117. Will explore all 5 dimensions.

