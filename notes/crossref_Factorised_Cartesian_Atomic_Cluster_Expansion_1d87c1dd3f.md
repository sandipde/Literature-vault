---
title: Factorised Cartesian Atomic Cluster Expansion for Low-Cost Machine-Learning
  Interatomic Potentials
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010957/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15010957/v1
captured_by: auto-scanner
date: '2026-10-23'
captured_at: '2026-10-23T20:11:01+00:00'
last_requested: '2026-10-23T20:11:01+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Albert Linda
published: '2026-10-23'
abstract: 'Machine-learning interatomic potentials can reach the accuracy of density
  functional theory at a fraction of its cost, but the most accurate equivariant models
  remain expensive, mainly because of the tensor operations they perform for every
  pair of neighbouring atoms. We present FACE, a factorised Cartesian atomic cluster
  expansion that removes this bottleneck. Each neighbour contributes only a small
  set of radial functions and messages, and all mixing of feature channels is done
  once per atom, so the cost per neighbour no longer grows with the size of the model.
  Custom GPU kernels evaluate the remaining steps, and long-range electrostatics,
  dispersion and short-range repulsion attach through a single interface. We show
  that the training divergences we encountered originate in how the network weights
  are scaled, and we introduce a distillation scheme in which an ensemble generates
  additional, uncertainty-checked training data. On five rMD17 molecules, with identical
  training budgets and hardware, FACE is about as accurate as a 64-channel MACE model
  (over three seeds: better on one molecule, within the seed spread on two, 7–14%
  higher force errors on two), while it is 5.7 times faster at inference (4.9 times
  at the same cutoff) and needs 3.5–3.9 times less GPU memory. Training costs about
  the same per step. Distillation lowers the energy and force errors of a single aspirin
  model by 20% at fixed width, to 2.26 meV and 6.74 meV/Å, close to the published
  MACE values (2.2 and 6.6), and the distilled model runs stably in molecular dynamics.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010957/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Factorised Cartesian Atomic Cluster Expansion for Low-Cost Machine-Learning Interatomic Potentials

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010957/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Albert Linda
- **Published:** 2026-10-23

## Summary
Machine-learning interatomic potentials can reach the accuracy of density functional theory at a fraction of its cost, but the most accurate equivariant models remain expensive, mainly because of the tensor operations they perform for every pair of neighbouring atoms. We present FACE, a factorised Cartesian atomic cluster expansion that removes this bottleneck. Each neighbour contributes only a small set of radial functions and messages, and all mixing of feature channels is done once per atom, so the cost per neighbour no longer grows with the size of the model. Custom GPU kernels evaluate the remaining steps, and long-range electrostatics, dispersion and short-range repulsion attach through a single interface. We show that the training divergences we encountered originate in how the network weights are scaled, and we introduce a distillation scheme in which an ensemble generates additional, uncertainty-checked training data. On five rMD17 molecules, with identical training budgets and hardware, FACE is about as accurate as a 64-channel MACE model (over three seeds: better on one molecule, within the seed spread on two, 7–14% higher force errors on two), while it is 5.7 times faster at inference (4.9 times at the same cutoff) and needs 3.5–3.9 times less GPU memory. Training costs about the same per step. Distillation lowers the energy and force errors of a single aspirin model by 20% at fixed width, to 2.26 meV and 6.74 meV/Å, close to the published MACE values (2.2 and 6.6), and the distilled model runs stably in molecular dynamics.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010957/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
