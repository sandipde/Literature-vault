---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [epr-simulation, spin-dynamics, liouville-space, spectral-fitting]
title: 'MaRs: A Universal Python Library for Steady-State and Time-Resolved EPR Simulations'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15009102/v2
canonical_url: https://doi.org/10.26434/chemrxiv.15009102/v2
captured_by: auto-scanner
date: '2026-10-15'
captured_at: '2026-10-15T20:09:48+00:00'
last_requested: '2026-10-15T20:09:48+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Arkady Samsonenko
- Ivan Kurganskii
- Alexander Maryasov
- Sergey Veber
- Matvey Fedin
published: '2026-10-15'
abstract: MaRs is an open-source Python library for the simulation and fitting of
  electron paramagnetic resonance (EPR) spectra. MaRs supports simulations of field-swept
  and frequency-swept continuous-wave EPR, accounting for various spin-sublevel polarizations.
  Moreover, MaRs is capable of simulating complete 2D time-resolved EPR spectra (in
  field-time domain). The latter can be computed in different levels of theoretical
  complexity. First, the time evolution can be computed either with kinetic rate equations,
  which describe population transfer, or in full Liouville space, which captures coherence
  dynamics. Second, the relaxation pathways in timeresolved simulations can be specified
  either through intuitive rate parameters that are automatically expanded into the
  Lindblad master-equation form, or derived microscopically using the Bloch-Redfield
  formalism. To handle physically complex relaxation scenarios, MaRs provides automatic
  thermal-balance enforcement and composition operations that allow multicomponent
  relaxation models to be assembled from simple building blocks. Built on PyTorch
  (popular platform for machine learning development), MaRs leverages operations on
  both CPU and CUDA (GPU) backends. We demonstrate MaRs time-resolved EPR capabilities
  as well the differences and limitations of each built-in approach to time-domain
  simulations on the examples of coupled triplet-doublet pairs and systems exhibiting
  the reverse intersystem crossing phenomenon. Separately, we validate stationary
  EPR simulations across diverse spin systems, including high-spin complexes, achieving
  excellent agreement with established packages. We also show the possibilities of
  parameter fitting framework, applicable to all spectrum types implemented in MaRs,
  that supports multiple optimization strategies and uncertainty quantification.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15009102/v2
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# MaRs: A Universal Python Library for Steady-State and Time-Resolved EPR Simulations

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15009102/v2
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Arkady Samsonenko, Ivan Kurganskii, Alexander Maryasov, Sergey Veber, Matvey Fedin
- **Published:** 2026-10-15

## Summary
MaRs is an open-source Python library for the simulation and fitting of electron paramagnetic resonance (EPR) spectra. MaRs supports simulations of field-swept and frequency-swept continuous-wave EPR, accounting for various spin-sublevel polarizations. Moreover, MaRs is capable of simulating complete 2D time-resolved EPR spectra (in field-time domain). The latter can be computed in different levels of theoretical complexity. First, the time evolution can be computed either with kinetic rate equations, which describe population transfer, or in full Liouville space, which captures coherence dynamics. Second, the relaxation pathways in timeresolved simulations can be specified either through intuitive rate parameters that are automatically expanded into the Lindblad master-equation form, or derived microscopically using the Bloch-Redfield formalism. To handle physically complex relaxation scenarios, MaRs provides automatic thermal-balance enforcement and composition operations that allow multicomponent relaxation models to be assembled from simple building blocks. Built on PyTorch (popular platform for machine learning development), MaRs leverages operations on both CPU and CUDA (GPU) backends. We demonstrate MaRs time-resolved EPR capabilities as well the differences and limitations of each built-in approach to time-domain simulations on the examples of coupled triplet-doublet pairs and systems exhibiting the reverse intersystem crossing phenomenon. Separately, we validate stationary EPR simulations across diverse spin systems, including high-spin complexes, achieving excellent agreement with established packages. We also show the possibilities of parameter fitting framework, applicable to all spectrum types implemented in MaRs, that supports multiple optimization strategies and uncertainty quantification.

## Provider details
- **Doi:** 10.26434/chemrxiv.15009102/v2
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment
- **Concise summary:** MaRs is a PyTorch-based EPR simulation and fitting library supporting continuous-wave and field–time spectra with rate-equation, Liouville-space, Lindblad, and Bloch–Redfield treatments.
- **Why it matters:** Exposing multiple relaxation descriptions in one fitting environment could help separate population-only approximations from coherence-sensitive spin dynamics.
- **Caveat:** The v2 preprint's agreement with established packages is reported rather than checked here; using PyTorch does not itself make this a learned force field or generative model.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15009102/v2); analysis based only on captured metadata, not independently verified full text.
