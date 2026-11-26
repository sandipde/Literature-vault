---
title: 'Benchmarking Machine-Learned Interatomic Potentials for Reactive Chemistry:
  Failure Modes in Nitromethane Decomposition'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15012828/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15012828/v1
captured_by: auto-scanner
date: '2026-11-26'
captured_at: '2026-11-26T14:39:56+00:00'
last_requested: '2026-11-26T14:39:56+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Cary B. Darwin
- Jan Dunal
- Steven O. Nielsen
published: '2026-11-26'
abstract: 'The failure modes of ab initio methods and empirical force fields are well
  documented, but those of machine-learned interatomic potentials (MLIPs) in reactive
  chemistry remain largely uncharacterized. We benchmark five MLIPs on condensed-phase
  nitromethane decomposition against coupled-cluster dissociation energies and published
  simulations, and trace each model’s failure to a specific component: the global
  spin label of MACE-OMol-0 and UMA-S-1P1 produces a spurious ~25 kcal/mol rise as
  fragments separate, gaps in the training data of ANI-1xnr cause it to underbind
  dissociation into two polyatomic radicals by up to 48 kcal/mol, and the absence
  of close-contact configurations from the training data of MACE-OFF23 and MACEOsaka24
  leads to unphysical energies at short interatomic distances, more severely in MACEOFF23.
  The responsible component determines the remedy: the spin-label artifact cannot
  be fixed within the models’ input format, the ANI-1xnr error is corrected to within
  1 kcal/mol by physics-constrained data augmentation, and the short-range failure
  of MACE-OFF23 persists even with a standard screened nuclear repulsion term. Because
  corrected dissociation energies do not by themselves restore physical decomposition
  kinetics, we join recent calls to judge MLIPs by their failure modes and predicted
  observables rather than by aggregate energy and force errors.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15012828/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Benchmarking Machine-Learned Interatomic Potentials for Reactive Chemistry: Failure Modes in Nitromethane Decomposition

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15012828/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Cary B. Darwin, Jan Dunal, Steven O. Nielsen
- **Published:** 2026-11-26

## Summary
The failure modes of ab initio methods and empirical force fields are well documented, but those of machine-learned interatomic potentials (MLIPs) in reactive chemistry remain largely uncharacterized. We benchmark five MLIPs on condensed-phase nitromethane decomposition against coupled-cluster dissociation energies and published simulations, and trace each model’s failure to a specific component: the global spin label of MACE-OMol-0 and UMA-S-1P1 produces a spurious ~25 kcal/mol rise as fragments separate, gaps in the training data of ANI-1xnr cause it to underbind dissociation into two polyatomic radicals by up to 48 kcal/mol, and the absence of close-contact configurations from the training data of MACE-OFF23 and MACEOsaka24 leads to unphysical energies at short interatomic distances, more severely in MACEOFF23. The responsible component determines the remedy: the spin-label artifact cannot be fixed within the models’ input format, the ANI-1xnr error is corrected to within 1 kcal/mol by physics-constrained data augmentation, and the short-range failure of MACE-OFF23 persists even with a standard screened nuclear repulsion term. Because corrected dissociation energies do not by themselves restore physical decomposition kinetics, we join recent calls to judge MLIPs by their failure modes and predicted observables rather than by aggregate energy and force errors.

## Provider details
- **Doi:** 10.26434/chemrxiv.15012828/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
