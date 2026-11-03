---
title: Bridging the Literature-to-Laboratory Gap with Language Models and Active Learning
  for Reaction Feasibility Prediction and Autonomous Exploration
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011623/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011623/v1
captured_by: auto-scanner
date: '2026-11-03'
captured_at: '2026-11-03T22:11:07+00:00'
last_requested: '2026-11-03T22:11:07+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Haowen Zhong
- Yi Yang
- Jiekai Jia
- Xin Yan
- Yongli Xie
- Yuan Li
- Xiaofeng Cui
- Sen Lin
- Peng Wang
- Xiaoxue Wang
published: '2026-11-03'
abstract: Predicting reaction feasibility is essential to organic synthesis, yet models
  trained on literature records often fail to generalize to laboratory data. Here,
  we present a two-stage distillation and adaptation framework that transfers reactivity
  knowledge from large, noisy literature datasets to small, controlled high-throughput
  experimentation (HTE) datasets, and further leverages this transferable knowledge
  to enable uncertainty-guided active learning. Literature reactions are curated and
  augmented with chemical reasoning to post-train reaction-specific language models
  through supervised fine-tuning (SFT) and reinforcement learning (RL), producing
  a compact generalist model. In zero-shot evaluation across Suzuki–Miyaura coupling,
  Buchwald–Hartwig amination and acid–amine condensation, the generalist model outperforms
  the strongest baseline by 41.5% in mean accuracy and 29.2% in macro-F1, while surpassing
  human expert accuracy by 8.9% and macro-F1 by 11.5%. To accelerate active exploration,
  generalist predictions are transferred into warm priors for Bayesian neural networks.
  This warm prior reduces the experimental labels needed to reach a held-out macro-F1
  ≥ 0.70 by 25.0–42.9% relative to a vanilla Bayesian neural network (BNN). Furthermore,
  uncertainty-guided acquisition prioritizes informative reactions, enabling the models
  to approach full-pool training performance using only about oneeighth of the total
  available reactions. To our knowledge, this work establishes the first experimentally
  validated literature-to-laboratory paradigm connecting 1 large-scale post-trained
  language models with active experimental design, providing a practical foundation
  for data-efficient, privacy-preserving, and autonomous chemical discovery.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011623/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Bridging the Literature-to-Laboratory Gap with Language Models and Active Learning for Reaction Feasibility Prediction and Autonomous Exploration

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011623/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Haowen Zhong, Yi Yang, Jiekai Jia, Xin Yan, Yongli Xie, Yuan Li, Xiaofeng Cui, Sen Lin, Peng Wang, Xiaoxue Wang
- **Published:** 2026-11-03

## Summary
Predicting reaction feasibility is essential to organic synthesis, yet models trained on literature records often fail to generalize to laboratory data. Here, we present a two-stage distillation and adaptation framework that transfers reactivity knowledge from large, noisy literature datasets to small, controlled high-throughput experimentation (HTE) datasets, and further leverages this transferable knowledge to enable uncertainty-guided active learning. Literature reactions are curated and augmented with chemical reasoning to post-train reaction-specific language models through supervised fine-tuning (SFT) and reinforcement learning (RL), producing a compact generalist model. In zero-shot evaluation across Suzuki–Miyaura coupling, Buchwald–Hartwig amination and acid–amine condensation, the generalist model outperforms the strongest baseline by 41.5% in mean accuracy and 29.2% in macro-F1, while surpassing human expert accuracy by 8.9% and macro-F1 by 11.5%. To accelerate active exploration, generalist predictions are transferred into warm priors for Bayesian neural networks. This warm prior reduces the experimental labels needed to reach a held-out macro-F1 ≥ 0.70 by 25.0–42.9% relative to a vanilla Bayesian neural network (BNN). Furthermore, uncertainty-guided acquisition prioritizes informative reactions, enabling the models to approach full-pool training performance using only about oneeighth of the total available reactions. To our knowledge, this work establishes the first experimentally validated literature-to-laboratory paradigm connecting 1 large-scale post-trained language models with active experimental design, providing a practical foundation for data-efficient, privacy-preserving, and autonomous chemical discovery.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011623/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
