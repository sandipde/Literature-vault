---
title: Interaction embedding via factorized linear models for multi-element machine
  learning interatomic potentials
type: paper
source: https://doi.org/10.1063/5.0345011
canonical_url: https://doi.org/10.1063/5.0345011
captured_by: auto-scanner
date: '2026-11-05'
captured_at: '2026-11-05T22:29:27+00:00'
last_requested: '2026-11-05T22:29:27+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Sung Hoon Jung
- Ilgar Baghishov
- Graeme Henkelman
published: '2026-11-07'
abstract: 'Linear machine-learning interatomic potentials, such as the Ultra-Fast
  Force Field (UF3), deliver near-density functional theory accuracy at low computational
  cost. Their number of parameters, however, grows combinatorially with the number
  of chemical species, limiting their use on multi-element systems. We address this
  scaling problem with pseudo-interaction UF3 (PI-UF3), a factorized linear model
  in which the Z(k) real k-body potentials are expressed as linear combinations of
  a small number P(k) ≪ Z(k) of shared pseudo-interactions. Learned element embeddings
  are standard in nonlinear potentials; inside a linear model, the embedding becomes
  a rank constraint on the coefficient matrix of each body order, and the resulting
  bilinear problem is trained with alternating least squares, where each block update
  is one closed-form linear solve. We benchmark PI-UF3 on a five-element refractory
  high-entropy alloy (HEA) and a subset of MD22, training on forces, with restarts
  and cross-validation. On the chemically homogeneous HEA, compression acts as implicit
  regularization: with three-body terms included, PI-UF3’s test force root-mean-squared
  error drops below the unfactorized UF3 baseline with 3% of the baseline’s parameters
  on the predefined split and 7% on every cross-validation fold, and the maximally
  compressed model recovers a chemically meaningful ordering of homonuclear interaction
  strengths consistent with experimental bulk melting temperatures. On the chemically
  heterogeneous MD22 subset, where UF3 is not expressive enough to overfit, PI-UF3
  approaches the baseline from above and reaches parity with it at about two thirds
  of the parameter count. Compression thus regularizes only where the unfactorized
  model overfits, while a parameter reduction is available in both regimes.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1063/5.0345011
  journal: The Journal of Chemical Physics
  publisher: AIP Publishing
  type: journal-article
  subjects: []
---

# Interaction embedding via factorized linear models for multi-element machine learning interatomic potentials

- **Type:** paper
- **Source:** https://doi.org/10.1063/5.0345011
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Sung Hoon Jung, Ilgar Baghishov, Graeme Henkelman
- **Published:** 2026-11-07

## Summary
Linear machine-learning interatomic potentials, such as the Ultra-Fast Force Field (UF3), deliver near-density functional theory accuracy at low computational cost. Their number of parameters, however, grows combinatorially with the number of chemical species, limiting their use on multi-element systems. We address this scaling problem with pseudo-interaction UF3 (PI-UF3), a factorized linear model in which the Z(k) real k-body potentials are expressed as linear combinations of a small number P(k) ≪ Z(k) of shared pseudo-interactions. Learned element embeddings are standard in nonlinear potentials; inside a linear model, the embedding becomes a rank constraint on the coefficient matrix of each body order, and the resulting bilinear problem is trained with alternating least squares, where each block update is one closed-form linear solve. We benchmark PI-UF3 on a five-element refractory high-entropy alloy (HEA) and a subset of MD22, training on forces, with restarts and cross-validation. On the chemically homogeneous HEA, compression acts as implicit regularization: with three-body terms included, PI-UF3’s test force root-mean-squared error drops below the unfactorized UF3 baseline with 3% of the baseline’s parameters on the predefined split and 7% on every cross-validation fold, and the maximally compressed model recovers a chemically meaningful ordering of homonuclear interaction strengths consistent with experimental bulk melting temperatures. On the chemically heterogeneous MD22 subset, where UF3 is not expressive enough to overfit, PI-UF3 approaches the baseline from above and reaches parity with it at about two thirds of the parameter count. Compression thus regularizes only where the unfactorized model overfits, while a parameter reduction is available in both regimes.

## Provider details
- **Doi:** 10.1063/5.0345011
- **Journal:** The Journal of Chemical Physics
- **Publisher:** AIP Publishing
- **Type:** journal-article
