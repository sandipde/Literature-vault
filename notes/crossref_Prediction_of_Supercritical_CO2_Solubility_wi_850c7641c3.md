---
enriched_on: '2026-10-28'
enrichment_method: llm-public-source-recovery
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [supercritical-solubility, equivariant-networks, thermodynamic-conditioning, molecular-properties]
recovery_status: recovered
recovery_checked_on: '2026-10-28'
title: Prediction of Supercritical CO2 Solubility with a Thermodynamics-Conditioned
  Equivariant Graph Neural Network Model
type: paper
source: https://doi.org/10.1016/j.greeac.2026.100395
canonical_url: https://doi.org/10.1016/j.greeac.2026.100395
captured_by: auto-scanner
date: '2026-10-16'
captured_at: '2026-10-16T09:27:31+00:00'
last_requested: '2026-10-16T09:27:31+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Moritz Effner
- Christopher Siller
- Mijo Stanic
- Michael Lämmerhofer
published: 2026-10
abstract: ''
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1016/j.greeac.2026.100395
  journal: Green Analytical Chemistry
  publisher: Elsevier BV
  type: journal-article
  subjects: []
---

# Prediction of Supercritical CO2 Solubility with a Thermodynamics-Conditioned Equivariant Graph Neural Network Model

- **Type:** paper
- **Source:** https://doi.org/10.1016/j.greeac.2026.100395
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Moritz Effner, Christopher Siller, Mijo Stanic, Michael Lämmerhofer
- **Published:** 2026-10

## Provider details
- **Doi:** 10.1016/j.greeac.2026.100395
- **Journal:** Green Analytical Chemistry
- **Publisher:** Elsevier BV
- **Type:** journal-article

## Source recovery
- **Retrieval date:** 2026-10-28.
- **Sources:** https://doi.org/10.1016/j.greeac.2026.100395 returned an Elsevier redirect page. https://api.openalex.org/works/https://doi.org/10.1016/j.greeac.2026.100395?select=id,doi,title,abstract_inverted_index supplied the indexed abstract.
- **Outcome:** The model combines PaiNN with FiLM conditioning on thermodynamic descriptors and is trained on 27,461 solubility measurements for 958 molecules. The abstract reports cross-validation R2 near 0.77 and uses relevance propagation and ablations to inspect chemical plausibility.
- **Limitations:** No full text, train/test grouping details, or model predictions were checked; plausible explanations are not mechanistic proof.

## AI enrichment
- **Concise summary:** A thermodynamics-conditioned equivariant graph model predicts organic-molecule solubility in supercritical CO2 from molecular geometry and bulk-condition descriptors.
- **Why it matters:** Combining structural and thermodynamic inputs targets condition-dependent solubility rather than treating it as an intrinsic molecule-only property.
- **Caveat:** The recovered performance claims are unverified; cross-validation does not alone establish new-molecule or cross-laboratory transfer, and this property predictor is not a force field.
- **Evidence:** [Captured source](https://doi.org/10.1016/j.greeac.2026.100395); [Recovered abstract](https://api.openalex.org/works/https://doi.org/10.1016/j.greeac.2026.100395?select=id,doi,title,abstract_inverted_index); analysis uses captured metadata and retrieved public abstract evidence, not independently verified full text.
