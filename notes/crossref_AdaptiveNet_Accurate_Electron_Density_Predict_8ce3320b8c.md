---
title: 'AdaptiveNet: Accurate Electron Density Prediction with Adaptive Global Charge
  Equilibration for Accelerating Large-Scale DFT Calculations'
type: paper
source: https://doi.org/10.1021/acs.jctc.6c01610
canonical_url: https://doi.org/10.1021/acs.jctc.6c01610
captured_by: auto-scanner
date: '2026-11-23'
captured_at: '2026-11-23T15:38:12+00:00'
last_requested: '2026-11-23T15:38:12+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Yuhang Lu
- Yibo Sun
- Zimo Li
- Jun Ni
published: '2026-11-23'
abstract: Abstract Accurate prediction of extended systems requires accounting for
  charge redistribution that reaches beyond the local coordination environment, and
  machine learning models offer various strategies to address this. We propose an
  alternative decoupling paradigm via AdaptiveNet, a deep learning framework that
  separates global charge equilibration from the electron density assignment. AdaptiveNet
  introduces an iterative layer on a sparse atomic graph, dynamically looping equivariant
  messages until convergence. A single cutoff-limited operator is applied repeatedly,
  so that the effective receptive field of the atomic representation grows with the
  number of iterations, without introducing any additional long-range term. The predicted
  Mulliken populations then serve as a compact physical bridge to modulate the electron
  density evaluation. Evaluated on the Materials Project data set, AdaptiveNet achieves
  a mean absolute percentage error of 0.158% for Mulliken populations and a normalized
  mean absolute percentage error of 0.469% for the electron density. Downstream tests
  on silicon demonstrate that the predicted densities precisely reproduce atomic forces,
  electronic band structures, and phonon dispersion. We further interface AdaptiveNet
  with DFT to accelerate structure relaxations of multiatom systems, with application
  to 90° twisted two-dimensional moiré superlattices In224O224Cl224, and identify
  that these superlattices host flat bands near the Fermi level. AdaptiveNet offers
  an accurate and efficient route for accelerating electronic structure calculations
  and large-scale materials simulations with machine learning.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1021/acs.jctc.6c01610
  journal: 'Journal of Chemical Theory

    and Computation'
  publisher: American Chemical Society (ACS)
  type: journal-article
  subjects: []
---

# AdaptiveNet: Accurate Electron Density Prediction with Adaptive Global Charge Equilibration for Accelerating Large-Scale DFT Calculations

- **Type:** paper
- **Source:** https://doi.org/10.1021/acs.jctc.6c01610
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Yuhang Lu, Yibo Sun, Zimo Li, Jun Ni
- **Published:** 2026-11-23

## Summary
Abstract Accurate prediction of extended systems requires accounting for charge redistribution that reaches beyond the local coordination environment, and machine learning models offer various strategies to address this. We propose an alternative decoupling paradigm via AdaptiveNet, a deep learning framework that separates global charge equilibration from the electron density assignment. AdaptiveNet introduces an iterative layer on a sparse atomic graph, dynamically looping equivariant messages until convergence. A single cutoff-limited operator is applied repeatedly, so that the effective receptive field of the atomic representation grows with the number of iterations, without introducing any additional long-range term. The predicted Mulliken populations then serve as a compact physical bridge to modulate the electron density evaluation. Evaluated on the Materials Project data set, AdaptiveNet achieves a mean absolute percentage error of 0.158% for Mulliken populations and a normalized mean absolute percentage error of 0.469% for the electron density. Downstream tests on silicon demonstrate that the predicted densities precisely reproduce atomic forces, electronic band structures, and phonon dispersion. We further interface AdaptiveNet with DFT to accelerate structure relaxations of multiatom systems, with application to 90° twisted two-dimensional moiré superlattices In224O224Cl224, and identify that these superlattices host flat bands near the Fermi level. AdaptiveNet offers an accurate and efficient route for accelerating electronic structure calculations and large-scale materials simulations with machine learning.

## Provider details
- **Doi:** 10.1021/acs.jctc.6c01610
- **Journal:** Journal of Chemical Theory
and Computation
- **Publisher:** American Chemical Society (ACS)
- **Type:** journal-article
