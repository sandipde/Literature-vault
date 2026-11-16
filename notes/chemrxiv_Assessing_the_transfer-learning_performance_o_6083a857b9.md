---
title: Assessing the transfer-learning performance of foundation models for energetic
  materials property prediction under low-data conditions
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15012261/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15012261/v1
captured_by: auto-scanner
date: '2026-11-16'
captured_at: '2026-11-16T13:18:51+00:00'
last_requested: '2026-11-16T13:18:51+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Andreas Backman
- Karthik Mohan
- Sohan Seth
- Carole A. Morrison
published: '2026-11-16'
abstract: This study evaluates the performance of off-the-shelf foundation model embeddings
  provided by CheMeleon, MolCLR, and MACE-OFF to predict energetic material properties
  from sparse datasets. Models were trained to predict crystal density, heat of formation
  and impact sensitivity from SMILES strings, with performance benchmarked against
  molecular representations provided by Morgan fingerprints and hand-crafted descriptors.
  Overall, the foundation model embeddings were found to be competitive with the hand-crafted
  descriptors, with MACE-OFF showing the strongest performance in numerical regression
  tasks. Heat of formation was found to be the most predictable property (R2 = 0.72),
  followed by crystal density (R2 = 0.54) and impact sensitivity (R2 = 0.47). Testing
  under more demanding cluster-based data splitting revealed that MACE-OFF retained
  the strongest performance across representations, suggesting that its learned embeddings
  generalise more effectively than hand-crafted descriptors to molecules that are
  more dissimilar to the training set distribution. Predictability for impact sensitivity
  improved noticeably when recast as a classification task, where CheMeleon emerged
  with comparable performance to the hand-crafted descriptors. These results show
  that while foundation model embeddings can provide useful low-input screening tools
  for energetic materials, they are not yet a competitive replacement for the bespoke
  models trained on larger datasets.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15012261/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Assessing the transfer-learning performance of foundation models for energetic materials property prediction under low-data conditions

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15012261/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Andreas Backman, Karthik Mohan, Sohan Seth, Carole A. Morrison
- **Published:** 2026-11-16

## Summary
This study evaluates the performance of off-the-shelf foundation model embeddings provided by CheMeleon, MolCLR, and MACE-OFF to predict energetic material properties from sparse datasets. Models were trained to predict crystal density, heat of formation and impact sensitivity from SMILES strings, with performance benchmarked against molecular representations provided by Morgan fingerprints and hand-crafted descriptors. Overall, the foundation model embeddings were found to be competitive with the hand-crafted descriptors, with MACE-OFF showing the strongest performance in numerical regression tasks. Heat of formation was found to be the most predictable property (R2 = 0.72), followed by crystal density (R2 = 0.54) and impact sensitivity (R2 = 0.47). Testing under more demanding cluster-based data splitting revealed that MACE-OFF retained the strongest performance across representations, suggesting that its learned embeddings generalise more effectively than hand-crafted descriptors to molecules that are more dissimilar to the training set distribution. Predictability for impact sensitivity improved noticeably when recast as a classification task, where CheMeleon emerged with comparable performance to the hand-crafted descriptors. These results show that while foundation model embeddings can provide useful low-input screening tools for energetic materials, they are not yet a competitive replacement for the bespoke models trained on larger datasets.

## Provider details
- **Doi:** 10.26434/chemrxiv.15012261/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
