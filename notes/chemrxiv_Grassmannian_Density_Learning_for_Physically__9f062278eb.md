---
title: Grassmannian Density Learning for Physically Consistent Kohn–Sham Electronic
  Structure Prediction
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010691/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15010691/v1
captured_by: auto-scanner
date: '2026-10-20'
captured_at: '2026-10-20T09:46:32+00:00'
last_requested: '2026-10-20T09:46:32+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Yifei Wang
- Pei Liu
- Yuheng He
- Jingwen Fu
- Yongqiang Ma
- Miao Kang
- Jianji Wang
- He Zhang
- Chang Liu
- Nanning Zheng
published: '2026-10-20'
abstract: Deep-learning electronic-structure models show great potential to accelerate
  first-principles calculations, with broad implications for materials science, biology
  and drug discovery. Yet no consensus has emerged on which physical quantity should
  be modeled to represent electronic states. As two fundamental quantities that arise
  naturally in Kohn–Sham density functional theory, the Kohn–Sham Hamiltonian and
  electronic density have attracted the most attention. Hamiltonian prediction, however,
  devotes substantial modeling capacity to degrees of freedom that do not affect the
  occupied electronic subspace, whereas direct regression of density matrices or real-space
  densities removes this redundancy but cannot ensure that the prediction represents
  a physically admissible electronic state. Motivated by the fact that electronic
  states themselves reside on a constrained manifold, we observe that predicting coordinates
  directly on this manifold can simultaneously eliminate redundant degrees of freedom
  and preserve physical admissibility. Here we introduce GeoK, a framework that predicts
  compact occupied–virtual orbital-rotation generators as coordinates on the manifold
  of electronic states, thereby ensuring each prediction corresponds to a valid electronic
  state of the target molecular system. We further develop a neural-network architecture
  tailored to this geometric prediction task. Across in-distribution and out-of-distribution
  benchmarks, as well as downstream applications, GeoK consistently improves electronic-state
  prediction over the evaluated Hamiltonian and unconstrained densityregression baselines,
  while supporting robust deployment in downstream first-principles workflows. These
  results establish orbital-rotation generator prediction as a principled and reliable
  paradigm for intrinsic electronic-state modeling, opening a route towards more accurate
  and transferable deep-learning electronic-structure models.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010691/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Grassmannian Density Learning for Physically Consistent Kohn–Sham Electronic Structure Prediction

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010691/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Yifei Wang, Pei Liu, Yuheng He, Jingwen Fu, Yongqiang Ma, Miao Kang, Jianji Wang, He Zhang, Chang Liu, Nanning Zheng
- **Published:** 2026-10-20

## Summary
Deep-learning electronic-structure models show great potential to accelerate first-principles calculations, with broad implications for materials science, biology and drug discovery. Yet no consensus has emerged on which physical quantity should be modeled to represent electronic states. As two fundamental quantities that arise naturally in Kohn–Sham density functional theory, the Kohn–Sham Hamiltonian and electronic density have attracted the most attention. Hamiltonian prediction, however, devotes substantial modeling capacity to degrees of freedom that do not affect the occupied electronic subspace, whereas direct regression of density matrices or real-space densities removes this redundancy but cannot ensure that the prediction represents a physically admissible electronic state. Motivated by the fact that electronic states themselves reside on a constrained manifold, we observe that predicting coordinates directly on this manifold can simultaneously eliminate redundant degrees of freedom and preserve physical admissibility. Here we introduce GeoK, a framework that predicts compact occupied–virtual orbital-rotation generators as coordinates on the manifold of electronic states, thereby ensuring each prediction corresponds to a valid electronic state of the target molecular system. We further develop a neural-network architecture tailored to this geometric prediction task. Across in-distribution and out-of-distribution benchmarks, as well as downstream applications, GeoK consistently improves electronic-state prediction over the evaluated Hamiltonian and unconstrained densityregression baselines, while supporting robust deployment in downstream first-principles workflows. These results establish orbital-rotation generator prediction as a principled and reliable paradigm for intrinsic electronic-state modeling, opening a route towards more accurate and transferable deep-learning electronic-structure models.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010691/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
