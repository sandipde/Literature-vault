---
title: Bayesian Optimization Outperforms Experts for Spectral Model Development
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15012162/v2
canonical_url: https://doi.org/10.26434/chemrxiv.15012162/v2
captured_by: auto-scanner
date: '2026-11-14'
captured_at: '2026-11-14T11:54:17+00:00'
last_requested: '2026-11-14T11:54:17+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Lennard D. Schulte
- Jörn Viell
- Eike Cramer
- Alexander Mitsos
- Luise F. Kaven
published: '2026-11-13'
abstract: Indirect Hard Modeling (IHM) is a physically motivated approach for quantitative
  spectral analysis that can account for nonlinear spectral changes, provides loweffort
  calibration, and allows extrapolation. However, realizing the full potential of
  IHM requires careful adjustment of model parameters and spectral preprocessing settings,
  which is typically performed manually and relies on expert knowledge. To address
  this limitation, we investigate Bayesian Optimization (BO) as a strategy for efficient
  IHM parameter tuning with mixed continuous, discrete, and categorical parameter
  spaces. We couple six alternative BO frameworks differing in surrogate model and
  sampling strategy with Peaxact, a state-of-the-art commercial software for IHM.
  We compare the calibration performance and computation time. We develop four spectroscopic
  models based on literature datasets. The corresponding IHM models in the form of
  published parameter settings serve only as benchmarks and are not used to initialize
  the optimization. We thus demonstrate that IHM models can be automatically optimized
  without expert intervention nor prior selected configurations. The results show
  that BO outperforms the published models, ranging from marginal changes to reductions
  of approximately 50% in cumulative cross-validation RMSE and approximately 60% in
  cumulative prediction RMSE, 1 with mean runtimes of approximately five hours or
  less on a standard desktop computer, supporting practical applicability. Moreover,
  the configurations obtained via BO partially agree with the expert-selected settings,
  indicating that BO can identify reasonable calibration settings from scratch. Overall,
  the findings demonstrate that BO can improve IHM model accuracy, reduce manual calibration
  effort, and support the broader use of IHM in spectroscopy.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15012162/v2
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Bayesian Optimization Outperforms Experts for Spectral Model Development

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15012162/v2
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Lennard D. Schulte, Jörn Viell, Eike Cramer, Alexander Mitsos, Luise F. Kaven
- **Published:** 2026-11-13

## Summary
Indirect Hard Modeling (IHM) is a physically motivated approach for quantitative spectral analysis that can account for nonlinear spectral changes, provides loweffort calibration, and allows extrapolation. However, realizing the full potential of IHM requires careful adjustment of model parameters and spectral preprocessing settings, which is typically performed manually and relies on expert knowledge. To address this limitation, we investigate Bayesian Optimization (BO) as a strategy for efficient IHM parameter tuning with mixed continuous, discrete, and categorical parameter spaces. We couple six alternative BO frameworks differing in surrogate model and sampling strategy with Peaxact, a state-of-the-art commercial software for IHM. We compare the calibration performance and computation time. We develop four spectroscopic models based on literature datasets. The corresponding IHM models in the form of published parameter settings serve only as benchmarks and are not used to initialize the optimization. We thus demonstrate that IHM models can be automatically optimized without expert intervention nor prior selected configurations. The results show that BO outperforms the published models, ranging from marginal changes to reductions of approximately 50% in cumulative cross-validation RMSE and approximately 60% in cumulative prediction RMSE, 1 with mean runtimes of approximately five hours or less on a standard desktop computer, supporting practical applicability. Moreover, the configurations obtained via BO partially agree with the expert-selected settings, indicating that BO can identify reasonable calibration settings from scratch. Overall, the findings demonstrate that BO can improve IHM model accuracy, reduce manual calibration effort, and support the broader use of IHM in spectroscopy.

## Provider details
- **Doi:** 10.26434/chemrxiv.15012162/v2
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
