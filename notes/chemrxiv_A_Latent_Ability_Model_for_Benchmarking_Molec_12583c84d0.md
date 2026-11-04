---
title: A Latent Ability Model for Benchmarking Molecular Representations
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011649/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011649/v1
captured_by: auto-scanner
date: '2026-11-04'
captured_at: '2026-11-04T12:44:30+00:00'
last_requested: '2026-11-04T12:44:30+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Nethaka Dassanayake
- Andrew T. McNutt
- Alexander Rich
published: '2026-11-04'
abstract: The growing number of chemical foundation models calls for a standardized
  benchmarking method both for practitioners choosing representations and researchers
  identifying gaps. Previous work that ranked latent abilities of various chemical
  embeddings to predict ADMET properties suffered from significant shortcomings, including
  the use of biased datasets incongruent with real world usage and overstating statistically
  significant differences in model performance. We derive from first principles a
  variance inflation factor of (M+1)/3 for the Bayesian Bradley-Terry model evaluating
  M models on E endpoints at the exchangeable null and use numerical simulation to
  show variance inflation is still present in the non-exchangeable case. We propose
  a new method to directly model the margin of error as a function of latent ability
  and use it to evaluate models retrospectively on the datasets from the OpenADMET
  Polaris, ExpansionRx, and PXR competitions. We compare 35 embeddings and 13 end-to-end
  fine-tuned models across 17 ADMET endpoints. Although endpoint-to-endpoint variability
  means that no neural representation is expected to outperform ECFP on a hypothetical
  new endpoint in more than 95% of cases, our model concludes that 29 of 47 representations
  outperform ECFP in terms of latent ability with posterior probability above 0.95.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011649/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# A Latent Ability Model for Benchmarking Molecular Representations

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011649/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Nethaka Dassanayake, Andrew T. McNutt, Alexander Rich
- **Published:** 2026-11-04

## Summary
The growing number of chemical foundation models calls for a standardized benchmarking method both for practitioners choosing representations and researchers identifying gaps. Previous work that ranked latent abilities of various chemical embeddings to predict ADMET properties suffered from significant shortcomings, including the use of biased datasets incongruent with real world usage and overstating statistically significant differences in model performance. We derive from first principles a variance inflation factor of (M+1)/3 for the Bayesian Bradley-Terry model evaluating M models on E endpoints at the exchangeable null and use numerical simulation to show variance inflation is still present in the non-exchangeable case. We propose a new method to directly model the margin of error as a function of latent ability and use it to evaluate models retrospectively on the datasets from the OpenADMET Polaris, ExpansionRx, and PXR competitions. We compare 35 embeddings and 13 end-to-end fine-tuned models across 17 ADMET endpoints. Although endpoint-to-endpoint variability means that no neural representation is expected to outperform ECFP on a hypothetical new endpoint in more than 95% of cases, our model concludes that 29 of 47 representations outperform ECFP in terms of latent ability with posterior probability above 0.95.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011649/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
