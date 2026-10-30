---
title: A latent-space extrapolation grade built into graph atomic cluster expansion
  foundation potentials
type: arxiv
source: https://arxiv.org/abs/2609.40060
canonical_url: https://arxiv.org/abs/2609.40060
captured_by: sandipde
date: '2026-10-30'
captured_at: '2026-10-30T11:14:21+00:00'
last_requested: '2026-10-30T11:14:21+00:00'
issue: '191'
status: to-read
authors:
- Yury Lysogorskiy
- Anton Bochkarev
- Ralf Drautz
published: '2026-09-30'
abstract: Foundation machine-learning interatomic potentials cover broad configurational
  and chemical spaces, but their reliability can vary across the atomic environments
  encountered during a simulation. Here we introduce the calibrated Mahalanobis (CALM)
  extrapolation grade $γ$, a piecewise differentiable per-atom quantity integrated
  into GRACE foundation models and evaluated alongside energies and forces in a single
  model pass. We define $γ$ from nearest-cluster Mahalanobis distances in latent feature
  space, setting $γ=1$ from the training-distance distribution separately for each
  element and cluster. Controlled tests show that a normalized random projection of
  the invariant many-body basis detects structural and chemical extrapolation. On
  different foundation datasets, OMat24 and SMAX, $γ$ correlates with atomic force
  errors and separates structures with different error distributions. The CALM grade
  adds percent-level computational cost, and its spatial gradient guides uncertainty-biased
  data collection toward configurations with larger absolute force errors.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2609.40060'
  categories:
  - cond-mat.mtrl-sci
  primary_category: cond-mat.mtrl-sci
  updated: '2026-09-30T16:21:09Z'
  doi: ''
---

# A latent-space extrapolation grade built into graph atomic cluster expansion foundation potentials

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2609.40060
- **Captured by:** @sandipde
- **Metadata:** complete (arXiv)
- **Authors:** Yury Lysogorskiy, Anton Bochkarev, Ralf Drautz
- **Published:** 2026-09-30

## Summary
Foundation machine-learning interatomic potentials cover broad configurational and chemical spaces, but their reliability can vary across the atomic environments encountered during a simulation. Here we introduce the calibrated Mahalanobis (CALM) extrapolation grade $γ$, a piecewise differentiable per-atom quantity integrated into GRACE foundation models and evaluated alongside energies and forces in a single model pass. We define $γ$ from nearest-cluster Mahalanobis distances in latent feature space, setting $γ=1$ from the training-distance distribution separately for each element and cluster. Controlled tests show that a normalized random projection of the invariant many-body basis detects structural and chemical extrapolation. On different foundation datasets, OMat24 and SMAX, $γ$ correlates with atomic force errors and separates structures with different error distributions. The CALM grade adds percent-level computational cost, and its spatial gradient guides uncertainty-biased data collection toward configurations with larger absolute force errors.

## Provider details
- **Arxiv Id:** 2609.40060
- **Categories:** ["cond-mat.mtrl-sci"]
- **Primary Category:** cond-mat.mtrl-sci
- **Updated:** 2026-09-30T16:21:09Z
