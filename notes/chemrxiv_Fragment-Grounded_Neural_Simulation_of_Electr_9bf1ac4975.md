---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [mass-spectrometry, molecular-fragmentation, spectrum-prediction]
title: Fragment-Grounded Neural Simulation of Electron Ionization Mass Spectra at
  Library Scale
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15008135/v2
canonical_url: https://doi.org/10.26434/chemrxiv.15008135/v2
captured_by: auto-scanner
date: '2026-10-24'
captured_at: '2026-10-24T09:15:55+00:00'
last_requested: '2026-10-24T09:15:55+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Magdalena Lederbauer
- Runzhong Wang
- Connor W. Coley
published: '2026-10-23'
abstract: Electron ionization mass spectrometry (EI-MS) is a sensitive, reproducible
  analytical technique, yet compound identification conventionally relies on reference
  databases that capture only a fraction of accessible chemical space. In silico prediction
  of EI-MS spectra can extend these libraries, but existing data-driven models generalize
  poorly beyond their training distribution, and physics-based simulations are too
  costly for library-scale use. Here, we present a fragment-grounded neural workflow
  that predicts an EI-MS spectrum by exhaustively enumerating the fragmentation graph
  of a molecule and then assigning intensities to the resulting substructures. By
  relating every predicted peak back to a candidate substructure, our model generalizes
  more reliably to unseen scaffolds and out-of-distribution chemistry than prior fingerprint-and
  black-box transformer-based predictors. On a scaffold split, it improves top-1 retrieval
  accuracy from formula-matched compounds by 32% relative to the strongest baseline,
  and it matches the accuracy of quantum-chemical simulation while being roughly seven
  orders of magnitude faster. To test the model’s capabilities under a harder, formula-agnostic
  setting, we further evaluate retrieval against a library of 87.3 million compounds
  from
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15008135/v2
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Fragment-Grounded Neural Simulation of Electron Ionization Mass Spectra at Library Scale

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15008135/v2
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Magdalena Lederbauer, Runzhong Wang, Connor W. Coley
- **Published:** 2026-10-23

## Summary
Electron ionization mass spectrometry (EI-MS) is a sensitive, reproducible analytical technique, yet compound identification conventionally relies on reference databases that capture only a fraction of accessible chemical space. In silico prediction of EI-MS spectra can extend these libraries, but existing data-driven models generalize poorly beyond their training distribution, and physics-based simulations are too costly for library-scale use. Here, we present a fragment-grounded neural workflow that predicts an EI-MS spectrum by exhaustively enumerating the fragmentation graph of a molecule and then assigning intensities to the resulting substructures. By relating every predicted peak back to a candidate substructure, our model generalizes more reliably to unseen scaffolds and out-of-distribution chemistry than prior fingerprint-and black-box transformer-based predictors. On a scaffold split, it improves top-1 retrieval accuracy from formula-matched compounds by 32% relative to the strongest baseline, and it matches the accuracy of quantum-chemical simulation while being roughly seven orders of magnitude faster. To test the model’s capabilities under a harder, formula-agnostic setting, we further evaluate retrieval against a library of 87.3 million compounds from

## Provider details
- **Doi:** 10.26434/chemrxiv.15008135/v2
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment

- **Concise summary:** The abstract describes predicting electron-ionization spectra by enumerating molecular fragments and learning their intensities. It reports improved scaffold-split retrieval while retaining a candidate structural explanation for each peak.
- **Why it matters:** Explicit fragment grounding may make spectral-library expansion more interpretable than unconstrained peak prediction.
- **Caveat:** This is a ChemRxiv v2 preprint and the captured abstract ends mid-sentence; speed and retrieval comparisons are author claims, not independently validated results. The version suffix identifies a revision, not a separate discovery.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15008135/v2); analysis based only on captured metadata, not independently verified full text.
