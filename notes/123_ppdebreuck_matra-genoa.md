---
title: ppdebreuck/matra-genoa
type: github
source: https://github.com/ppdebreuck/matra-genoa
canonical_url: https://github.com/ppdebreuck/matra-genoa
captured_by: sandipde
date: '2026-10-11'
captured_at: '2026-10-11T18:03:44+00:00'
last_requested: '2026-10-11T18:03:44+00:00'
issue: '123'
status: to-read
authors: []
published: ''
abstract: ''
metadata_provider: GitHub
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-public-source-recovery
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [crystal-generation, transformers, wyckoff-representation]
recovery_status: recovered
recovery_checked_on: '2026-10-28'
provider_data:
  description: null
  language: Python
  topics: []
  license: NOASSERTION
  stars: 5
  forks: 0
  open_issues: 0
  created_at: '2025-09-17T12:43:47Z'
  pushed_at: '2026-09-14T10:14:29Z'
  default_branch: main
---

# ppdebreuck/matra-genoa

- **Type:** github
- **Source:** https://github.com/ppdebreuck/matra-genoa
- **Captured by:** @sandipde
- **Metadata:** complete (GitHub)

## Provider details
- **Language:** Python
- **License:** NOASSERTION
- **Stars:** 5
- **Forks:** 0
- **Open Issues:** 0
- **Created At:** 2025-09-17T12:43:47Z
- **Pushed At:** 2026-09-14T10:14:29Z
- **Default Branch:** main

## Source recovery

- **Checked on:** 2026-10-28.
- **Retrieved source:** https://github.com/ppdebreuck/matra-genoa
- **Outcome:** The public README describes a generative material transformer using an invertible, symmetry-aware crystal representation, conditioned on composition, stability, space groups, and Wyckoff positions. It recommends relaxing generated structures with a separate universal ML interatomic potential.
- **Limitations:** README evidence only; no code execution or independent evaluation. This is crystal generation, not demonstrated amorphous generation or a force field.

## AI enrichment

- **Concise summary:** Matra-Genoa generates symmetry-aware crystal structures with a tokenized transformer representation. The recovered README separates generation from subsequent MLIP relaxation.
- **Why it matters:** It offers a concrete symmetry-constrained generative workflow to compare with approaches intended for disordered structures.
- **Caveat:** The original capture lacks an abstract; the README does not establish applicability to amorphous materials or validate generated structures.
- **Evidence:** [Captured source](https://github.com/ppdebreuck/matra-genoa); [retrieved README](https://github.com/ppdebreuck/matra-genoa), retrieved 2026-10-28; analysis uses captured metadata and this public source, not independently verified paper full text.
