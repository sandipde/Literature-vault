---
title: ADAPTIVE-WEIGHTED PHYSICS-INFORMED NEURAL NETWORK FOR MULTI-PHASE GUIDED PROJECTILE
  EXTERIOR BALLISTIC TRAJECTORY SOLVING
type: paper
source: https://doi.org/10.12783/ballistics26/37594
canonical_url: https://doi.org/10.12783/ballistics26/37594
captured_by: auto-scanner
date: '2026-11-16'
captured_at: '2026-11-16T13:18:51+00:00'
last_requested: '2026-11-16T13:18:51+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Ziyang Zhang
- Jinquan Chen
- Xugang Wang
- Zhongyuan Wang
published: '2026-11-01'
abstract: This paper establishes a physics-informed neural network (PINN) framework
  for solving the multi-phase exterior ballistic initial value problem of guided projectiles,
  without relying on pre-generated trajectory datasets. Smooth sigmoid functions are
  employed to unify thrust switching and angle-of-attack regulation across five flight
  sub-phases into a single continuously differentiable system. To address the optimization
  imbalance caused by disparate gradient scales among the four coupled equation components,
  a gradient-norm-based adaptive weighting mechanism is introduced to construct an
  adaptive-weighted PINN (AW-PINN), which dynamically adjusts component loss weights
  based on exponentially smoothed gradient norms. Under identical network architecture
  and training conditions, AW-PINN is compared with standard PINN and residual-adaptive
  sampling PINN (RAS-PINN), using independently computed RK45 numerical solutions
  as the evaluation benchmark. Results show that AW-PINN reduces full-trajectory RMSE
  by approximately 85–92% relative to standard PINN across all state variables, achieving
  the highest overall accuracy among the three strategies.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.12783/ballistics26/37594
  journal: Ballistics 2026
  publisher: Destech Publications, Inc.
  type: proceedings-article
  subjects: []
---

# ADAPTIVE-WEIGHTED PHYSICS-INFORMED NEURAL NETWORK FOR MULTI-PHASE GUIDED PROJECTILE EXTERIOR BALLISTIC TRAJECTORY SOLVING

- **Type:** paper
- **Source:** https://doi.org/10.12783/ballistics26/37594
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Ziyang Zhang, Jinquan Chen, Xugang Wang, Zhongyuan Wang
- **Published:** 2026-11-01

## Summary
This paper establishes a physics-informed neural network (PINN) framework for solving the multi-phase exterior ballistic initial value problem of guided projectiles, without relying on pre-generated trajectory datasets. Smooth sigmoid functions are employed to unify thrust switching and angle-of-attack regulation across five flight sub-phases into a single continuously differentiable system. To address the optimization imbalance caused by disparate gradient scales among the four coupled equation components, a gradient-norm-based adaptive weighting mechanism is introduced to construct an adaptive-weighted PINN (AW-PINN), which dynamically adjusts component loss weights based on exponentially smoothed gradient norms. Under identical network architecture and training conditions, AW-PINN is compared with standard PINN and residual-adaptive sampling PINN (RAS-PINN), using independently computed RK45 numerical solutions as the evaluation benchmark. Results show that AW-PINN reduces full-trajectory RMSE by approximately 85–92% relative to standard PINN across all state variables, achieving the highest overall accuracy among the three strategies.

## Provider details
- **Doi:** 10.12783/ballistics26/37594
- **Journal:** Ballistics 2026
- **Publisher:** Destech Publications, Inc.
- **Type:** proceedings-article
