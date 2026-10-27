---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: ML interatomic potentials
enrichment_tags: [equivariant-models, low-precision, gpu-acceleration]
title: Accelerating SO(2)-Equivariant Materials Models through Low-Precision Emulation
type: arxiv
source: https://arxiv.org/abs/2610.35164
canonical_url: https://arxiv.org/abs/2610.35164
captured_by: auto-scanner
date: '2026-10-27'
captured_at: '2026-10-27T10:10:23+00:00'
last_requested: '2026-10-27T10:10:23+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Denghui Lu
- Alexander Maeder
- Alexandros Nikolaos Ziogas
- Mathieu Luisier
- Manasa Kaniselvan
published: '2026-10-26'
abstract: Rotationally equivariant architectures improve the physical fidelity of
  machine-learned (ML) universal materials models based on graph neural networks (GNNs).
  However, their scalability is limited by the use of non-trivial, high-precision
  tensor operations during both training and inference. Adopting the reduced-precision
  formats of matrix multiplication units (MMUs), e.g., FP8 instead of FP32, provides
  massive increases in throughput, up to 30x (60x) on NVIDIA Hopper (Blackwell) GPUs,
  but may lead to drastic loss of accuracy. Here, we introduce tailored 'emulated'
  low-precision operations under the integer Ozaki scheme to accelerate the 'SO(2)-equivariant'
  processing layers of GNNs, which dominate the runtime of (1) many state-of-the-art
  ML interatomic potentials (MLIPs) and (2) most universal ML Hamiltonian (MLH) models.
  Our framework, FlashSO(2), outperforms TF32, the most accurate native low-precision
  MMU format, in throughput, accuracy, and memory footprint at once. At the SO(2)
  layer level, it reaches 40x (7x) the throughput of MALOQ's (UMA's) reference implementation,
  an MLH (MLIP) model, sustaining up to 236 (232) effective Tflop/s on an NVIDIA GH200,
  3.5x the FP32 peak. At the model level, FlashSO(2) helps train MALOQ 3.9x faster
  than its pure-FP32 version while reducing peak memory by 58% at no loss in accuracy.
  In molecular dynamics simulations with UMA, the speedup factor is 3.3x, and the
  peak memory is reduced by 51%. FlashSO(2) thus pushes the speed-accuracy Pareto
  frontier of equivariant materials models beyond the native low-precision formats
  and substantially lowers the resources required to exploit their scaling laws.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.35164'
  categories:
  - cs.LG
  - cs.DC
---

# Accelerating SO(2)-Equivariant Materials Models through Low-Precision Emulation

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.35164
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Denghui Lu, Alexander Maeder, Alexandros Nikolaos Ziogas, Mathieu Luisier, Manasa Kaniselvan
- **Published:** 2026-10-26

## Summary
Rotationally equivariant architectures improve the physical fidelity of machine-learned (ML) universal materials models based on graph neural networks (GNNs). However, their scalability is limited by the use of non-trivial, high-precision tensor operations during both training and inference. Adopting the reduced-precision formats of matrix multiplication units (MMUs), e.g., FP8 instead of FP32, provides massive increases in throughput, up to 30x (60x) on NVIDIA Hopper (Blackwell) GPUs, but may lead to drastic loss of accuracy. Here, we introduce tailored 'emulated' low-precision operations under the integer Ozaki scheme to accelerate the 'SO(2)-equivariant' processing layers of GNNs, which dominate the runtime of (1) many state-of-the-art ML interatomic potentials (MLIPs) and (2) most universal ML Hamiltonian (MLH) models. Our framework, FlashSO(2), outperforms TF32, the most accurate native low-precision MMU format, in throughput, accuracy, and memory footprint at once. At the SO(2) layer level, it reaches 40x (7x) the throughput of MALOQ's (UMA's) reference implementation, an MLH (MLIP) model, sustaining up to 236 (232) effective Tflop/s on an NVIDIA GH200, 3.5x the FP32 peak. At the model level, FlashSO(2) helps train MALOQ 3.9x faster than its pure-FP32 version while reducing peak memory by 58% at no loss in accuracy. In molecular dynamics simulations with UMA, the speedup factor is 3.3x, and the peak memory is reduced by 51%. FlashSO(2) thus pushes the speed-accuracy Pareto frontier of equivariant materials models beyond the native low-precision formats and substantially lowers the resources required to exploit their scaling laws.

## Provider details
- **Arxiv Id:** 2610.35164
- **Categories:** ["cs.LG", "cs.DC"]

## AI enrichment

- **Concise summary:** FlashSO(2) uses emulated low-precision operations to accelerate equivariant layers in materials models while reporting preserved accuracy and lower memory use.
- **Why it matters:** Optimizing symmetry-aware operations could reduce the practical cost of both potential inference and Hamiltonian-model training.
- **Caveat:** Preprint benchmark claims are model- and hardware-specific; layer throughput is not interchangeable with end-to-end speedup.
- **Evidence:** [Captured source](https://arxiv.org/abs/2610.35164); analysis based only on captured metadata, not independently verified full text.
