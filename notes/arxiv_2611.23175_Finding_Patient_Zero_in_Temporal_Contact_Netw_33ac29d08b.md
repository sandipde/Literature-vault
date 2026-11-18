---
title: 'Finding Patient Zero in Temporal Contact Networks: A Comparative Study'
type: arxiv
source: https://arxiv.org/abs/2611.23175
canonical_url: https://arxiv.org/abs/2611.23175
captured_by: auto-scanner
date: '2026-11-18'
captured_at: '2026-11-18T13:38:13+00:00'
last_requested: '2026-11-18T13:38:13+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Nathan Cincera Brack
- Martin Sterchi
- Lorenz Hilfiker
- Abraham Bernstein
published: '2026-11-17'
abstract: Identifying the source of an epidemic, i.e., the patient zero, in a temporal
  contact network is important for effective outbreak containment and resource allocation.
  While several methods have been proposed for this task, they have rarely been evaluated
  under comparable conditions, and no systematic comparison exists for temporal contact
  networks. We address this gap with a comparative study of seven major methods, namely
  Steiner Tree (ST), Individual-Based Approximation (IBA), Dynamic Message Passing
  (DMP), Monte Carlo Mean-Field (MCMF), Soft Margin Estimator (SME), Backtracking
  Network (BN, a graph neural network), and Belief Propagation (BP). We unify all
  methods under a single problem formulation and evaluate them on eight diverse temporal
  networks. In the main experiment, we compare source detection performance for varying
  basic reproduction numbers. Three complementary experiments on a subset of networks
  study (i) learning curves, (ii) partial observability, and (iii) parameter misspecification.
  We find that BP and BN are the strongest source detectors overall. SME is strong
  under partial observation but mediocre otherwise. IBA, DMP, and MCMF share a common
  weakness rooted in their factorized-likelihood assumption, leading to overconfident
  predictions. We identify scaling these methods to larger networks as the most pressing
  direction for future work.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.23175'
  categories:
  - cs.SI
---

# Finding Patient Zero in Temporal Contact Networks: A Comparative Study

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.23175
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Nathan Cincera Brack, Martin Sterchi, Lorenz Hilfiker, Abraham Bernstein
- **Published:** 2026-11-17

## Summary
Identifying the source of an epidemic, i.e., the patient zero, in a temporal contact network is important for effective outbreak containment and resource allocation. While several methods have been proposed for this task, they have rarely been evaluated under comparable conditions, and no systematic comparison exists for temporal contact networks. We address this gap with a comparative study of seven major methods, namely Steiner Tree (ST), Individual-Based Approximation (IBA), Dynamic Message Passing (DMP), Monte Carlo Mean-Field (MCMF), Soft Margin Estimator (SME), Backtracking Network (BN, a graph neural network), and Belief Propagation (BP). We unify all methods under a single problem formulation and evaluate them on eight diverse temporal networks. In the main experiment, we compare source detection performance for varying basic reproduction numbers. Three complementary experiments on a subset of networks study (i) learning curves, (ii) partial observability, and (iii) parameter misspecification. We find that BP and BN are the strongest source detectors overall. SME is strong under partial observation but mediocre otherwise. IBA, DMP, and MCMF share a common weakness rooted in their factorized-likelihood assumption, leading to overconfident predictions. We identify scaling these methods to larger networks as the most pressing direction for future work.

## Provider details
- **Arxiv Id:** 2611.23175
- **Categories:** ["cs.SI"]
