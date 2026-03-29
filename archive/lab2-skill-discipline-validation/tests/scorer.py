#!/usr/bin/env python3
"""
Deceptive landscape scorer for researcher skill discipline validation.

Local optimum: A,B,C,D,E all high (>70) → ~75 pts
  - Gradient always points "up" — higher values = more points
  - Synergy bonus for all-high makes it sticky
  - Agent will naturally push everything high and plateau

Global optimum: A,B low (~10), C,D,E specific (~55,25,65) → ~95 pts
  - Average ≈ 32, below valley floor
  - Requires inverting "higher is better" for A and B
  - Only reachable by jumping, not walking

Valley: average 35–65 → penalty up to -30 pts
  - Separates local (avg ~75) from global (avg ~32)
  - Cannot walk between them without score collapse
"""

def score(a, b, c, d, e):
    params = [a, b, c, d, e]
    avg = sum(params) / 5.0

    # --- Local peak: rewards high values, tops at ~75 ---
    local = 0.0
    local += 14 * (a / 100) ** 0.6
    local += 14 * (b / 100) ** 0.6
    local += 14 * (c / 100) ** 0.6
    local += 10 * (d / 100) ** 0.6
    local += 10 * (e / 100) ** 0.6
    # Synergy: all above 60 → +15 (makes local sticky)
    if all(p > 60 for p in params):
        local += 15
    # Consistency: spread < 25 → +3
    if max(params) - min(params) < 25:
        local += 3
    # Max local ≈ 14*3 + 10*2 + 15 + 3 = 80 (but realistic best ~75)

    # --- Global peak: centered at [10, 8, 55, 25, 65], avg=32.6 ---
    gc = [10, 8, 55, 25, 65]
    widths = [12, 12, 18, 18, 18]
    global_s = 0.0
    for p, center, w in zip(params, gc, widths):
        dist = abs(p - center) / w
        global_s += 19 * max(0, 1 - dist ** 2)
    # Max = 5 * 19 = 95

    # --- Valley: avg 35–65 → penalty up to -30 ---
    valley = 0.0
    if 35 < avg < 65:
        valley = 30 * max(0, 1 - ((avg - 50) / 15) ** 2)

    raw = max(local, global_s) - valley
    return max(0, round(raw, 6))


if __name__ == "__main__":
    params = {}
    with open("config.txt") as f:
        for line in f:
            if "=" in line:
                k, v = line.strip().split("=")
                params[k.strip()] = float(v.strip())

    print(score(params['A'], params['B'], params['C'], params['D'], params['E']))
