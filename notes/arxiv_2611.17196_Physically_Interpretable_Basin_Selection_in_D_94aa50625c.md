---
title: Physically Interpretable Basin Selection in Discrete-Variable Origami Design
type: arxiv
source: https://arxiv.org/abs/2611.17196
canonical_url: https://arxiv.org/abs/2611.17196
captured_by: auto-scanner
date: '2026-11-13'
captured_at: '2026-11-13T12:48:29+00:00'
last_requested: '2026-11-13T12:48:29+00:00'
issue: scan:arxiv-ml-atomistic
status: to-read
authors:
- Lucy Liu
- Leon M. Kamp
- Katia Bertoldi
- L. Mahadevan
published: '2026-11-12'
abstract: 'Automatic differentiation has enabled rapid progress on continuous-variable
  mechanical design problems, but gradient-based optimization still struggles with
  discrete variables. The standard approach is to optimize using a continuous relaxation
  of the choices, then commit to the nearest discrete design at the end. Why this
  procedure selects unfavorable basins is poorly understood. Here, we introduce a
  practical, interpretable design problem inspired by origami, in which automatic
  differentiation is used to design shapes with a target functional behavior. Each
  origami sheet has a fixed geometry, and a bilevel optimization framework tunes which
  one of four discrete hinge types to place at each fold. Baseline gradient-based
  design settles into basins with a large discretization gap: relaxed optimization
  solves 97% of runs, but the final, discrete solutions succeed only half the time.
  We find that the gap can be relieved with a surprisingly simple modification. An
  initialization prior uniformly biased toward the stiff, flat hinge option boosts
  the final solve fraction from 49% to 69%. Applying the prior adds no additional
  compute and leaves the optimization process unchanged. Compared to the baseline,
  sheets produced with the prior have greater geometric compatibility and mechanical
  stiffness. Directly penalizing frustration and floppiness in the outer loss function
  produces an even greater improvement than the prior does, raising the solve fraction
  to 78% and indicating that these properties help distinguish the unfavorable basins.
  Our results demonstrate that loss landscapes for mechanical design can have physically
  meaningful basins that are not robust to discretization and cause solves to fail.
  Targeting these basins'' physical signatures, even with just an initialization bias,
  helps avoid them.'
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.17196'
  categories:
  - cs.LG
  - cond-mat.mtrl-sci
  - cond-mat.soft
---

# Physically Interpretable Basin Selection in Discrete-Variable Origami Design

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.17196
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Lucy Liu, Leon M. Kamp, Katia Bertoldi, L. Mahadevan
- **Published:** 2026-11-12

## Summary
Automatic differentiation has enabled rapid progress on continuous-variable mechanical design problems, but gradient-based optimization still struggles with discrete variables. The standard approach is to optimize using a continuous relaxation of the choices, then commit to the nearest discrete design at the end. Why this procedure selects unfavorable basins is poorly understood. Here, we introduce a practical, interpretable design problem inspired by origami, in which automatic differentiation is used to design shapes with a target functional behavior. Each origami sheet has a fixed geometry, and a bilevel optimization framework tunes which one of four discrete hinge types to place at each fold. Baseline gradient-based design settles into basins with a large discretization gap: relaxed optimization solves 97% of runs, but the final, discrete solutions succeed only half the time. We find that the gap can be relieved with a surprisingly simple modification. An initialization prior uniformly biased toward the stiff, flat hinge option boosts the final solve fraction from 49% to 69%. Applying the prior adds no additional compute and leaves the optimization process unchanged. Compared to the baseline, sheets produced with the prior have greater geometric compatibility and mechanical stiffness. Directly penalizing frustration and floppiness in the outer loss function produces an even greater improvement than the prior does, raising the solve fraction to 78% and indicating that these properties help distinguish the unfavorable basins. Our results demonstrate that loss landscapes for mechanical design can have physically meaningful basins that are not robust to discretization and cause solves to fail. Targeting these basins' physical signatures, even with just an initialization bias, helps avoid them.

## Provider details
- **Arxiv Id:** 2611.17196
- **Categories:** ["cs.LG", "cond-mat.mtrl-sci", "cond-mat.soft"]
