# Branch Registry

| Branch | Forked from | Status | Experiments | Best metric | Notes |
|--------|-------------|--------|-------------|-------------|-------|
| research/two-peak-optimization | main | active | 1-7 | 95.0 | Main research branch; found global max at exp#1 |
| research/peak2-fine-tuning | exp#1 (96d50a9) | done | 8-10 | 95.0 | Fine-tuning confirmed 95.0 is ceiling |
| research/grid-sampling | baseline (b5b9134) | done | 11-15 | 78.206 | Confirmed no hidden peaks; peak2 center remains global max |
| research/inverted-assumptions | baseline (b5b9134) | active | - | - | Plateau guardrail triggered; inverted assumptions: avoid known peaks |
