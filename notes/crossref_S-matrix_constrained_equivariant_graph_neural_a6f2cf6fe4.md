---
title: S-matrix constrained equivariant graph neural network for Hamiltonian inversion
  of Kagome and quasiperiodic non-Hermitian systems
type: paper
source: https://doi.org/10.1088/2632-2153/aec366
canonical_url: https://doi.org/10.1088/2632-2153/aec366
captured_by: auto-scanner
date: '2026-11-17'
captured_at: '2026-11-17T23:42:53+00:00'
last_requested: '2026-11-17T23:42:53+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Qi Dongkai
- Huang Huang
- Xiaohong Ye
- Chia Sien Lim
- Sivakumar Vengusamy
- Yu Li
published: '2026-11-17'
abstract: "Abstract Reconstructing Hamiltonian parameters from noisy scattering data\
  \ is an ill-posed inverse problem in non-Hermitian quantum systems. We propose an\
  \ S-matrix Constrained Equivariant Graph Neural Network (SCEGNN) that embeds two\
  \ architectural hard constraints to reduce the solution ambiguity. An equivariant\
  \ message-passing encoder incorporates lattice point-group symmetry and permutation-invariant\
  \ aggregation (for the Aubry–André–Harper quasiperiodic chain), thereby suppressing\
  \ symmetry-induced parameter variability. A deterministic S-matrix solver serves\
  \ as a fixed decoder that enforces the scattering equations within the assumed model,\
  \ eliminating the need for physics-based residual loss terms. Inference is performed\
  \ via a two-stage hybrid optimisation: offline pre-training on synthetic data, followed\
  \ by online single-sample fine-tuning in a low-dimensional latent space. On a 48-site\
  \ Kagome supercell and a 50-site Aubry–André–Harper quasiperiodic chain, using a\
  \ synthetic dataset of 120,000 samples (100,000 training, 10,000 validation, 10,000\
  \ test) with additive white Gaussian noise (0–10%), the mean absolute percentage\
  \ error of reconstructed parameters remains below 5% for both systems under 10%\
  \ noise, with per-parameter standard deviations below 7% across 20 independent repetitions.\
  \ The transmission spectrum reconstruction RMSE is 0.026±0.003 (Kagome) and 0.029±0.003\
  \ (Aubry–André–Harper) at 10% noise. Single-sample CPU inference takes 23 s (offline\
  \ simulation scenario), achieving a 5.6-fold speedup over least-squares fitting\
  \ with five restarts. Ablation studies confirm that each architectural component\
  \ contributes to the reported performance. \rFor the AAH quasiperiodic chain, we\
  \ consider two scenarios: a uniform-dissipation scenario with two independent parameters\
  \ (V0 and γ), which serves as our primary benchmark. Unless otherwise stated, all\
  \ numerical results reported in the main text for the AAH chain correspond to the\
  \ uniform-dissipation scenario.All experiments are conducted on synthetic data;\
  \ the method is validated as a proof-of-concept for the two benchmark systems under\
  \ the wide-band approximation and does not claim general applicability to arbitrary\
  \ non-Hermitian systems or experimental real-time control."
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1088/2632-2153/aec366
  journal: 'Machine Learning: Science and Technology'
  publisher: IOP Publishing
  type: journal-article
  subjects: []
---

# S-matrix constrained equivariant graph neural network for Hamiltonian inversion of Kagome and quasiperiodic non-Hermitian systems

- **Type:** paper
- **Source:** https://doi.org/10.1088/2632-2153/aec366
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Qi Dongkai, Huang Huang, Xiaohong Ye, Chia Sien Lim, Sivakumar Vengusamy, Yu Li
- **Published:** 2026-11-17

## Summary
Abstract Reconstructing Hamiltonian parameters from noisy scattering data is an ill-posed inverse problem in non-Hermitian quantum systems. We propose an S-matrix Constrained Equivariant Graph Neural Network (SCEGNN) that embeds two architectural hard constraints to reduce the solution ambiguity. An equivariant message-passing encoder incorporates lattice point-group symmetry and permutation-invariant aggregation (for the Aubry–André–Harper quasiperiodic chain), thereby suppressing symmetry-induced parameter variability. A deterministic S-matrix solver serves as a fixed decoder that enforces the scattering equations within the assumed model, eliminating the need for physics-based residual loss terms. Inference is performed via a two-stage hybrid optimisation: offline pre-training on synthetic data, followed by online single-sample fine-tuning in a low-dimensional latent space. On a 48-site Kagome supercell and a 50-site Aubry–André–Harper quasiperiodic chain, using a synthetic dataset of 120,000 samples (100,000 training, 10,000 validation, 10,000 test) with additive white Gaussian noise (0–10%), the mean absolute percentage error of reconstructed parameters remains below 5% for both systems under 10% noise, with per-parameter standard deviations below 7% across 20 independent repetitions. The transmission spectrum reconstruction RMSE is 0.026±0.003 (Kagome) and 0.029±0.003 (Aubry–André–Harper) at 10% noise. Single-sample CPU inference takes 23 s (offline simulation scenario), achieving a 5.6-fold speedup over least-squares fitting with five restarts. Ablation studies confirm that each architectural component contributes to the reported performance. For the AAH quasiperiodic chain, we consider two scenarios: a uniform-dissipation scenario with two independent parameters (V0 and γ), which serves as our primary benchmark. Unless otherwise stated, all numerical results reported in the main text for the AAH chain correspond to the uniform-dissipation scenario.All experiments are conducted on synthetic data; the method is validated as a proof-of-concept for the two benchmark systems under the wide-band approximation and does not claim general applicability to arbitrary non-Hermitian systems or experimental real-time control.

## Provider details
- **Doi:** 10.1088/2632-2153/aec366
- **Journal:** Machine Learning: Science and Technology
- **Publisher:** IOP Publishing
- **Type:** journal-article
