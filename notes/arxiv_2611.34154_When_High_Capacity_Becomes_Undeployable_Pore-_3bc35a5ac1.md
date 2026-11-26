---
title: 'When High Capacity Becomes Undeployable: Pore-Filling Constraints for Multi-Objective
  Optimization of Direct Air Capture Sorbents'
type: arxiv
source: https://arxiv.org/abs/2611.34154
canonical_url: https://arxiv.org/abs/2611.34154
captured_by: auto-scanner
date: '2026-11-26'
captured_at: '2026-11-26T14:39:56+00:00'
last_requested: '2026-11-26T14:39:56+00:00'
issue: scan:arxiv-ml-atomistic
status: to-read
authors:
- Yujie Liu
- Xuehua Shen
- Zuotai Zhang
published: '2026-11-25'
abstract: 'Amine-impregnated sorbents with the highest nominal CO2 capacity are frequently
  the least deployable, as amine beyond the pore-volume limit blocks active sites.
  Yet multi-objective Bayesian optimization (MOBO) for direct air capture (DAC) treats
  formulation search as unconstrained. We encode the pore-filling boundary as an explicit
  outcome constraint, c(x) = tanh(1 - phi_hat) - tau, and use it as a diagnostic instrument
  on a hand-curated, DOI-traceable benchmark of 618 solid-amine formulations from
  43 publications. Unconstrained MOBO attains higher nominal capacity (3.639 +/- 0.815
  vs. 2.964 +/- 0.728 mmol/g, p = 1.0e-11), but across 100 seeds 63.2% of its Pareto-optimal
  candidates violate the pore-filling boundary versus 39.3% under the constraint:
  it is rewarded for proposing candidates outside the pore-confined design regime.
  The constraint steers the front to lower loadings (55.8 vs. 65.2 wt%) and larger
  pores. The boundary is corroborated once apparatus effects are harmonized hierarchically:
  77.8% of kinetic variance is between-laboratory, and pore filling carries a significant
  kinetic penalty (p = 0.002). Standard hypervolume over-credits feasibility-agnostic
  methods by 13.9-16.1% (vs. 11.1% constrained), and three surrogate-based analyses---the
  constrained front, a regeneration-energy third objective, and harmonized kinetics---consistently
  point to a conservative deployable window at pore filling phi_hat ~ 0.4-0.5 (45-55
  wt% loading). The benchmark and associated analysis outputs accompany this submission.'
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.34154'
  categories:
  - cs.LG
  - cond-mat.mtrl-sci
---

# When High Capacity Becomes Undeployable: Pore-Filling Constraints for Multi-Objective Optimization of Direct Air Capture Sorbents

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.34154
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Yujie Liu, Xuehua Shen, Zuotai Zhang
- **Published:** 2026-11-25

## Summary
Amine-impregnated sorbents with the highest nominal CO2 capacity are frequently the least deployable, as amine beyond the pore-volume limit blocks active sites. Yet multi-objective Bayesian optimization (MOBO) for direct air capture (DAC) treats formulation search as unconstrained. We encode the pore-filling boundary as an explicit outcome constraint, c(x) = tanh(1 - phi_hat) - tau, and use it as a diagnostic instrument on a hand-curated, DOI-traceable benchmark of 618 solid-amine formulations from 43 publications. Unconstrained MOBO attains higher nominal capacity (3.639 +/- 0.815 vs. 2.964 +/- 0.728 mmol/g, p = 1.0e-11), but across 100 seeds 63.2% of its Pareto-optimal candidates violate the pore-filling boundary versus 39.3% under the constraint: it is rewarded for proposing candidates outside the pore-confined design regime. The constraint steers the front to lower loadings (55.8 vs. 65.2 wt%) and larger pores. The boundary is corroborated once apparatus effects are harmonized hierarchically: 77.8% of kinetic variance is between-laboratory, and pore filling carries a significant kinetic penalty (p = 0.002). Standard hypervolume over-credits feasibility-agnostic methods by 13.9-16.1% (vs. 11.1% constrained), and three surrogate-based analyses---the constrained front, a regeneration-energy third objective, and harmonized kinetics---consistently point to a conservative deployable window at pore filling phi_hat ~ 0.4-0.5 (45-55 wt% loading). The benchmark and associated analysis outputs accompany this submission.

## Provider details
- **Arxiv Id:** 2611.34154
- **Categories:** ["cs.LG", "cond-mat.mtrl-sci"]
