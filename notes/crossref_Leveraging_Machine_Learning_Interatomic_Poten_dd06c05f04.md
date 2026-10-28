---
enriched_on: '2026-10-28'
enrichment_method: llm-public-source-recovery
enrichment_category: ML interatomic potentials
enrichment_tags: [force-field-parameterization, amber, mlip-surrogates, bonded-parameters]
recovery_status: recovered
recovery_checked_on: '2026-10-28'
title: Leveraging Machine Learning Interatomic Potentials for Fast and Accurate AMBER-Compatible
  Force Field Parameterization
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15008812/v2
canonical_url: https://doi.org/10.26434/chemrxiv.15008812/v2
captured_by: auto-scanner
date: '2026-10-13'
captured_at: '2026-10-13T21:42:05+00:00'
last_requested: '2026-10-13T21:42:05+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Xuchao Zhou
- Xujian Wang
- Jiahao Xie
- Leshen Zhang
- Junmei Wang
published: '2026-10-13'
abstract: ''
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15008812/v2
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Leveraging Machine Learning Interatomic Potentials for Fast and Accurate AMBER-Compatible Force Field Parameterization

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15008812/v2
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Xuchao Zhou, Xujian Wang, Jiahao Xie, Leshen Zhang, Junmei Wang
- **Published:** 2026-10-13

## Provider details
- **Doi:** 10.26434/chemrxiv.15008812/v2
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## Source recovery
- **Retrieval date:** 2026-10-28.
- **Sources:** https://doi.org/10.26434/chemrxiv.15008812/v2 returned HTTP 403 at ChemRxiv. https://api.openalex.org/works/https://doi.org/10.26434/chemrxiv.15008812/v2?select=id,doi,title,abstract_inverted_index supplied the exact-version indexed abstract.
- **Outcome:** ParmFit uses MLIPs to derive AMBER/GAFF-compatible parameters for small molecules, modified residues, and metal-coordination sites. The abstract reports a 1.17 kcal/mol reduction in mean unsigned hydration-free-energy error on a challenging FreeSolv subset, with lower parameterization cost than QM refinement.
- **Limitations:** Indexed abstract only; no parameter files, simulation trajectories, or claimed cost comparisons were independently tested.

## AI enrichment
- **Concise summary:** ParmFit uses MLIP-guided refinement to generate molecule-specific parameters compatible with conventional AMBER/GAFF workflows.
- **Why it matters:** It offers a bridge from learned atomistic models to established force-field ecosystems without requiring every downstream simulation to run a neural potential directly.
- **Caveat:** ChemRxiv v2 accuracy, stability, and cost claims are unverified; stable simulated geometry alone does not establish correct thermodynamics for every modified residue or metal site.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15008812/v2); [Recovered abstract](https://api.openalex.org/works/https://doi.org/10.26434/chemrxiv.15008812/v2?select=id,doi,title,abstract_inverted_index); analysis uses captured metadata and retrieved public abstract evidence, not independently verified full text.
