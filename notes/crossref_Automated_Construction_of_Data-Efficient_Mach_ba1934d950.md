---
title: Automated Construction of Data-Efficient Machine-Learned Force Fields for Polymers
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15012033/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15012033/v1
captured_by: auto-scanner
date: '2026-11-12'
captured_at: '2026-11-12T13:29:56+00:00'
last_requested: '2026-11-12T13:29:56+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Tobias Henkes
- Alexandre Tkatchenko
- Igor Poltavsky
published: '2026-11-12'
abstract: General-purpose machine-learned force fields (GP-MLFFs) provide near-first-principles
  accuracy across broad chemical spaces, but their reliability is limited by training
  coverage and reference level of quantum mechanics. We present an automated active-learning
  workflow using the open-source package aims-PAX that builds on GP-MLFF sampling
  to generate targeted, higher-accuracy reference data for fine-tuning or training
  models with task-specific architectures. We demonstrate this approach by training
  a single model on approximately 4,000 hybrid-DFT structures spanning seven chemically
  distinct polymers. The model predicts densities and glass-transition temperatures
  with accuracy comparable to GP-MLFFs trained on hundreds to thousands of times more
  data, supports stable molecular dynamics of approximately 10,000 atoms, and transfers
  to unseen polymers. An explicit dispersion term is indispensable in this low-data
  regime, providing the inter-chain cohesion that GP-MLFFs must otherwise learn implicitly
  from large datasets. Replay fine-tuning extends the model to silicon-containing
  polydimethylsiloxane while preserving accuracy on the original polymers. Beyond
  collective properties, the aims-PAX model better describes the local response to
  hydrogen bonding. The model reproduces experimentally observed frequency shifts
  of the nylon-6 amide group, which a polymer-specific GP-MLFF captures only partially,
  and their cooperative enhancement along hydrogen-bonded chains, which a classical
  force field cannot represent. These results establish aims-PAX as a data-efficient
  route from general-purpose sampling to specialized MLFFs, combining targeted chemical
  coverage, suitable architectures, and the reference accuracy the problem requires.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15012033/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Automated Construction of Data-Efficient Machine-Learned Force Fields for Polymers

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15012033/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Tobias Henkes, Alexandre Tkatchenko, Igor Poltavsky
- **Published:** 2026-11-12

## Summary
General-purpose machine-learned force fields (GP-MLFFs) provide near-first-principles accuracy across broad chemical spaces, but their reliability is limited by training coverage and reference level of quantum mechanics. We present an automated active-learning workflow using the open-source package aims-PAX that builds on GP-MLFF sampling to generate targeted, higher-accuracy reference data for fine-tuning or training models with task-specific architectures. We demonstrate this approach by training a single model on approximately 4,000 hybrid-DFT structures spanning seven chemically distinct polymers. The model predicts densities and glass-transition temperatures with accuracy comparable to GP-MLFFs trained on hundreds to thousands of times more data, supports stable molecular dynamics of approximately 10,000 atoms, and transfers to unseen polymers. An explicit dispersion term is indispensable in this low-data regime, providing the inter-chain cohesion that GP-MLFFs must otherwise learn implicitly from large datasets. Replay fine-tuning extends the model to silicon-containing polydimethylsiloxane while preserving accuracy on the original polymers. Beyond collective properties, the aims-PAX model better describes the local response to hydrogen bonding. The model reproduces experimentally observed frequency shifts of the nylon-6 amide group, which a polymer-specific GP-MLFF captures only partially, and their cooperative enhancement along hydrogen-bonded chains, which a classical force field cannot represent. These results establish aims-PAX as a data-efficient route from general-purpose sampling to specialized MLFFs, combining targeted chemical coverage, suitable architectures, and the reference accuracy the problem requires.

## Provider details
- **Doi:** 10.26434/chemrxiv.15012033/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
