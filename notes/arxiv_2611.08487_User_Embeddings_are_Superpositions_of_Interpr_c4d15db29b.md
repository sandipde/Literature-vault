---
title: User Embeddings are Superpositions of Interpretable Behavioral Modes
type: arxiv
source: https://arxiv.org/abs/2611.08487
canonical_url: https://arxiv.org/abs/2611.08487
captured_by: auto-scanner
date: '2026-11-06'
captured_at: '2026-11-06T12:40:38+00:00'
last_requested: '2026-11-06T12:40:38+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Jonathan Kozaczuk
- Zheng Dong
- Noyan Evirgen
- Keivan Majidi
- Eddie K. H. Ng
- Chris Porter
- Qi Zhao
- Jia Geng
- Changmao Li
- Brandon R. Feng
published: '2026-11-05'
abstract: User embeddings are central components of modern recommendation, personalization,
  and behavioral modeling systems. Though these embeddings can compactly encode rich
  behavioral information, they are inherently dense and opaque, limiting interpretability.
  To address this gap, we argue that user embeddings can be understood as sparse superpositions
  of interpretable behavioral modes. This structure is directly predicted by generative
  models of user behavior for linear embeddings and extends approximately to deep-learning
  representations by the superposition hypothesis. Superimposed modes can naturally
  be recovered by sparse dictionary learning methods, such as sparse autoencoders
  (SAEs), and recovered modes can be automatically named and queried in natural language.
  We validate mode recovery against known ground truth on synthetic data, where SAEs
  recover modes better than classical sparse baselines, including on transformer-encoded
  embeddings. We then apply the method to classical and transformer-based user embeddings
  from two real-world datasets. We also show how the corresponding natural-language
  labels enable zero-shot audience retrieval and characterization over embeddings
  never trained on text. The framework is post-hoc and model-agnostic, requiring no
  modification to the upstream embedding system.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.08487'
  categories:
  - cs.LG
---

# User Embeddings are Superpositions of Interpretable Behavioral Modes

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.08487
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Jonathan Kozaczuk, Zheng Dong, Noyan Evirgen, Keivan Majidi, Eddie K. H. Ng, Chris Porter, Qi Zhao, Jia Geng, Changmao Li, Brandon R. Feng
- **Published:** 2026-11-05

## Summary
User embeddings are central components of modern recommendation, personalization, and behavioral modeling systems. Though these embeddings can compactly encode rich behavioral information, they are inherently dense and opaque, limiting interpretability. To address this gap, we argue that user embeddings can be understood as sparse superpositions of interpretable behavioral modes. This structure is directly predicted by generative models of user behavior for linear embeddings and extends approximately to deep-learning representations by the superposition hypothesis. Superimposed modes can naturally be recovered by sparse dictionary learning methods, such as sparse autoencoders (SAEs), and recovered modes can be automatically named and queried in natural language. We validate mode recovery against known ground truth on synthetic data, where SAEs recover modes better than classical sparse baselines, including on transformer-encoded embeddings. We then apply the method to classical and transformer-based user embeddings from two real-world datasets. We also show how the corresponding natural-language labels enable zero-shot audience retrieval and characterization over embeddings never trained on text. The framework is post-hoc and model-agnostic, requiring no modification to the upstream embedding system.

## Provider details
- **Arxiv Id:** 2611.08487
- **Categories:** ["cs.LG"]
