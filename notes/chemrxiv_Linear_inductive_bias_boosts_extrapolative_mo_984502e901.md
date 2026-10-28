---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Mathematics and algorithms
enrichment_tags: [bayesian-active-learning, gaussian-processes, extrapolation, small-data]
title: Linear inductive bias boosts extrapolative molecular discovery by Bayesian
  active learning in the small-data limit
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010454/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15010454/v1
captured_by: auto-scanner
date: '2026-10-14'
captured_at: '2026-10-14T09:53:53+00:00'
last_requested: '2026-10-14T09:53:53+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Min Young Ha
published: '2026-10-14'
abstract: 'Bayesian active learning is widely used for molecular discovery, yet surrogate
  selection remains challenging when scarce initial data must guide the search beyond
  the observed property range. Here we benchmark diverse Gaussian process (GP) configurations
  across ten small-molecule and polymer datasets, focusing on the extrapolative regime
  where the initial labeled samples are drawn exclusively from below the median of
  the target property distribution. We identify explicit linear structure as an effective
  inductive bias for data-scarce extrapolative discovery: linear-kernel GPs provide
  a strong baseline, while adding linear components to a stationary kernel helps mitigate
  poor outcomes in the tail of the performance distribution. However, this advantage
  weakens under later-stage interpolative regime, where adaptive surrogate selection
  can further improve the discovery performance. These findings support incorporating
  linear inductive biases into data-driven materials discovery, where data scarcity
  and limited coverage of the design space are the norm rather than the exception.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010454/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Linear inductive bias boosts extrapolative molecular discovery by Bayesian active learning in the small-data limit

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010454/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Min Young Ha
- **Published:** 2026-10-14

## Summary
Bayesian active learning is widely used for molecular discovery, yet surrogate selection remains challenging when scarce initial data must guide the search beyond the observed property range. Here we benchmark diverse Gaussian process (GP) configurations across ten small-molecule and polymer datasets, focusing on the extrapolative regime where the initial labeled samples are drawn exclusively from below the median of the target property distribution. We identify explicit linear structure as an effective inductive bias for data-scarce extrapolative discovery: linear-kernel GPs provide a strong baseline, while adding linear components to a stationary kernel helps mitigate poor outcomes in the tail of the performance distribution. However, this advantage weakens under later-stage interpolative regime, where adaptive surrogate selection can further improve the discovery performance. These findings support incorporating linear inductive biases into data-driven materials discovery, where data scarcity and limited coverage of the design space are the norm rather than the exception.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010454/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment
- **Concise summary:** Across ten molecular and polymer datasets, the authors benchmark Gaussian-process surrogates initialized only with below-median property examples. Explicit linear kernels or linear components help early extrapolative discovery, while their advantage weakens as the task becomes interpolative.
- **Why it matters:** Surrogate selection should reflect the discovery regime rather than assume the most flexible stationary kernel is always preferable.
- **Caveat:** ChemRxiv v1 findings are unverified and depend on deliberately restricted initialization; they do not show linear models dominate at every campaign stage.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15010454/v1); analysis based only on captured metadata, not independently verified full text.
