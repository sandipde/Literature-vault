---
title: 'SCO-Hyper-Meta-Double-GroupNN: A Double-Group SU(2) Hyper-/Meta-Graph Neural
  Network for Cooperative Spin-Crossover Potential Energy Surfaces'
type: arxiv
source: https://arxiv.org/abs/2611.34547
canonical_url: https://arxiv.org/abs/2611.34547
captured_by: auto-scanner
date: '2026-11-26'
captured_at: '2026-11-26T14:39:56+00:00'
last_requested: '2026-11-26T14:39:56+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Rong Fu
- Tianhao Su
- Shunbo Hu
- Musen Li
published: '2026-11-25'
abstract: Learning potential energy surfaces for magnetic materials requires resolving
  coupled local spin manifolds and geometric frustration. We introduce SCO-Hyper-Meta-Double-GroupNN,
  a geometry-only architecture combining a pretrained O(3)-equivariant backbone with
  SU(2) spinor Hamiltonians and cooperative hyper-/meta-graph interactions. Analytic
  thermal spinor density matrices provide non-polynomial two- and three-body structural
  invariants, while frustrated-triangle hyperedges and a multi-shell sideway gate
  couple geometric representations to local spin manifolds. A variationally consistent,
  doubly-centered zero-gauge free-energy functional couples multiplet occupations
  and signed spin orientations, yielding conservative autograd forces without spin
  inputs at inference. On a first-principles Co-Cr-Ni benchmark comprising 346 training
  and 59 held-out validation supercells across crystalline, amorphous, glassy, and
  liquid regimes, compact models with 56k-77k parameters outperform a 207k-parameter
  spin-conditioned magnetic MACE baseline. Energy MAE decreases by 37-44%, reaching
  3.82 versus 6.83 meV/atom, and force MAE decreases by 10.8-14.2 meV/Angstrom, reaching
  165.8-169.2 versus 180.0 meV/Angstrom. The models preserve Kramers degeneracy to
  within $6\times10^{-15}$ eV, predict equilibrium local magnetic moments from geometry
  alone with an absolute-moment MAE of $0.181\,μ_B$, and support stable molecular
  dynamics up to 2,200 K. This framework integrates local spinor symmetry and cooperative
  magnetic interactions into geometry-only interatomic potentials.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.34547'
  categories:
  - cs.CE
  - cond-mat.dis-nn
  - physics.comp-ph
---

# SCO-Hyper-Meta-Double-GroupNN: A Double-Group SU(2) Hyper-/Meta-Graph Neural Network for Cooperative Spin-Crossover Potential Energy Surfaces

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.34547
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Rong Fu, Tianhao Su, Shunbo Hu, Musen Li
- **Published:** 2026-11-25

## Summary
Learning potential energy surfaces for magnetic materials requires resolving coupled local spin manifolds and geometric frustration. We introduce SCO-Hyper-Meta-Double-GroupNN, a geometry-only architecture combining a pretrained O(3)-equivariant backbone with SU(2) spinor Hamiltonians and cooperative hyper-/meta-graph interactions. Analytic thermal spinor density matrices provide non-polynomial two- and three-body structural invariants, while frustrated-triangle hyperedges and a multi-shell sideway gate couple geometric representations to local spin manifolds. A variationally consistent, doubly-centered zero-gauge free-energy functional couples multiplet occupations and signed spin orientations, yielding conservative autograd forces without spin inputs at inference. On a first-principles Co-Cr-Ni benchmark comprising 346 training and 59 held-out validation supercells across crystalline, amorphous, glassy, and liquid regimes, compact models with 56k-77k parameters outperform a 207k-parameter spin-conditioned magnetic MACE baseline. Energy MAE decreases by 37-44%, reaching 3.82 versus 6.83 meV/atom, and force MAE decreases by 10.8-14.2 meV/Angstrom, reaching 165.8-169.2 versus 180.0 meV/Angstrom. The models preserve Kramers degeneracy to within $6\times10^{-15}$ eV, predict equilibrium local magnetic moments from geometry alone with an absolute-moment MAE of $0.181\,μ_B$, and support stable molecular dynamics up to 2,200 K. This framework integrates local spinor symmetry and cooperative magnetic interactions into geometry-only interatomic potentials.

## Provider details
- **Arxiv Id:** 2611.34547
- **Categories:** ["cs.CE", "cond-mat.dis-nn", "physics.comp-ph"]
