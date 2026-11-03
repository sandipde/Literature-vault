---
title: 'FACTO: fast atom-centered tensor operator for accurate and efficient foundational
  machine-learned interatomic potentials'
type: arxiv
source: https://arxiv.org/abs/2611.03276
canonical_url: https://arxiv.org/abs/2611.03276
captured_by: auto-scanner
date: '2026-11-03'
captured_at: '2026-11-03T12:34:47+00:00'
last_requested: '2026-11-03T12:34:47+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Siyuan Liu
- Chang Han
- Sheng Gong
- Yanping Yang
- Tianze Zheng
- Yu Xia
- Kuang Yu
- Shenzhen Xu
- Wen Yan
published: '2026-11-02'
abstract: High-throughput inference remains a central challenge for equivariant machine-learned
  interatomic potentials. Here we introduce FACTO, an atom-centered equivariant architecture
  that confines evolving learned state and dense channel mixing to atoms, expressing
  neighbor interactions as fully fusible reductions. We complement this design with
  custom register-accumulated aggregation kernels and tensor-core FP32 emulation,
  accelerating inference while retaining FP32-level energy conservation under emulated
  arithmetic in molecular dynamics. Comprehensive evaluations on Matbench Discovery,
  MLIP Arena and MatCalc demonstrate high throughput alongside strong predictive accuracy
  and physical reliability. On Matbench Discovery, the four FACTO-OAM variants show
  top-tier performance by overall rank sum among 46 models with complete scores, advancing
  the accuracy-throughput Pareto frontier. On MLIP Arena, FACTO achieves state- of-the-art
  stability under extreme heating and compression, alongside high fidelity in hydrogen
  combustion. On MatCalc, FACTO outperforms the compared baselines in structural and
  elastic predictions while retaining competitive accuracy for energetic and thermal
  properties.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.03276'
  categories:
  - physics.chem-ph
---

# FACTO: fast atom-centered tensor operator for accurate and efficient foundational machine-learned interatomic potentials

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.03276
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Siyuan Liu, Chang Han, Sheng Gong, Yanping Yang, Tianze Zheng, Yu Xia, Kuang Yu, Shenzhen Xu, Wen Yan
- **Published:** 2026-11-02

## Summary
High-throughput inference remains a central challenge for equivariant machine-learned interatomic potentials. Here we introduce FACTO, an atom-centered equivariant architecture that confines evolving learned state and dense channel mixing to atoms, expressing neighbor interactions as fully fusible reductions. We complement this design with custom register-accumulated aggregation kernels and tensor-core FP32 emulation, accelerating inference while retaining FP32-level energy conservation under emulated arithmetic in molecular dynamics. Comprehensive evaluations on Matbench Discovery, MLIP Arena and MatCalc demonstrate high throughput alongside strong predictive accuracy and physical reliability. On Matbench Discovery, the four FACTO-OAM variants show top-tier performance by overall rank sum among 46 models with complete scores, advancing the accuracy-throughput Pareto frontier. On MLIP Arena, FACTO achieves state- of-the-art stability under extreme heating and compression, alongside high fidelity in hydrogen combustion. On MatCalc, FACTO outperforms the compared baselines in structural and elastic predictions while retaining competitive accuracy for energetic and thermal properties.

## Provider details
- **Arxiv Id:** 2611.03276
- **Categories:** ["physics.chem-ph"]
