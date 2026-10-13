---
title: Reaction-Level Machine Learning for Condition Optimization in Suzuki–Miyaura
  Cross-Coupling
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010362/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15010362/v1
captured_by: auto-scanner
date: '2026-10-13'
captured_at: '2026-10-13T12:25:46+00:00'
last_requested: '2026-10-13T12:25:46+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Pranav Manne
published: '2026-10-13'
abstract: 'Selecting the ligand, base and solvent for a Suzuki–Miyaura coupling remains
  largely empirical, and highthroughput experimentation (HTE) screens are usually
  mined only for one reaction’s best condition. This study tests whether condition–yield
  relationships learned from some reactions transfer to reactions a model has never
  seen. Using a published HTE dataset of 5,760 reactions (15 quinoline couplings ×
  384 ligandbase–solvent combinations), models were trained in MATLAB on categorical
  condition descriptors with whole reactions held out: a global strategy trained on
  12 reactions and was tested on 3; a focused strategy trained on 3 reactions sharing
  a boronic acid and was tested on a fourth. Selected models were compared with a
  majority-class predictor and a no-learning condition-average ranker, with 95% bootstrap
  confidence intervals. Ranking transferred: high-yield (≥62%) precision–recall AUC
  was 0.21–0.34 where only 6–8% of conditions were high-yield and 0.92–0.96 where
  most were, above the base rate on every held-out reaction. However, the condition-average
  ranker matched the trained models within overlapping confidence intervals on all
  four held-out reactions, so what transfers is mainly the persistence of good-on-average
  conditions. At a fixed 62% cut-off, a RUSBoosted ensemble flagged 58–96% of high-yield
  conditions against 6–27% for the untuned average. Accuracy misled: naive Bayes scored
  94.8% where always predicting low yield scores 94.3%. Exact yields did not transfer
  (external R2 at or below zero on most reactions), and focusing the training set
  left ranking unchanged (PR-AUC 0.943 vs 0.942). Reaction-level splits, minority-class
  metrics and a condition-average baseline should be standard when evaluating models
  on HTE data.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010362/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Reaction-Level Machine Learning for Condition Optimization in Suzuki–Miyaura Cross-Coupling

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010362/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Pranav Manne
- **Published:** 2026-10-13

## Summary
Selecting the ligand, base and solvent for a Suzuki–Miyaura coupling remains largely empirical, and highthroughput experimentation (HTE) screens are usually mined only for one reaction’s best condition. This study tests whether condition–yield relationships learned from some reactions transfer to reactions a model has never seen. Using a published HTE dataset of 5,760 reactions (15 quinoline couplings × 384 ligandbase–solvent combinations), models were trained in MATLAB on categorical condition descriptors with whole reactions held out: a global strategy trained on 12 reactions and was tested on 3; a focused strategy trained on 3 reactions sharing a boronic acid and was tested on a fourth. Selected models were compared with a majority-class predictor and a no-learning condition-average ranker, with 95% bootstrap confidence intervals. Ranking transferred: high-yield (≥62%) precision–recall AUC was 0.21–0.34 where only 6–8% of conditions were high-yield and 0.92–0.96 where most were, above the base rate on every held-out reaction. However, the condition-average ranker matched the trained models within overlapping confidence intervals on all four held-out reactions, so what transfers is mainly the persistence of good-on-average conditions. At a fixed 62% cut-off, a RUSBoosted ensemble flagged 58–96% of high-yield conditions against 6–27% for the untuned average. Accuracy misled: naive Bayes scored 94.8% where always predicting low yield scores 94.3%. Exact yields did not transfer (external R2 at or below zero on most reactions), and focusing the training set left ranking unchanged (PR-AUC 0.943 vs 0.942). Reaction-level splits, minority-class metrics and a condition-average baseline should be standard when evaluating models on HTE data.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010362/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
