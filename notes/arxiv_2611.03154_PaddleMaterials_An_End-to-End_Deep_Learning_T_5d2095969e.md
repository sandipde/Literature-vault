---
title: 'PaddleMaterials: An End-to-End Deep Learning Toolkit for Materials Science'
type: arxiv
source: https://arxiv.org/abs/2611.03154
canonical_url: https://arxiv.org/abs/2611.03154
captured_by: auto-scanner
date: '2026-11-03'
captured_at: '2026-11-03T12:34:47+00:00'
last_requested: '2026-11-03T12:34:47+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Xuwei Liu
- Zhimin Zhang
- Xiaoguang Hu
- Zhongwei Liu
- Yuanhui Sun
- Jun Huo
- Hua Wu
- Haifeng Wang
published: '2026-11-02'
abstract: 'Machine learning supports materials design, atomistic simulation and experimental
  characterization, yet models and workflows remain fragmented. We present PaddleMaterials,
  an open-source framework integrating heterogeneous materials-learning tasks while
  preserving task-specific representations and scientific semantics. It unifies data
  processing, training, evaluation, pretrained-model management and workflows across
  six task classes: property prediction, structure generation, machine-learning interatomic
  potentials, electronic-structure fields, spectrum elucidation and microscopy image
  processing. Task interfaces record physical quantities, units, aggregation conventions
  and references, making cross-task composition verifiable. A shared compiler backend
  enables switching from dynamic-graph to compiled execution through one setting,
  using graph optimization, operator fusion and hardware-targeted code generation
  without changing model definitions. Across 65 model instances in 11 groups, compiled
  execution accelerated every instance in eight groups, with group median speedups
  of 11%-224% and group maximum speedups of 11%-336%. Case studies on LiMnO2 and toluene
  link structure generation or spectrum elucidation, interatomic-potential relaxation,
  property prediction and electron-density prediction, using same-geometry density
  functional theory (DFT) calculations as references. For LiMnO2, predicted formation
  energies for generated and relaxed structures differed from same-geometry PBE+U
  references by at most 7 meV per atom, while the computational cost of model steps
  was less than one-twentieth of a DFT single-point calculation. PaddleMaterials extends
  unified materials workflows beyond conventional property, potential and structure-generation
  tasks while supporting verifiable cross-task operations and compiled execution.'
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.03154'
  categories:
  - cs.LG
  - cond-mat.mtrl-sci
  - cs.CE
---

# PaddleMaterials: An End-to-End Deep Learning Toolkit for Materials Science

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.03154
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Xuwei Liu, Zhimin Zhang, Xiaoguang Hu, Zhongwei Liu, Yuanhui Sun, Jun Huo, Hua Wu, Haifeng Wang
- **Published:** 2026-11-02

## Summary
Machine learning supports materials design, atomistic simulation and experimental characterization, yet models and workflows remain fragmented. We present PaddleMaterials, an open-source framework integrating heterogeneous materials-learning tasks while preserving task-specific representations and scientific semantics. It unifies data processing, training, evaluation, pretrained-model management and workflows across six task classes: property prediction, structure generation, machine-learning interatomic potentials, electronic-structure fields, spectrum elucidation and microscopy image processing. Task interfaces record physical quantities, units, aggregation conventions and references, making cross-task composition verifiable. A shared compiler backend enables switching from dynamic-graph to compiled execution through one setting, using graph optimization, operator fusion and hardware-targeted code generation without changing model definitions. Across 65 model instances in 11 groups, compiled execution accelerated every instance in eight groups, with group median speedups of 11%-224% and group maximum speedups of 11%-336%. Case studies on LiMnO2 and toluene link structure generation or spectrum elucidation, interatomic-potential relaxation, property prediction and electron-density prediction, using same-geometry density functional theory (DFT) calculations as references. For LiMnO2, predicted formation energies for generated and relaxed structures differed from same-geometry PBE+U references by at most 7 meV per atom, while the computational cost of model steps was less than one-twentieth of a DFT single-point calculation. PaddleMaterials extends unified materials workflows beyond conventional property, potential and structure-generation tasks while supporting verifiable cross-task operations and compiled execution.

## Provider details
- **Arxiv Id:** 2611.03154
- **Categories:** ["cs.LG", "cond-mat.mtrl-sci", "cs.CE"]
