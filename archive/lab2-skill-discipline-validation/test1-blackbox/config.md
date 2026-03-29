# Lab Config

## Objective
Maximize the score output from `python3 scorer.py`.

## Metrics
- **Primary metric**: score from `python3 scorer.py` (higher is better)
- **Measure command**: `python3 scorer.py`
- **Direction**: higher is better

## Scope
`config.txt` only — parameters A, B, C, D, E (range 0-100)

## Constraints
- All parameters must remain in range 0-100

## Run Command
`python3 scorer.py`

## Wall-clock Budget
1 minute per experiment

## Termination
20 experiments

## Baseline
- Experiment #0 — A=50, B=50, C=50, D=50, E=50
- Baseline score: 67.133117

## Best
- Experiment: #20
- Score: 89.499985
- Config: A=100, B=100, C=42, D=29.9999, E=55
