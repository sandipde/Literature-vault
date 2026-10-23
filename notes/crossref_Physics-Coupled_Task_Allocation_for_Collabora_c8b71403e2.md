---
title: Physics-Coupled Task Allocation for Collaborative Robotic Welding of Dissimilar
  Steel Joints Using an α-Potential Game and a Physics-Informed Neural Network Surrogate
type: paper
source: https://doi.org/10.21203/rs.3.rs-11280089/v1
canonical_url: https://doi.org/10.21203/rs.3.rs-11280089/v1
captured_by: auto-scanner
date: '2026-10-23'
captured_at: '2026-10-23T20:11:01+00:00'
last_requested: '2026-10-23T20:11:01+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- mohammad reza omidi
published: '2026-10-23'
abstract: 'Abstract Collaborative robotic welding of dissimilar steel joints involves
  coupled decisions concerning task assignment, welding sequence, thermal interaction,
  energy consumption, and production time. Conventional distance-based allocation
  methods do not explicitly account for the fact that neighboring welding operations
  may modify the thermal state and mechanical response of subsequent operations. This
  study proposes a physics-coupled task-allocation framework in which collaborative
  welding robots are modelled as players of an α-potential game and the thermo-mechanical
  response is evaluated using a physics-informed neural-network (PINN) surrogate.
  The α-potential formulation represents the bounded discrepancy between individual
  utility changes and changes in a common potential function resulting from non-additive
  thermal interactions. A sufficient equilibrium result is established: under a finite
  feasible strategy space, a global maximizer of the α-potential is an α-Nash equilibrium.
  Log-linear learning is employed as a stochastic strategy-update mechanism, while
  finite-time convergence results from the potential-game literature are invoked only
  for the exact-potential case and under their stated assumptions. The PINN incorporates
  the transient heat-conduction and mechanical-equilibrium equations into its training
  objective and provides a reduced-cost approximation of repeated thermo-mechanical
  evaluations. In the computational study, the proposed framework reduced normalized
  makespan and energy consumption relative to the distance-driven allocation strategy
  while simultaneously accounting for residual stress and carbon redistribution. The
  results indicate that coupling physical response with distributed task allocation
  can improve the quality of multi-robot welding decisions. The reported numerical
  values are computational predictions and should be independently validated experimentally
  before being generalized to industrial welding applications.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.21203/rs.3.rs-11280089/v1
  journal: ''
  publisher: Springer Science and Business Media LLC
  type: posted-content
  subjects: []
---

# Physics-Coupled Task Allocation for Collaborative Robotic Welding of Dissimilar Steel Joints Using an α-Potential Game and a Physics-Informed Neural Network Surrogate

- **Type:** paper
- **Source:** https://doi.org/10.21203/rs.3.rs-11280089/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** mohammad reza omidi
- **Published:** 2026-10-23

## Summary
Abstract Collaborative robotic welding of dissimilar steel joints involves coupled decisions concerning task assignment, welding sequence, thermal interaction, energy consumption, and production time. Conventional distance-based allocation methods do not explicitly account for the fact that neighboring welding operations may modify the thermal state and mechanical response of subsequent operations. This study proposes a physics-coupled task-allocation framework in which collaborative welding robots are modelled as players of an α-potential game and the thermo-mechanical response is evaluated using a physics-informed neural-network (PINN) surrogate. The α-potential formulation represents the bounded discrepancy between individual utility changes and changes in a common potential function resulting from non-additive thermal interactions. A sufficient equilibrium result is established: under a finite feasible strategy space, a global maximizer of the α-potential is an α-Nash equilibrium. Log-linear learning is employed as a stochastic strategy-update mechanism, while finite-time convergence results from the potential-game literature are invoked only for the exact-potential case and under their stated assumptions. The PINN incorporates the transient heat-conduction and mechanical-equilibrium equations into its training objective and provides a reduced-cost approximation of repeated thermo-mechanical evaluations. In the computational study, the proposed framework reduced normalized makespan and energy consumption relative to the distance-driven allocation strategy while simultaneously accounting for residual stress and carbon redistribution. The results indicate that coupling physical response with distributed task allocation can improve the quality of multi-robot welding decisions. The reported numerical values are computational predictions and should be independently validated experimentally before being generalized to industrial welding applications.

## Provider details
- **Doi:** 10.21203/rs.3.rs-11280089/v1
- **Publisher:** Springer Science and Business Media LLC
- **Type:** posted-content
