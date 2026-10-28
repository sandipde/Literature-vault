---
enriched_on: '2026-10-28'
enrichment_method: llm-public-source-recovery
enrichment_category: Other and possible scan noise
enrichment_tags: [merchant-analytics, explainable-ml, trend-features]
recovery_status: recovered
recovery_checked_on: '2026-10-28'
title: An explainable machine learning framework with trend-sensitive features for
  predicting high-potential merchants in mobile payment ecosystems
type: paper
source: https://doi.org/10.1007/s10791-026-10593-0
canonical_url: https://doi.org/10.1007/s10791-026-10593-0
captured_by: auto-scanner
date: '2026-10-15'
captured_at: '2026-10-15T20:09:48+00:00'
last_requested: '2026-10-15T20:09:48+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- JrJung Lyu
- Chun-Hung Hsieh
published: '2026-10-15'
abstract: ''
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1007/s10791-026-10593-0
  journal: Discover Computing
  publisher: Springer Science and Business Media LLC
  type: journal-article
  subjects: []
---

# An explainable machine learning framework with trend-sensitive features for predicting high-potential merchants in mobile payment ecosystems

- **Type:** paper
- **Source:** https://doi.org/10.1007/s10791-026-10593-0
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** JrJung Lyu, Chun-Hung Hsieh
- **Published:** 2026-10-15

## Provider details
- **Doi:** 10.1007/s10791-026-10593-0
- **Journal:** Discover Computing
- **Publisher:** Springer Science and Business Media LLC
- **Type:** journal-article

## Source recovery
- **Retrieved on:** 2026-10-28
- **Source:** https://api.openalex.org/works/https://doi.org/10.1007/s10791-026-10593-0
- **Outcome:** Exact-DOI lookup recovered an abstract describing growth-trajectory features, XGBoost, and SHAP for merchant prioritization using 61,280 merchant-month records from 3,939 merchants. “High potential” means the top future-GMV quintile, contrasted with the bottom quintile.
- **Limitations:** The abstract concerns one payment provider and a polar-group sample, not the entire merchant population; it reports no user-study or measured business-outcome validation.

## AI enrichment
- **Concise summary:** The recovered study predicts future merchant transaction potential using trend-sensitive features and an explainable classification workflow.
- **Why it matters:** Its target-label definition is crucial to interpreting prediction claims, but merchant prioritization is outside the vault's core atomistic scope.
- **Caveat:** Reported held-out metrics come from an indexed abstract and a single-provider top-versus-bottom sample, not independently checked deployment results.
- **Evidence:** [Captured source](https://doi.org/10.1007/s10791-026-10593-0); [recovered abstract](https://api.openalex.org/works/https://doi.org/10.1007/s10791-026-10593-0), retrieved 2026-10-28. Analysis uses captured metadata and public indexed evidence, not independently verified full text.
