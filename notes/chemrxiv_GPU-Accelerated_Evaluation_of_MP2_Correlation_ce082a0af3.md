---
title: GPU-Accelerated Evaluation of MP2 Correlation Energy Densities for Machine
  Learning of Density Functionals
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15012314/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15012314/v1
captured_by: auto-scanner
date: '2026-11-17'
captured_at: '2026-11-17T14:04:00+00:00'
last_requested: '2026-11-17T14:04:00+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Elias Polak
- Heng Zhao
- Stefan Vuckovic
published: '2026-11-17'
abstract: Second-order Møller–Plesset (MP2) correlation energy densities can serve
  as ingredients for machine learning (ML) of density functionals that improve upon
  MP2-based double hybrids. However, limitations of existing implementations have
  restricted the evaluation of these energy densities and of ML-based functionals
  employing them to small systems. Here, we develop a GPU-accelerated implementation
  for evaluating MP2 correlation energy densities and their regularized and spin-resolved
  variants by combining a density fitting scheme that preserves high pointwise accuracy
  with memory-efficient tensor contractions. We demonstrate the use of the resulting
  energy densities in ML-based density functional approximations (DFAs) through the
  previously developed MLS2 model [Nat. Commun. 16, 11306 (2025)] and limMLS2, a variant
  introduced here that enforces a high density limit constraint to MLS2. The GPU-accelerated
  evaluation of MP2 energy densities enables routine application of these ML-based
  DFAs to systems described by more than 5000 atomic orbitals, with predictions remaining
  robust to the density fitting approximations and grid sizes tested. Overall, by
  making MP2 correlation energy densities accessible for larger systems, our work
  broadens their use in the development and application of highly accurate ML-based
  DFAs.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15012314/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# GPU-Accelerated Evaluation of MP2 Correlation Energy Densities for Machine Learning of Density Functionals

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15012314/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Elias Polak, Heng Zhao, Stefan Vuckovic
- **Published:** 2026-11-17

## Summary
Second-order Møller–Plesset (MP2) correlation energy densities can serve as ingredients for machine learning (ML) of density functionals that improve upon MP2-based double hybrids. However, limitations of existing implementations have restricted the evaluation of these energy densities and of ML-based functionals employing them to small systems. Here, we develop a GPU-accelerated implementation for evaluating MP2 correlation energy densities and their regularized and spin-resolved variants by combining a density fitting scheme that preserves high pointwise accuracy with memory-efficient tensor contractions. We demonstrate the use of the resulting energy densities in ML-based density functional approximations (DFAs) through the previously developed MLS2 model [Nat. Commun. 16, 11306 (2025)] and limMLS2, a variant introduced here that enforces a high density limit constraint to MLS2. The GPU-accelerated evaluation of MP2 energy densities enables routine application of these ML-based DFAs to systems described by more than 5000 atomic orbitals, with predictions remaining robust to the density fitting approximations and grid sizes tested. Overall, by making MP2 correlation energy densities accessible for larger systems, our work broadens their use in the development and application of highly accurate ML-based DFAs.

## Provider details
- **Doi:** 10.26434/chemrxiv.15012314/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
