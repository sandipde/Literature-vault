---
title: 'Perfumer: A Large Language Model-based Agentic Framework Accelerating Structural
  Relaxation and Electronic Band Prediction for First-Principle Calculation'
type: arxiv
source: https://arxiv.org/abs/2611.26349
canonical_url: https://arxiv.org/abs/2611.26349
captured_by: auto-scanner
date: '2026-11-20'
captured_at: '2026-11-20T22:56:01+00:00'
last_requested: '2026-11-20T22:56:01+00:00'
issue: scan:arxiv-ml-atomistic
status: to-read
authors:
- Zhiwei Li
- Yuhao Zhou
- Yikai Yang
- Haonan Wang
- Qing Ye
- Jiancheng Lv
- Kazunari Matsuda
published: '2026-11-19'
abstract: First-principles structural relaxation and band calculations require substantial
  computation and expertise. Here we present Perfumer, a large language model-based
  agentic framework that couples Quantum ESPRESSO with two predictive models. Across
  tested structures, pre-relaxation with Perfumer-relax model followed by QE refinement
  yielded a 2.75-fold overall speedup over QE alone. Perfumer-band model combines
  a periodic graph neural network with a latent Hermitian spectral head returns 12
  band energies at any requested wavevector, preserving reciprocal lattice periodicity
  and time-reversal symmetry without constructing Hamiltonian. Trained on 125,153
  self-curated band structures, Perfumer-band model reaches a median per-material
  mean absolute error of 0.157 eV on 2,607 test materials, including lanthanide, actinide
  and magnetic compounds, from held-out composition families spanning 85 elements,
  taking about 97 ms per material on two consumer CPU cores. The agent turns natural-language
  requests into relaxation-to-band workflows, from a single uploaded structure to
  automatically constructed new candidates and returns predicted properties.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.26349'
  categories:
  - cond-mat.mtrl-sci
  - cs.LG
---

# Perfumer: A Large Language Model-based Agentic Framework Accelerating Structural Relaxation and Electronic Band Prediction for First-Principle Calculation

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.26349
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Zhiwei Li, Yuhao Zhou, Yikai Yang, Haonan Wang, Qing Ye, Jiancheng Lv, Kazunari Matsuda
- **Published:** 2026-11-19

## Summary
First-principles structural relaxation and band calculations require substantial computation and expertise. Here we present Perfumer, a large language model-based agentic framework that couples Quantum ESPRESSO with two predictive models. Across tested structures, pre-relaxation with Perfumer-relax model followed by QE refinement yielded a 2.75-fold overall speedup over QE alone. Perfumer-band model combines a periodic graph neural network with a latent Hermitian spectral head returns 12 band energies at any requested wavevector, preserving reciprocal lattice periodicity and time-reversal symmetry without constructing Hamiltonian. Trained on 125,153 self-curated band structures, Perfumer-band model reaches a median per-material mean absolute error of 0.157 eV on 2,607 test materials, including lanthanide, actinide and magnetic compounds, from held-out composition families spanning 85 elements, taking about 97 ms per material on two consumer CPU cores. The agent turns natural-language requests into relaxation-to-band workflows, from a single uploaded structure to automatically constructed new candidates and returns predicted properties.

## Provider details
- **Arxiv Id:** 2611.26349
- **Categories:** ["cond-mat.mtrl-sci", "cs.LG"]
