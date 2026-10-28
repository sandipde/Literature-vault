---
title: Challenging Atomistic Foundation Models on Disordered Carbons
type: arxiv
source: https://arxiv.org/abs/2610.26701
canonical_url: https://arxiv.org/abs/2610.26701
captured_by: auto-scanner
date: '2026-10-20'
captured_at: '2026-10-20T09:46:32+00:00'
last_requested: '2026-10-20T09:46:32+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Joseph Hart
- Samuel G. H. Brookes
- Fabian L. Thiemann
- Christoph Schran
published: '2026-10-19'
abstract: Foundation machine-learned interatomic potentials (MLIPs) promise broad
  transferability, yet their out-of-domain reliability is hard to establish. Here,
  we use pure and O/H-containing disordered carbon spanning multiple phases, competing
  hybridisations and porous frameworks to stress-test six popular foundation MLIPs.
  We first screen all six on density functional theory (DFT) energy and force errors
  and binding curves, then subject four to melt-quench-anneal molecular dynamics and
  evaluate the resulting structural observables. Binding curves and O/H-containing
  trajectories reveal unphysical extrapolation and dynamical failures that low DFT
  energy and force errors fail to reveal. Of the models tested, MACE-MH-1 is the most
  consistently robust, with low DFT errors and stable MD. Despite differing architectures,
  OMAT-based models share structural biases, highlighting the importance of training
  coverage. All four models generate structures of nanoporous carbon that reproduce
  the principal experimental and specialised carbon potential signatures. Incorporating
  O/H leaves short-range order largely unchanged but shifts pore-size distributions
  towards larger pores. These results emphasise the need for application-specific
  validation and extend molecular dynamics modelling of nanoporous carbon towards
  experimentally realistic structures.
metadata_provider: arXiv
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: ML interatomic potentials
enrichment_tags: [disordered-carbon, foundation-potentials, dynamical-validation]
provider_data:
  arxiv_id: '2610.26701'
  categories:
  - physics.chem-ph
  - cond-mat.mtrl-sci
  - physics.comp-ph
---

# Challenging Atomistic Foundation Models on Disordered Carbons

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.26701
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Joseph Hart, Samuel G. H. Brookes, Fabian L. Thiemann, Christoph Schran
- **Published:** 2026-10-19

## Summary
Foundation machine-learned interatomic potentials (MLIPs) promise broad transferability, yet their out-of-domain reliability is hard to establish. Here, we use pure and O/H-containing disordered carbon spanning multiple phases, competing hybridisations and porous frameworks to stress-test six popular foundation MLIPs. We first screen all six on density functional theory (DFT) energy and force errors and binding curves, then subject four to melt-quench-anneal molecular dynamics and evaluate the resulting structural observables. Binding curves and O/H-containing trajectories reveal unphysical extrapolation and dynamical failures that low DFT energy and force errors fail to reveal. Of the models tested, MACE-MH-1 is the most consistently robust, with low DFT errors and stable MD. Despite differing architectures, OMAT-based models share structural biases, highlighting the importance of training coverage. All four models generate structures of nanoporous carbon that reproduce the principal experimental and specialised carbon potential signatures. Incorporating O/H leaves short-range order largely unchanged but shifts pore-size distributions towards larger pores. These results emphasise the need for application-specific validation and extend molecular dynamics modelling of nanoporous carbon towards experimentally realistic structures.

## Provider details
- **Arxiv Id:** 2610.26701
- **Categories:** ["physics.chem-ph", "cond-mat.mtrl-sci", "physics.comp-ph"]

## AI enrichment

- **Concise summary:** Six foundation MLIPs are screened on disordered carbon, with four tested through melt-quench-anneal dynamics. The abstract reports extrapolation failures missed by energy/force errors and identifies MACE-MH-1 as the most consistently robust tested model.
- **Why it matters:** This directly motivates validating trajectories and pore statistics for amorphous or nanoporous carbon rather than relying on near-reference regression metrics.
- **Caveat:** Structure formation here uses force-field-driven dynamics, not a learned generative structure model; the preprint's comparative ranking is domain-specific.
- **Evidence:** [Captured source](https://arxiv.org/abs/2610.26701); analysis based only on captured metadata, not independently verified full text.
