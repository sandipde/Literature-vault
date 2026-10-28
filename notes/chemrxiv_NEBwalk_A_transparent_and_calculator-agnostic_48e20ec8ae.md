---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: ML interatomic potentials
enrichment_tags: [nudged-elastic-band, reproducible-workflows, transition-states, dft-validation]
title: 'NEBwalk: A transparent and calculator-agnostic framework for reproducible
  nudged elastic band workflows with machine-learned potentials and firstprinciples
  calculators'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010372/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15010372/v1
captured_by: auto-scanner
date: '2026-10-13'
captured_at: '2026-10-13T21:42:05+00:00'
last_requested: '2026-10-13T21:42:05+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Md. Rifat Khandaker
- Ali Ghiami-Shomami
- Mohammad Asaduzzaman Chowdhury
published: '2026-10-13'
abstract: 'The nudged elastic band (NEB) method is established, but a reproducible
  transition-state calculation requires more than the NEB equations. Path construction,
  calculator isolation, restart behaviour, convergence monitoring, provenance, failure
  handling, and the transfer from inexpensive potentials to first-principles checks
  must remain consistent throughout the workflow. We developed NEBwalk as an open-source,
  calculator-agnostic Python framework for NEB and climbing-image NEB (CI-NEB) calculations
  built around the Atomic Simulation Environment (ASE). NEBwalk v0.11.0 supports improved-tangent
  NEB forces, variable springs, FIRE optimisation, minimum-image-aware periodic geometry,
  linear, IDPP, and regularized geodesic-style interpolation, restartable runs, structured
  result export, fresh calculator construction for each image, MLIP-assisted image
  selection, DFT-labelled data export, an optional MACE fine-tuning and evaluation
  handoff, resumable campaign infrastructure, reproducibility bundles, and conservative
  Quantum ESPRESSO recovery logic. A September 2026 audit re-examined 20 historical
  system-calculator cases rather than treating old documentation as automatically
  valid: 13 were re-audited and reconfirmed from surviving output artefacts, while
  7 are retained only as historical provenance and excluded from the current quantitative
  validation claim. Ten artefact-backed vacancy-migration cases also have DOI-traceable
  literature comparators for the same element, crystal structure, and migration-hop
  class; because the numerical settings differ, we use these only as physical-scale
  checks. In two matched-physical-input implementation tests, NEBwalk and ASE differ
  by no more than 0.04 meV in the barrier and about 0.002 Å in the converged path
  geometry. A MACEMP-0 H/Cu(111) calculation gives a converged fcc-to-hcp barrier
  of about 0.126 eV, close to published DFT values of about 0.13-0.15 eV, although
  the literature itself disagrees on the sign of the small fcc-hcp site splitting.
  NEBwalk is therefore not presented as a new NEB algorithm or as a replacement for
  ASE or first-principles engines. Its role is to keep path optimisation, MLIP screening,
  DFT validation, reproducibility, and failure-aware execution in one inspectable
  workflow.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010372/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# NEBwalk: A transparent and calculator-agnostic framework for reproducible nudged elastic band workflows with machine-learned potentials and firstprinciples calculators

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010372/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Md. Rifat Khandaker, Ali Ghiami-Shomami, Mohammad Asaduzzaman Chowdhury
- **Published:** 2026-10-13

## Summary
The nudged elastic band (NEB) method is established, but a reproducible transition-state calculation requires more than the NEB equations. Path construction, calculator isolation, restart behaviour, convergence monitoring, provenance, failure handling, and the transfer from inexpensive potentials to first-principles checks must remain consistent throughout the workflow. We developed NEBwalk as an open-source, calculator-agnostic Python framework for NEB and climbing-image NEB (CI-NEB) calculations built around the Atomic Simulation Environment (ASE). NEBwalk v0.11.0 supports improved-tangent NEB forces, variable springs, FIRE optimisation, minimum-image-aware periodic geometry, linear, IDPP, and regularized geodesic-style interpolation, restartable runs, structured result export, fresh calculator construction for each image, MLIP-assisted image selection, DFT-labelled data export, an optional MACE fine-tuning and evaluation handoff, resumable campaign infrastructure, reproducibility bundles, and conservative Quantum ESPRESSO recovery logic. A September 2026 audit re-examined 20 historical system-calculator cases rather than treating old documentation as automatically valid: 13 were re-audited and reconfirmed from surviving output artefacts, while 7 are retained only as historical provenance and excluded from the current quantitative validation claim. Ten artefact-backed vacancy-migration cases also have DOI-traceable literature comparators for the same element, crystal structure, and migration-hop class; because the numerical settings differ, we use these only as physical-scale checks. In two matched-physical-input implementation tests, NEBwalk and ASE differ by no more than 0.04 meV in the barrier and about 0.002 Å in the converged path geometry. A MACEMP-0 H/Cu(111) calculation gives a converged fcc-to-hcp barrier of about 0.126 eV, close to published DFT values of about 0.13-0.15 eV, although the literature itself disagrees on the sign of the small fcc-hcp site splitting. NEBwalk is therefore not presented as a new NEB algorithm or as a replacement for ASE or first-principles engines. Its role is to keep path optimisation, MLIP screening, DFT validation, reproducibility, and failure-aware execution in one inspectable workflow.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010372/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment
- **Concise summary:** NEBwalk wraps ASE-based NEB calculations in restartable, provenance-aware workflows linking MLIP screening with first-principles checks and optional MACE fine-tuning. Its audit distinguishes reconfirmed cases from historical records lacking sufficient surviving artifacts.
- **Why it matters:** Calculator isolation, restart behavior, and explicit failure handling can matter as much as optimizer choice for reproducible barrier calculations.
- **Caveat:** The preprint does not claim a new NEB algorithm; tiny implementation differences and literature-scale comparisons do not establish universal physical accuracy or validate the seven excluded historical cases.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15010372/v1); analysis based only on captured metadata, not independently verified full text.
