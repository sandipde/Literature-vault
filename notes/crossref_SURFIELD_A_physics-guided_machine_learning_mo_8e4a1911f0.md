---
title: 'SURFIELD: A physics-guided machine learning model for atomistic simulation
  of surfaces under electric fields'
type: paper
source: https://doi.org/10.2139/ssrn.7635624
canonical_url: https://doi.org/10.2139/ssrn.7635624
captured_by: auto-scanner
date: '2026-10-19'
captured_at: '2026-10-19T21:19:36+00:00'
last_requested: '2026-10-19T21:19:36+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Moradpur-Tari Ehsan
- Andreas Kyritsakis
- Tauno Tiirats
- Veronika Zadin
published: '2026-10-19'
abstract: External electric fields influence surface diffusion, field evaporation
  and nanoscale morphology, but their atomistic simulation remains computationally
  demanding. We introduce SURFIELD, a physics-guided machine-learning framework for
  metallic surfaces under external electric fields. The framework learns local dipole
  moments, polarizabilities and zero-field potential energies, then combines them
  with response theory to calculate field-induced and total forces. Directional smooth
  overlap of atomic positions (D-SOAP) augments SOAP with four quaternion components
  to encode environmental orientation. For lithium and tungsten surfaces, test normalised
  root-mean-square errors are 3.7–3.8% for dipole moments, 3.4–5.6% for polarizabilities
  and 6.7–10.7% for field-induced forces. DFT-derived forces on a flat lithium slab
  reproduce analytical Maxwell stress, while finite-field calculations support the
  linear-response approximation over the investigated range. Under the reported benchmark
  conditions, SURFIELD is approximately 389 times faster than DFT, providing an efficient
  approach to modelling the surface-normal electric-field response of metallic surfaces.
metadata_provider: Crossref
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: ML interatomic potentials
enrichment_tags: [electric-field-response, metallic-surfaces, response-theory]
provider_data:
  doi: 10.2139/ssrn.7635624
  journal: ''
  publisher: Elsevier BV
  type: posted-content
  subjects: []
---

# SURFIELD: A physics-guided machine learning model for atomistic simulation of surfaces under electric fields

- **Type:** paper
- **Source:** https://doi.org/10.2139/ssrn.7635624
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Moradpur-Tari Ehsan, Andreas Kyritsakis, Tauno Tiirats, Veronika Zadin
- **Published:** 2026-10-19

## Summary
External electric fields influence surface diffusion, field evaporation and nanoscale morphology, but their atomistic simulation remains computationally demanding. We introduce SURFIELD, a physics-guided machine-learning framework for metallic surfaces under external electric fields. The framework learns local dipole moments, polarizabilities and zero-field potential energies, then combines them with response theory to calculate field-induced and total forces. Directional smooth overlap of atomic positions (D-SOAP) augments SOAP with four quaternion components to encode environmental orientation. For lithium and tungsten surfaces, test normalised root-mean-square errors are 3.7–3.8% for dipole moments, 3.4–5.6% for polarizabilities and 6.7–10.7% for field-induced forces. DFT-derived forces on a flat lithium slab reproduce analytical Maxwell stress, while finite-field calculations support the linear-response approximation over the investigated range. Under the reported benchmark conditions, SURFIELD is approximately 389 times faster than DFT, providing an efficient approach to modelling the surface-normal electric-field response of metallic surfaces.

## Provider details
- **Doi:** 10.2139/ssrn.7635624
- **Publisher:** Elsevier BV
- **Type:** posted-content

## AI enrichment

- **Concise summary:** SURFIELD learns local dipoles, polarizabilities, and zero-field energies, then uses response theory to construct field-dependent forces. Directional SOAP encodes orientation, with lithium and tungsten surfaces as the stated tests.
- **Why it matters:** Explicit response quantities offer a structured way to extend surface potentials beyond a single zero-field energy landscape.
- **Caveat:** Linear-response validity and the reported 389-fold speedup apply to investigated fields and benchmark conditions, not arbitrary fields or materials.
- **Evidence:** [Captured source](https://doi.org/10.2139/ssrn.7635624); analysis based only on captured metadata, not independently verified full text.
