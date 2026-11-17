---
title: Large-scale Monte Carlo/Molecular Dynamics simulations with Atomic Cluster
  Expansion potentials in LAMMPS
type: arxiv
source: https://arxiv.org/abs/2611.21147
canonical_url: https://arxiv.org/abs/2611.21147
captured_by: auto-scanner
date: '2026-11-17'
captured_at: '2026-11-17T14:04:00+00:00'
last_requested: '2026-11-17T14:04:00+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Lorenzo Piersante
- Anirudh Raju Natarajan
published: '2026-11-16'
abstract: Monte Carlo/molecular dynamics (MCMD) simulations are widely used to study
  the properties of materials at the mesoscale. Simulations with hundreds of thousands
  of atoms usually rely on empirical potentials because MCMD with machine-learning
  interatomic potentials is impractical at this scale in existing implementations.
  Here, we introduce a hybrid MPI/OpenMP scheme for MCMD with Atomic Cluster Expansion
  (ACE) potentials in LAMMPS. Monte Carlo moves are evaluated from local energy changes
  and carried out in parallel over MPI ranks, while molecular dynamics is parallelized
  over OpenMP threads. At a fixed number of CPUs, the wall time of the Monte Carlo
  moves decreases by a factor equal to the number of MPI ranks. Larger simulation
  cells also reduce the statistical errors of free energy calculations because thermal
  fluctuations decrease with system size. We demonstrate the scheme by calculating
  free energies of the HCP and BCC phases in the strongly anharmonic Hf--Ti system
  and by simulating zirconium segregation in a nanocrystalline copper sample of 670,000
  atoms. For Cu--Zr, an ACE potential and an empirical potential predict similar grain
  boundary compositions but different amounts of zirconium dissolved in the grains.
  The scheme makes MCMD simulations with machine-learning interatomic potentials practical
  at the length scales of microstructure.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.21147'
  categories:
  - cond-mat.mtrl-sci
  - cond-mat.mes-hall
  - physics.comp-ph
---

# Large-scale Monte Carlo/Molecular Dynamics simulations with Atomic Cluster Expansion potentials in LAMMPS

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.21147
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Lorenzo Piersante, Anirudh Raju Natarajan
- **Published:** 2026-11-16

## Summary
Monte Carlo/molecular dynamics (MCMD) simulations are widely used to study the properties of materials at the mesoscale. Simulations with hundreds of thousands of atoms usually rely on empirical potentials because MCMD with machine-learning interatomic potentials is impractical at this scale in existing implementations. Here, we introduce a hybrid MPI/OpenMP scheme for MCMD with Atomic Cluster Expansion (ACE) potentials in LAMMPS. Monte Carlo moves are evaluated from local energy changes and carried out in parallel over MPI ranks, while molecular dynamics is parallelized over OpenMP threads. At a fixed number of CPUs, the wall time of the Monte Carlo moves decreases by a factor equal to the number of MPI ranks. Larger simulation cells also reduce the statistical errors of free energy calculations because thermal fluctuations decrease with system size. We demonstrate the scheme by calculating free energies of the HCP and BCC phases in the strongly anharmonic Hf--Ti system and by simulating zirconium segregation in a nanocrystalline copper sample of 670,000 atoms. For Cu--Zr, an ACE potential and an empirical potential predict similar grain boundary compositions but different amounts of zirconium dissolved in the grains. The scheme makes MCMD simulations with machine-learning interatomic potentials practical at the length scales of microstructure.

## Provider details
- **Arxiv Id:** 2611.21147
- **Categories:** ["cond-mat.mtrl-sci", "cond-mat.mes-hall", "physics.comp-ph"]
