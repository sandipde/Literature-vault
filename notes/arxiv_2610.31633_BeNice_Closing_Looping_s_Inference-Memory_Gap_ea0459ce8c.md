---
title: BeNice! Closing Looping's Inference-Memory Gap via KV-Sharing
type: arxiv
source: https://arxiv.org/abs/2610.31633
canonical_url: https://arxiv.org/abs/2610.31633
captured_by: auto-scanner
date: '2026-10-23'
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: AI agents and retrieval
enrichment_tags: [language-model-inference, kv-sharing, looped-architectures]
captured_at: '2026-10-23T09:43:13+00:00'
last_requested: '2026-10-23T09:43:13+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Hayden Prairie
- Jacob M. Ryan
- Taylor Berg-Kirkpatrick
- Daniel Y. Fu
published: '2026-10-22'
abstract: 'Looped architectures scale quality while keeping parameter count fixed
  by repeatedly passing activations through the same block of layers. During inference,
  each recurrence generates independent KV-caches, causing memory to grow linearly.
  To address this challenge, prior work has proposed KV-sharing (i.e., sharing KV-caches
  across depth), finding that, in some cases, the KV-cache of the final recurrence
  can be shared with the earlier recurrences without quality loss, a property we denote
  as KV-shareability. However, the mechanisms underlying KV-shareability remain poorly
  understood, with even identically trained looped architectures not consistently
  exhibiting it. In this paper, we study how KV-shareability can be enabled in looped
  models. We propose a two-stage method: in the first stage, we use stochastic depth
  during pretraining, which induces contractive residual dynamics that drive representations
  toward a common limit across recurrences. In the second stage, we propose BeNice!,
  a post-training method that broadcasts the final recurrence''s KV-cache into the
  first recurrence, training it to produce compatible residuals while preserving the
  original model''s quality. As a result, BeNice! enables KV-shareability while matching
  standard finetuning''s unshared validation perplexity. Using BeNice!, we show that
  KV-sharing is complementary to alternative KV-compression methods, composing with
  memory-efficient sequence mixers (e.g., multi-latent attention, Kimi delta attention)
  and low-precision KV-cache quantization (e.g., fp8, mxfp8, nvfp4). Finally, in simulated
  low-memory, long-context inference, KV-sharing improves cache hit rates by up to
  31.4%, increases throughput by up to 23.6%, and reduces p90 time-to-first-token
  by up to 83.6%.'
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.31633'
  categories:
  - cs.LG
---

# BeNice! Closing Looping's Inference-Memory Gap via KV-Sharing

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.31633
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Hayden Prairie, Jacob M. Ryan, Taylor Berg-Kirkpatrick, Daniel Y. Fu
- **Published:** 2026-10-22

## Summary
Looped architectures scale quality while keeping parameter count fixed by repeatedly passing activations through the same block of layers. During inference, each recurrence generates independent KV-caches, causing memory to grow linearly. To address this challenge, prior work has proposed KV-sharing (i.e., sharing KV-caches across depth), finding that, in some cases, the KV-cache of the final recurrence can be shared with the earlier recurrences without quality loss, a property we denote as KV-shareability. However, the mechanisms underlying KV-shareability remain poorly understood, with even identically trained looped architectures not consistently exhibiting it. In this paper, we study how KV-shareability can be enabled in looped models. We propose a two-stage method: in the first stage, we use stochastic depth during pretraining, which induces contractive residual dynamics that drive representations toward a common limit across recurrences. In the second stage, we propose BeNice!, a post-training method that broadcasts the final recurrence's KV-cache into the first recurrence, training it to produce compatible residuals while preserving the original model's quality. As a result, BeNice! enables KV-shareability while matching standard finetuning's unshared validation perplexity. Using BeNice!, we show that KV-sharing is complementary to alternative KV-compression methods, composing with memory-efficient sequence mixers (e.g., multi-latent attention, Kimi delta attention) and low-precision KV-cache quantization (e.g., fp8, mxfp8, nvfp4). Finally, in simulated low-memory, long-context inference, KV-sharing improves cache hit rates by up to 31.4%, increases throughput by up to 23.6%, and reduces p90 time-to-first-token by up to 83.6%.

## Provider details
- **Arxiv Id:** 2610.31633
- **Categories:** ["cs.LG"]

## AI enrichment
- **Concise summary:** The preprint presents BeNice, a KV-sharing approach intended to reduce the inference-memory costs of looped language-model architectures.
- **Why it matters:** Inference memory can limit the practical benefits of parameter-efficient recurrent designs.
- **Caveat:** This is a preprint; claimed memory or quality trade-offs are not independently verified.
- **Evidence:** [Captured source](https://arxiv.org/abs/2610.31633); analysis based only on captured metadata, not independently verified full text.
