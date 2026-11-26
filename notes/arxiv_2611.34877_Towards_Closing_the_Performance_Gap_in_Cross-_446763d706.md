---
title: Towards Closing the Performance Gap in Cross-Modal Place Recognition
type: arxiv
source: https://arxiv.org/abs/2611.34877
canonical_url: https://arxiv.org/abs/2611.34877
captured_by: auto-scanner
date: '2026-11-26'
captured_at: '2026-11-26T14:39:56+00:00'
last_requested: '2026-11-26T14:39:56+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Ofer Idan
- Dan Badur
- Yoli Shavit
published: '2026-11-25'
abstract: Cross-modal place recognition (CMPR) matches natural language descriptions
  against databases of geo-tagged reference images, enabling localization without
  visual queries. Despite its potential for language-guided navigation, existing vision-language
  models lag far behind visual place recognition (VPR) baselines, even after task
  adaptation. Unlike general-purpose text-to-image retrieval, place recognition relies
  on subtle local cues to distinguish visually similar locations. We therefore hypothesize
  that a primary bottleneck in CMPR is capturing fine-grained correspondences between
  image regions and text details, which requires higher visual token granularity,
  strong text representation capacity, and local cross-modal matching. To address
  this challenge, we propose CrossPlace, a two-stage CMPR framework. Stage 1 performs
  global retrieval by pairing a jointly aligned DINOv2-B/14 visual backbone with a
  progressively fine-tuned BGE-Large text encoder, while Stage 2 refines top candidates
  using a lightweight token-level cross-attention reranker. Through systematic analysis,
  we isolate the drivers of retrieval accuracy and show that visual token density
  provides the largest performance improvement, while text encoder capacity and task
  fine-tuning offer complementary gains. To evaluate robustness under realistic conditions,
  we also extend CMPR evaluation to city-scale and severe weather and illumination
  settings. Across all existing and new benchmarks, CrossPlace achieves double-digit
  Recall@1 improvements over prior cross-modal methods, closes the gap to unimodal
  text retrieval, and narrows it to unimodal VPR. Code and benchmarks are available
  at https://github.com/oferidan1/CrossPlace
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.34877'
  categories:
  - cs.CV
---

# Towards Closing the Performance Gap in Cross-Modal Place Recognition

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.34877
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Ofer Idan, Dan Badur, Yoli Shavit
- **Published:** 2026-11-25

## Summary
Cross-modal place recognition (CMPR) matches natural language descriptions against databases of geo-tagged reference images, enabling localization without visual queries. Despite its potential for language-guided navigation, existing vision-language models lag far behind visual place recognition (VPR) baselines, even after task adaptation. Unlike general-purpose text-to-image retrieval, place recognition relies on subtle local cues to distinguish visually similar locations. We therefore hypothesize that a primary bottleneck in CMPR is capturing fine-grained correspondences between image regions and text details, which requires higher visual token granularity, strong text representation capacity, and local cross-modal matching. To address this challenge, we propose CrossPlace, a two-stage CMPR framework. Stage 1 performs global retrieval by pairing a jointly aligned DINOv2-B/14 visual backbone with a progressively fine-tuned BGE-Large text encoder, while Stage 2 refines top candidates using a lightweight token-level cross-attention reranker. Through systematic analysis, we isolate the drivers of retrieval accuracy and show that visual token density provides the largest performance improvement, while text encoder capacity and task fine-tuning offer complementary gains. To evaluate robustness under realistic conditions, we also extend CMPR evaluation to city-scale and severe weather and illumination settings. Across all existing and new benchmarks, CrossPlace achieves double-digit Recall@1 improvements over prior cross-modal methods, closes the gap to unimodal text retrieval, and narrows it to unimodal VPR. Code and benchmarks are available at https://github.com/oferidan1/CrossPlace

## Provider details
- **Arxiv Id:** 2611.34877
- **Categories:** ["cs.CV"]
