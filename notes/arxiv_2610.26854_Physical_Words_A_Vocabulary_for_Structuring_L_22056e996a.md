---
title: 'Physical Words: A Vocabulary for Structuring Latent Reasoning in Robot Manipulation'
type: arxiv
source: https://arxiv.org/abs/2610.26854
canonical_url: https://arxiv.org/abs/2610.26854
captured_by: auto-scanner
date: '2026-10-20'
captured_at: '2026-10-20T09:46:32+00:00'
last_requested: '2026-10-20T09:46:32+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Jiaming Liu
- Xinghao Zhu
- Yiming Zhang
- Shanghang Zhang
- Yinxi Wang
- Yichu Yang
- Zhuoyang Liu
- Dantong Niu
- Soha Pouya
- Juekun Li
- Yan Chang
published: '2026-10-19'
abstract: Multimodal reasoning provides robotic foundation models with predictive
  context needed for reliable action generation. However, language-based reasoning
  captures task semantics but struggles to express fine-grained physical dynamics,
  while latent reasoning models future state evolution but offers limited structure
  for organizing these dynamics into reusable reasoning primitives. To bridge this
  gap, we introduce PhysWord, a reasoning-before-acting foundation model built on
  Physical Words, which use atomic action verbs as shared semantic anchors for continuous
  representations of physical dynamics. Specifically, PhysWord predicts upcoming atomic
  action words and directly aligns their contextual hidden states with latent targets
  derived from the corresponding future observations. Building on these primitives,
  we construct a temporally structured PhysWord space with visual and optional tactile
  variants of each action word. Autoregressively predicting Physical Words across
  future timesteps captures transitions between execution stages, providing structured
  multimodal context for action generation. PhysWord achieves state-of-the-art success
  rates of 90.3\% on visuotactile UniVTAC and 99.6\% on vision-based LIBERO-Long,
  and outperforms competing methods on real-world tasks using bimanual grippers and
  dexterous hands. Further evaluations demonstrate that our structured latent reasoning
  framework generalizes to unseen scenarios and enables long-horizon manipulation.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.26854'
  categories:
  - cs.RO
---

# Physical Words: A Vocabulary for Structuring Latent Reasoning in Robot Manipulation

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.26854
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Jiaming Liu, Xinghao Zhu, Yiming Zhang, Shanghang Zhang, Yinxi Wang, Yichu Yang, Zhuoyang Liu, Dantong Niu, Soha Pouya, Juekun Li, Yan Chang
- **Published:** 2026-10-19

## Summary
Multimodal reasoning provides robotic foundation models with predictive context needed for reliable action generation. However, language-based reasoning captures task semantics but struggles to express fine-grained physical dynamics, while latent reasoning models future state evolution but offers limited structure for organizing these dynamics into reusable reasoning primitives. To bridge this gap, we introduce PhysWord, a reasoning-before-acting foundation model built on Physical Words, which use atomic action verbs as shared semantic anchors for continuous representations of physical dynamics. Specifically, PhysWord predicts upcoming atomic action words and directly aligns their contextual hidden states with latent targets derived from the corresponding future observations. Building on these primitives, we construct a temporally structured PhysWord space with visual and optional tactile variants of each action word. Autoregressively predicting Physical Words across future timesteps captures transitions between execution stages, providing structured multimodal context for action generation. PhysWord achieves state-of-the-art success rates of 90.3\% on visuotactile UniVTAC and 99.6\% on vision-based LIBERO-Long, and outperforms competing methods on real-world tasks using bimanual grippers and dexterous hands. Further evaluations demonstrate that our structured latent reasoning framework generalizes to unseen scenarios and enables long-horizon manipulation.

## Provider details
- **Arxiv Id:** 2610.26854
- **Categories:** ["cs.RO"]
