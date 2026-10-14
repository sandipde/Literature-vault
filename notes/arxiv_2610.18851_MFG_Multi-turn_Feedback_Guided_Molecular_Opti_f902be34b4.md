---
title: 'MFG: Multi-turn Feedback Guided Molecular Optimization'
type: arxiv
source: https://arxiv.org/abs/2610.18851
canonical_url: https://arxiv.org/abs/2610.18851
captured_by: auto-scanner
date: '2026-10-14'
captured_at: '2026-10-14T09:53:53+00:00'
last_requested: '2026-10-14T09:53:53+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Trieu Nguyen
- Frazier N. Baker
- Ruoxi Gao
- Daniel Adu-Ampratwum
- Xia Ning
published: '2026-10-13'
abstract: Multi-objective molecular optimization is a critical process in drug discovery
  that aims to modify a given molecule to simultaneously improve multiple properties
  while maintaining a similar overall structure. This process often requires iterative
  modifications guided by computational or experimental feedback. Recent large language
  model (LLM)-based methods have begun to explore this iterative approach; however,
  these methods are not explicitly trained to leverage such feedback, while existing
  approaches primarily focus on single-turn molecular optimization. To address this
  gap, we introduce Multi-turn Feedback Guided (MFG) molecular optimization, a reinforcement
  learning framework that trains an LLM to progressively optimize molecules using
  feedback from previous turns. MFG introduces a feedback vector capturing both property
  improvements and source molecule similarity, alongside a feedback-aligned reward
  function that promotes progressive improvement across turns. We apply MFG over $\text{GeLLM}^{3}\text{O}$,
  a state-of-the-art LLM model for multi-objective molecular optimization, evaluate
  $\text{GeLLM}^{3}\text{O-MFG}$ on ten multi-objective molecular optimization tasks.
  The results demonstrate that $\text{GeLLM}^{3}\text{O-MFG}$ achieves the highest
  average similarity-constrained success rate ($81.50%$), outperforming the base model
  $\text{GeLLM}^{3}\text{O}$ ($70.81%$).
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.18851'
  categories:
  - cs.AI
  - cs.LG
  - q-bio.QM
---

# MFG: Multi-turn Feedback Guided Molecular Optimization

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.18851
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Trieu Nguyen, Frazier N. Baker, Ruoxi Gao, Daniel Adu-Ampratwum, Xia Ning
- **Published:** 2026-10-13

## Summary
Multi-objective molecular optimization is a critical process in drug discovery that aims to modify a given molecule to simultaneously improve multiple properties while maintaining a similar overall structure. This process often requires iterative modifications guided by computational or experimental feedback. Recent large language model (LLM)-based methods have begun to explore this iterative approach; however, these methods are not explicitly trained to leverage such feedback, while existing approaches primarily focus on single-turn molecular optimization. To address this gap, we introduce Multi-turn Feedback Guided (MFG) molecular optimization, a reinforcement learning framework that trains an LLM to progressively optimize molecules using feedback from previous turns. MFG introduces a feedback vector capturing both property improvements and source molecule similarity, alongside a feedback-aligned reward function that promotes progressive improvement across turns. We apply MFG over $\text{GeLLM}^{3}\text{O}$, a state-of-the-art LLM model for multi-objective molecular optimization, evaluate $\text{GeLLM}^{3}\text{O-MFG}$ on ten multi-objective molecular optimization tasks. The results demonstrate that $\text{GeLLM}^{3}\text{O-MFG}$ achieves the highest average similarity-constrained success rate ($81.50%$), outperforming the base model $\text{GeLLM}^{3}\text{O}$ ($70.81%$).

## Provider details
- **Arxiv Id:** 2610.18851
- **Categories:** ["cs.AI", "cs.LG", "q-bio.QM"]
