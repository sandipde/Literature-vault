---
title: 'LunaTP: Enabling Efficient and Scalable Tensor Product for Equivariant MLIPs'
type: arxiv
source: https://arxiv.org/abs/2610.18393
canonical_url: https://arxiv.org/abs/2610.18393
captured_by: auto-scanner
date: '2026-10-14'
captured_at: '2026-10-14T09:53:53+00:00'
last_requested: '2026-10-14T09:53:53+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Yuanchang Zhou
- Mingzhen Li
- Chen Wang
- Xiangyu Zhang
- Guangming Tan
- Weile Jia
published: '2026-10-13'
abstract: Equivariant machine learning interatomic potentials (MLIPs) promise atomistic
  simulations with accuracy approaching that of quantum-mechanical calculations. However,
  the high computational cost of their core Clebsch--Gordan tensor product (CGTP)
  convolutions severely limits model scalability and efficiency. In this paper, we
  rethink the parallel execution of CGTP convolutions and introduce LunaTP. Built
  on node-centric execution, LunaTP exploits path-group parallelism and multi-level
  reuse to accelerate CGTP convolutions and higher-order derivative computation while
  preserving the underlying mathematical formulation. On an NVIDIA H100 GPU, LunaTP
  achieves kernel speedups of up to 250.0$\times$ over e3nn and 17.1$\times$ over
  OpenEquivariance. It also delivers end-to-end training throughput gains of up to
  28.7$\times$ over e3nn and 3.11$\times$ over OpenEquivariance. Finally, LunaTP demonstrates
  scalability and robust performance across models, workload scales, and GPUs, delivering
  substantial acceleration for training and atomistic simulation with high-accuracy
  equivariant MLIPs.
metadata_provider: arXiv
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: ML interatomic potentials
enrichment_tags: [tensor-products, gpu-kernels, equivariant-networks]
provider_data:
  arxiv_id: '2610.18393'
  categories:
  - cs.DC
  - cs.LG
---

# LunaTP: Enabling Efficient and Scalable Tensor Product for Equivariant MLIPs

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.18393
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Yuanchang Zhou, Mingzhen Li, Chen Wang, Xiangyu Zhang, Guangming Tan, Weile Jia
- **Published:** 2026-10-13

## Summary
Equivariant machine learning interatomic potentials (MLIPs) promise atomistic simulations with accuracy approaching that of quantum-mechanical calculations. However, the high computational cost of their core Clebsch--Gordan tensor product (CGTP) convolutions severely limits model scalability and efficiency. In this paper, we rethink the parallel execution of CGTP convolutions and introduce LunaTP. Built on node-centric execution, LunaTP exploits path-group parallelism and multi-level reuse to accelerate CGTP convolutions and higher-order derivative computation while preserving the underlying mathematical formulation. On an NVIDIA H100 GPU, LunaTP achieves kernel speedups of up to 250.0$\times$ over e3nn and 17.1$\times$ over OpenEquivariance. It also delivers end-to-end training throughput gains of up to 28.7$\times$ over e3nn and 3.11$\times$ over OpenEquivariance. Finally, LunaTP demonstrates scalability and robust performance across models, workload scales, and GPUs, delivering substantial acceleration for training and atomistic simulation with high-accuracy equivariant MLIPs.

## Provider details
- **Arxiv Id:** 2610.18393
- **Categories:** ["cs.DC", "cs.LG"]

## AI enrichment

- **Concise summary:** LunaTP reorganizes Clebsch-Gordan tensor-product execution using node-centric parallelism and reuse, including higher-order derivatives. The abstract reports large kernel and smaller end-to-end training gains on an H100.
- **Why it matters:** Accelerating the equivariant primitive without changing its mathematics could reduce a shared computational bottleneck across MLIP architectures.
- **Caveat:** Preprint speedups are workload- and baseline-dependent; peak kernel gains should not be read as universal simulation speedups.
- **Evidence:** [Captured source](https://arxiv.org/abs/2610.18393); analysis based only on captured metadata, not independently verified full text.
