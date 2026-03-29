# Experiment Log

## Experiment 25 — A=14 Single Unit Below Center (Final)
Branch: research/inverted-assumptions / Type: real / Parent: #0
Hypothesis: A=14 (one below center) - final confirmation
Changes: A=14, B=10, C=20, D=5, E=15
Result: 94.208333
Duration: 1s
Status: discard
Insight: 94.2 < 95.0. All 25 experiments confirm [15,10,20,5,15] is the unique global maximum at 95.0.

## FINAL SUMMARY
- Global maximum: 95.0
- Optimal config: A=15, B=10, C=20, D=5, E=15
- Found at: Experiment #1
- Peak 1 max: 70.0 at [80,85,75,90,80]
- Peak 2 max: 95.0 at [15,10,20,5,15] (GLOBAL MAXIMUM)
- Confirmed: No hidden peaks, valley penalty region [30<avg<60] severely penalizes mixed configs
- 24 experiments explored without finding anything higher than 95.0

## Experiment 24 — Random Starting Point
Branch: research/inverted-assumptions / Type: real / Parent: #0
Hypothesis: Random [37,63,12,84,51] - confirm no hidden attractor basins
Changes: A=37, B=63, C=12, D=84, E=51
Result: 16.326476
Duration: 1s
Status: discard
Insight: avg=(37+63+12+84+51)/5=49.4, deep in valley. Score 16.3. No hidden basins.

## Experiment 23 — E=16 Single Unit Shift
Branch: research/inverted-assumptions / Type: real / Parent: #0
Hypothesis: E=16 instead of 15 - can any single unit shift beat 95?
Changes: A=15,B=10,C=20,D=5,E=16
Result: 94.208333
Duration: 1s
Status: discard
Insight: 94.2 < 95.0. Confirmed: exact center [15,10,20,5,15] is uniquely optimal. Single unit deviations reduce score.

## Experiment 22 — All 30s Valley Boundary
Branch: research/inverted-assumptions / Type: real / Parent: #0
Hypothesis: All 30s - avg exactly at valley boundary (30)
Changes: A=30, B=30, C=30, D=30, E=30
Result: 63.581703
Duration: 1s
Status: discard
Insight: 63.6 at valley boundary. The condition is 30 < avg < 60, so avg=30 exactly avoids valley (not strictly >30). Still much below 95.0.

## Experiment 21 — All -50 Extreme Negative
Branch: research/inverted-assumptions / Type: real / Parent: #0
Hypothesis: Extreme negative values - can unbounded negatives exceed 95?
Changes: A=-50, B=-50, C=-50, D=-50, E=-50
Result: 0
Duration: 1s
Status: discard
Insight: Score=0 because max(0, 1-dist2/120) = max(0, negative) = 0. Distance from peak2 center is too large. Negative values move further from both peaks.

## Re-Validation after Experiment 20
Re-ran current best HEAD (Peak2 center: A=15,B=10,C=20,D=5,E=15)
Result: 95.0 — matches recorded best. No drift. Global maximum confirmed.

## Experiment 19 — A=30 Others at Peak2 Center
Branch: research/inverted-assumptions / Type: real / Parent: #0
Hypothesis: A=30 (at valley boundary), others at peak2 center
Changes: A=30, B=10, C=20, D=5, E=15
Result: 83.125
Duration: 1s
Status: discard
Insight: 83.1 < 95.0. Moving A from 15 to 30 increases dist2 and decreases peak2. avg=(30+10+20+5+15)/5=16, still outside valley.

## Experiment 18 — All 90s Near Peak1
Branch: research/inverted-assumptions / Type: real / Parent: #0
Hypothesis: All 90s - near peak1 D value
Changes: A=90, B=90, C=90, D=90, E=90
Result: 60.100505
Duration: 1s
Status: discard
Insight: 60.1, below peak1 center (70.0) and peak2 (95.0). Confirmed both peaks are the best regions.

## Experiment 17 — Mixed High/Peak2 Values
Branch: research/inverted-assumptions / Type: real / Parent: #0
Hypothesis: A=60,B=10,C=70,D=5,E=60 - mix peak2 optimal B/D with high A/C/E
Changes: A=60, B=10, C=70, D=5, E=60
Result: 16.262111
Duration: 1s
Status: discard
Insight: avg=(60+10+70+5+60)/5=41, deep in valley range. Valley penalty heavy. No way to beat 95.0 this way.

