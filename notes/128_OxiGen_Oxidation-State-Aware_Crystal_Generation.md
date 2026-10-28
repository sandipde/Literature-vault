---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [crystal-generation, diffusion-models, oxidation-states, charge-neutrality]
title: 'OxiGen: Oxidation-State-Aware Crystal Generation'
type: arxiv
source: https://arxiv.org/abs/2610.08296
canonical_url: https://arxiv.org/abs/2610.08296
captured_by: sandipde
date: '2026-10-12'
captured_at: '2026-10-12T14:52:44+00:00'
last_requested: '2026-10-12T14:52:44+00:00'
issue: '128'
status: to-read
authors:
- Dylan John
- Kim E. Jelfs
- Alex M. Ganose
- Eleonora Giunchiglia
published: '2026-10-06'
abstract: Generative models have the potential to accelerate inorganic materials discovery
  by enabling inverse design, but generating experimentally realisable crystals remains
  challenging. Oxidation states are widely used to assess the compositional validity
  of crystals and guide inorganic materials discovery. While existing generative models
  for crystals can generate materials with charge-neutral oxidation-state assignments,
  they poorly reproduce the distributions of oxidation states observed in synthesised
  materials. To address this limitation, we propose OxiGen, an oxidation-state-aware
  crystal diffusion model that explicitly represents oxidation states during generation.
  OxiGen enforces global charge neutrality by construction using a structured output
  layer with exact inference over a finite-state automaton. Empirically, OxiGen substantially
  improves oxidation-state fidelity, generates the highest rate of stable, unique,
  and novel crystals among evaluated methods, and maintains high compositional validity
  even under property conditioning.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.08296'
  categories:
  - cs.LG
  - cond-mat.mtrl-sci
  primary_category: cs.LG
  updated: '2026-10-06T13:01:35Z'
  doi: ''
---

# OxiGen: Oxidation-State-Aware Crystal Generation

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.08296
- **Captured by:** @sandipde
- **Metadata:** complete (arXiv)
- **Authors:** Dylan John, Kim E. Jelfs, Alex M. Ganose, Eleonora Giunchiglia
- **Published:** 2026-10-06

## Summary
Generative models have the potential to accelerate inorganic materials discovery by enabling inverse design, but generating experimentally realisable crystals remains challenging. Oxidation states are widely used to assess the compositional validity of crystals and guide inorganic materials discovery. While existing generative models for crystals can generate materials with charge-neutral oxidation-state assignments, they poorly reproduce the distributions of oxidation states observed in synthesised materials. To address this limitation, we propose OxiGen, an oxidation-state-aware crystal diffusion model that explicitly represents oxidation states during generation. OxiGen enforces global charge neutrality by construction using a structured output layer with exact inference over a finite-state automaton. Empirically, OxiGen substantially improves oxidation-state fidelity, generates the highest rate of stable, unique, and novel crystals among evaluated methods, and maintains high compositional validity even under property conditioning.

## Provider details
- **Arxiv Id:** 2610.08296
- **Categories:** ["cs.LG", "cond-mat.mtrl-sci"]
- **Primary Category:** cs.LG
- **Updated:** 2026-10-06T13:01:35Z

## AI enrichment
- **Concise summary:** OxiGen represents oxidation states explicitly in a crystal diffusion model and uses finite-state-automaton inference to enforce global charge neutrality.
- **Why it matters:** Moving beyond merely valid charge assignments toward experimentally observed oxidation-state distributions offers a chemically informed constraint for generative crystal design, not a force-field model.
- **Caveat:** The arXiv abstract reports superior stability, uniqueness, and novelty rates without captured benchmark details or independent verification.
- **Evidence:** [Captured source](https://arxiv.org/abs/2610.08296); analysis based only on captured metadata, not independently verified full text.
