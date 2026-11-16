---
title: 'Physical Fidelity of Learned Nonlinear Vehicle Dynamics: Validation Selection,
  Observational Bias, and Architecture-Conditioned Inductive Bias'
type: paper
source: https://doi.org/10.21203/rs.3.rs-11443334/v1
canonical_url: https://doi.org/10.21203/rs.3.rs-11443334/v1
captured_by: auto-scanner
date: '2026-11-16'
captured_at: '2026-11-16T13:18:51+00:00'
last_requested: '2026-11-16T13:18:51+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Josafat Leal FIlho
- Antônio Augusto Fröhlich
published: '2026-11-16'
abstract: 'Abstract Learned vehicle-dynamics models can reproduce nominal trajectories
  while misrepresenting local tangent and finite-time behavior. We evaluate this discrepancy
  using analytical 3-, 7-, and 14-state nonlinear vehicle models with vector-field,
  Jacobian, directional-deformation, and frozen-local propagator metrics. Reference-based
  validation selectors substantially enrich critical-region coverage: at a 10\% budget,
  symmetric growth reaches macro recall 0.4338 versus 0.1011 for random sampling.
  In fresh-seed training, physics-inspired selection reduces 14-state Jacobian error
  by 2.09\%, below the predefined 5\% practical threshold, while the 5.80\% propagator
  reduction is not significant after Holm correction. A coverage-constrained Lagrangian
  selector improves Jacobian error by 16.5\% but worsens propagator error by 27.6\%,
  showing that better local derivative fidelity does not guarantee better finite-time
  response. Adaptive loss balancing and Adam-to-L-BFGS refinement provide no consistent
  gains, and architecture effects depend on learner parameterization. A post-hoc state-resolved
  analysis of 716 frozen checkpoints further shows that training interventions redistribute
  fidelity across physical states: M1 improves the longitudinal, pitch-rate, and wheel-spin
  equations while degrading lateral-velocity and roll-rate dynamics. These results
  support target-specific, coverage-aware training and validation rather than assuming
  that more physics-selected data or stronger physical priors improve all fidelity
  measures.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.21203/rs.3.rs-11443334/v1
  journal: ''
  publisher: Springer Science and Business Media LLC
  type: posted-content
  subjects: []
---

# Physical Fidelity of Learned Nonlinear Vehicle Dynamics: Validation Selection, Observational Bias, and Architecture-Conditioned Inductive Bias

- **Type:** paper
- **Source:** https://doi.org/10.21203/rs.3.rs-11443334/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Josafat Leal FIlho, Antônio Augusto Fröhlich
- **Published:** 2026-11-16

## Summary
Abstract Learned vehicle-dynamics models can reproduce nominal trajectories while misrepresenting local tangent and finite-time behavior. We evaluate this discrepancy using analytical 3-, 7-, and 14-state nonlinear vehicle models with vector-field, Jacobian, directional-deformation, and frozen-local propagator metrics. Reference-based validation selectors substantially enrich critical-region coverage: at a 10\% budget, symmetric growth reaches macro recall 0.4338 versus 0.1011 for random sampling. In fresh-seed training, physics-inspired selection reduces 14-state Jacobian error by 2.09\%, below the predefined 5\% practical threshold, while the 5.80\% propagator reduction is not significant after Holm correction. A coverage-constrained Lagrangian selector improves Jacobian error by 16.5\% but worsens propagator error by 27.6\%, showing that better local derivative fidelity does not guarantee better finite-time response. Adaptive loss balancing and Adam-to-L-BFGS refinement provide no consistent gains, and architecture effects depend on learner parameterization. A post-hoc state-resolved analysis of 716 frozen checkpoints further shows that training interventions redistribute fidelity across physical states: M1 improves the longitudinal, pitch-rate, and wheel-spin equations while degrading lateral-velocity and roll-rate dynamics. These results support target-specific, coverage-aware training and validation rather than assuming that more physics-selected data or stronger physical priors improve all fidelity measures.

## Provider details
- **Doi:** 10.21203/rs.3.rs-11443334/v1
- **Publisher:** Springer Science and Business Media LLC
- **Type:** posted-content
