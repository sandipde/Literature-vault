---
title: 'Label-Efficient Patient Prioritization from Pairwise Preferences: A Simulation-Based
  Evaluation of Learning-to-Rank and Active-Learning Strategies'
type: paper
source: https://doi.org/10.2139/ssrn.7664978
canonical_url: https://doi.org/10.2139/ssrn.7664978
captured_by: auto-scanner
date: '2026-10-30'
captured_at: '2026-10-30T21:20:44+00:00'
last_requested: '2026-10-30T21:20:44+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Maya Makov Assif
- Maya Dagan
- Seffi Cohen
- Matthew McDermott
- Richard Zemel
- Noa Dagan
published: '2026-10-30'
abstract: Objective. Proactive care programs require health systems to prioritize
  patients when outreach capacity is limited, yet risk-only tools may not capture
  clinicians’ trade-offs among risk, actionability, care gaps, and expected benefit.
  We evaluated whether pairwise preference learning can support label-efficient patient
  prioritization in a controlled simulation setting with complete reference rankings.
  Materials and Methods. A synthetic cohort of 1,000 adults was generated with age,
  a cardiovascular-risk proxy, and 16 binary actionable care-gap indicators. Ten clinician-inspired
  preference simulators produced pairwise labels reflecting diverse prioritization
  policies. RankNet, XGBoost, and logistic regression were trained under fixed pair
  sampling and active learning; a risk-only ranking served as a clinical baseline.
  Performance was evaluated on held-out patients using pairwise area under the curve
  (AUC) and top-of-list metrics. Results. Performance improved rapidly and plateaued
  after approximately 400 labeled comparisons. RankNet performed best overall. At
  400 labeled pairs, RankNet with systematic fixed sampling achieved AUC 0.88 and
  normalized discounted cumulative gain at 20 (NDCG@20) 0.93. Replacing fixed sampling
  with active learning (Top-of-List Margin Refinement) improved head-of-list fidelity,
  increasing mean average precision at 20 (MAP@20) from 0.45 to 0.64 and rank-biased
  overlap (RBO) from 0.48 to 0.64, with AUC decreasing from 0.88 to 0.84. Learned
  rankings outperformed the risk-only baseline, and an exploratory large-language-model
  robustness extension preserved the same cross-model ordering. Conclusion. Pairwise
  preference learning recovered heterogeneous prioritization policies from limited
  pairwise supervision, while top-focused active learning improved fidelity at the
  head of the ranking.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.2139/ssrn.7664978
  journal: ''
  publisher: Elsevier BV
  type: posted-content
  subjects: []
---

# Label-Efficient Patient Prioritization from Pairwise Preferences: A Simulation-Based Evaluation of Learning-to-Rank and Active-Learning Strategies

- **Type:** paper
- **Source:** https://doi.org/10.2139/ssrn.7664978
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Maya Makov Assif, Maya Dagan, Seffi Cohen, Matthew McDermott, Richard Zemel, Noa Dagan
- **Published:** 2026-10-30

## Summary
Objective. Proactive care programs require health systems to prioritize patients when outreach capacity is limited, yet risk-only tools may not capture clinicians’ trade-offs among risk, actionability, care gaps, and expected benefit. We evaluated whether pairwise preference learning can support label-efficient patient prioritization in a controlled simulation setting with complete reference rankings. Materials and Methods. A synthetic cohort of 1,000 adults was generated with age, a cardiovascular-risk proxy, and 16 binary actionable care-gap indicators. Ten clinician-inspired preference simulators produced pairwise labels reflecting diverse prioritization policies. RankNet, XGBoost, and logistic regression were trained under fixed pair sampling and active learning; a risk-only ranking served as a clinical baseline. Performance was evaluated on held-out patients using pairwise area under the curve (AUC) and top-of-list metrics. Results. Performance improved rapidly and plateaued after approximately 400 labeled comparisons. RankNet performed best overall. At 400 labeled pairs, RankNet with systematic fixed sampling achieved AUC 0.88 and normalized discounted cumulative gain at 20 (NDCG@20) 0.93. Replacing fixed sampling with active learning (Top-of-List Margin Refinement) improved head-of-list fidelity, increasing mean average precision at 20 (MAP@20) from 0.45 to 0.64 and rank-biased overlap (RBO) from 0.48 to 0.64, with AUC decreasing from 0.88 to 0.84. Learned rankings outperformed the risk-only baseline, and an exploratory large-language-model robustness extension preserved the same cross-model ordering. Conclusion. Pairwise preference learning recovered heterogeneous prioritization policies from limited pairwise supervision, while top-focused active learning improved fidelity at the head of the ranking.

## Provider details
- **Doi:** 10.2139/ssrn.7664978
- **Publisher:** Elsevier BV
- **Type:** posted-content
