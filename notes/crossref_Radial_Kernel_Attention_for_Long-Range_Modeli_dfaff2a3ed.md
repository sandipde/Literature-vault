---
title: Radial Kernel Attention for Long-Range Modeling in Polymer Machine Learning
  Force Fields
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011478/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011478/v1
captured_by: auto-scanner
date: '2026-11-02'
captured_at: '2026-11-02T13:02:05+00:00'
last_requested: '2026-11-02T13:02:05+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Wenbo Fu
- Chenghui Mao
- Chengwen Hu
- Haifeng Lv
- Zhou Lv
published: '2026-11-02'
abstract: We introduce Radial Kernel Attention (RKA) for long-range modeling in polymer
  machine learning force fields. Local neighbor graphs constrain communication across
  polymer chains and their surrounding environments, while explicit all-pair attention
  incurs quadratic cost. RKA maps atomic distances from the cluster centroid to learned
  radial features and combines their overlap with content-dependent queries and keys.
  Factorized aggregation and readout enable global feature exchange at linear cost
  in atom count for fixed feature dimensions. We insert the invariant scalar update
  between EquiformerV3 local blocks and obtain conservative forces by differentiating
  the total energy, including its radial coordinate dependence. We evaluate energy
  and force prediction for finite polymer-derived clusters in OPoly26. Our models
  are trained on the official training split for 12 epochs and evaluated directly
  after training on the complete official validation split. A matched 5M comparison
  shows that RKA reduces per-atom energy and force MAEs by 67.4% and 36.3%, respectively.
  The 20M RKA model is compared with UMA-S-1.2 and UMA-S-1.2.1 on the same validation
  structures. The 20M model attains a total-energy MAE of 15.81 meV and a force MAE
  of 2.619 meV/Å; its per-atom energy MAE is 0.1182 meV/atom. RKA provides a compact
  global communication pathway that improves energy and force prediction on the evaluated
  polymer-derived clusters.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011478/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Radial Kernel Attention for Long-Range Modeling in Polymer Machine Learning Force Fields

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011478/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Wenbo Fu, Chenghui Mao, Chengwen Hu, Haifeng Lv, Zhou Lv
- **Published:** 2026-11-02

## Summary
We introduce Radial Kernel Attention (RKA) for long-range modeling in polymer machine learning force fields. Local neighbor graphs constrain communication across polymer chains and their surrounding environments, while explicit all-pair attention incurs quadratic cost. RKA maps atomic distances from the cluster centroid to learned radial features and combines their overlap with content-dependent queries and keys. Factorized aggregation and readout enable global feature exchange at linear cost in atom count for fixed feature dimensions. We insert the invariant scalar update between EquiformerV3 local blocks and obtain conservative forces by differentiating the total energy, including its radial coordinate dependence. We evaluate energy and force prediction for finite polymer-derived clusters in OPoly26. Our models are trained on the official training split for 12 epochs and evaluated directly after training on the complete official validation split. A matched 5M comparison shows that RKA reduces per-atom energy and force MAEs by 67.4% and 36.3%, respectively. The 20M RKA model is compared with UMA-S-1.2 and UMA-S-1.2.1 on the same validation structures. The 20M model attains a total-energy MAE of 15.81 meV and a force MAE of 2.619 meV/Å; its per-atom energy MAE is 0.1182 meV/atom. RKA provides a compact global communication pathway that improves energy and force prediction on the evaluated polymer-derived clusters.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011478/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
