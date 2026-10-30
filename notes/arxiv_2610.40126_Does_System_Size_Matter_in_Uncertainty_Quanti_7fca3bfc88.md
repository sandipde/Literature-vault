---
title: Does System Size Matter in Uncertainty Quantification for Machine Learning
  Interatomic Potentials?
type: arxiv
source: https://arxiv.org/abs/2610.40126
canonical_url: https://arxiv.org/abs/2610.40126
captured_by: auto-scanner
date: '2026-10-30'
captured_at: '2026-10-30T11:09:08+00:00'
last_requested: '2026-10-30T11:09:08+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Chayaphol Lortaraprasert
- Nontawat Charoenphakdee
- Wenwen Li
- Yong-Bin Zhuang
- Yuta Tsuboi
published: '2026-10-29'
abstract: Machine-learning interatomic potentials (MLIPs) commonly use uncertainty
  estimates to flag out-of-distribution (OOD) configurations and select structures
  for active learning. A key question is whether the resulting structure-level uncertainty
  scores remain comparable across different system sizes. A common practice is to
  aggregate per-atom uncertainties by their mean or maximum and compare the resulting
  score against a fixed threshold, implicitly assuming such comparability. We test
  this assumption across several in-distribution (ID)/OOD pairs by characterizing
  both aggregations as a function of atom count. The two aggregations exhibit distinct
  size dependencies. Mean aggregation remains size-independent for homogeneous systems
  but loses sensitivity to defects in large cells. In contrast, maximum aggregation
  grows with system size for ID systems while remaining approximately flat for defect-containing
  systems, narrowing the ID-OOD gap in a manner consistent with extreme-value statistics.
  Although highly uncertain atoms in large structures may indicate novel local environments,
  retraining on these structures yields little improvement, in contrast to retraining
  on OOD structures constructed to lie outside the training distribution. Our results
  reveal a practical limitation of size-unaware uncertainty criteria and motivate
  size-aware calibration for more reliable OOD detection in large-scale atomistic
  simulations.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.40126'
  categories:
  - cs.LG
  - cond-mat.mtrl-sci
---

# Does System Size Matter in Uncertainty Quantification for Machine Learning Interatomic Potentials?

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.40126
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Chayaphol Lortaraprasert, Nontawat Charoenphakdee, Wenwen Li, Yong-Bin Zhuang, Yuta Tsuboi
- **Published:** 2026-10-29

## Summary
Machine-learning interatomic potentials (MLIPs) commonly use uncertainty estimates to flag out-of-distribution (OOD) configurations and select structures for active learning. A key question is whether the resulting structure-level uncertainty scores remain comparable across different system sizes. A common practice is to aggregate per-atom uncertainties by their mean or maximum and compare the resulting score against a fixed threshold, implicitly assuming such comparability. We test this assumption across several in-distribution (ID)/OOD pairs by characterizing both aggregations as a function of atom count. The two aggregations exhibit distinct size dependencies. Mean aggregation remains size-independent for homogeneous systems but loses sensitivity to defects in large cells. In contrast, maximum aggregation grows with system size for ID systems while remaining approximately flat for defect-containing systems, narrowing the ID-OOD gap in a manner consistent with extreme-value statistics. Although highly uncertain atoms in large structures may indicate novel local environments, retraining on these structures yields little improvement, in contrast to retraining on OOD structures constructed to lie outside the training distribution. Our results reveal a practical limitation of size-unaware uncertainty criteria and motivate size-aware calibration for more reliable OOD detection in large-scale atomistic simulations.

## Provider details
- **Arxiv Id:** 2610.40126
- **Categories:** ["cs.LG", "cond-mat.mtrl-sci"]
