---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [quantum-kernels, molecular-properties, neutral-atom-arrays]
title: Quantum evolution kernel for molecular machine learning on programmable neutral-atom
  arrays
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011111/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011111/v1
captured_by: auto-scanner
date: '2026-10-27'
captured_at: '2026-10-27T21:06:03+00:00'
last_requested: '2026-10-27T21:06:03+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Saiyam Sakhuja
- Victor Drouin-Touchette
- Viki Kumar Prasad
published: '2026-10-27'
abstract: Neutral-atom quantum processors can embed molecular graphs natively through
  the geometry of atom arrays, which makes them a natural platform for graph-based
  quantum kernels. Existing quantum evolution kernels, however, encode limited chemical
  information and have been applied to molecular classification but not to regression.
  Here we introduce ChemQEK, a quantum evolution kernel framework for molecular property
  prediction on analog neutral-atom quantum processors. ChemQEK encodes atom-specific
  descriptors through local addressability and atom-pair London dispersion coefficients
  ($C^{ij}_6$) into the parameters of the Rydberg Hamiltonian, and it combines global,
  local and pairwise observables of the evolved state within a single kernel. We further
  introduce kernel pooling strategies that combine information across evolution times
  and addressability schemes. Using noiseless emulation, we evaluate ChemQEK with
  kernel-based regression models on the ESOL, FreeSolv, Jean-Claude Bradley Open Melting
  Point, and QM9 datasets. Pooling over both evolution times and addressability schemes
  outperforms pooling over either alone and yields test $R^2$ values of 0.90, 0.84,
  and 0.69 for ESOL, FreeSolv, and melting point, respectively. On QM9, ChemQEK outperforms
  the quantum evolution kernel and generalized-distance quantum-correlation frameworks,
  each of which relies on a single observable type, for all eight properties considered.
  The QM9 experiments also reveal property dependent trade-offs between predictive
  performance and the number of quantum feature configurations, with up to $\sim$79\%
  fewer measurements retaining competitive performance for several properties. These
  results highlight the importance of chemically informed encoding, complementary
  observables, and multidimensional kernel pooling for quantum kernel-based molecular
  property prediction.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011111/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Quantum evolution kernel for molecular machine learning on programmable neutral-atom arrays

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011111/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Saiyam Sakhuja, Victor Drouin-Touchette, Viki Kumar Prasad
- **Published:** 2026-10-27

## Summary
Neutral-atom quantum processors can embed molecular graphs natively through the geometry of atom arrays, which makes them a natural platform for graph-based quantum kernels. Existing quantum evolution kernels, however, encode limited chemical information and have been applied to molecular classification but not to regression. Here we introduce ChemQEK, a quantum evolution kernel framework for molecular property prediction on analog neutral-atom quantum processors. ChemQEK encodes atom-specific descriptors through local addressability and atom-pair London dispersion coefficients ($C^{ij}_6$) into the parameters of the Rydberg Hamiltonian, and it combines global, local and pairwise observables of the evolved state within a single kernel. We further introduce kernel pooling strategies that combine information across evolution times and addressability schemes. Using noiseless emulation, we evaluate ChemQEK with kernel-based regression models on the ESOL, FreeSolv, Jean-Claude Bradley Open Melting Point, and QM9 datasets. Pooling over both evolution times and addressability schemes outperforms pooling over either alone and yields test $R^2$ values of 0.90, 0.84, and 0.69 for ESOL, FreeSolv, and melting point, respectively. On QM9, ChemQEK outperforms the quantum evolution kernel and generalized-distance quantum-correlation frameworks, each of which relies on a single observable type, for all eight properties considered. The QM9 experiments also reveal property dependent trade-offs between predictive performance and the number of quantum feature configurations, with up to $\sim$79\% fewer measurements retaining competitive performance for several properties. These results highlight the importance of chemically informed encoding, complementary observables, and multidimensional kernel pooling for quantum kernel-based molecular property prediction.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011111/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment

- **Concise summary:** ChemQEK encodes chemical descriptors into neutral-atom evolution kernels and pools observables across settings for molecular-property regression.
- **Why it matters:** Chemically informed encoding may matter as much as the quantum substrate when designing molecular kernels.
- **Caveat:** The preprint evaluates noiseless emulation; the abstract does not establish hardware performance or superiority over strong classical alternatives.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15011111/v1); analysis based only on captured metadata, not independently verified full text.
