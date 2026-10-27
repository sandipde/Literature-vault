---
title: Toward Interpretable Graph-Based Machine Learning for Combustion Kinetic Model
  Generation
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010767/v2
canonical_url: https://doi.org/10.26434/chemrxiv.15010767/v2
captured_by: auto-scanner
date: '2026-10-23'
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [combustion-chemistry, graph-neural-networks, version-update]
captured_at: '2026-10-23T09:43:13+00:00'
last_requested: '2026-10-23T09:43:13+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- James H. Du
- Suryanarayan Ramachandran
- Suo Yang
published: '2026-10-23'
abstract: This work presents an atom-conserving and interpretable graph neural network
  (GNN) for combustion kinetic model generation, where atoms are represented as nodes,
  covalent bonds are represented as edges, and reactions are represented as bond-rearrangement
  operations. Its artificial-intelligence (AI) contribution is a reaction generator
  that extends a standard Graph Isomorphism Network with Edges (GINE) architecture
  through reaction-context embeddings, reaction branching & third-body reaction inputs,
  Arrhenius-rate-parameter prediction, pairwise decoding, and stochastic inference
  over evolving reactant pools. Trained on the Li–Dryer hydrogen combustion kinetic
  model (8 species and 21 reactions), the GNN reproduces trained chemistry and generates
  element-balanced new reactions and intermediate species outside the training dataset,
  many of which have experimental analogues. When trained on a subset of the Li–Dryer
  dataset, the model recovered most held-out reactions and revealed relationships
  between samples (reactions) in the model’s latent space. The results suggest that
  the model learns transferable local reaction structures and generates valid species
  and reactions. As with any reaction generators, the generated reaction models require
  thermochemical and kinetic verification; the intended engineering application is
  low-cost reaction-pathway exploration for new fuels and prioritization of experiments
  and first-principles calculations to develop new combustion kinetic models.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010767/v2
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Toward Interpretable Graph-Based Machine Learning for Combustion Kinetic Model Generation

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010767/v2
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** James H. Du, Suryanarayan Ramachandran, Suo Yang
- **Published:** 2026-10-23

## Summary
This work presents an atom-conserving and interpretable graph neural network (GNN) for combustion kinetic model generation, where atoms are represented as nodes, covalent bonds are represented as edges, and reactions are represented as bond-rearrangement operations. Its artificial-intelligence (AI) contribution is a reaction generator that extends a standard Graph Isomorphism Network with Edges (GINE) architecture through reaction-context embeddings, reaction branching & third-body reaction inputs, Arrhenius-rate-parameter prediction, pairwise decoding, and stochastic inference over evolving reactant pools. Trained on the Li–Dryer hydrogen combustion kinetic model (8 species and 21 reactions), the GNN reproduces trained chemistry and generates element-balanced new reactions and intermediate species outside the training dataset, many of which have experimental analogues. When trained on a subset of the Li–Dryer dataset, the model recovered most held-out reactions and revealed relationships between samples (reactions) in the model’s latent space. The results suggest that the model learns transferable local reaction structures and generates valid species and reactions. As with any reaction generators, the generated reaction models require thermochemical and kinetic verification; the intended engineering application is low-cost reaction-pathway exploration for new fuels and prioritization of experiments and first-principles calculations to develop new combustion kinetic models.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010767/v2
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment
- **Concise summary:** This v2 preprint record describes an atom-conserving graph neural network for interpretable combustion kinetic model generation, also captured as v1 on October 21.
- **Why it matters:** Preserving atom balance in graph-based reaction proposals addresses a basic chemical constraint while supporting model generation.
- **Caveat:** This is a versioned preprint capture; it is retained separately from v1, and its claims are not independently verified.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15010767/v2); analysis based only on captured metadata, not independently verified full text.
