---
title: Bond-informed search for ordered configurations in multi-principal element
  alloys
type: arxiv
source: https://arxiv.org/html/2610.21718v1
canonical_url: https://arxiv.org/abs/2610.21718
captured_by: sandipde
date: '2026-10-21'
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [alloy-ordering, monte-carlo, interatomic-models]
captured_at: '2026-10-21T10:39:56+00:00'
last_requested: '2026-10-21T10:39:56+00:00'
issue: '173'
status: to-read
authors:
- Gaurav Arora
- Alex Tai
- Rodrigo Freitas
- David Cereceda
published: '2026-10-15'
abstract: Ordered configurations in multi-principal element alloys (MPEAs) control
  their local structure and influence a broad range of mechanical and thermodynamic
  properties. Yet they are notoriously difficult to identify. Locating low-energy
  ordered candidates requires exploring a configurational space that grows combinatorially
  with the number of elements, and Monte Carlo searches driven by density-functional
  theory (DFT) need a new electronic-structure calculation at every trial step. Here
  we introduce MECx (Minimum Energy Configuration eXplorer), a framework that guides
  Monte Carlo searches with a surrogate energy model trained on configurations stratified
  in bond-count space. Applied to ternary, quaternary, and quinary BCC alloys using
  compact training sets of 100 DFT-labeled configurations, MECx identifies ordered
  configurations with lower energies than those found by direct DFT-based Monte Carlo
  within practical computational limits. These configurations exhibit distinct pair-specific
  ordering, including B2- and B32-like motifs, and undergo progressive disordering
  as temperature increases. The MPEA-trained models also transfer to selected binary
  subsystems without retraining. The resulting ordered configurations agree with those
  obtained by direct DFT-based Monte Carlo and produce experimentally distinguishable
  superlattice reflections in simulated neutron diffraction patterns.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.21718'
  categories:
  - cond-mat.mtrl-sci
  primary_category: cond-mat.mtrl-sci
  updated: '2026-10-15T11:37:40Z'
  doi: ''
---

# Bond-informed search for ordered configurations in multi-principal element alloys

- **Type:** arxiv
- **Source:** https://arxiv.org/html/2610.21718v1
- **Captured by:** @sandipde
- **Metadata:** complete (arXiv)
- **Authors:** Gaurav Arora, Alex Tai, Rodrigo Freitas, David Cereceda
- **Published:** 2026-10-15

## Summary
Ordered configurations in multi-principal element alloys (MPEAs) control their local structure and influence a broad range of mechanical and thermodynamic properties. Yet they are notoriously difficult to identify. Locating low-energy ordered candidates requires exploring a configurational space that grows combinatorially with the number of elements, and Monte Carlo searches driven by density-functional theory (DFT) need a new electronic-structure calculation at every trial step. Here we introduce MECx (Minimum Energy Configuration eXplorer), a framework that guides Monte Carlo searches with a surrogate energy model trained on configurations stratified in bond-count space. Applied to ternary, quaternary, and quinary BCC alloys using compact training sets of 100 DFT-labeled configurations, MECx identifies ordered configurations with lower energies than those found by direct DFT-based Monte Carlo within practical computational limits. These configurations exhibit distinct pair-specific ordering, including B2- and B32-like motifs, and undergo progressive disordering as temperature increases. The MPEA-trained models also transfer to selected binary subsystems without retraining. The resulting ordered configurations agree with those obtained by direct DFT-based Monte Carlo and produce experimentally distinguishable superlattice reflections in simulated neutron diffraction patterns.

## Provider details
- **Arxiv Id:** 2610.21718
- **Categories:** ["cond-mat.mtrl-sci"]
- **Primary Category:** cond-mat.mtrl-sci
- **Updated:** 2026-10-15T11:37:40Z

## AI enrichment
- **Concise summary:** The abstract describes MECx, which uses a bond-count-stratified surrogate to guide searches for ordered configurations in multi-principal element alloys.
- **Why it matters:** The approach targets the cost of exploring large alloy configuration spaces with repeated first-principles calculations.
- **Caveat:** This is a preprint abstract; reported comparisons and transfer behavior are not independently verified here.
- **Evidence:** [Captured source](https://arxiv.org/html/2610.21718v1); analysis based only on captured metadata, not independently verified full text.