## Experiment 16 — D=5 Only, Others=0 (Inverted Assumption)
Branch: research/inverted-assumptions / Type: real / Parent: #0
Hypothesis: Only D at peak2-optimal (5), others at extreme low (0)
Changes: A=0, B=0, C=0, D=5, E=0
Result: 70.599195
Duration: 1s
Status: discard
Insight: 70.6 - below 95.0. Confirms all 5 params must be close to center simultaneously.

## Fork: research/inverted-assumptions from baseline
Reason: Plateau guardrail triggered (global best unchanged for 14+ experiments since #1).
Inverted assumption: Instead of seeking known peaks, can unusual combinations beat 95.0?
Strategy: Test deeply asymmetric combinations, try valley exploitation, try one param at extreme while others optimized.

## Experiment 15 — All 5s Near Zero
Branch: research/grid-sampling / Type: real / Parent: #0
Hypothesis: All 5s - near zero, close to peak2 footprint
Changes: A=5, B=5, C=5, D=5, E=5
Result: 78.206214
Duration: 1s
Status: discard
Insight: All 5s gives 78.2. dist2 from [15,10,20,5,15] = sqrt(100+25+225+0+100)=sqrt(450)≈21.2, peak2=95*(1-21.2/120)=95*0.82=77.9 (close). Below 95.0 at center.

## Experiment 14 — Peak2 Center Except E=100
Branch: research/grid-sampling / Type: real / Parent: #0
Hypothesis: Peak2 center on ABCD, E=100 - test asymmetric scoring
Changes: A=15,B=10,C=20,D=5,E=100
Result: 27.708333
Duration: 1s
Status: discard
Insight: dist2 jumps to sqrt(0+0+0+0+(100-15)^2) = 85, peak2=95*(1-85/120)=27.7. Setting even one param far from center drastically drops score. All 5 must be near center.

## Experiment 13 — +5 from Peak2 Center
Branch: research/grid-sampling / Type: real / Parent: #0
Hypothesis: [20,15,25,10,20] - move +5 from peak2 center
Changes: A=20, B=15, C=25, D=10, E=20
Result: 86.148898
Duration: 1s
Status: discard
Insight: Confirms gradient toward peak2 center - 86.1 is lower than 95.0. Approaching center increases score monotonically.

## Experiment 12 — All 25s Grid Point
Branch: research/grid-sampling / Type: real / Parent: #0
Hypothesis: All 25s between the two peaks - explore gradient
Changes: A=25, B=25, C=25, D=25, E=25
Result: 71.919149
Duration: 1s
Status: discard
Insight: 71.9 is actually on the peak2 slope - avg=25 is just outside valley range (30-60). dist2≈29.15, peak2=71.9. Confirms peak2 slope extends to this region but still below 95.0 at center.

## Experiment 11 — All 100s Corner
Branch: research/grid-sampling / Type: real / Parent: #0
Hypothesis: All 100s extreme corner exploration
Changes: A=100, B=100, C=100, D=100, E=100
Result: 50.477933
Duration: 1s
Status: discard
Insight: dist1 from [80,85,75,90,80] = sqrt(20^2+15^2+25^2+10^2+20^2) = sqrt(400+225+625+100+400)=sqrt(1750)~41.8, peak1=70*(1-41.8/150)=70*0.72=50.5. Matches! No hidden peaks at corners.

## Re-Validation after Experiment 10
Re-ran current HEAD (experiment #1 config: A=15,B=10,C=20,D=5,E=15)
Result: 95.0 — matches recorded best. No drift. System stable.

## Experiment 9 — High B Corner
Branch: research/peak2-fine-tuning / Type: real / Parent: #0
Hypothesis: A=0,B=100 corner - explore for hidden peaks
Changes: A=0, B=100, C=0, D=0, E=0
Result: 20.000289
Duration: 1s
Status: discard
Insight: High B corner gives low score. No hidden peaks in this region.

## Experiment 8 — Fractional Perturbation +0.001
Branch: research/peak2-fine-tuning / Type: real / Parent: #1
Hypothesis: Tiny +0.001 offset on all params - test floating point behavior
Changes: All params +0.001 from center
Result: 94.99823
Duration: 1s
Status: discard
Insight: Any movement from exact center reduces score. 95.0 is the absolute maximum.

## Fork: research/peak2-fine-tuning from exp#1
Reason: 6 discards in a row (guardrail triggered). Forking to fine-tune around Peak 2 center.
Hypothesis to test: Can fractional offsets from center create any score above 95.0 due to floating point?
Strategy: Grid search with small perturbations and fractional values.

## Experiment 7 — Mixed Peak1+Peak2 Values
Branch: research/two-peak-optimization / Type: real / Parent: #0
Hypothesis: A=15,B=85,C=20,D=90,E=15 - mix peak1/peak2 values
Changes: A=15,B=85,C=20,D=90,E=15
Result: 0.010001
Duration: 1s
Status: discard
Insight: Mixed values give nearly 0. avg=(15+85+20+90+15)/5=45, which is in valley range [30,60]. Valley penalty at avg=45: valley=20*(1-|45-45|/15)=20. Both peaks are far from these mixed values. Confirms two-peak structure with strong valley penalty in middle.

## Experiment 6 — Extreme A Corner
Branch: research/two-peak-optimization / Type: real / Parent: #0
Hypothesis: A=100, others=0 - probe extreme corner for hidden peaks
Changes: A=100, B=0, C=0, D=0, E=0
Result: 24.301906
Duration: 1s
Status: discard
Insight: No hidden peak here. Peak2 center remains global maximum.

## Experiment 5 — Negative D Boundary Test
Branch: research/two-peak-optimization / Type: real / Parent: #1
Hypothesis: Negative D - test if scorer enforces constraints
Changes: D=-5 (others same as peak2 center)
Result: 87.083333
Duration: 1s
Status: discard
Insight: Scorer doesn't enforce constraints - accepted negative D. But score is lower (87.08 vs 95.0). Peak2 center D=5 is still the optimal D value. Negative values move further from center [15,10,20,5,15].

## Experiment 4 — All Zeros Boundary Test
Branch: research/two-peak-optimization / Type: real / Parent: #1
Hypothesis: All zeros - boundary test for scoring behavior
Changes: A=0, B=0, C=0, D=0, E=0
Result: 70.280216
Duration: 1s
Status: discard
Insight: All zeros gives 70.28 - interesting! This is because avg=0 so no valley penalty, and dist from peak2 center [15,10,20,5,15] is sqrt(15^2+10^2+20^2+5^2+15^2)=sqrt(225+100+400+25+225)=sqrt(975)≈31.2, so peak2=95*(1-31.2/120)≈70.3. That matches. Still lower than 95.0 at exact center.

## Experiment 3 — Peak 1 Center Verification
Branch: research/two-peak-optimization / Type: real / Parent: #0
Hypothesis: Peak 1 center [80,85,75,90,80] should yield ~70 pts (lower than peak2)
Changes: A=80, B=85, C=75, D=90, E=80
Result: 70.0
Duration: 1s
Status: discard
Insight: Peak 1 confirmed at 70.0 max. Peak 2 at 95.0 is the global maximum. Returning to Peak 2 best config.

## Experiment 2 — Peak 2 Slight Shift Down
Branch: research/two-peak-optimization / Type: real / Parent: #1
Hypothesis: Slight -1 shift on all params - confirm 95.0 is the true max
Changes: A=14, B=9, C=19, D=4, E=14
Result: 93.22978
Duration: 1s
Status: discard
Insight: Lower score confirms center [15,10,20,5,15] gives maximum for Peak 2. The function falls off as distance increases from center.

## Experiment 1 — Peak 2 Center
Branch: research/two-peak-optimization / Type: real / Parent: #0
Hypothesis: Peak 2 center [15,10,20,5,15] should yield ~95 pts
Changes: A=15, B=10, C=20, D=5, E=15
Result: 95.0
Duration: 1s
Status: keep
Insight: Achieved exact theoretical maximum for Peak 2. This is 95.0 - the formula max(peak1,peak2)-valley gives exactly 95 at center with no valley penalty (avg=13, well outside [30,60]). Need to verify if this is truly the global max or if there are even higher values possible.

## Experiment 0 — Baseline
Branch: research/two-peak-optimization / Type: real / Parent: -
Hypothesis: Baseline measurement with default config
Changes: None
Result: 22.853454
Duration: 1s
Status: baseline
Insight: Default config (all 50s) hits the valley penalty region (avg=50, in [30,60] range). Score is low. Two known peaks: Peak1 ~70pts at [80,85,75,90,80], Peak2 ~95pts at [15,10,20,5,15]. Must explore Peak 2 first as it has higher maximum.

