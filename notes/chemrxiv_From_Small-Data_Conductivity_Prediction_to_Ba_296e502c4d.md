---
title: From Small-Data Conductivity Prediction to Bayesian Optimization of Electrolyte
  Formulations with a Tabular Foundation Model
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011969/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011969/v1
captured_by: auto-scanner
date: '2026-11-11'
captured_at: '2026-11-11T12:22:55+00:00'
last_requested: '2026-11-11T12:22:55+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Yuqi He
- Xufengyu Huang
published: '2026-11-11'
abstract: 'We evaluate whether a frozen tabular foundation model, TabPFN, can use
  limited measurements to predict conductivity and guide electrolyte formulation search
  without explicit transport equations or task-specific physics-constrained training.
  On the AMPERE conductivity dataset, 40 labeled context samples yield a mean absolute
  percentage error (MAPE) of 5.56% on 60 held-out measurements, close to the 5.32%
  reported for the original physics-augmented AMPERE model and below the conventional
  regression baselines under locally matched conditions. Additional evaluations on
  CALiSol-23, Flores, ionic-liquid, and polymer-electrolyte datasets support broader
  predictive applicability, while target-domain measurements improve shifted-domain
  predictions through context updates alone. The main Bayesian optimization application
  revisits the AMPERE rate-performance search setting: TabPFN-predicted conductivity
  and operating salt concentration form a two-dimensional representation for a separate
  Gaussian process (GP) surrogate. Across two temperatures, measured-pool replays
  require 13.90 evaluations on average to find the best measured formulation, reducing
  cost by 45.6% relative to random search and 9.1% relative to composition inputs.
  Two further applications examine TabPFN as a direct objective surrogate. In sequential
  Clio conductivity replay, a fixed acquisition rule requires 11.5 evaluations on
  ten new starts, 38.2% fewer than random search and close to independently selected
  GP (11.0). In the ionic-polymer study, seven initial measurements support ranking
  the source study''s recommended formulation at 21–27 among 497 candidates, versus
  44 for Gaussian process regression. Together, these cases show how context-based
  prediction can support candidate selection through property-informed representations
  and direct objective surrogates.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011969/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# From Small-Data Conductivity Prediction to Bayesian Optimization of Electrolyte Formulations with a Tabular Foundation Model

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011969/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Yuqi He, Xufengyu Huang
- **Published:** 2026-11-11

## Summary
We evaluate whether a frozen tabular foundation model, TabPFN, can use limited measurements to predict conductivity and guide electrolyte formulation search without explicit transport equations or task-specific physics-constrained training. On the AMPERE conductivity dataset, 40 labeled context samples yield a mean absolute percentage error (MAPE) of 5.56% on 60 held-out measurements, close to the 5.32% reported for the original physics-augmented AMPERE model and below the conventional regression baselines under locally matched conditions. Additional evaluations on CALiSol-23, Flores, ionic-liquid, and polymer-electrolyte datasets support broader predictive applicability, while target-domain measurements improve shifted-domain predictions through context updates alone. The main Bayesian optimization application revisits the AMPERE rate-performance search setting: TabPFN-predicted conductivity and operating salt concentration form a two-dimensional representation for a separate Gaussian process (GP) surrogate. Across two temperatures, measured-pool replays require 13.90 evaluations on average to find the best measured formulation, reducing cost by 45.6% relative to random search and 9.1% relative to composition inputs. Two further applications examine TabPFN as a direct objective surrogate. In sequential Clio conductivity replay, a fixed acquisition rule requires 11.5 evaluations on ten new starts, 38.2% fewer than random search and close to independently selected GP (11.0). In the ionic-polymer study, seven initial measurements support ranking the source study's recommended formulation at 21–27 among 497 candidates, versus 44 for Gaussian process regression. Together, these cases show how context-based prediction can support candidate selection through property-informed representations and direct objective surrogates.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011969/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
