---
title: An inexact stochastic variance-reduced gradient method for constrained convex
  finite-sum optimization
type: arxiv
source: https://arxiv.org/abs/2611.23221
canonical_url: https://arxiv.org/abs/2611.23221
captured_by: auto-scanner
date: '2026-11-18'
captured_at: '2026-11-18T13:38:13+00:00'
last_requested: '2026-11-18T13:38:13+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Zhaosong Lu
- Yifeng Xiao
published: '2026-11-17'
abstract: In this paper, we study a class of constrained convex finite-sum optimization
  problems. In many practical applications, all or some of the constraints are hard
  constraints that represent imperative requirements. Consequently, any desirable
  approximate solution must (nearly) satisfy these constraints. Motivated by this,
  we focus on computing an $ε$-$surely\ feasible\ stochastic\ optimal$ ($ε$-SFSO)
  solution, in which the constraint violation is deterministically bounded by $ε$,
  and the expected optimality gap is at most $ε$. While a recently proposed stochastic
  variance-reduced first-order penalty method can compute an $ε$-SFSO solution, there
  remains a significant gap between its first-order oracle complexity for computing
  an $ε$-SFSO solution and that for computing an $ε$-$expected\ feasible\ stochastic\
  optimal$ solution, where both the expected constraint violation and the expected
  optimality gap are bounded by $ε$. To narrow this gap, we propose an inexact stochastic
  variance-reduced gradient (SVRG) method that significantly improves the previously
  best-known first-order oracle complexity for computing an $ε$-SFSO solution. Furthermore,
  when the objective consists of a single function, the proposed method reduces to
  a novel deterministic first-order method for solving standard convex conic optimization.
  It achieves a significantly lower gradient evaluation complexity with respect to
  the objective function compared to existing methods, and can outperform them when
  computing constraint gradients and projections onto the associated cone is cheaper
  than evaluating the objective gradient. Preliminary numerical results are presented
  to illustrate the performance of the proposed method.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.23221'
  categories:
  - math.OC
  - cs.LG
---

# An inexact stochastic variance-reduced gradient method for constrained convex finite-sum optimization

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.23221
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Zhaosong Lu, Yifeng Xiao
- **Published:** 2026-11-17

## Summary
In this paper, we study a class of constrained convex finite-sum optimization problems. In many practical applications, all or some of the constraints are hard constraints that represent imperative requirements. Consequently, any desirable approximate solution must (nearly) satisfy these constraints. Motivated by this, we focus on computing an $ε$-$surely\ feasible\ stochastic\ optimal$ ($ε$-SFSO) solution, in which the constraint violation is deterministically bounded by $ε$, and the expected optimality gap is at most $ε$. While a recently proposed stochastic variance-reduced first-order penalty method can compute an $ε$-SFSO solution, there remains a significant gap between its first-order oracle complexity for computing an $ε$-SFSO solution and that for computing an $ε$-$expected\ feasible\ stochastic\ optimal$ solution, where both the expected constraint violation and the expected optimality gap are bounded by $ε$. To narrow this gap, we propose an inexact stochastic variance-reduced gradient (SVRG) method that significantly improves the previously best-known first-order oracle complexity for computing an $ε$-SFSO solution. Furthermore, when the objective consists of a single function, the proposed method reduces to a novel deterministic first-order method for solving standard convex conic optimization. It achieves a significantly lower gradient evaluation complexity with respect to the objective function compared to existing methods, and can outperform them when computing constraint gradients and projections onto the associated cone is cheaper than evaluating the objective gradient. Preliminary numerical results are presented to illustrate the performance of the proposed method.

## Provider details
- **Arxiv Id:** 2611.23221
- **Categories:** ["math.OC", "cs.LG"]
