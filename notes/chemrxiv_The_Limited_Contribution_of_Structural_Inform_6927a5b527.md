---
title: The Limited Contribution of Structural Information Relative to Language-Model
  Signal in Data-Limited Cryptic Pocket Prediction
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011675/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011675/v1
captured_by: auto-scanner
date: '2026-11-05'
captured_at: '2026-11-05T12:53:59+00:00'
last_requested: '2026-11-05T12:53:59+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Emmanuel Brown
- Phenil Shah
published: '2026-11-04'
abstract: 'Cryptic pockets, drug-binding sites absent from a protein’s static structure
  but exposed through conformational change, expand the scope of druggable targets,
  yet remain difficult to identify computationally. PocketMiner, a structure-based
  graph neural network trained on molecular dynamics simulation data, predicts cryptic
  pocket formation from a single static structure (ROC-AUC 0.87). Recent protein language
  model (PLM)-based approaches report further improvements over this structure-only
  baseline (up to 0.93), but do so by simultaneously replacing the structural architecture
  with a sequence-only model and switching to substantially larger, differently-sourced
  training data–leaving it unclear whether these gains stem from the languagemodel
  signal itself or from increased training data scale. We isolate this variable directly:
  holding architecture family and PocketMiner’s original, small molecular-dynamics-derived
  training set fixed, we compare three matched variants–geometry-only (baseline),
  ESM2 embeddings only, and both combined (fused)–under identical training conditions.
  The geometry-only baseline achieves chance-level test performance (ROC-AUC 0.498),
  while both the ESM2-only (0.817) and fused (0.835) variants perform far above it,
  with statistically indistinguishable confidence intervals between the two, indicating
  that language-model signal alone accounts for nearly all of the achievable performance,
  and that structural information contributes marginally under these conditions. This
  result is confirmed on CryptoBench, an independent, larger benchmark (baseline 0.494
  vs. fused 0.716, non-overlapping confidence intervals), and holds consistently across
  every pocket-formation mechanism examined in a stratified analysis. These findings
  suggest that a substantial share of the improvement reported by prior sequence-based
  methods is attributable to language-model signal itself rather than training data
  scale, with implications for data-efficient strategies in structure-based pocket
  prediction more broadly.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011675/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# The Limited Contribution of Structural Information Relative to Language-Model Signal in Data-Limited Cryptic Pocket Prediction

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011675/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Emmanuel Brown, Phenil Shah
- **Published:** 2026-11-04

## Summary
Cryptic pockets, drug-binding sites absent from a protein’s static structure but exposed through conformational change, expand the scope of druggable targets, yet remain difficult to identify computationally. PocketMiner, a structure-based graph neural network trained on molecular dynamics simulation data, predicts cryptic pocket formation from a single static structure (ROC-AUC 0.87). Recent protein language model (PLM)-based approaches report further improvements over this structure-only baseline (up to 0.93), but do so by simultaneously replacing the structural architecture with a sequence-only model and switching to substantially larger, differently-sourced training data–leaving it unclear whether these gains stem from the languagemodel signal itself or from increased training data scale. We isolate this variable directly: holding architecture family and PocketMiner’s original, small molecular-dynamics-derived training set fixed, we compare three matched variants–geometry-only (baseline), ESM2 embeddings only, and both combined (fused)–under identical training conditions. The geometry-only baseline achieves chance-level test performance (ROC-AUC 0.498), while both the ESM2-only (0.817) and fused (0.835) variants perform far above it, with statistically indistinguishable confidence intervals between the two, indicating that language-model signal alone accounts for nearly all of the achievable performance, and that structural information contributes marginally under these conditions. This result is confirmed on CryptoBench, an independent, larger benchmark (baseline 0.494 vs. fused 0.716, non-overlapping confidence intervals), and holds consistently across every pocket-formation mechanism examined in a stratified analysis. These findings suggest that a substantial share of the improvement reported by prior sequence-based methods is attributable to language-model signal itself rather than training data scale, with implications for data-efficient strategies in structure-based pocket prediction more broadly.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011675/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
