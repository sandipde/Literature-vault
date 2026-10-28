---
title: 'Resolving the Al2O3 phase diagram to 600 GPa with a machine-learned potential:
  Anharmonic effects and shock melting'
type: paper
source: https://doi.org/10.1016/j.commt.2026.100067
canonical_url: https://doi.org/10.1016/j.commt.2026.100067
captured_by: auto-scanner
date: '2026-10-18'
captured_at: '2026-10-18T09:18:02+00:00'
last_requested: '2026-10-18T09:18:02+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Qiannian Zhu
- Chuan Wang
- Xueli Zhang
- Qiyu Zeng
- Xiaoju Chang
- Weidong Ling
- Bo Chen
- Dongdong Kang
- Jiayu Dai
published: 2026-10
abstract: ''
metadata_provider: Crossref
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-public-source-recovery
enrichment_category: ML interatomic potentials
enrichment_tags: [alumina, high-pressure-phases, anharmonicity]
recovery_status: recovered
recovery_checked_on: '2026-10-28'
provider_data:
  doi: 10.1016/j.commt.2026.100067
  journal: Computational Materials Today
  publisher: Elsevier BV
  type: journal-article
  subjects: []
---

# Resolving the Al2O3 phase diagram to 600 GPa with a machine-learned potential: Anharmonic effects and shock melting

- **Type:** paper
- **Source:** https://doi.org/10.1016/j.commt.2026.100067
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Qiannian Zhu, Chuan Wang, Xueli Zhang, Qiyu Zeng, Xiaoju Chang, Weidong Ling, Bo Chen, Dongdong Kang, Jiayu Dai
- **Published:** 2026-10

## Provider details
- **Doi:** 10.1016/j.commt.2026.100067
- **Journal:** Computational Materials Today
- **Publisher:** Elsevier BV
- **Type:** journal-article

## Source recovery

- **Checked on:** 2026-10-28.
- **Attempted source:** https://doi.org/10.1016/j.commt.2026.100067 returned an Elsevier redirect shell.
- **Retrieved source:** https://api.openalex.org/works/https://doi.org/10.1016/j.commt.2026.100067?select=doi,title,abstract_inverted_index
- **Outcome:** The exact-DOI abstract describes a SCAN-level Deep Potential with active-learning configuration screening to suppress unphysical liquid clustering. It uses nonequilibrium thermodynamic integration for solid boundaries and reports a shock-melting region of 416.4-507.9 GPa.
- **Limitations:** Indexed abstract only; phase free energies, screening bias, and comparisons with measurements were not independently checked.

## AI enrichment

- **Concise summary:** The recovered abstract uses a learned Al2O3 potential to compute high-pressure melting curves and anharmonic solid-phase boundaries up to 600 GPa.
- **Why it matters:** Explicit anharmonic sampling can change phase-boundary predictions that quasiharmonic approximations miss under extreme conditions.
- **Caveat:** The phase diagram inherits the SCAN reference and model-training domain; reported agreement with sound-speed measurements is not independently verified.
- **Evidence:** [Captured source](https://doi.org/10.1016/j.commt.2026.100067); [recovered OpenAlex abstract](https://api.openalex.org/works/https://doi.org/10.1016/j.commt.2026.100067?select=doi,title,abstract_inverted_index), retrieved 2026-10-28; no independent full-text verification.
