---
title: Accelerating Equivariant Interatomic Potentials for Molecular Dynamics through
  Radial tabulation and Kernel Fusion
type: arxiv
source: https://arxiv.org/abs/2611.31865
canonical_url: https://arxiv.org/abs/2611.31865
captured_by: auto-scanner
date: '2026-11-26'
captured_at: '2026-11-26T14:39:56+00:00'
last_requested: '2026-11-26T14:39:56+00:00'
issue: scan:arxiv-mlips
status: to-read
authors:
- Jaekyun Yoo
- Suyeon Ju
published: '2026-11-24'
abstract: Equivariant machine-learned interatomic potentials (MLIPs) achieve near-quantum-chemical
  accuracy, but their computational cost and GPU memory footprint restrict molecular
  dynamics (MD) at extended length and time scales. Even when the tensor product (TP)
  is accelerated, both bottlenecks remain governed by evaluating and storing per-edge
  radial weights in the NequIP convolution. We introduce JET-MLIPs (Joint-Kernel Equivariant
  Convolution with Tabulated Radial Weights for MLIP simulation), a GPU backend applicable
  to pretrained NequIP-family potentials without retraining. JET-MLIPs replaces the
  radial multilayer perceptron (MLP) with a piecewise cubic Hermite table and fuses
  table lookup, spherical harmonics, TP and neighbor aggregation into a single kernel,
  eliminating per-edge radial-weight and MLP-intermediate storage during force evaluation.
  Across 15 released potentials from SevenNet, MACE, NequIP-OAM, Nequix and EquFlash
  on a 5632-atom liquid electrolyte, LAMMPS MD attains 1.5-5.9$\times$ step-time speed-ups
  and 2.4-24$\times$ peak memory reductions relative to each family's existing TP-accelerated
  backend on a single H200 GPU while preserving single-precision (fp32) accuracy and
  dynamical stability. These reductions enable multi-nanosecond transport-property
  simulations of roughly $10^4$-atom systems on a single GPU and broaden access to
  large-scale equivariant MLIP MD on widely available GPUs.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.31865'
  categories:
  - cond-mat.mtrl-sci
  - cs.PF
---

# Accelerating Equivariant Interatomic Potentials for Molecular Dynamics through Radial tabulation and Kernel Fusion

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.31865
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Jaekyun Yoo, Suyeon Ju
- **Published:** 2026-11-24

## Summary
Equivariant machine-learned interatomic potentials (MLIPs) achieve near-quantum-chemical accuracy, but their computational cost and GPU memory footprint restrict molecular dynamics (MD) at extended length and time scales. Even when the tensor product (TP) is accelerated, both bottlenecks remain governed by evaluating and storing per-edge radial weights in the NequIP convolution. We introduce JET-MLIPs (Joint-Kernel Equivariant Convolution with Tabulated Radial Weights for MLIP simulation), a GPU backend applicable to pretrained NequIP-family potentials without retraining. JET-MLIPs replaces the radial multilayer perceptron (MLP) with a piecewise cubic Hermite table and fuses table lookup, spherical harmonics, TP and neighbor aggregation into a single kernel, eliminating per-edge radial-weight and MLP-intermediate storage during force evaluation. Across 15 released potentials from SevenNet, MACE, NequIP-OAM, Nequix and EquFlash on a 5632-atom liquid electrolyte, LAMMPS MD attains 1.5-5.9$\times$ step-time speed-ups and 2.4-24$\times$ peak memory reductions relative to each family's existing TP-accelerated backend on a single H200 GPU while preserving single-precision (fp32) accuracy and dynamical stability. These reductions enable multi-nanosecond transport-property simulations of roughly $10^4$-atom systems on a single GPU and broaden access to large-scale equivariant MLIP MD on widely available GPUs.

## Provider details
- **Arxiv Id:** 2611.31865
- **Categories:** ["cond-mat.mtrl-sci", "cs.PF"]
