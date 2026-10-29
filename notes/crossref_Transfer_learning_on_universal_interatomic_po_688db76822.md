---
title: Transfer learning on universal interatomic potential embeddings improves generalization
  in structure-property defect models
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15003938/v2
canonical_url: https://doi.org/10.26434/chemrxiv.15003938/v2
captured_by: auto-scanner
date: '2026-10-29'
captured_at: '2026-10-29T11:14:56+00:00'
last_requested: '2026-10-29T11:14:56+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Matthew D. Witman
- Sebastian Pujet
- Andrew J. E. Rowberg
- Christopher Sutton
- Joel B. Varley
- Stephan Lany
- Robert B. Wexler
published: '2026-10-29'
abstract: Oxygen vacancy formation energies govern the performance of metal oxides
  across energy conversion, catalysis, and electronics, yet predicting them accurately
  without density functional theory calculations for novel chemical systems remains
  challenging. Here, we show that frozen 256-dimensional embeddings extracted from
  a pretrained MACE universal machine-learning interatomic potential encode information
  sufficient to predict vacancy formation energies obtained from density functional
  theory without requiring supercell construction, vacancy creation, or geometry optimization.
  A lightweight multilayer perceptron trained on these embeddings (MACE-dGNN) achieves
  an element-wise cross-validation mean absolute error of 0.38 eV, halving the error
  of a baseline graph neural network trained from scratch (0.72 eV) and offering a
  modest advantage over direct MACE relaxation calculations (0.51 eV). Because the
  embedding approach decouples representation from the prediction task and generalizes
  well with limited data, it will (1) extend naturally to fine-tuning and prediction
  of properties (e.g., charged defects) that are inaccessible to generic energy-and
  force-output interatomic potentials and (2) be trainable on necessarily small datasets,
  potentially enabling the use of more expensive but accurate tools for generating
  training data (e.g., hybrid functional calculations) for which training or fine-tuning
  of interatomic potentials will be difficult. We demonstrate practical impact by
  revisiting a prior screening of thermochemical water-splitting materials, where
  improved generalization alters ∼45 % of candidate classifications.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15003938/v2
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Transfer learning on universal interatomic potential embeddings improves generalization in structure-property defect models

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15003938/v2
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Matthew D. Witman, Sebastian Pujet, Andrew J. E. Rowberg, Christopher Sutton, Joel B. Varley, Stephan Lany, Robert B. Wexler
- **Published:** 2026-10-29

## Summary
Oxygen vacancy formation energies govern the performance of metal oxides across energy conversion, catalysis, and electronics, yet predicting them accurately without density functional theory calculations for novel chemical systems remains challenging. Here, we show that frozen 256-dimensional embeddings extracted from a pretrained MACE universal machine-learning interatomic potential encode information sufficient to predict vacancy formation energies obtained from density functional theory without requiring supercell construction, vacancy creation, or geometry optimization. A lightweight multilayer perceptron trained on these embeddings (MACE-dGNN) achieves an element-wise cross-validation mean absolute error of 0.38 eV, halving the error of a baseline graph neural network trained from scratch (0.72 eV) and offering a modest advantage over direct MACE relaxation calculations (0.51 eV). Because the embedding approach decouples representation from the prediction task and generalizes well with limited data, it will (1) extend naturally to fine-tuning and prediction of properties (e.g., charged defects) that are inaccessible to generic energy-and force-output interatomic potentials and (2) be trainable on necessarily small datasets, potentially enabling the use of more expensive but accurate tools for generating training data (e.g., hybrid functional calculations) for which training or fine-tuning of interatomic potentials will be difficult. We demonstrate practical impact by revisiting a prior screening of thermochemical water-splitting materials, where improved generalization alters ∼45 % of candidate classifications.

## Provider details
- **Doi:** 10.26434/chemrxiv.15003938/v2
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
