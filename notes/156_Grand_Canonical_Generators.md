---
title: Grand Canonical Generators
type: arxiv
source: https://arxiv.org/abs/2610.00683
canonical_url: https://arxiv.org/abs/2610.00683
captured_by: sandipde
date: '2026-10-17'
captured_at: '2026-10-17T08:44:46+00:00'
last_requested: '2026-10-17T08:44:46+00:00'
issue: '156'
status: to-read
authors:
- Andreas Burger
- Malte Franke
- Luka Mucko
- Kjell Jorner
- Alan Aspuru-Guzik
published: '2026-09-30'
abstract: We introduce Grand Canonical Generators (GCG), a generative framework that
  extends Boltzmann generators to the grand canonical ensemble. We present two designs.
  The first conditions a variable-size generative model on the chemical potential,
  sampling particle number and configuration jointly. The second factorizes the grand
  canonical distribution into a particle-number distribution and the corresponding
  canonical Boltzmann density. This factorized formulation can use any existing Boltzmann
  generator for the canonical component, encodes the known linear chemical-potential
  dependence analytically, and yields a tractable likelihood that supports self-normalized
  importance sampling (SNIS). Empirically, GCG accurately reproduces grand canonical
  observables on a Lennard--Jones fluid and methane adsorption in a zeolite, demonstrating
  generalization across chemical potentials and correction via SNIS and grand canonical
  Monte Carlo.
metadata_provider: arXiv
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [boltzmann-generators, grand-canonical-ensemble, adsorption]
provider_data:
  arxiv_id: '2610.00683'
  categories:
  - cs.LG
  - stat.ML
  primary_category: cs.LG
  updated: '2026-10-06T14:08:53Z'
  doi: ''
---

# Grand Canonical Generators

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.00683
- **Captured by:** @sandipde
- **Metadata:** complete (arXiv)
- **Authors:** Andreas Burger, Malte Franke, Luka Mucko, Kjell Jorner, Alan Aspuru-Guzik
- **Published:** 2026-09-30

## Summary
We introduce Grand Canonical Generators (GCG), a generative framework that extends Boltzmann generators to the grand canonical ensemble. We present two designs. The first conditions a variable-size generative model on the chemical potential, sampling particle number and configuration jointly. The second factorizes the grand canonical distribution into a particle-number distribution and the corresponding canonical Boltzmann density. This factorized formulation can use any existing Boltzmann generator for the canonical component, encodes the known linear chemical-potential dependence analytically, and yields a tractable likelihood that supports self-normalized importance sampling (SNIS). Empirically, GCG accurately reproduces grand canonical observables on a Lennard--Jones fluid and methane adsorption in a zeolite, demonstrating generalization across chemical potentials and correction via SNIS and grand canonical Monte Carlo.

## Provider details
- **Arxiv Id:** 2610.00683
- **Categories:** ["cs.LG", "stat.ML"]
- **Primary Category:** cs.LG
- **Updated:** 2026-10-06T14:08:53Z

## AI enrichment

- **Concise summary:** Grand Canonical Generators sample particle counts and configurations either jointly or through a factorized particle-number and canonical-density model. The abstract reports tests on a Lennard-Jones fluid and methane adsorption in a zeolite with importance-sampling correction.
- **Why it matters:** Variable particle number directly addresses adsorption ensembles that fixed-size configuration generators cannot represent without additional machinery.
- **Caveat:** This preprint's examples do not establish amorphous-solid generation, and reported ensemble accuracy has not been independently checked.
- **Evidence:** [Captured source](https://arxiv.org/abs/2610.00683); analysis based only on captured metadata, not independently verified full text.
