---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [literature-data, grouped-validation, bismuth-recovery, local-calibration]
title: 'Machine learning prediction of bismuth recovery from literature data: publication-grouped
  validation, anchored calibration and chemical interpretation'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010302/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15010302/v1
captured_by: auto-scanner
date: '2026-10-13'
captured_at: '2026-10-13T12:25:46+00:00'
last_requested: '2026-10-13T12:25:46+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Subash Chandra Bose Rapaka
published: '2026-10-13'
abstract: Machine learning models trained on published leaching data often report
  high accuracy from random splits that place runs of one study in both training and
  test sets. This study tested whether reported operating conditions can predict bismuth
  recovery for a study that the model has not seen. A data set of 485 runs from 82
  sources was compiled across six unit operations; runs designed to retain bismuth,
  plate part of a bath or recover another metal were set aside, leaving 375 recovery
  runs from 72 studies. Thirteen models, including a mean baseline, were compared
  under random, publication-grouped and feedstock-grouped validation, and six of them
  under temporal validation. Random splits gave R2 up to 0.57, whereas publication-grouped
  validation gave at most 0.09 (95% interval −0.22 to 0.28); about half of the residual
  variance lay between publications. Three measured runs from a new study raised R2
  for its remaining runs from about zero to 0.48, and Gaussian-process predictions
  were positively rank-correlated with measured recovery in 83% of studies. Within
  studies, recovery rose with acid concentration and temperature, although the temperature
  trend tended to reverse across studies. Literature data can therefore rank conditions
  for a new feed, but absolute prediction needs a few local measurements; an offline
  browser tool that applies this approach to leaching is provided.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010302/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Machine learning prediction of bismuth recovery from literature data: publication-grouped validation, anchored calibration and chemical interpretation

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010302/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Subash Chandra Bose Rapaka
- **Published:** 2026-10-13

## Summary
Machine learning models trained on published leaching data often report high accuracy from random splits that place runs of one study in both training and test sets. This study tested whether reported operating conditions can predict bismuth recovery for a study that the model has not seen. A data set of 485 runs from 82 sources was compiled across six unit operations; runs designed to retain bismuth, plate part of a bath or recover another metal were set aside, leaving 375 recovery runs from 72 studies. Thirteen models, including a mean baseline, were compared under random, publication-grouped and feedstock-grouped validation, and six of them under temporal validation. Random splits gave R2 up to 0.57, whereas publication-grouped validation gave at most 0.09 (95% interval −0.22 to 0.28); about half of the residual variance lay between publications. Three measured runs from a new study raised R2 for its remaining runs from about zero to 0.48, and Gaussian-process predictions were positively rank-correlated with measured recovery in 83% of studies. Within studies, recovery rose with acid concentration and temperature, although the temperature trend tended to reverse across studies. Literature data can therefore rank conditions for a new feed, but absolute prediction needs a few local measurements; an offline browser tool that applies this approach to leaching is provided.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010302/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment
- **Concise summary:** Models of bismuth recovery lose most apparent predictive power when validation holds out publications instead of randomly splitting runs. A few measurements from a new study improve local calibration, while within-study ranking remains more promising than absolute transfer.
- **Why it matters:** Publication identity can encode hidden experimental conditions, making random-split accuracy a poor guide to performance on a new feedstock or laboratory.
- **Caveat:** The preprint's calibration and ranking results are unverified; the grouped-validation interval includes negative R2 and does not support universal zero-shot prediction.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15010302/v1); analysis based only on captured metadata, not independently verified full text.
