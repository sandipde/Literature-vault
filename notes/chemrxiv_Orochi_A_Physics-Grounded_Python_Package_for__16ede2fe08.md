---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [pair-distribution, total-scattering, structural-refinement]
title: 'Orochi: A Physics-Grounded Python Package for Pair Distribution Function Analysis
  of Crystalline and Low-Dimensional Materials'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010802/v2
canonical_url: https://doi.org/10.26434/chemrxiv.15010802/v2
captured_by: auto-scanner
date: '2026-10-26'
captured_at: '2026-10-26T10:43:25+00:00'
last_requested: '2026-10-26T10:43:25+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Satoshi Tominaka
published: '2026-10-26'
abstract: 'Atomic pair distribution function (PDF) analysis from X-ray total scattering
  is a powerful methodology for determining atomic structure and arrangements across
  crystalline, disordered, nanostructured, and low-dimensional materials on both laboratory
  and synchrotron instruments. Fundamentally, PDF analysis relies on two core pillars—PDF
  data reduction from one-dimensional (1D) total scattering profiles and real-space
  structural modeling—often accompanied in rapid-acquisition experiments by upstream
  two-dimensional (2D) detector image processing. However, conventional workflows
  remain fragmented across disconnected software tools, forcing researchers to manually
  combine multiple programs and preventing the simultaneous optimization of measurement
  reduction parameters and crystal structure parameters that is standard in X-ray
  Rietveld refinement. Furthermore, mainstream PDF modeling engines rely on legacy
  physical approximations: they enforce three-dimensional (3D) periodic boundary conditions
  (requiring artificial vacuum supercells for 2D nanosheets), treat atomic scattering
  factors as angle-independent constants (causing peak distortions in compounds with
  large atomic number contrast), and approximate number density baselines using macroscopic
  bulk volume assumptions. Here, the open-source, pure-Python architecture of Orochi
  (version 4.0) is presented, implementing physical calculations from scratch in Python
  (accelerated via Numba) to unify total scattering data reduction, symmetry-aware
  crystallographic modeling, and real-space PDF simulation alongside a dedicated high-Q
  2D detector processing module within a self-contained Python environment. Originally
  developed for laboratory total scattering studies of pharmaceutical glasses and
  deployed as compiled executable (β-version) tools at SPring-8 beamlines, Orochi
  has been completely redesigned around an externalized parameter management core
  (orochi.base) in which parameters are stored in standardized Python dictionaries
  and accessed via hierarchical string addresses. By bringing parameters outside the
  calculation engines rather than locking them inside built-in optimizers, this architecture
  allows multiple module instances across data reduction and structural modeling to
  be optimized simultaneously by modern optimization algorithms, machine learning
  libraries, and autonomous AI agents. For structural simulation, intra-cell atomic
  pair vectors are decoupled from lattice translation vectors to natively support
  arbitrary periodic boundary conditions across 3D crystals, 2D nanosheets, 1D nanowires,
  and 0D clusters. The simulation engine incorporates the full scattering vector (Q)
  dependence of atomic form factors, enabling accurate modeling of heavy/light-element
  oxides and permitting direct instrumental calibration using standard CeO2 powder
  rather than monoatomic nickel substitutes. Furthermore, a sinc-convolution density
  formulation is established to accurately reproduce baseline ripples arising from
  finite Qmin cutoffs in nanostructured systems. Complete mathematical formulations
  for all reduction and simulation algorithms are consolidated to establish a rigorous
  foundation for automated crystallographic analysis.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010802/v2
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Orochi: A Physics-Grounded Python Package for Pair Distribution Function Analysis of Crystalline and Low-Dimensional Materials

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010802/v2
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Satoshi Tominaka
- **Published:** 2026-10-26

## Summary
Atomic pair distribution function (PDF) analysis from X-ray total scattering is a powerful methodology for determining atomic structure and arrangements across crystalline, disordered, nanostructured, and low-dimensional materials on both laboratory and synchrotron instruments. Fundamentally, PDF analysis relies on two core pillars—PDF data reduction from one-dimensional (1D) total scattering profiles and real-space structural modeling—often accompanied in rapid-acquisition experiments by upstream two-dimensional (2D) detector image processing. However, conventional workflows remain fragmented across disconnected software tools, forcing researchers to manually combine multiple programs and preventing the simultaneous optimization of measurement reduction parameters and crystal structure parameters that is standard in X-ray Rietveld refinement. Furthermore, mainstream PDF modeling engines rely on legacy physical approximations: they enforce three-dimensional (3D) periodic boundary conditions (requiring artificial vacuum supercells for 2D nanosheets), treat atomic scattering factors as angle-independent constants (causing peak distortions in compounds with large atomic number contrast), and approximate number density baselines using macroscopic bulk volume assumptions. Here, the open-source, pure-Python architecture of Orochi (version 4.0) is presented, implementing physical calculations from scratch in Python (accelerated via Numba) to unify total scattering data reduction, symmetry-aware crystallographic modeling, and real-space PDF simulation alongside a dedicated high-Q 2D detector processing module within a self-contained Python environment. Originally developed for laboratory total scattering studies of pharmaceutical glasses and deployed as compiled executable (β-version) tools at SPring-8 beamlines, Orochi has been completely redesigned around an externalized parameter management core (orochi.base) in which parameters are stored in standardized Python dictionaries and accessed via hierarchical string addresses. By bringing parameters outside the calculation engines rather than locking them inside built-in optimizers, this architecture allows multiple module instances across data reduction and structural modeling to be optimized simultaneously by modern optimization algorithms, machine learning libraries, and autonomous AI agents. For structural simulation, intra-cell atomic pair vectors are decoupled from lattice translation vectors to natively support arbitrary periodic boundary conditions across 3D crystals, 2D nanosheets, 1D nanowires, and 0D clusters. The simulation engine incorporates the full scattering vector (Q) dependence of atomic form factors, enabling accurate modeling of heavy/light-element oxides and permitting direct instrumental calibration using standard CeO2 powder rather than monoatomic nickel substitutes. Furthermore, a sinc-convolution density formulation is established to accurately reproduce baseline ripples arising from finite Qmin cutoffs in nanostructured systems. Complete mathematical formulations for all reduction and simulation algorithms are consolidated to establish a rigorous foundation for automated crystallographic analysis.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010802/v2
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment

- **Concise summary:** Orochi presents a Python workflow joining total-scattering reduction and pair-distribution modeling with shared parameters and dimensionality-aware structural calculations.
- **Why it matters:** Joint optimization of measurement and structure parameters could reduce errors introduced by disconnected analysis tools.
- **Caveat:** This versioned software preprint describes capabilities rather than independently reproduced accuracy, usability or performance.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15010802/v2); analysis based only on captured metadata, not independently verified full text.
