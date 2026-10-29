---
title: Autonomous discovery of reaction networks from active-learning-driven reactive
  molecular dynamics
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011187/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011187/v1
captured_by: auto-scanner
date: '2026-10-28'
captured_at: '2026-10-28T21:29:02+00:00'
last_requested: '2026-10-28T21:29:02+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Jan A. Meissner
- Jan Meisner
published: '2026-10-28'
abstract: Reaction networks underlie complex chemical systems such as combustion,
  catalysis, and atmospheric chemistry and can comprise thousands of elementary reactions.
  Ab initio nanoreactor molecular dynamics explores such networks efficiently by accelerated
  sampling of the potential energy surface, but computational cost limits how far
  it can sample. This work presents a transferable methodology coupling nanoreactor
  molecular dynamics with active learning to autonomously generate reaction networks
  from starting molecules. An agentdeveloped parser extracts elementary reactions
  from trajectories, and a large-language-model coding agent improves transition-state
  search strategies. Applied to the atmospheric oxidation of dimethyl sulfide, the
  methodology yields 980 nanoseconds of simulation, requiring only 290,195 quantum-chemical
  calculations. Initializing reaction discovery from already discovered species drastically
  speeds up reaction network exploration leading to 13,271 elementary reactions and
  6,995 species. The reaction network covers most of the established mechanism but
  also unveils novel species such as an isomer of the key intermediate HPMTF.
metadata_provider: Crossref
metadata_status: complete
enriched_on: '2026-10-29'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [reactive-md, active-learning, reaction-networks, llm-agents]
provider_data:
  doi: 10.26434/chemrxiv.15011187/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Autonomous discovery of reaction networks from active-learning-driven reactive molecular dynamics

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011187/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Jan A. Meissner, Jan Meisner
- **Published:** 2026-10-28

## Summary
Reaction networks underlie complex chemical systems such as combustion, catalysis, and atmospheric chemistry and can comprise thousands of elementary reactions. Ab initio nanoreactor molecular dynamics explores such networks efficiently by accelerated sampling of the potential energy surface, but computational cost limits how far it can sample. This work presents a transferable methodology coupling nanoreactor molecular dynamics with active learning to autonomously generate reaction networks from starting molecules. An agentdeveloped parser extracts elementary reactions from trajectories, and a large-language-model coding agent improves transition-state search strategies. Applied to the atmospheric oxidation of dimethyl sulfide, the methodology yields 980 nanoseconds of simulation, requiring only 290,195 quantum-chemical calculations. Initializing reaction discovery from already discovered species drastically speeds up reaction network exploration leading to 13,271 elementary reactions and 6,995 species. The reaction network covers most of the established mechanism but also unveils novel species such as an isomer of the key intermediate HPMTF.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011187/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment

- **Concise summary:** The abstract describes an active-learning nanoreactor workflow that automates reaction extraction and transition-state search, applied to dimethyl-sulfide oxidation to expand a reaction network.
- **Why it matters:** It connects adaptive simulation with agent-assisted analysis, a potentially useful route for exploring reactive systems whose pathways are too numerous for manual enumeration.
- **Caveat:** This is a ChemRxiv version 1 preprint. The reported simulation duration, calculation count, network size, and newly identified species are author-reported; no full-text review or independent reproduction was performed.
- **Evidence:** Captured Crossref title, abstract, and provider metadata; [ChemRxiv record](https://doi.org/10.26434/chemrxiv.15011187/v1). The analysis uses captured metadata only, not full text.
