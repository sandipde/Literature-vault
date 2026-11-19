---
title: Machine-learned acceleration of earthquake sequence simulations
type: arxiv
source: https://arxiv.org/abs/2611.23561
canonical_url: https://arxiv.org/abs/2611.23561
captured_by: auto-scanner
date: '2026-11-19'
captured_at: '2026-11-19T14:04:33+00:00'
last_requested: '2026-11-19T14:04:33+00:00'
issue: scan:arxiv-ml-atomistic
status: to-read
authors:
- Reo Yanagi
- Taeho Kim
- Kaushik Bhattacharya
- Nadia Lapusta
published: '2026-11-17'
abstract: Earthquake sequence simulations involve slow interseismic processes and
  rapid dynamic ruptures. During interseismic periods, a numerical solver can take
  large time steps efficiently. During seismic periods, in contrast, the solver must
  drastically reduce the time step, and elastodynamic wave-mediated memory effects
  become significant; long-term simulations are therefore computationally expensive.
  We investigate the use of neural operators to accelerate earthquake sequence simulations.
  We train a Fourier neural operator (FNO) on data from high-fidelity, fully dynamic
  simulations to learn a jump map that advances the system state from before a seismic
  rupture to after it. We propose a hybrid modeling framework in which a conventional
  quasi-dynamic solver simulates the slow interseismic evolution, and the trained
  FNO replaces the solver during the computationally intensive seismic periods with
  wave-mediated inertial effects. The hybrid model reproduces key long-term statistics
  of fully dynamic simulations, including distributions of event magnitudes and recurrence
  times. Furthermore, it provides a much better approximation to the fully dynamic
  simulations than the commonly used quasi-dynamic approximation at a reduced computational
  expense.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.23561'
  categories:
  - physics.geo-ph
  - cond-mat.mtrl-sci
---

# Machine-learned acceleration of earthquake sequence simulations

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.23561
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Reo Yanagi, Taeho Kim, Kaushik Bhattacharya, Nadia Lapusta
- **Published:** 2026-11-17

## Summary
Earthquake sequence simulations involve slow interseismic processes and rapid dynamic ruptures. During interseismic periods, a numerical solver can take large time steps efficiently. During seismic periods, in contrast, the solver must drastically reduce the time step, and elastodynamic wave-mediated memory effects become significant; long-term simulations are therefore computationally expensive. We investigate the use of neural operators to accelerate earthquake sequence simulations. We train a Fourier neural operator (FNO) on data from high-fidelity, fully dynamic simulations to learn a jump map that advances the system state from before a seismic rupture to after it. We propose a hybrid modeling framework in which a conventional quasi-dynamic solver simulates the slow interseismic evolution, and the trained FNO replaces the solver during the computationally intensive seismic periods with wave-mediated inertial effects. The hybrid model reproduces key long-term statistics of fully dynamic simulations, including distributions of event magnitudes and recurrence times. Furthermore, it provides a much better approximation to the fully dynamic simulations than the commonly used quasi-dynamic approximation at a reduced computational expense.

## Provider details
- **Arxiv Id:** 2611.23561
- **Categories:** ["physics.geo-ph", "cond-mat.mtrl-sci"]
