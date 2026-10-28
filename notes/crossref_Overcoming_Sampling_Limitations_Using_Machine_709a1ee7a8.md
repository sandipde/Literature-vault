---
title: 'Overcoming Sampling Limitations Using Machine-Learned Interatomic Potentials:
  The Case of Water-in-Salt Electrolytes'
type: paper
source: https://doi.org/10.1021/acs.jctc.6c00579.s001
canonical_url: https://doi.org/10.1021/acs.jctc.6c00579.s001
captured_by: auto-scanner
date: '2026-10-13'
captured_at: '2026-10-13T21:42:05+00:00'
last_requested: '2026-10-13T21:42:05+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors: []
published: '2026-10-13'
abstract: ''
metadata_provider: Crossref
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-public-source-recovery
enrichment_category: ML interatomic potentials
enrichment_tags: [water-in-salt, sampling-limitations, potential-finetuning]
recovery_status: partial
recovery_checked_on: '2026-10-28'
provider_data:
  doi: 10.1021/acs.jctc.6c00579.s001
  journal: ''
  publisher: American Chemical Society (ACS)
  type: component
  subjects: []
---

# Overcoming Sampling Limitations Using Machine-Learned Interatomic Potentials: The Case of Water-in-Salt Electrolytes

- **Type:** paper
- **Source:** https://doi.org/10.1021/acs.jctc.6c00579.s001
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Published:** 2026-10-13

## Provider details
- **Doi:** 10.1021/acs.jctc.6c00579.s001
- **Publisher:** American Chemical Society (ACS)
- **Type:** component

## Source recovery

- **Checked on:** 2026-10-28.
- **Attempted sources:** https://doi.org/10.1021/acs.jctc.6c00579.s001 ; https://pubs.acs.org/doi/10.1021/acs.jctc.6c00579 returned HTTP 403 for the supplement and parent article.
- **Retrieved sources:** https://api.crossref.org/works/10.1021%2Facs.jctc.6c00579.s001 ; https://api.openalex.org/works/https://doi.org/10.1021/acs.jctc.6c00579?select=doi,title,abstract_inverted_index
- **Outcome:** Crossref explicitly identifies this component as supplemental information for 10.1021/acs.jctc.6c00579. The linked parent's indexed abstract compares foundation, fine-tuned, and from-scratch MACE models for 21 m LiTFSI water-in-salt electrolyte, emphasizing sampling and difficult short Li-Li distances.
- **Limitations:** The supplement itself remains unread; parent-abstract information is not a summary of the supplement's contents.

## AI enrichment

- **Concise summary:** This DOI identifies supporting information, not a separate primary article. The recovered parent abstract examines MLIP sampling of concentrated LiTFSI electrolyte and reports advantages of fine-tuning and sensitivity to dispersion corrections.
- **Why it matters:** Distinguishing the component from its parent avoids double-counting evidence while retaining a useful pointer to sampling and reference-functional choices.
- **Caveat:** Parent-abstract claims cannot establish what is contained in the inaccessible supplement or independently validate structural agreement.
- **Evidence:** [Captured source](https://doi.org/10.1021/acs.jctc.6c00579.s001); [component identity](https://api.crossref.org/works/10.1021%2Facs.jctc.6c00579.s001) and [linked parent abstract](https://api.openalex.org/works/https://doi.org/10.1021/acs.jctc.6c00579?select=doi,title,abstract_inverted_index), retrieved 2026-10-28; no independent full-text verification.
