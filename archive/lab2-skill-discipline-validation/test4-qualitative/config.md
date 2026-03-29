# Lab Configuration

- **Objective:** Improve error message quality for user experience
- **Primary metric:** Composite quality score (higher is better)
  - Measure: Multi-Evaluator Protocol (3 haiku subagents per experiment)
- **Rubric:**
  | Criterion | Weight | Scale | Definition |
  |-----------|--------|-------|------------|
  | Clarity | 0.30 | 1-10 | User immediately understands what happened |
  | Actionability | 0.30 | 1-10 | User knows exactly what to do next |
  | Tone | 0.20 | 1-10 | Empathetic, professional, not robotic or blame-shifting |
  | Brevity | 0.20 | 1-10 | No unnecessary words, respects user's time |
- **Run command:** N/A (qualitative)
- **Scope:** `error_message.txt`
- **Constraints:** Must remain a payment error message with error code and transaction ID
- **Wall-clock budget:** Unlimited per experiment
- **Termination:** 10 experiments
- **Baseline:** 7.10/10
- **Best:** 7.10/10 — experiment #0
