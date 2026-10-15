---
title: A MACHINE-LEARNING BENCHMARK FOR SOLAR FLARE FORECASTING USING SDO/HMI ACTIVE-REGION
  PARAMETERS
type: paper
source: https://doi.org/10.2139/ssrn.7615933
canonical_url: https://doi.org/10.2139/ssrn.7615933
captured_by: auto-scanner
date: '2026-10-15'
captured_at: '2026-10-15T20:09:48+00:00'
last_requested: '2026-10-15T20:09:48+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Deepak Pandey
- Garima Punetha
published: '2026-10-15'
abstract: Solar-flare forecasting is a rare-event classification problem in which
  measured machine-learning skill depends on both algorithm choice and experimental
  design. This study performs a controlled comparison of logistic regression (LR),
  a calibrated linear support vector machine (SVM), random forest (RF), a feed-forward
  artificial neural network (ANN), and a long short-term memory (LSTM) network using
  a public SDO/HMI SHARP–GOES dataset spanning 1 January 2023–31 May 2025. The primary
  task is 24 h prediction of M- or X-class activity from nine normalized SHARP magnetic
  parameters. Padding records were removed from the static experiment, the supplied
  chronological test set was retained as a future-time holdout, and three active regions
  appearing in both supplied partitions were excluded from the final test set. The
  development data were split by HARP identifier into 220 training and 55 validation
  active regions; the final independent test contained 14,055 forecast records from
  32 active regions, including 2,203 positive cases. Decision thresholds were selected
  on validation data by maximum True Skill Statistic (TSS) and then frozen. On the
  independent temporal test, the linear SVM achieved the highest TSS (0.297), closely
  followed by LR (0.292) and LSTM (0.258); RF and ANN obtained TSS values of 0.118
  and 0.017, respectively. LR and SVM produced similar ROC-AUC values (0.658), whereas
  LSTM achieved the highest ROC-AUC (0.672) but lower event detection at its frozen
  threshold. Grouped bootstrap intervals were wide because only 32 independent test
  active regions were available. Feature-group ablation of LR showed the largest reduction
  in PR-AUC when current/helicity variables were removed (ΔPR-AUC = -0.046). These
  results show that, for this recent-cycle dataset, simple linear classifiers remain
  competitive with more complex models and that active-region-independent temporal
  evaluation materially constrains claims of state-of-the-art performance.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.2139/ssrn.7615933
  journal: ''
  publisher: Elsevier BV
  type: posted-content
  subjects: []
---

# A MACHINE-LEARNING BENCHMARK FOR SOLAR FLARE FORECASTING USING SDO/HMI ACTIVE-REGION PARAMETERS

- **Type:** paper
- **Source:** https://doi.org/10.2139/ssrn.7615933
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Deepak Pandey, Garima Punetha
- **Published:** 2026-10-15

## Summary
Solar-flare forecasting is a rare-event classification problem in which measured machine-learning skill depends on both algorithm choice and experimental design. This study performs a controlled comparison of logistic regression (LR), a calibrated linear support vector machine (SVM), random forest (RF), a feed-forward artificial neural network (ANN), and a long short-term memory (LSTM) network using a public SDO/HMI SHARP–GOES dataset spanning 1 January 2023–31 May 2025. The primary task is 24 h prediction of M- or X-class activity from nine normalized SHARP magnetic parameters. Padding records were removed from the static experiment, the supplied chronological test set was retained as a future-time holdout, and three active regions appearing in both supplied partitions were excluded from the final test set. The development data were split by HARP identifier into 220 training and 55 validation active regions; the final independent test contained 14,055 forecast records from 32 active regions, including 2,203 positive cases. Decision thresholds were selected on validation data by maximum True Skill Statistic (TSS) and then frozen. On the independent temporal test, the linear SVM achieved the highest TSS (0.297), closely followed by LR (0.292) and LSTM (0.258); RF and ANN obtained TSS values of 0.118 and 0.017, respectively. LR and SVM produced similar ROC-AUC values (0.658), whereas LSTM achieved the highest ROC-AUC (0.672) but lower event detection at its frozen threshold. Grouped bootstrap intervals were wide because only 32 independent test active regions were available. Feature-group ablation of LR showed the largest reduction in PR-AUC when current/helicity variables were removed (ΔPR-AUC = -0.046). These results show that, for this recent-cycle dataset, simple linear classifiers remain competitive with more complex models and that active-region-independent temporal evaluation materially constrains claims of state-of-the-art performance.

## Provider details
- **Doi:** 10.2139/ssrn.7615933
- **Publisher:** Elsevier BV
- **Type:** posted-content
