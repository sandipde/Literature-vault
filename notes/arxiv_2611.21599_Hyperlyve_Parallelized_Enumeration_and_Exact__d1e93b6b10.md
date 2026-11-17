---
title: 'Hyperlyve: Parallelized Enumeration and Exact Lyapunov Stability Certification
  for Deep ReLU Networks'
type: arxiv
source: https://arxiv.org/abs/2611.21599
canonical_url: https://arxiv.org/abs/2611.21599
captured_by: auto-scanner
date: '2026-11-17'
captured_at: '2026-11-17T14:04:00+00:00'
last_requested: '2026-11-17T14:04:00+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Brian Yarbrough
- Jesse Wayment
- Jingbo Wang
- Philip E. Paré
- Shreyas Sundaram
published: '2026-11-16'
abstract: We introduce Hyperlyve (Hyperplane Partitioned Lyapunov Verification and
  Enumeration), a framework for proving the asymptotic stability of nonlinear dynamical
  systems, including those with neural network controllers. Hyperlyve learns and formally
  certifies continuous piecewise-affine (CPA) neural Lyapunov functions within a counterexample-guided
  inductive synthesis (CEGIS) loop. Hyperlyve's key innovation is a parallel algorithm
  that enumerates the hyperplane arrangement formed by the ReLU activations of deep
  networks and certifies that Lyapunov conditions hold within each polyhedral region.
  We derive sound and complete regional tests to verify the asymptotic stability of
  the exact smooth dynamics (rather than a piecewise-linear approximation) within
  a compact domain of interest. Furthermore, we formally characterize the computational
  complexity of the CPA neural Lyapunov verification problem as co-NP-complete, filling
  a key gap in the literature. Empirical results demonstrate that Hyperlyve enumerates
  ReLU networks over 150-times faster than competing tools, which contributes to Hyperlyve
  proving the asymptotic stability of systems that are currently intractable for state-of-the-art
  verifiers.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.21599'
  categories:
  - eess.SY
  - cs.CG
  - cs.LG
  - cs.LO
  - math.DS
---

# Hyperlyve: Parallelized Enumeration and Exact Lyapunov Stability Certification for Deep ReLU Networks

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.21599
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Brian Yarbrough, Jesse Wayment, Jingbo Wang, Philip E. Paré, Shreyas Sundaram
- **Published:** 2026-11-16

## Summary
We introduce Hyperlyve (Hyperplane Partitioned Lyapunov Verification and Enumeration), a framework for proving the asymptotic stability of nonlinear dynamical systems, including those with neural network controllers. Hyperlyve learns and formally certifies continuous piecewise-affine (CPA) neural Lyapunov functions within a counterexample-guided inductive synthesis (CEGIS) loop. Hyperlyve's key innovation is a parallel algorithm that enumerates the hyperplane arrangement formed by the ReLU activations of deep networks and certifies that Lyapunov conditions hold within each polyhedral region. We derive sound and complete regional tests to verify the asymptotic stability of the exact smooth dynamics (rather than a piecewise-linear approximation) within a compact domain of interest. Furthermore, we formally characterize the computational complexity of the CPA neural Lyapunov verification problem as co-NP-complete, filling a key gap in the literature. Empirical results demonstrate that Hyperlyve enumerates ReLU networks over 150-times faster than competing tools, which contributes to Hyperlyve proving the asymptotic stability of systems that are currently intractable for state-of-the-art verifiers.

## Provider details
- **Arxiv Id:** 2611.21599
- **Categories:** ["eess.SY", "cs.CG", "cs.LG", "cs.LO", "math.DS"]
