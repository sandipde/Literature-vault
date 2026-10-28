---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [multireference-theory, natural-orbitals, correlation-energy, orbital-truncation]
title: 'The Regularized Frozen Natural Orbital approach to CASPT2: extension to Restricted
  Active Space wave functions, different multiplicities and assessment of correlation
  effects'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15007726/v2
canonical_url: https://doi.org/10.26434/chemrxiv.15007726/v2
captured_by: auto-scanner
date: '2026-10-17'
captured_at: '2026-10-17T08:58:51+00:00'
last_requested: '2026-10-17T08:58:51+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Juliana Cuéllar-Zuquin
- Javier Segarra-Martí
- Francesco Aquilante
published: '2026-10-16'
abstract: The frozen natural orbital (FNO) method is a well-known approximation that
  significantly reduces the cost of many-body perturbation theory treatments for obtaining
  correlation energies in a systematic and controlled manner, enabling the simulation
  of larger and more realistic molecular systems. Here, we implement FNO on top of
  restricted active-space self-consistent field (RASSCF) wave function within second-order
  perturbation theory, leading to the FNO-RASPT2 method. To account for the additional
  approximations incurred when using restricted RASSCF wave functions, as well as
  to apply it to states of different molecular charge and spin multiplicity, we introduce
  a regularisation approach via a level-shift in the orbital deletion procedure, which
  helps avoid singularities resulting from vanishing denominators due to the reduced
  occupation of restricted (active) virtual orbitals and that we show does not significantly
  influence the final energies obtained. Numerical results on vertical excitation
  energies showcase the FNO to be up to ∼3.5 faster than the parent computation while
  retaining ∼95% of the dynamic correlation energy and being within 0.1 eV of the
  reference calculation, with the CASPT2 equations-the main bottleneck in large molecular
  systems-registering over an order of magnitude speed-up. An in-depth analysis shows
  the regularized FNO approach to retain electron correlation appropriately for internal
  and semi-internal contributions, while displaying larger deviations for the external
  term, which originates from the initial FNO truncation based on an approximated
  one-electron reduced density matrix. Ongoing efforts are directed towards improving
  and extending our current implementation to the calculation of analytic gradients
  and non-adiabatic couplings to enable faster non-adiabatic molecular dynamics simulations
  in larger and more realistic molecular systems.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15007726/v2
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# The Regularized Frozen Natural Orbital approach to CASPT2: extension to Restricted Active Space wave functions, different multiplicities and assessment of correlation effects

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15007726/v2
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Juliana Cuéllar-Zuquin, Javier Segarra-Martí, Francesco Aquilante
- **Published:** 2026-10-16

## Summary
The frozen natural orbital (FNO) method is a well-known approximation that significantly reduces the cost of many-body perturbation theory treatments for obtaining correlation energies in a systematic and controlled manner, enabling the simulation of larger and more realistic molecular systems. Here, we implement FNO on top of restricted active-space self-consistent field (RASSCF) wave function within second-order perturbation theory, leading to the FNO-RASPT2 method. To account for the additional approximations incurred when using restricted RASSCF wave functions, as well as to apply it to states of different molecular charge and spin multiplicity, we introduce a regularisation approach via a level-shift in the orbital deletion procedure, which helps avoid singularities resulting from vanishing denominators due to the reduced occupation of restricted (active) virtual orbitals and that we show does not significantly influence the final energies obtained. Numerical results on vertical excitation energies showcase the FNO to be up to ∼3.5 faster than the parent computation while retaining ∼95% of the dynamic correlation energy and being within 0.1 eV of the reference calculation, with the CASPT2 equations-the main bottleneck in large molecular systems-registering over an order of magnitude speed-up. An in-depth analysis shows the regularized FNO approach to retain electron correlation appropriately for internal and semi-internal contributions, while displaying larger deviations for the external term, which originates from the initial FNO truncation based on an approximated one-electron reduced density matrix. Ongoing efforts are directed towards improving and extending our current implementation to the calculation of analytic gradients and non-adiabatic couplings to enable faster non-adiabatic molecular dynamics simulations in larger and more realistic molecular systems.

## Provider details
- **Doi:** 10.26434/chemrxiv.15007726/v2
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment
- **Concise summary:** Regularized frozen natural orbitals extend perturbation-theory cost reduction to restricted-active-space wavefunctions and different charge and spin states. A level shift stabilizes orbital deletion, with vertical-excitation tests reporting retained correlation energy and reduced runtime.
- **Why it matters:** Controlled virtual-space reduction can make larger multireference calculations practical without replacing the underlying electronic-structure method with a learned surrogate.
- **Caveat:** ChemRxiv v2 results are unverified; external correlation contributions show larger deviations, and analytic gradients and nonadiabatic couplings are described as future work.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15007726/v2); analysis based only on captured metadata, not independently verified full text.
