---
title: Exchange–Correlation Functional Screening and Development of a High Dimensional
  Neural Network Interatomic Potential for UO2
type: paper
source: https://doi.org/10.24200/jonra.2026.2052.1242
canonical_url: https://doi.org/10.24200/jonra.2026.2052.1242
captured_by: auto-scanner
date: '2026-10-13'
captured_at: '2026-10-13T12:25:46+00:00'
last_requested: '2026-10-13T12:25:46+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Mahmoud Payami Shabestar
- Samira Sheykhi
- Mohammad Reza Basaadat
published: '2027-02-01'
abstract: ''
metadata_provider: Crossref
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-public-source-recovery
enrichment_category: ML interatomic potentials
enrichment_tags: [uranium-dioxide, neural-potentials, active-learning]
recovery_status: recovered
recovery_checked_on: '2026-10-28'
provider_data:
  doi: 10.24200/jonra.2026.2052.1242
  journal: Journal of  Nuclear Research and Applications
  publisher: SCI AND TECH UNIVERSAL INC
  type: journal-article
  subjects: []
---

# Exchange–Correlation Functional Screening and Development of a High Dimensional Neural Network Interatomic Potential for UO2

- **Type:** paper
- **Source:** https://doi.org/10.24200/jonra.2026.2052.1242
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Mahmoud Payami Shabestar, Samira Sheykhi, Mohammad Reza Basaadat
- **Published:** 2027-02-01

## Provider details
- **Doi:** 10.24200/jonra.2026.2052.1242
- **Journal:** Journal of  Nuclear Research and Applications
- **Publisher:** SCI AND TECH UNIVERSAL INC
- **Type:** journal-article

## Source recovery

- **Checked on:** 2026-10-28.
- **Retrieved sources:** https://doi.org/10.24200/jonra.2026.2052.1242 ; https://jonra.nstri.ir/article_1820.html
- **Outcome:** The publisher abstract describes an actively learned Behler-Parrinello potential for UO2 using variable-cell Quantum ESPRESSO trajectories and LAMMPS deployment. Its reference models the paramagnetic state with non-spin-polarized DFT without Hubbard U; reported elastic-constant discrepancies are 2-17%.
- **Limitations:** Abstract recovery only; no independent testing of the reference approximation, irradiation behavior, or reported errors.

## AI enrichment

- **Concise summary:** The recovered abstract develops a UO2 high-dimensional neural potential from actively selected DFT trajectories and tests lattice and elastic properties.
- **Why it matters:** The chosen electronic-structure reference is central to what the surrogate can reproduce, especially for a correlated oxide.
- **Caveat:** Small held-out regression errors do not validate non-spin-polarized, no-U reference physics or establish accuracy for irradiation defects.
- **Evidence:** [Captured source](https://doi.org/10.24200/jonra.2026.2052.1242); [recovered publisher abstract](https://jonra.nstri.ir/article_1820.html), retrieved 2026-10-28; no independent full-text or performance verification.
