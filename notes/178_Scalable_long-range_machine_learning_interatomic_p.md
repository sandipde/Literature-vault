---
title: Scalable long-range machine learning interatomic potentials with electrical
  response for atomistic material modeling
type: arxiv
source: https://arxiv.org/abs/2610.23643
canonical_url: https://arxiv.org/abs/2610.23643
captured_by: sandipde
date: '2026-11-19'
captured_at: '2026-11-19T13:40:52+00:00'
last_requested: '2026-11-19T13:40:52+00:00'
issue: '178'
status: to-read
authors:
- Yicheng Chen
- Xiaoyun Yu
- Hyejeong Song
- Xintian Wang
- Zihui Li
- Zixi Xia
- Junmin Chen
- Peichen Zhong
published: '2026-10-16'
abstract: Accurate atomistic simulations of materials under electric fields require
  long-range electrostatics and electrical-response modeling at length scales beyond
  the reach of conventional first-principles methods. Yet these capabilities remain
  difficult to reconcile with the scalability of machine-learning interatomic potentials
  (MLIPs). Strictly local models enable efficient spatial parallelization but neglect
  long-range interactions, whereas existing electrostatic extensions introduce global
  dependencies that hinder distributed computation. Here, we overcome this limitation
  by analytically separating the long-range electrostatic forces and Born effective
  charges (BECs) into a global electrostatics calculation and strictly local derivatives
  of learned latent charges. This formulation preserves the spatial decomposability
  of equivariant MLIPs while enabling distributed evaluation of energies, forces,
  stresses, and BECs across different boundary conditions. Implemented as DPA4C-LR
  on the \texttt{nvalchemi} platform, the framework scales to 5.2 million atoms on
  four GPUs at approximately twice the computational cost of its short-range backbone.
  Trained on energies and forces, DPA4C-LR accurately infers BECs and reproduces the
  field-dependent infrared spectra of water. We further demonstrate its capabilities
  by recovering the characteristic slim polarization hysteresis of relaxor \ce{Pb(Mg_{1/3}Nb_{2/3})O3},
  which is obscured by finite-size effects in smaller simulations; predicting a room-temperature
  field-driven ionic conductivity of $6.8 \pm 0.7$~mS/cm in amorphous \ce{Li_{0.9}NbO_{0.9}Cl_{4.1}};
  and modeling interfacial thermal transport across Si/diamond interfaces with slab-corrected
  electrostatics. By combining long-range physics, electrical-response inference,
  and distributed computation, this framework extends predictive atomistic modeling
  toward device-relevant length scales.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.23643'
  categories:
  - cond-mat.mtrl-sci
  - cs.LG
  primary_category: cond-mat.mtrl-sci
  updated: '2026-10-16T15:44:07Z'
  doi: ''
---

# Scalable long-range machine learning interatomic potentials with electrical response for atomistic material modeling

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.23643
- **Captured by:** @sandipde
- **Metadata:** complete (arXiv)
- **Authors:** Yicheng Chen, Xiaoyun Yu, Hyejeong Song, Xintian Wang, Zihui Li, Zixi Xia, Junmin Chen, Peichen Zhong
- **Published:** 2026-10-16

## Summary
Accurate atomistic simulations of materials under electric fields require long-range electrostatics and electrical-response modeling at length scales beyond the reach of conventional first-principles methods. Yet these capabilities remain difficult to reconcile with the scalability of machine-learning interatomic potentials (MLIPs). Strictly local models enable efficient spatial parallelization but neglect long-range interactions, whereas existing electrostatic extensions introduce global dependencies that hinder distributed computation. Here, we overcome this limitation by analytically separating the long-range electrostatic forces and Born effective charges (BECs) into a global electrostatics calculation and strictly local derivatives of learned latent charges. This formulation preserves the spatial decomposability of equivariant MLIPs while enabling distributed evaluation of energies, forces, stresses, and BECs across different boundary conditions. Implemented as DPA4C-LR on the \texttt{nvalchemi} platform, the framework scales to 5.2 million atoms on four GPUs at approximately twice the computational cost of its short-range backbone. Trained on energies and forces, DPA4C-LR accurately infers BECs and reproduces the field-dependent infrared spectra of water. We further demonstrate its capabilities by recovering the characteristic slim polarization hysteresis of relaxor \ce{Pb(Mg_{1/3}Nb_{2/3})O3}, which is obscured by finite-size effects in smaller simulations; predicting a room-temperature field-driven ionic conductivity of $6.8 \pm 0.7$~mS/cm in amorphous \ce{Li_{0.9}NbO_{0.9}Cl_{4.1}}; and modeling interfacial thermal transport across Si/diamond interfaces with slab-corrected electrostatics. By combining long-range physics, electrical-response inference, and distributed computation, this framework extends predictive atomistic modeling toward device-relevant length scales.

## Provider details
- **Arxiv Id:** 2610.23643
- **Categories:** ["cond-mat.mtrl-sci", "cs.LG"]
- **Primary Category:** cond-mat.mtrl-sci
- **Updated:** 2026-10-16T15:44:07Z
