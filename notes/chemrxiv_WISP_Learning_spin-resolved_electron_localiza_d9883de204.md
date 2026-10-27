---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [electron-localization, spin-resolved, materials-screening]
title: 'WISP: Learning spin-resolved electron localization from atomic environments'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011092/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011092/v1
captured_by: auto-scanner
date: '2026-10-27'
captured_at: '2026-10-27T10:10:23+00:00'
last_requested: '2026-10-27T10:10:23+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Austin Ellis
published: '2026-10-27'
abstract: The electron localization function (ELF) reveals bonding and interstitial
  localization in crystals, but obtaining it usually requires an electronic-structure
  calculation. Here we develop WISP, Wavefunction-free Inference of Scalar Properties,
  in which a nonlinear decoder predicts spin-resolved ELF from encoded atomic environments
  at arbitrarily chosen positions. Signed site moments supply the magnetic information,
  and two evaluations of a shared network with opposite moments enforce exact spin-channel
  exchange. We obtain a structure-weighted paired-channel mean absolute error (MAE)
  of 0.01065 for the model with far-field input on the complete grids of 21,922 held-out
  structures from a frozen MatPES-derived PBE dataset. With moments predicted from
  geometry by a separate network, we obtain an average-field MAE of 0.00974. The predictions
  retain the spin contrast of the magnetic examples and resolve the interstitial localization
  for electride screening. We propose using predicted ELF to select structures for
  further electronic-structure calculations.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011092/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# WISP: Learning spin-resolved electron localization from atomic environments

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011092/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Austin Ellis
- **Published:** 2026-10-27

## Summary
The electron localization function (ELF) reveals bonding and interstitial localization in crystals, but obtaining it usually requires an electronic-structure calculation. Here we develop WISP, Wavefunction-free Inference of Scalar Properties, in which a nonlinear decoder predicts spin-resolved ELF from encoded atomic environments at arbitrarily chosen positions. Signed site moments supply the magnetic information, and two evaluations of a shared network with opposite moments enforce exact spin-channel exchange. We obtain a structure-weighted paired-channel mean absolute error (MAE) of 0.01065 for the model with far-field input on the complete grids of 21,922 held-out structures from a frozen MatPES-derived PBE dataset. With moments predicted from geometry by a separate network, we obtain an average-field MAE of 0.00974. The predictions retain the spin contrast of the magnetic examples and resolve the interstitial localization for electride screening. We propose using predicted ELF to select structures for further electronic-structure calculations.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011092/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment

- **Concise summary:** WISP predicts spin-resolved electron localization from atomic environments and site moments, enforcing spin-channel exchange through paired network evaluations.
- **Why it matters:** Fast localization estimates could prioritize magnetic or electride candidates for more expensive electronic-structure calculations.
- **Caveat:** The preprint evaluates a fixed PBE-derived dataset; agreement with those labels does not establish accuracy outside that electronic-structure reference.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15011092/v1); analysis based only on captured metadata, not independently verified full text.
