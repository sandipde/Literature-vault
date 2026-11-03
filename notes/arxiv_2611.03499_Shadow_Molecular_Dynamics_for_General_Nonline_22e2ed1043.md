---
title: Shadow Molecular Dynamics for General Nonlinear Flexible-Charge Models
type: arxiv
source: https://arxiv.org/abs/2611.03499
canonical_url: https://arxiv.org/abs/2611.03499
captured_by: auto-scanner
date: '2026-11-03'
captured_at: '2026-11-03T12:34:47+00:00'
last_requested: '2026-11-03T12:34:47+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Jos Thomas
- Anthony P. Baldo
- Rae A. Corrigan Grove
- Mehmet Cagri Kaymak
- Joshua Finkelstein
- James Goff
- Maksim Kulichenko
- Sergei Tretiak
- Nicholas Lubbers
- Vishikh Athavale
- Christian F. A. Negre
- Michael Wall
- Anders M. N. Niklasson
published: '2026-11-02'
abstract: Machine-learned interatomic potentials have greatly expanded the reach of
  molecular dynamics simulations, but complex chemical environments often require
  explicit treatment of long-range electronic response, including charge transfer
  and polarization. Physics-based flexible-charge models capture these effects but
  require global nonlinear charge equilibration at every time step to obtain Born-Oppenheimer
  energies and forces. This process is computationally expensive and can lead to instabilities
  unless tightly converged. Here, we introduce a shadow molecular dynamics framework
  for flexible-charge models with arbitrary local nonlinearities and long-range multipolar
  electrostatics. We replace the exact Born-Oppenheimer potential with a nearby shadow
  potential obtained by exactly equilibrating a partially linearized electronic energy
  functional. This provides conservative forces and reduces the global nonlinear equilibration
  to a quasi-diagonal linear problem that can be solved directly at low cost. Auxiliary
  dynamical electronic degrees of freedom, propagated through an extended-Lagrangian
  dynamics, capture the long-range electronic response and define the reference state
  for the linearization of the energy functional. GPU-accelerated simulations with
  over 100,000 atoms demonstrate that the shadow potential closely follows the tightly
  converged Born-Oppenheimer surface, while maintaining long-term stability at a computational
  cost approaching that of a fixed-charge model. These advances establish an efficient
  and broadly applicable framework for machine-learned interatomic potentials that
  explicitly incorporate long-range electrostatic interactions and environment-dependent
  electronic response.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.03499'
  categories:
  - physics.chem-ph
---

# Shadow Molecular Dynamics for General Nonlinear Flexible-Charge Models

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.03499
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Jos Thomas, Anthony P. Baldo, Rae A. Corrigan Grove, Mehmet Cagri Kaymak, Joshua Finkelstein, James Goff, Maksim Kulichenko, Sergei Tretiak, Nicholas Lubbers, Vishikh Athavale, Christian F. A. Negre, Michael Wall, Anders M. N. Niklasson
- **Published:** 2026-11-02

## Summary
Machine-learned interatomic potentials have greatly expanded the reach of molecular dynamics simulations, but complex chemical environments often require explicit treatment of long-range electronic response, including charge transfer and polarization. Physics-based flexible-charge models capture these effects but require global nonlinear charge equilibration at every time step to obtain Born-Oppenheimer energies and forces. This process is computationally expensive and can lead to instabilities unless tightly converged. Here, we introduce a shadow molecular dynamics framework for flexible-charge models with arbitrary local nonlinearities and long-range multipolar electrostatics. We replace the exact Born-Oppenheimer potential with a nearby shadow potential obtained by exactly equilibrating a partially linearized electronic energy functional. This provides conservative forces and reduces the global nonlinear equilibration to a quasi-diagonal linear problem that can be solved directly at low cost. Auxiliary dynamical electronic degrees of freedom, propagated through an extended-Lagrangian dynamics, capture the long-range electronic response and define the reference state for the linearization of the energy functional. GPU-accelerated simulations with over 100,000 atoms demonstrate that the shadow potential closely follows the tightly converged Born-Oppenheimer surface, while maintaining long-term stability at a computational cost approaching that of a fixed-charge model. These advances establish an efficient and broadly applicable framework for machine-learned interatomic potentials that explicitly incorporate long-range electrostatic interactions and environment-dependent electronic response.

## Provider details
- **Arxiv Id:** 2611.03499
- **Categories:** ["physics.chem-ph"]
