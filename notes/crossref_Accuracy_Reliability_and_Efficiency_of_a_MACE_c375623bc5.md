---
title: 'Accuracy, Reliability, and Efficiency of a MACE Machine-Learning Interatomic
  Potential for Aspirin: A Reproducible Benchmark for Molecular Simulation'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011308/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011308/v1
captured_by: auto-scanner
date: '2026-10-30'
captured_at: '2026-10-30T11:09:08+00:00'
last_requested: '2026-10-30T11:09:08+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Modupe A. Omoniyi
published: '2026-10-30'
abstract: Machine-learning interatomic potentials (MLIPs) can reproduce density functional
  theory (DFT) energies and forces at a small fraction of the computational cost,
  yet an average benchmark error is an incomplete measure of their reliability in
  molecular simulation. This study presents a reproducible workflow that assesses
  prediction accuracy, error heterogeneity, and dynamical stability together, using
  aspirin (C9H8O4), a widely used pharmaceutical compound, as an initial molecular
  benchmark en route to metal-containing systems. A MACE equivariant graph neural
  network potential is trained on the MD17 dataset and deployed for molecular dynamics
  through the Atomic Simulation Environment (ASE). Across 210 762 held-out configurations
  the potential attains a force root-mean-square error of 15.30 meV Å−1, within the
  published MACE benchmark range, with a validation-to-test generalization gap of
  7.6%. Force error correlates positively with configuration energy (Pearson r = 0.51),
  the carboxyl carbon emerges as the least reliable atomic site, and 90% of force
  predictions lie within 23.5 meV Å−1 of the DFT reference. Microcanonical simulations
  conserve total energy and canonical trajectories remain stable, while single-configuration
  evaluation is approximately four orders of magnitude (a roughly ten-thousand-fold)
  faster than the corresponding DFT calculation. By combining aggregate accuracy with
  configuration-and atom-resolved error analysis and explicit dynamical tests, the
  workflow exposes behavior that a single error metric conceals. The resulting aspirin
  benchmark establishes a documented baseline for subsequent validation on metal-containing
  systems and illustrates the value of assessing error distributions and dynamical
  behavior alongside mean prediction accuracy.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011308/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Accuracy, Reliability, and Efficiency of a MACE Machine-Learning Interatomic Potential for Aspirin: A Reproducible Benchmark for Molecular Simulation

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011308/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Modupe A. Omoniyi
- **Published:** 2026-10-30

## Summary
Machine-learning interatomic potentials (MLIPs) can reproduce density functional theory (DFT) energies and forces at a small fraction of the computational cost, yet an average benchmark error is an incomplete measure of their reliability in molecular simulation. This study presents a reproducible workflow that assesses prediction accuracy, error heterogeneity, and dynamical stability together, using aspirin (C9H8O4), a widely used pharmaceutical compound, as an initial molecular benchmark en route to metal-containing systems. A MACE equivariant graph neural network potential is trained on the MD17 dataset and deployed for molecular dynamics through the Atomic Simulation Environment (ASE). Across 210 762 held-out configurations the potential attains a force root-mean-square error of 15.30 meV Å−1, within the published MACE benchmark range, with a validation-to-test generalization gap of 7.6%. Force error correlates positively with configuration energy (Pearson r = 0.51), the carboxyl carbon emerges as the least reliable atomic site, and 90% of force predictions lie within 23.5 meV Å−1 of the DFT reference. Microcanonical simulations conserve total energy and canonical trajectories remain stable, while single-configuration evaluation is approximately four orders of magnitude (a roughly ten-thousand-fold) faster than the corresponding DFT calculation. By combining aggregate accuracy with configuration-and atom-resolved error analysis and explicit dynamical tests, the workflow exposes behavior that a single error metric conceals. The resulting aspirin benchmark establishes a documented baseline for subsequent validation on metal-containing systems and illustrates the value of assessing error distributions and dynamical behavior alongside mean prediction accuracy.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011308/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
