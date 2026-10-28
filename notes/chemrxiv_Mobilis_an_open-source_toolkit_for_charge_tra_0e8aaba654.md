---
title: 'Mobilis: an open-source toolkit for charge transport in organic semiconductors,
  from crystal structures to temperaturedependent mobilities with dynamic disorder
  and active learning'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011171/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011171/v1
captured_by: auto-scanner
date: '2026-10-28'
captured_at: '2026-10-28T10:56:07+00:00'
last_requested: '2026-10-28T10:56:07+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Ya-Rui Shi
- Yarui Shi
published: '2026-10-28'
abstract: 'Computing a charge mobility for an organic semiconductor involves a chain
  of steps: monomer site energies, intermolecular couplings, the thermal fluctuation
  of those couplings, and a transport model whose validity depends on the ratio of
  coupling to reorganization energy. These steps are usually carried out with separate
  scripts and different quantum-chemistry codes, which makes results hard to reproduce
  and models hard to compare. Mobilis is an open-source Python package (GPL-3.0) with
  a graphical interface and a command-line interface that runs the whole chain from
  a CIF file or an MD morphology. It prepares and reads Gaussian and ADF calculations
  (and xtb from the command line), and contains its own extended-Hückel and ZINDO
  couplings, a polarizable site-energy model, Marcus–Jortner hopping with kinetic
  Monte Carlo, and transient localization theory. For dynamic disorder it builds coupling
  surfaces over the six rigidbody intermolecular coordinates and samples them by full-crystal
  rigid-body molecular dynamics. A Gaussian-process active-learning loop chooses the
  DFT dimer calculations needed for these surfaces and stops when the posterior uncertainty
  of the coupling fluctuation σV falls below a target. For pentacene, 24–40 DFT dimers
  per pair reproduce σV within 4%, against 273 points for a quadratic fit. Chiral
  molecules in centrosymmetric crystals, such as mer-Alq3 and Ir(III) emitters, are
  treated by mirror-image fragments. The code is tested by 34 automated test scripts,
  including an exact-solution check of the kinetic Monte Carlo, and is archived on
  Zenodo (doi:10.5281/zenodo.23593488).'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011171/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Mobilis: an open-source toolkit for charge transport in organic semiconductors, from crystal structures to temperaturedependent mobilities with dynamic disorder and active learning

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011171/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Ya-Rui Shi, Yarui Shi
- **Published:** 2026-10-28

## Summary
Computing a charge mobility for an organic semiconductor involves a chain of steps: monomer site energies, intermolecular couplings, the thermal fluctuation of those couplings, and a transport model whose validity depends on the ratio of coupling to reorganization energy. These steps are usually carried out with separate scripts and different quantum-chemistry codes, which makes results hard to reproduce and models hard to compare. Mobilis is an open-source Python package (GPL-3.0) with a graphical interface and a command-line interface that runs the whole chain from a CIF file or an MD morphology. It prepares and reads Gaussian and ADF calculations (and xtb from the command line), and contains its own extended-Hückel and ZINDO couplings, a polarizable site-energy model, Marcus–Jortner hopping with kinetic Monte Carlo, and transient localization theory. For dynamic disorder it builds coupling surfaces over the six rigidbody intermolecular coordinates and samples them by full-crystal rigid-body molecular dynamics. A Gaussian-process active-learning loop chooses the DFT dimer calculations needed for these surfaces and stops when the posterior uncertainty of the coupling fluctuation σV falls below a target. For pentacene, 24–40 DFT dimers per pair reproduce σV within 4%, against 273 points for a quadratic fit. Chiral molecules in centrosymmetric crystals, such as mer-Alq3 and Ir(III) emitters, are treated by mirror-image fragments. The code is tested by 34 automated test scripts, including an exact-solution check of the kinetic Monte Carlo, and is archived on Zenodo (doi:10.5281/zenodo.23593488).

## Provider details
- **Doi:** 10.26434/chemrxiv.15011171/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
