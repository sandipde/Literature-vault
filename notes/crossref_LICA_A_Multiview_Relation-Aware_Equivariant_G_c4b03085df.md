---
title: 'LICA: A Multiview Relation-Aware Equivariant Graph Neural Network with Interfacial
  Atomic-Pair Attention for Protein–Ligand Binding Affinity Prediction'
type: paper
source: https://doi.org/10.1021/acs.jcim.6c02767
canonical_url: https://doi.org/10.1021/acs.jcim.6c02767
captured_by: auto-scanner
date: '2026-11-24'
captured_at: '2026-11-24T03:08:07+00:00'
last_requested: '2026-11-24T03:08:07+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Ronghui Zhan
- Xin Zeng
- Xiaoling Zhang
- Xingwen Zhu
- Yi Li
published: '2026-11-23'
abstract: Abstract Accurate prediction of protein–ligand binding affinity is foundational
  in structure-based drug design, yet existing 3D graph models often mix heterogeneous
  chemical relations and dilute sparse interfacial signals through global pooling.
  We present LICA, a relation-aware equivariant graph neural network that explicitly
  distinguishes covalent, spatial, and interfacial contacts on a unified 3D graph.
  A multiview readout extracts complementary information from the ligand, the pocket,
  and explicit interfacial atom pairs. Trained under a leakage-controlled Tanimoto
  split and tested independently on CASF-2016, LICA shows that prediction errors concentrate
  in sparsely sampled extreme-affinity regions, exhibiting a regression-to-the-mean
  extrapolation bottleneck. Ablation studies demonstrate that the explicit interfacial
  atom-pair attention provides a meaningful geometric inductive bias rather than merely
  adding parameters. This bias is particularly effective for spatially directional
  interactions, such as cation−π contacts. Using structural annotations as a reference,
  we further show that the learned interface attention highly overlaps with true short-range
  contacts. However, case studies reveal that these attention weights serve as a qualitative
  map of physical interactions and should not be interpreted as a quantitative decomposition
  of binding free energy. Overall, explicit interface pairing improves affinity regression
  while yielding a chemically verifiable representation of protein–ligand interactions.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1021/acs.jcim.6c02767
  journal: 'Journal of Chemical Information

    and Modeling'
  publisher: American Chemical Society (ACS)
  type: journal-article
  subjects: []
---

# LICA: A Multiview Relation-Aware Equivariant Graph Neural Network with Interfacial Atomic-Pair Attention for Protein–Ligand Binding Affinity Prediction

- **Type:** paper
- **Source:** https://doi.org/10.1021/acs.jcim.6c02767
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Ronghui Zhan, Xin Zeng, Xiaoling Zhang, Xingwen Zhu, Yi Li
- **Published:** 2026-11-23

## Summary
Abstract Accurate prediction of protein–ligand binding affinity is foundational in structure-based drug design, yet existing 3D graph models often mix heterogeneous chemical relations and dilute sparse interfacial signals through global pooling. We present LICA, a relation-aware equivariant graph neural network that explicitly distinguishes covalent, spatial, and interfacial contacts on a unified 3D graph. A multiview readout extracts complementary information from the ligand, the pocket, and explicit interfacial atom pairs. Trained under a leakage-controlled Tanimoto split and tested independently on CASF-2016, LICA shows that prediction errors concentrate in sparsely sampled extreme-affinity regions, exhibiting a regression-to-the-mean extrapolation bottleneck. Ablation studies demonstrate that the explicit interfacial atom-pair attention provides a meaningful geometric inductive bias rather than merely adding parameters. This bias is particularly effective for spatially directional interactions, such as cation−π contacts. Using structural annotations as a reference, we further show that the learned interface attention highly overlaps with true short-range contacts. However, case studies reveal that these attention weights serve as a qualitative map of physical interactions and should not be interpreted as a quantitative decomposition of binding free energy. Overall, explicit interface pairing improves affinity regression while yielding a chemically verifiable representation of protein–ligand interactions.

## Provider details
- **Doi:** 10.1021/acs.jcim.6c02767
- **Journal:** Journal of Chemical Information
and Modeling
- **Publisher:** American Chemical Society (ACS)
- **Type:** journal-article
