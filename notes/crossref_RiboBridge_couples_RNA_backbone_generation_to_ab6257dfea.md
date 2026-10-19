---
title: RiboBridge couples RNA backbone generation to sequence design through a learned
  interaction topology
type: paper
source: https://doi.org/10.64898/2026.10.15.759394
canonical_url: https://doi.org/10.64898/2026.10.15.759394
captured_by: auto-scanner
date: '2026-10-19'
captured_at: '2026-10-19T10:27:53+00:00'
last_requested: '2026-10-19T10:27:53+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Zhiqi Ma
- Yefeng Zheng
published: '2026-10-19'
abstract: Designing ribonucleic acid (RNA) molecules with prescribed structures and
  functions is central to RNA engineering. Backbone-first approaches generate three-dimensional
  geometry before assigning a nucleotide sequence, yet leave open how that geometry
  should be represented for downstream sequence design. Here we introduce RiboBridge,
  which infers a probabilistic residue-pair state from backbone geometry, recycles
  binary pair probabilities through a second pass and transfers binary and typed signals
  as soft attention biases for sequence decoding. On 550 generated backbones, pair-type
  decoding achieved joint refolding validity of 0.451 versus 0.335 for an architecture-matched
  topology-free decoder. On a matched 110-backbone intervention cohort, replacing
  aligned pair states with exact-length donors matched on pair-state statistics reduced
  joint validity from 0.464 to 0.214, showing backbone alignment matters. Pair-confidence
  ranking enriched the joint-validity rate from 0.451 overall to 0.596 among the top
  248 before external refolding, with the same ranking signal transferring to independently
  generated RFDpoly and RNA-FrameFlow backbones. On 53 experimentally determined backbones,
  pair-coupled decoding improved secondary-structure agreement relative to residue-wise
  argmax. These results support a learned relational interface between sequence-free
  backbone generation and sequence design.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.64898/2026.10.15.759394
  journal: ''
  publisher: openRxiv
  type: posted-content
  subjects: []
---

# RiboBridge couples RNA backbone generation to sequence design through a learned interaction topology

- **Type:** paper
- **Source:** https://doi.org/10.64898/2026.10.15.759394
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Zhiqi Ma, Yefeng Zheng
- **Published:** 2026-10-19

## Summary
Designing ribonucleic acid (RNA) molecules with prescribed structures and functions is central to RNA engineering. Backbone-first approaches generate three-dimensional geometry before assigning a nucleotide sequence, yet leave open how that geometry should be represented for downstream sequence design. Here we introduce RiboBridge, which infers a probabilistic residue-pair state from backbone geometry, recycles binary pair probabilities through a second pass and transfers binary and typed signals as soft attention biases for sequence decoding. On 550 generated backbones, pair-type decoding achieved joint refolding validity of 0.451 versus 0.335 for an architecture-matched topology-free decoder. On a matched 110-backbone intervention cohort, replacing aligned pair states with exact-length donors matched on pair-state statistics reduced joint validity from 0.464 to 0.214, showing backbone alignment matters. Pair-confidence ranking enriched the joint-validity rate from 0.451 overall to 0.596 among the top 248 before external refolding, with the same ranking signal transferring to independently generated RFDpoly and RNA-FrameFlow backbones. On 53 experimentally determined backbones, pair-coupled decoding improved secondary-structure agreement relative to residue-wise argmax. These results support a learned relational interface between sequence-free backbone generation and sequence design.

## Provider details
- **Doi:** 10.64898/2026.10.15.759394
- **Publisher:** openRxiv
- **Type:** posted-content
