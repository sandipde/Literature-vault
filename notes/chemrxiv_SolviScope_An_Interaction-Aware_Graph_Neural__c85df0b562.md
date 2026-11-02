---
title: 'SolviScope: An Interaction-Aware Graph Neural Network for Solvent Ranking
  of Small Organic Molecules in Pure and Multicomponent Solvent Systems'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011474/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011474/v1
captured_by: auto-scanner
date: '2026-11-02'
captured_at: '2026-11-02T13:02:05+00:00'
last_requested: '2026-11-02T13:02:05+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Maansi Jain
- Ayan Kashyap
- Chanukya Nanduru
- Antarip Halder
published: '2026-11-02'
abstract: Selecting effective solvents and antisolvents requires navigating vast chemical,
  composition, and temperature spaces where exhaustive experimentation is prohibitively
  costly and low average regression errors do not guarantee that the best candidates
  appear within a short experimental screen. We introduce SolviScope, a graph neural
  network framework for solubility prediction and solvent ranking in pure and binary
  solvent systems. SolviScope-Pure combines a two-dimensional gated graph encoder
  with intermolecular cross-attention, avoiding three-dimensional conformer generation.
  SolviScope-Binary integrates hierarchical message passing with Kamlet–Taft and Hansen
  descriptors and temperature–composition conditioning. Both models use explicit ranking
  objectives. SolviScope-Pure achieves a molar logS root-mean-square error of 0.77
  on a 7,264-measurement structural hold-out set, lower errors than FastSolv on two
  overlap-filtered external benchmarks, and better solvent-ranking correlations for
  8 of 10 industrially relevant solutes. Across two industrial mixture benchmarks
  comprising 13 solutes, SolviScope-Binary achieves per-solute Spearman’s ρ of 0.51–0.91
  and recovers the experimentally most and least soluble systems within its top-five
  and bottom-five predictions for every solute. Retrospective studies of two unseen
  APIs further demonstrate solvent/antisolvent prioritization and correct composition
  ordering in solvent–water mixtures. Cooling-crystallization assessments reveal that
  successful isothermal ranking does not establish reliable cooling-drop ranking or
  quantitative working-capacity prediction. These results support SolviScope as a
  tool for prioritizing experimental solvent screens, with prospective validation
  needed to establish broader applicability and experimental savings.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011474/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# SolviScope: An Interaction-Aware Graph Neural Network for Solvent Ranking of Small Organic Molecules in Pure and Multicomponent Solvent Systems

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011474/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Maansi Jain, Ayan Kashyap, Chanukya Nanduru, Antarip Halder
- **Published:** 2026-11-02

## Summary
Selecting effective solvents and antisolvents requires navigating vast chemical, composition, and temperature spaces where exhaustive experimentation is prohibitively costly and low average regression errors do not guarantee that the best candidates appear within a short experimental screen. We introduce SolviScope, a graph neural network framework for solubility prediction and solvent ranking in pure and binary solvent systems. SolviScope-Pure combines a two-dimensional gated graph encoder with intermolecular cross-attention, avoiding three-dimensional conformer generation. SolviScope-Binary integrates hierarchical message passing with Kamlet–Taft and Hansen descriptors and temperature–composition conditioning. Both models use explicit ranking objectives. SolviScope-Pure achieves a molar logS root-mean-square error of 0.77 on a 7,264-measurement structural hold-out set, lower errors than FastSolv on two overlap-filtered external benchmarks, and better solvent-ranking correlations for 8 of 10 industrially relevant solutes. Across two industrial mixture benchmarks comprising 13 solutes, SolviScope-Binary achieves per-solute Spearman’s ρ of 0.51–0.91 and recovers the experimentally most and least soluble systems within its top-five and bottom-five predictions for every solute. Retrospective studies of two unseen APIs further demonstrate solvent/antisolvent prioritization and correct composition ordering in solvent–water mixtures. Cooling-crystallization assessments reveal that successful isothermal ranking does not establish reliable cooling-drop ranking or quantitative working-capacity prediction. These results support SolviScope as a tool for prioritizing experimental solvent screens, with prospective validation needed to establish broader applicability and experimental savings.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011474/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
