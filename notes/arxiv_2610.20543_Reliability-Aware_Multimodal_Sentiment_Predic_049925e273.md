---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Other and possible scan noise
enrichment_tags: [multimodal-sentiment, missing-data, evaluation-leakage]
title: Reliability-Aware Multimodal Sentiment Prediction Under Local Modality Missingness
type: arxiv
source: https://arxiv.org/abs/2610.20543
canonical_url: https://arxiv.org/abs/2610.20543
captured_by: auto-scanner
date: '2026-10-15'
captured_at: '2026-10-15T09:34:27+00:00'
last_requested: '2026-10-15T09:34:27+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Minghao Kong
- Deng Yao
- Xi Zhang
- Ying Gao
- Jiurun Chen
- Zirong Liu
- Rongjie Wang
published: '2026-10-14'
abstract: Multimodal sentiment models are usually evaluated on complete utterances,
  yet streams often lose a contiguous span of text, audio, or video. We study local
  missingness on aligned CMU-MOSEI features. Our reliability-aware network (RM-Net)
  keeps the original temporal positions, represents unobserved positions with a learned
  token, outputs bounded per-modality intensity contributions gated by observation
  quality, and is trained with dual-view masking of contiguous segments. We fuse five
  RM-Net seeds with a LoRA-adapted BERT text expert, using a fusion weight that depends
  only on the visible fraction of content tokens. Architecture, checkpoint, and fusion
  choices were made on the validation split. On the held-out split, the fused model
  reaches a macro-F1 of 0.655 on clean inputs and 0.634 under 40\% mixed missingness;
  its two-view average exceeds the auxiliary-head baseline by 0.024 (95\% video-cluster
  bootstrap interval [0.003, 0.045]). Because this split was inspected during development,
  these numbers are not a blind test. For explanations, exact Shapley attributions
  over the eight modality subsets and position-level occlusion show that top-ranked
  positions reduce the predicted-class probability faster than random positions (AUC
  gap 0.113 on validation). We also describe an auditable word-level alignment pipeline
  for raw clips; its outputs do not feed the predictive models.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.20543'
  categories:
  - cs.CV
---

# Reliability-Aware Multimodal Sentiment Prediction Under Local Modality Missingness

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.20543
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Minghao Kong, Deng Yao, Xi Zhang, Ying Gao, Jiurun Chen, Zirong Liu, Rongjie Wang
- **Published:** 2026-10-14

## Summary
Multimodal sentiment models are usually evaluated on complete utterances, yet streams often lose a contiguous span of text, audio, or video. We study local missingness on aligned CMU-MOSEI features. Our reliability-aware network (RM-Net) keeps the original temporal positions, represents unobserved positions with a learned token, outputs bounded per-modality intensity contributions gated by observation quality, and is trained with dual-view masking of contiguous segments. We fuse five RM-Net seeds with a LoRA-adapted BERT text expert, using a fusion weight that depends only on the visible fraction of content tokens. Architecture, checkpoint, and fusion choices were made on the validation split. On the held-out split, the fused model reaches a macro-F1 of 0.655 on clean inputs and 0.634 under 40\% mixed missingness; its two-view average exceeds the auxiliary-head baseline by 0.024 (95\% video-cluster bootstrap interval [0.003, 0.045]). Because this split was inspected during development, these numbers are not a blind test. For explanations, exact Shapley attributions over the eight modality subsets and position-level occlusion show that top-ranked positions reduce the predicted-class probability faster than random positions (AUC gap 0.113 on validation). We also describe an auditable word-level alignment pipeline for raw clips; its outputs do not feed the predictive models.

## Provider details
- **Arxiv Id:** 2610.20543
- **Categories:** ["cs.CV"]

## AI enrichment
- **Concise summary:** RM-Net models contiguous missing spans in text, audio, and video using quality-gated modality contributions and fuses its outputs with a text expert.
- **Why it matters:** Its explicit disclosure that the held-out split was inspected is a useful evaluation warning, though sentiment prediction is peripheral to atomistic materials research.
- **Caveat:** The preprint's reported macro-F1 scores are not blind-test results; validation-based explanation metrics also do not establish causal interpretability.
- **Evidence:** [Captured source](https://arxiv.org/abs/2610.20543); analysis based only on captured metadata, not independently verified full text.
