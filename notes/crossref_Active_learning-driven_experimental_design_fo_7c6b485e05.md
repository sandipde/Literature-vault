---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Mathematics and algorithms
enrichment_tags: [active-learning, gaussian-processes, multi-objective-optimization, torrefaction]
title: Active learning-driven experimental design for torrefaction process optimization
  using multi-objective Gaussian process surrogates
type: paper
source: https://doi.org/10.21203/rs.3.rs-11027924/v1
canonical_url: https://doi.org/10.21203/rs.3.rs-11027924/v1
captured_by: auto-scanner
date: '2026-10-19'
captured_at: '2026-10-19T10:27:53+00:00'
last_requested: '2026-10-19T10:27:53+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Mohammed R. AlAttar¹
- Amr Y. Elbanhawy¹
- Zakaria Ghoneim²
published: '2026-10-19'
abstract: Abstract Data-driven optimization of biomass torrefaction is constrained
  by the high cost and time required for experimental exploration. We present an active
  learning framework that couples Gaussian Process Regression (GPR) surrogates with
  a multi-objective acquisition function to recommend the most informative next experiments
  for improving mass yield, higher heating value (HHV), and energy yield (EY). Using
  486 torrefaction observations, GPR models with automatic relevance determination
  (ARD) kernels achieved cross-validated R² values of 0.854 (mass yield), 0.971 (HHV),
  and 0.869 (EY), outperforming random forest, support vector regression, and neural
  networks. A hybrid acquisition function balanced uncertainty reduction (40%) with
  expected improvement for mass yield (30%) and HHV (30%), while diversity-aware batch
  selection (K = 10) ensured spatial coverage. Cross-validated calibration confirmed
  93.2% coverage for mass yield. ARD length scales identified temperature and residence
  time as dominant features. The recommended batch spans 200–315°C and 30–1089 s within
  the conventional torrefaction regime. Ablation and sensitivity analyses demonstrated
  component contributions and robustness. The Pareto front shows recommended points
  near the trade-off curve. This interpretable, uncertainty-aware framework provides
  a systematic methodology for accelerating torrefaction process development.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.21203/rs.3.rs-11027924/v1
  journal: ''
  publisher: Springer Science and Business Media LLC
  type: posted-content
  subjects: []
---

# Active learning-driven experimental design for torrefaction process optimization using multi-objective Gaussian process surrogates

- **Type:** paper
- **Source:** https://doi.org/10.21203/rs.3.rs-11027924/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Mohammed R. AlAttar¹, Amr Y. Elbanhawy¹, Zakaria Ghoneim²
- **Published:** 2026-10-19

## Summary
Abstract Data-driven optimization of biomass torrefaction is constrained by the high cost and time required for experimental exploration. We present an active learning framework that couples Gaussian Process Regression (GPR) surrogates with a multi-objective acquisition function to recommend the most informative next experiments for improving mass yield, higher heating value (HHV), and energy yield (EY). Using 486 torrefaction observations, GPR models with automatic relevance determination (ARD) kernels achieved cross-validated R² values of 0.854 (mass yield), 0.971 (HHV), and 0.869 (EY), outperforming random forest, support vector regression, and neural networks. A hybrid acquisition function balanced uncertainty reduction (40%) with expected improvement for mass yield (30%) and HHV (30%), while diversity-aware batch selection (K = 10) ensured spatial coverage. Cross-validated calibration confirmed 93.2% coverage for mass yield. ARD length scales identified temperature and residence time as dominant features. The recommended batch spans 200–315°C and 30–1089 s within the conventional torrefaction regime. Ablation and sensitivity analyses demonstrated component contributions and robustness. The Pareto front shows recommended points near the trade-off curve. This interpretable, uncertainty-aware framework provides a systematic methodology for accelerating torrefaction process development.

## Provider details
- **Doi:** 10.21203/rs.3.rs-11027924/v1
- **Publisher:** Springer Science and Business Media LLC
- **Type:** posted-content

## AI enrichment
- **Concise summary:** A torrefaction optimization preprint fits Gaussian-process surrogates to 486 observations and recommends diverse batches using a weighted uncertainty/improvement acquisition function.
- **Why it matters:** It illustrates uncertainty-aware experiment design with explicit trade-offs between mass yield and heating value rather than a single best-point search.
- **Caveat:** Cross-validation and recommended points are described, not prospective confirmation that the proposed batch improves a real process; the acquisition weights are study-specific choices.
- **Evidence:** [Captured source](https://doi.org/10.21203/rs.3.rs-11027924/v1); analysis based only on captured metadata, not independently verified full text.
