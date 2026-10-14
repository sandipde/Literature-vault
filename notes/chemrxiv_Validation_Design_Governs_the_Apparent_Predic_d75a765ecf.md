---
title: Validation Design Governs the Apparent Predictive Performance of Machine Learning
  for PLGA Drug Release
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010439/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15010439/v1
captured_by: auto-scanner
date: '2026-10-14'
captured_at: '2026-10-14T09:53:53+00:00'
last_requested: '2026-10-14T09:53:53+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Tengxiao Liu
- Juchen Zhang
- Hongtao Sun
published: '2026-10-14'
abstract: Reliable generalization is essential for machine-learning models intended
  to predict drug-release behavior across heterogeneous experimental settings. However,
  multi-study experimental data often contain closely related formulations generated
  under shared materials, processing conditions, release protocols, and laboratory
  practices, creating hidden dependencies between training and test data. Such dependencies
  can make model performance appear stronger than its ability to generalize to genuinely
  new experimental domains. Here, we examine how validation topology governs the apparent
  predictability of poly(lactic-co-glycolic acid) (PLGA) microparticle drug release
  using a public dataset containing 321 formulations and 4,913 release observations
  collected across 113 studies. Using a common LightGBM prediction framework, we compare
  validation schemes ranging from random observation splitting to strict study-grouped
  holdout. Predictive performance decreases markedly as train–test independence becomes
  more stringent, with 𝑅! declining from 0.939 under random point splitting to 0.616–0.625
  under formulation-level holdout and 0.372 when entire studies are withheld. Controlled
  overlap experiments further show that retaining samestudy sibling formulations in
  the training set systematically increases apparent performance, while nearest-neighbor
  analysis reveals lower prediction error for formulations lying closer to the training
  distribution, particularly when their nearest training counterpart originates from
  the same study. These results show that formulation-level independence alone does
  not ensure experimental-domain independence and demonstrate that apparent drug-release
  predictability is strongly conditioned by validation design. Study-aware validation
  therefore provides a more rigorous basis for assessing generalization of machine-learning
  models trained on heterogeneous multi-study experimental data.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010439/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Validation Design Governs the Apparent Predictive Performance of Machine Learning for PLGA Drug Release

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010439/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Tengxiao Liu, Juchen Zhang, Hongtao Sun
- **Published:** 2026-10-14

## Summary
Reliable generalization is essential for machine-learning models intended to predict drug-release behavior across heterogeneous experimental settings. However, multi-study experimental data often contain closely related formulations generated under shared materials, processing conditions, release protocols, and laboratory practices, creating hidden dependencies between training and test data. Such dependencies can make model performance appear stronger than its ability to generalize to genuinely new experimental domains. Here, we examine how validation topology governs the apparent predictability of poly(lactic-co-glycolic acid) (PLGA) microparticle drug release using a public dataset containing 321 formulations and 4,913 release observations collected across 113 studies. Using a common LightGBM prediction framework, we compare validation schemes ranging from random observation splitting to strict study-grouped holdout. Predictive performance decreases markedly as train–test independence becomes more stringent, with 𝑅! declining from 0.939 under random point splitting to 0.616–0.625 under formulation-level holdout and 0.372 when entire studies are withheld. Controlled overlap experiments further show that retaining samestudy sibling formulations in the training set systematically increases apparent performance, while nearest-neighbor analysis reveals lower prediction error for formulations lying closer to the training distribution, particularly when their nearest training counterpart originates from the same study. These results show that formulation-level independence alone does not ensure experimental-domain independence and demonstrate that apparent drug-release predictability is strongly conditioned by validation design. Study-aware validation therefore provides a more rigorous basis for assessing generalization of machine-learning models trained on heterogeneous multi-study experimental data.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010439/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
