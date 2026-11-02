---
title: Construction of a Curated Literature Dataset and Machine Learning-Guided Exploration
  of Supported Metal Catalysts for Low- to Intermediate-Temperature Reverse Water–Gas
  Shift Reaction
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011499/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011499/v1
captured_by: auto-scanner
date: '2026-11-02'
captured_at: '2026-11-02T13:02:05+00:00'
last_requested: '2026-11-02T13:02:05+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Umi Shin
- Shinya Mine
- Aritomo Yamaguchi
- Toshiaki Taira
published: '2026-11-02'
abstract: Literature-derived results on reverse water–gas shift (RWGS) catalysts contain
  extensive information about catalyst design, yet their fragmentation makes systematic,
  data-driven exploration difficult. Here, we establish a framework that connects
  a curated RWGS literature dataset to interpretable machine-learning (ML) models
  and a flexible catalyst-search algorithm. We compiled 607 experimental records from
  42 publications on supported metal and metal oxide catalysts evaluated at 300–450
  °C, integrating catalyst compositions, preparation and reaction conditions, and
  CO yields. By systematically comparing nine regression algorithms and nine input
  representations, we obtained mean cross-validated test R2 values of 0.80, 0.73,
  and 0.58 for models optimized for the full, 300 °C, and 400 °C datasets, respectively.
  SHAP analysis identified compositional and experimental features contributing to
  model predictions, while leave-one-out validation exposed substantial prediction
  errors in some literature records. In offline sequential-search simulations repeated
  100 times, ML-guided search identified high-yield literature entries more efficiently
  than random selection. Importantly, our newly developed Local-search algorithm jointly
  explored elemental combinations, loadings, support materials, and experimental conditions
  without exhaustive enumeration, generating candidates beyond the compositions represented
  in the training data. The 300 °C search favored Pt–Na/ZrO2-containing candidates,
  whereas Pd–Na/CeO2-containing candidates predominated at 400 °C. Although these
  predictions await experimental validation and some violate RWGS equilibrium constraints,
  this integrated framework provides a reusable data resource and a practical route
  from accumulated literature knowledge to testable catalyst-design hypotheses.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011499/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Construction of a Curated Literature Dataset and Machine Learning-Guided Exploration of Supported Metal Catalysts for Low- to Intermediate-Temperature Reverse Water–Gas Shift Reaction

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011499/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Umi Shin, Shinya Mine, Aritomo Yamaguchi, Toshiaki Taira
- **Published:** 2026-11-02

## Summary
Literature-derived results on reverse water–gas shift (RWGS) catalysts contain extensive information about catalyst design, yet their fragmentation makes systematic, data-driven exploration difficult. Here, we establish a framework that connects a curated RWGS literature dataset to interpretable machine-learning (ML) models and a flexible catalyst-search algorithm. We compiled 607 experimental records from 42 publications on supported metal and metal oxide catalysts evaluated at 300–450 °C, integrating catalyst compositions, preparation and reaction conditions, and CO yields. By systematically comparing nine regression algorithms and nine input representations, we obtained mean cross-validated test R2 values of 0.80, 0.73, and 0.58 for models optimized for the full, 300 °C, and 400 °C datasets, respectively. SHAP analysis identified compositional and experimental features contributing to model predictions, while leave-one-out validation exposed substantial prediction errors in some literature records. In offline sequential-search simulations repeated 100 times, ML-guided search identified high-yield literature entries more efficiently than random selection. Importantly, our newly developed Local-search algorithm jointly explored elemental combinations, loadings, support materials, and experimental conditions without exhaustive enumeration, generating candidates beyond the compositions represented in the training data. The 300 °C search favored Pt–Na/ZrO2-containing candidates, whereas Pd–Na/CeO2-containing candidates predominated at 400 °C. Although these predictions await experimental validation and some violate RWGS equilibrium constraints, this integrated framework provides a reusable data resource and a practical route from accumulated literature knowledge to testable catalyst-design hypotheses.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011499/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
