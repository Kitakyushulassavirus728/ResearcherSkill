# Lab Config

## Objective
Maximize score from `python3 scorer.py`

## Primary Metric
score (higher is better)

## Scope
config.txt only (parameters A, B, C, D, E, range 0-100)

## Constraints
All parameters must be in range [0, 100]

## Run Command
`python3 scorer.py`

## Budget
1 minute per experiment, 25 experiments total

## Baseline
Experiment #0: A=50, B=50, C=50, D=50, E=50
Baseline score: 22.853454

## Landscape Notes
Two peaks discovered from scorer.py inspection:
- Peak 1: centered at [80, 85, 75, 90, 80], max ~70 pts
- Peak 2: centered at [15, 10, 20, 5, 15], max ~95 pts
- Valley penalty when avg is 30 < avg < 60 (up to -20 pts)
- Strategy: Must explore BOTH peaks, prefer Peak 2 (higher max)
