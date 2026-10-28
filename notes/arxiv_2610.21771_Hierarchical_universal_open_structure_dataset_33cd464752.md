---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: ML interatomic potentials
enrichment_tags: [training-datasets, structural-diversity, coresets, dataset-deduplication]
title: Hierarchical universal open structure dataset for atomistic modeling
type: arxiv
source: https://arxiv.org/abs/2610.21771
canonical_url: https://arxiv.org/abs/2610.21771
captured_by: auto-scanner
date: '2026-10-16'
captured_at: '2026-10-16T09:27:31+00:00'
last_requested: '2026-10-16T14:48:26+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Sofiia Chorna
- Cesare Malosso
- Jonathan Schmidt
- Michele Ceriotti
published: '2026-10-15'
abstract: Atomic-scale simulations have been transformed by machine-learning models
  that predict the properties of atomistic structures with the accuracy of quantum
  calculations, but at a small fraction of the cost. These models have increased dramatically
  in generality, thanks to the availability of synthetic datasets of ever-increasing
  size and scope. The proliferation of datasets, with properties often computed using
  different levels of electronic-structure approximation, is problematic, as there
  is often overlap between different datasets, and strong correlations between structures
  obtained with short molecular dynamics trajectories or geometry optimization. To
  address these problems, we introduce a protocol to stratify a dataset into a hierarchy
  of nested subsets, subsampling from the coarsest to the finest resolution based
  on an "ecumetric" built to reflect the latent space representation of several popular
  universal machine-learning interatomic potentials. We then use this approach to
  combine most of the open structural datasets currently available, consolidating
  them into MAD-COSMO, a well-organized collection of almost 1.7 billion structures,
  whose $2^{24}$ most diverse members form the MAD-CORE stratified coreset, which
  can be easily used for all sorts of tasks, from exploratory experiments to the training
  of foundation models at scale. We envision that this collection will guide and help
  coordinate future efforts, focusing them on the most relevant and/or undersampled
  regions of chemical and structural space, and that it will be further extended to
  incorporate the outcomes of the collective work of this community.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.21771'
  categories:
  - physics.chem-ph
---

# Hierarchical universal open structure dataset for atomistic modeling

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.21771
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Sofiia Chorna, Cesare Malosso, Jonathan Schmidt, Michele Ceriotti
- **Published:** 2026-10-15

## Summary
Atomic-scale simulations have been transformed by machine-learning models that predict the properties of atomistic structures with the accuracy of quantum calculations, but at a small fraction of the cost. These models have increased dramatically in generality, thanks to the availability of synthetic datasets of ever-increasing size and scope. The proliferation of datasets, with properties often computed using different levels of electronic-structure approximation, is problematic, as there is often overlap between different datasets, and strong correlations between structures obtained with short molecular dynamics trajectories or geometry optimization. To address these problems, we introduce a protocol to stratify a dataset into a hierarchy of nested subsets, subsampling from the coarsest to the finest resolution based on an "ecumetric" built to reflect the latent space representation of several popular universal machine-learning interatomic potentials. We then use this approach to combine most of the open structural datasets currently available, consolidating them into MAD-COSMO, a well-organized collection of almost 1.7 billion structures, whose $2^{24}$ most diverse members form the MAD-CORE stratified coreset, which can be easily used for all sorts of tasks, from exploratory experiments to the training of foundation models at scale. We envision that this collection will guide and help coordinate future efforts, focusing them on the most relevant and/or undersampled regions of chemical and structural space, and that it will be further extended to incorporate the outcomes of the collective work of this community.

## Provider details
- **Arxiv Id:** 2610.21771
- **Categories:** ["physics.chem-ph"]

## AI enrichment
- **Concise summary:** A hierarchical subsampling protocol uses an “ecumetric” derived from several universal MLIP representations to organize nearly 1.7 billion structures into MAD-COSMO. Its most diverse 2^24 members form the MAD-CORE coreset.
- **Why it matters:** Reducing duplicate and correlated structures could make foundation-model training and coverage analysis more informative than simply accumulating larger datasets.
- **Caveat:** The preprint's scale and usefulness are unverified; structural consolidation does not by itself reconcile heterogeneous electronic-structure labels or eliminate representation bias.
- **Evidence:** [Captured source](https://arxiv.org/abs/2610.21771); analysis based only on captured metadata, not independently verified full text.
