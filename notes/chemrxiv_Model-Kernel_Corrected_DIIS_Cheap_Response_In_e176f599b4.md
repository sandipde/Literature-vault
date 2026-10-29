---
title: 'Model-Kernel Corrected DIIS: Cheap Response Information for the Roothaan Step'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011121/v2
canonical_url: https://doi.org/10.26434/chemrxiv.15011121/v2
captured_by: auto-scanner
date: '2026-10-28'
captured_at: '2026-10-28T21:29:02+00:00'
last_requested: '2026-10-28T21:29:02+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Fang Sun
- Miranda Yang Li
- Hekai Cheng
- Jason Cong
- Yizhou Sun
published: '2026-10-28'
abstract: Nearly all Kohn–Sham density functional theory (DFT) and Hartree–Fock calculations
  solve the self-consistent field (SCF) equations with the direct inversion in the
  iterative subspace (DIIS). Their cost is set by the number of Fock builds that DIIS
  needs. Each DIIS cycle diagonalizes an extrapolated Fock matrix as if this matrix
  stayed fixed while the electrons move. The charge that the step moves, however,
  changes the Coulomb potential, and the next cycle has to undo part of the step.
  This charge sloshing makes DIIS slower as molecules grow. We correct every step
  with a model kernel, an inexpensive approximation of this Coulomb response that
  is built from a few Gaussian functions on each atom and contains no fitted parameters.
  The resulting method, MK-DIIS, needs no extra Fock build, converges to the same
  solution as DIIS and adds about 1% to the run time. On 170 transition-metal complexes
  and organic molecules it needs about one third fewer Fock builds than DIIS, fewer
  than any SCF algorithm of a production code that we compared with. On molecules
  with up to 300 atoms it needs about half as many, and on linear acenes its number
  of Fock builds does not grow with length. The saving is smaller with more exact
  exchange and in a continuum solvent, both of which screen the Coulomb response.
  For open-shell molecules, a delayed start keeps the reliability of DIIS. Because
  only the diagonalization step changes, the correction can be added to existing SCF
  codes and combined with other convergence aids.
metadata_provider: Crossref
metadata_status: complete
enriched_on: '2026-10-29'
enrichment_method: llm-captured-metadata
enrichment_category: Mathematics and algorithms
enrichment_tags: [scf-convergence, diis, density-functional-theory, hartree-fock]
provider_data:
  doi: 10.26434/chemrxiv.15011121/v2
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Model-Kernel Corrected DIIS: Cheap Response Information for the Roothaan Step

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011121/v2
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Fang Sun, Miranda Yang Li, Hekai Cheng, Jason Cong, Yizhou Sun
- **Published:** 2026-10-28

## Summary
Nearly all Kohn–Sham density functional theory (DFT) and Hartree–Fock calculations solve the self-consistent field (SCF) equations with the direct inversion in the iterative subspace (DIIS). Their cost is set by the number of Fock builds that DIIS needs. Each DIIS cycle diagonalizes an extrapolated Fock matrix as if this matrix stayed fixed while the electrons move. The charge that the step moves, however, changes the Coulomb potential, and the next cycle has to undo part of the step. This charge sloshing makes DIIS slower as molecules grow. We correct every step with a model kernel, an inexpensive approximation of this Coulomb response that is built from a few Gaussian functions on each atom and contains no fitted parameters. The resulting method, MK-DIIS, needs no extra Fock build, converges to the same solution as DIIS and adds about 1% to the run time. On 170 transition-metal complexes and organic molecules it needs about one third fewer Fock builds than DIIS, fewer than any SCF algorithm of a production code that we compared with. On molecules with up to 300 atoms it needs about half as many, and on linear acenes its number of Fock builds does not grow with length. The saving is smaller with more exact exchange and in a continuum solvent, both of which screen the Coulomb response. For open-shell molecules, a delayed start keeps the reliability of DIIS. Because only the diagonalization step changes, the correction can be added to existing SCF codes and combined with other convergence aids.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011121/v2
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment

- **Concise summary:** The abstract proposes correcting DIIS's Roothaan step with an inexpensive model of Coulomb response, aiming to reduce charge-sloshing-related self-consistent-field iterations without extra Fock builds.
- **Why it matters:** If validated in broader workloads, a low-overhead convergence improvement could benefit routine DFT and Hartree–Fock calculations, especially as molecular systems grow.
- **Caveat:** This is a ChemRxiv version 2 preprint. The reported Fock-build reductions, runtime overhead, scaling, and convergence behavior are author-reported; they were not independently benchmarked or reproduced.
- **Evidence:** Captured Crossref title, abstract, and provider metadata; [ChemRxiv record](https://doi.org/10.26434/chemrxiv.15011121/v2). The analysis uses captured metadata only, not full text.
