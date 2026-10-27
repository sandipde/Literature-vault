---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [mass-spectrometry, fragment-models, molecular-identification]
title: Fragment-Grounded Neural Simulation of Electron Ionization Mass Spectra at
  Library Scale
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15008135/v3
canonical_url: https://doi.org/10.26434/chemrxiv.15008135/v3
captured_by: auto-scanner
date: '2026-10-26'
captured_at: '2026-10-26T10:43:25+00:00'
last_requested: '2026-10-26T10:43:25+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Magdalena Lederbauer
- Runzhong Wang
- Connor W. Coley
published: '2026-10-26'
abstract: Electron ionization mass spectrometry (EI-MS) is a sensitive analytical
  technique, yet compound identification conventionally relies on reference libraries
  that contain spectra for at most about one million compounds, which is a small subset
  of chemical space. In silico prediction of EI-MS spectra can extend these libraries,
  but existing data-driven models generalize poorly beyond their training distribution,
  and physics-based simulations are too costly for library-scale use. Here, we present
  a fragment-grounded neural workflow that predicts an EI-MS spectrum by exhaustively
  enumerating the fragmentation graph of a molecule and then assigning intensities
  to the resulting substructures with a model trained on experimental spectra. By
  relating every predicted peak back to a candidate substructure, our model generalizes
  more reliably to unseen scaffolds and out-of-distribution chemistry than prior fingerprint-
  and black-box transformer-based predictors. On a scaffold split, it identifies the
  correct structure among up to fifty same-formula isomers in 43.0% of cases, compared
  to 32.5% for the strongest baseline. Further, it matches the accuracy of quantum-chemical
  simulation while being roughly seven orders of magnitude faster. To test the model's
  capabilities under a harder, formula-agnostic setting, we further evaluate retrieval
  against a library of 87.3 million compounds from PubChem. There, our model achieves
  a top-1 accuracy of 3.3%, compared to 1.1% for the strongest baseline, and a peak-mass-window
  filter further raises its top-1 accuracy to 5.3%. The predicted spectra for 87.3
  million compounds serve as an augmented reference library to facilitate database-dependent
  structure elucidation.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15008135/v3
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Fragment-Grounded Neural Simulation of Electron Ionization Mass Spectra at Library Scale

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15008135/v3
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Magdalena Lederbauer, Runzhong Wang, Connor W. Coley
- **Published:** 2026-10-26

## Summary
Electron ionization mass spectrometry (EI-MS) is a sensitive analytical technique, yet compound identification conventionally relies on reference libraries that contain spectra for at most about one million compounds, which is a small subset of chemical space. In silico prediction of EI-MS spectra can extend these libraries, but existing data-driven models generalize poorly beyond their training distribution, and physics-based simulations are too costly for library-scale use. Here, we present a fragment-grounded neural workflow that predicts an EI-MS spectrum by exhaustively enumerating the fragmentation graph of a molecule and then assigning intensities to the resulting substructures with a model trained on experimental spectra. By relating every predicted peak back to a candidate substructure, our model generalizes more reliably to unseen scaffolds and out-of-distribution chemistry than prior fingerprint- and black-box transformer-based predictors. On a scaffold split, it identifies the correct structure among up to fifty same-formula isomers in 43.0% of cases, compared to 32.5% for the strongest baseline. Further, it matches the accuracy of quantum-chemical simulation while being roughly seven orders of magnitude faster. To test the model's capabilities under a harder, formula-agnostic setting, we further evaluate retrieval against a library of 87.3 million compounds from PubChem. There, our model achieves a top-1 accuracy of 3.3%, compared to 1.1% for the strongest baseline, and a peak-mass-window filter further raises its top-1 accuracy to 5.3%. The predicted spectra for 87.3 million compounds serve as an augmented reference library to facilitate database-dependent structure elucidation.

## Provider details
- **Doi:** 10.26434/chemrxiv.15008135/v3
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment

- **Concise summary:** A neural EI-MS workflow assigns intensities to enumerated molecular fragments and uses predicted spectra to expand structure-search libraries.
- **Why it matters:** Linking peaks to candidate fragments offers a chemically structured alternative to opaque spectrum prediction.
- **Caveat:** This versioned preprint reports low absolute top-one accuracy in its large formula-agnostic search; speed comparisons and generalization claims remain unverified.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15008135/v3); analysis based only on captured metadata, not independently verified full text.
