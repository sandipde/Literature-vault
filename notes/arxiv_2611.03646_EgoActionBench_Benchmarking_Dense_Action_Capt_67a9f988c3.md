---
title: 'EgoActionBench: Benchmarking Dense Action Captioning for Egocentric Human
  Videos'
type: arxiv
source: https://arxiv.org/abs/2611.03646
canonical_url: https://arxiv.org/abs/2611.03646
captured_by: auto-scanner
date: '2026-11-03'
captured_at: '2026-11-03T12:34:47+00:00'
last_requested: '2026-11-03T12:34:47+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Yujiao Shen
- Jiahe Song
- Haitian Li
- Jingkang Yang
- Ziwei Liu
published: '2026-11-02'
abstract: Learning from human data offers a scalable path toward embodied intelligence,
  yet it requires models to accurately understand fine-grained human actions from
  egocentric observations. However, existing benchmarks remain limited in action atomicity,
  temporal precision, and hand-action association. We introduce EgoActionBench, a
  benchmark that represents continuous human manipulation as temporally localized
  atomic actions associated with the left hand, right hand, or both hands. EgoActionBench
  contains 1,407 episodes with 41,132 human-refined action annotations. To evaluate
  such dense predictions, we propose an evaluation protocol that retrieves temporally
  eligible candidates, selects a prediction by content agreement, and scores semantic
  fidelity and temporal overlap alongside action precision and recall, jointly capturing
  what happens, when it happens, and which hand performs it. We benchmark 20 baseline
  models and systems on EgoActionBench and further adapt two backbones, Qwen3-VL-4B
  and LLaVA-OneVision-2-8B, through supervised fine-tuning followed by reinforcement
  learning on automatically annotated training episodes. EgoAction improves EgoActionScore
  by 15.9 and 23.2 points on the two backbones, and both adapted models outperform
  all open-source baselines. Our experiments reveal substantial limitations of current
  models in action atomicity, temporal precision, and hand-action association, highlighting
  the gap between general video understanding and the action understanding required
  for embodied intelligence.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.03646'
  categories:
  - cs.CV
---

# EgoActionBench: Benchmarking Dense Action Captioning for Egocentric Human Videos

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.03646
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Yujiao Shen, Jiahe Song, Haitian Li, Jingkang Yang, Ziwei Liu
- **Published:** 2026-11-02

## Summary
Learning from human data offers a scalable path toward embodied intelligence, yet it requires models to accurately understand fine-grained human actions from egocentric observations. However, existing benchmarks remain limited in action atomicity, temporal precision, and hand-action association. We introduce EgoActionBench, a benchmark that represents continuous human manipulation as temporally localized atomic actions associated with the left hand, right hand, or both hands. EgoActionBench contains 1,407 episodes with 41,132 human-refined action annotations. To evaluate such dense predictions, we propose an evaluation protocol that retrieves temporally eligible candidates, selects a prediction by content agreement, and scores semantic fidelity and temporal overlap alongside action precision and recall, jointly capturing what happens, when it happens, and which hand performs it. We benchmark 20 baseline models and systems on EgoActionBench and further adapt two backbones, Qwen3-VL-4B and LLaVA-OneVision-2-8B, through supervised fine-tuning followed by reinforcement learning on automatically annotated training episodes. EgoAction improves EgoActionScore by 15.9 and 23.2 points on the two backbones, and both adapted models outperform all open-source baselines. Our experiments reveal substantial limitations of current models in action atomicity, temporal precision, and hand-action association, highlighting the gap between general video understanding and the action understanding required for embodied intelligence.

## Provider details
- **Arxiv Id:** 2611.03646
- **Categories:** ["cs.CV"]
