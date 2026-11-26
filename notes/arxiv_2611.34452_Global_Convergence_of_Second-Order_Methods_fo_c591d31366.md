---
title: Global Convergence of Second-Order Methods for Physics-Informed Neural Networks
  in the Overparameterized Limit
type: arxiv
source: https://arxiv.org/abs/2611.34452
canonical_url: https://arxiv.org/abs/2611.34452
captured_by: auto-scanner
date: '2026-11-26'
captured_at: '2026-11-26T14:39:56+00:00'
last_requested: '2026-11-26T14:39:56+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Konstantin Riedl
- Justin Sirignano
- Konstantinos Spiliopoulos
published: '2026-11-25'
abstract: 'Solving high-dimensional partial differential equations (PDEs) constitutes
  a core task in many engineering and scientific disciplines. Physics-informed neural
  networks and the deep Galerkin method effectively leverage machine learning models
  to approximate solutions of known PDEs by minimizing residuals corresponding to
  the PDE operator alongside external constraints. Although second-order optimizers
  are becoming increasingly popular for training neural networks (NNs) to solve PDEs
  and empirically outperform their first-order counterparts in both speed and accuracy,
  the convergence theory for training such models is essentially confined to first-order
  methods. In this paper, we close this gap and develop a convergence analysis for
  the regularized Newton and Gauss-Newton methods. As the number of hidden units tends
  to infinity, the training dynamics converge in probability, with explicit rates,
  to the solution of a deterministic limit equation involving a Newton neural tangent
  kernel operator associated with the PDE. Although the limiting kernel operator admits
  no spectral gap, we prove that, in the overparameterized limit, the PDE residual
  vanishes as training proceeds, and, under mild assumptions, the NN converges to
  the PDE solution. We further show that, provided a sufficiently small regularization
  parameter, the projection of the residual onto any fixed number of leading eigenfunctions
  decays exponentially fast, demonstrating that this hyperparameter acts as a spectral
  filter: it lifts the convergence rates of high-frequency components toward those
  of low-frequency ones, thereby mitigating the spectral bias inherent in gradient
  descent. Mathematical challenges arise from the implicit parameter update involving
  a linear system whose dimension increases with the NN width and, for Newton''s method,
  a potentially indefinite Hessian, as well as from the PDE operator entering the
  kernel.'
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.34452'
  categories:
  - math.NA
  - cs.LG
  - math.AP
  - math.OC
  - stat.ML
---

# Global Convergence of Second-Order Methods for Physics-Informed Neural Networks in the Overparameterized Limit

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.34452
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Konstantin Riedl, Justin Sirignano, Konstantinos Spiliopoulos
- **Published:** 2026-11-25

## Summary
Solving high-dimensional partial differential equations (PDEs) constitutes a core task in many engineering and scientific disciplines. Physics-informed neural networks and the deep Galerkin method effectively leverage machine learning models to approximate solutions of known PDEs by minimizing residuals corresponding to the PDE operator alongside external constraints. Although second-order optimizers are becoming increasingly popular for training neural networks (NNs) to solve PDEs and empirically outperform their first-order counterparts in both speed and accuracy, the convergence theory for training such models is essentially confined to first-order methods. In this paper, we close this gap and develop a convergence analysis for the regularized Newton and Gauss-Newton methods. As the number of hidden units tends to infinity, the training dynamics converge in probability, with explicit rates, to the solution of a deterministic limit equation involving a Newton neural tangent kernel operator associated with the PDE. Although the limiting kernel operator admits no spectral gap, we prove that, in the overparameterized limit, the PDE residual vanishes as training proceeds, and, under mild assumptions, the NN converges to the PDE solution. We further show that, provided a sufficiently small regularization parameter, the projection of the residual onto any fixed number of leading eigenfunctions decays exponentially fast, demonstrating that this hyperparameter acts as a spectral filter: it lifts the convergence rates of high-frequency components toward those of low-frequency ones, thereby mitigating the spectral bias inherent in gradient descent. Mathematical challenges arise from the implicit parameter update involving a linear system whose dimension increases with the NN width and, for Newton's method, a potentially indefinite Hessian, as well as from the PDE operator entering the kernel.

## Provider details
- **Arxiv Id:** 2611.34452
- **Categories:** ["math.NA", "cs.LG", "math.AP", "math.OC", "stat.ML"]
