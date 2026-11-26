---
title: 'Phono3GPU: GPU-Accelerated Linear Tetrahedron Integration for Phonon Thermal
  Transport'
type: arxiv
source: https://arxiv.org/abs/2611.33912
canonical_url: https://arxiv.org/abs/2611.33912
captured_by: auto-scanner
date: '2026-11-26'
captured_at: '2026-11-26T14:39:56+00:00'
last_requested: '2026-11-26T14:39:56+00:00'
issue: scan:arxiv-mlips
status: to-read
authors:
- Jinhyeong Jo
- Sungwoo Kang
- Byungju Lee
- Jung-Hoon Lee
- Seugchul Kim
published: '2026-11-25'
abstract: Materials with high or low thermal conductivity are increasingly important
  for thermal management and energy technologies. Machine-learned interatomic potentials
  have accelerated anharmonic force-constant calculations, shifting the bottleneck
  toward phonon transport calculations for large materials datasets. Existing GPU
  solvers often rely on smearing, whose width can require material-dependent choices,
  while the linear tetrahedron method used in phono3py avoids this parameter but becomes
  costly for complex structures. Here we introduce Phono3GPU, which reformulates three-phonon
  scattering and linear tetrahedron integration for massively parallel GPU execution.
  Across benchmark crystals, Phono3GPU accelerates total calculations by up to 41
  times relative to a CPU implementation, with larger gains for complex unit cells,
  and by 2 to 6 times relative to a recent GPU plug-in for phono3py. We further demonstrate
  atom-resolved scattering analysis in defective silicon supercells as an application
  enabled by the reduced computational cost. Phono3GPU thus lowers the cost of tetrahedron-based
  thermal-conductivity calculations and of detailed investigations of structure-dependent
  phonon transport.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.33912'
  categories:
  - cond-mat.mtrl-sci
---

# Phono3GPU: GPU-Accelerated Linear Tetrahedron Integration for Phonon Thermal Transport

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.33912
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Jinhyeong Jo, Sungwoo Kang, Byungju Lee, Jung-Hoon Lee, Seugchul Kim
- **Published:** 2026-11-25

## Summary
Materials with high or low thermal conductivity are increasingly important for thermal management and energy technologies. Machine-learned interatomic potentials have accelerated anharmonic force-constant calculations, shifting the bottleneck toward phonon transport calculations for large materials datasets. Existing GPU solvers often rely on smearing, whose width can require material-dependent choices, while the linear tetrahedron method used in phono3py avoids this parameter but becomes costly for complex structures. Here we introduce Phono3GPU, which reformulates three-phonon scattering and linear tetrahedron integration for massively parallel GPU execution. Across benchmark crystals, Phono3GPU accelerates total calculations by up to 41 times relative to a CPU implementation, with larger gains for complex unit cells, and by 2 to 6 times relative to a recent GPU plug-in for phono3py. We further demonstrate atom-resolved scattering analysis in defective silicon supercells as an application enabled by the reduced computational cost. Phono3GPU thus lowers the cost of tetrahedron-based thermal-conductivity calculations and of detailed investigations of structure-dependent phonon transport.

## Provider details
- **Arxiv Id:** 2611.33912
- **Categories:** ["cond-mat.mtrl-sci"]
