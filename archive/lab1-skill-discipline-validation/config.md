# Lab Configuration

- **Objective:** Improve researcher.md skill quality based on LLM compliance research findings
- **Primary metric:** Composite quality score (higher is better)
  - Measure: agent judgment with rubric
- **Rubric:**
  | Criterion | Weight | Scale | Definition |
  |-----------|--------|-------|------------|
  | Clarity | 0.25 | 1-10 | Agent unambiguously knows what to do at every step |
  | Completeness | 0.20 | 1-10 | No missing edge cases or scenarios |
  | Conciseness | 0.25 | 1-10 | No redundancy, minimal token count for same information |
  | Structure effectiveness | 0.15 | 1-10 | Flow is logical, critical rules positioned optimally (primacy/recency) |
  | Robustness | 0.15 | 1-10 | Skill resists LLM attention decay, sycophancy, instruction drift |
- **Secondary metrics:** Token count (lower is better), Line count (lower is better)
- **Run command:** N/A — qualitative research
- **Scope:** researcher.md, README.md
- **Constraints:** None
- **Time budget:** Unlimited per experiment
- **Termination:** Infinite (until user interrupts)
- **Baseline:** 6.25/10 (clarity=7, completeness=8, conciseness=5, structure=6, robustness=5) | 345 lines, 2644 words
- **Best:** 9.23/10 — experiment #17, research/improve-researcher-skill
