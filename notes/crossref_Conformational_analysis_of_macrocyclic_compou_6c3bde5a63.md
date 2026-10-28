---
title: Conformational analysis of macrocyclic compounds using a machine-learned interatomic
  potential
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv-2025-bktvd
canonical_url: https://doi.org/10.26434/chemrxiv-2025-bktvd
captured_by: auto-scanner
date: '2026-10-10'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Hani Hashim
- Jeremy Harvey
published: '2025-06-19'
abstract: Macrocyclic compounds play a vital role in many chemical and biological
  systems, yet their conformational analysis remains a significant challenge. In this
  work, we investigate the conformational landscape of macrocyclic compounds using
  a machine-learned interatomic potential (MLIP) based on a Nequip-like graph neural
  network. This MLIP is trained on the energy differences between ωB97XD3 and GFN1-xTB.
  The model not only reproduces the DFT relative conformer energies of the macrocycles
  with high fidelity but also yields optimized structures that are practically identical
  to those obtained via density functional theory. Furthermore, when integrated into
  a metadynamics-based conformational sampling framework (CREST), we recover structures
  that very closely match the structure obtained after gas-phase optimization with
  DFT starting from the crystal structure. These results underscore the potential
  of machine learning to overcome longstanding challenges in the conformational analysis
  of complex macrocyclic systems.
metadata_provider: Crossref
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: ML interatomic potentials
enrichment_tags: [macrocycles, delta-learning, conformational-sampling]
provider_data:
  doi: 10.26434/chemrxiv-2025-bktvd
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Conformational analysis of macrocyclic compounds using a machine-learned interatomic potential

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv-2025-bktvd
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Hani Hashim, Jeremy Harvey
- **Published:** 2025-06-19

## Summary
Macrocyclic compounds play a vital role in many chemical and biological systems, yet their conformational analysis remains a significant challenge. In this work, we investigate the conformational landscape of macrocyclic compounds using a machine-learned interatomic potential (MLIP) based on a Nequip-like graph neural network. This MLIP is trained on the energy differences between ωB97XD3 and GFN1-xTB. The model not only reproduces the DFT relative conformer energies of the macrocycles with high fidelity but also yields optimized structures that are practically identical to those obtained via density functional theory. Furthermore, when integrated into a metadynamics-based conformational sampling framework (CREST), we recover structures that very closely match the structure obtained after gas-phase optimization with DFT starting from the crystal structure. These results underscore the potential of machine learning to overcome longstanding challenges in the conformational analysis of complex macrocyclic systems.

## Provider details
- **Doi:** 10.26434/chemrxiv-2025-bktvd
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment

- **Concise summary:** A NequIP-like potential learns the energy correction between omegaB97XD3 and GFN1-xTB for macrocycles. Coupling it to CREST metadynamics reportedly recovers conformers close to gas-phase DFT-optimized crystal-derived structures.
- **Why it matters:** Delta learning offers a focused route from inexpensive baseline energetics to higher-level conformational ranking and optimization.
- **Caveat:** This preprint's gas-phase conformer agreement does not establish solution populations or generalization to arbitrary macrocyclic chemistry.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv-2025-bktvd); analysis based only on captured metadata, not independently verified full text.
