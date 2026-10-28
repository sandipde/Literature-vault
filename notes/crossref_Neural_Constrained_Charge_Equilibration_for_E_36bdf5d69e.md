---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: ML interatomic potentials
enrichment_tags: [charge-equilibration, charge-transport, diabatic-states, electronic-coupling]
title: Neural Constrained Charge Equilibration for Extracting Charge Transport Parameters
  from Machine Learned Interatomic Potentials
type: paper
source: https://doi.org/10.1021/acsomega.6c04842
canonical_url: https://doi.org/10.1021/acsomega.6c04842
captured_by: auto-scanner
date: '2026-10-13'
captured_at: '2026-10-13T12:25:46+00:00'
last_requested: '2026-10-13T12:25:46+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Carson Farmer
- Hector Medina
published: '2026-10-13'
abstract: Abstract Machine-learned interatomic potentials (MLIPs) continue to gain
  popularity as efficient tools for predicting energies and forces for atomic structures
  at an accuracy comparable to quantum chemistry. However, there are limited trained
  MLIPs for certain important applications such as in charge transport. Accelerating
  and automating the determination of parameters for such applications can be of critical
  importance in the rapid discovery of materials such as organic electronics (e.g.,
  OLEDs). This work develops and introduces neural constrained charge equilibriation
  (NcQEq) and applies the technique to AimNet2 and OrbMol-V2. The new method enables
  extracting information about the diabatic states and thereby charge transport parameters.
  The approach is demonstrated on model systems against constrained density functional
  theory charge transport and then tested on intramolecular hole transport properties
  for polyethylene. This work demonstrates that the NcQeq approach is compatible with
  the charge equilibration schemes for AimNet2 and the latent charge predictions of
  OrbMol-V2. After calibration to reference data, the method enables estimation of
  the electronic coupling, reorganization energy, and the free energy difference.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1021/acsomega.6c04842
  journal: ACS Omega
  publisher: American Chemical Society (ACS)
  type: journal-article
  subjects: []
---

# Neural Constrained Charge Equilibration for Extracting Charge Transport Parameters from Machine Learned Interatomic Potentials

- **Type:** paper
- **Source:** https://doi.org/10.1021/acsomega.6c04842
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Carson Farmer, Hector Medina
- **Published:** 2026-10-13

## Summary
Abstract Machine-learned interatomic potentials (MLIPs) continue to gain popularity as efficient tools for predicting energies and forces for atomic structures at an accuracy comparable to quantum chemistry. However, there are limited trained MLIPs for certain important applications such as in charge transport. Accelerating and automating the determination of parameters for such applications can be of critical importance in the rapid discovery of materials such as organic electronics (e.g., OLEDs). This work develops and introduces neural constrained charge equilibriation (NcQEq) and applies the technique to AimNet2 and OrbMol-V2. The new method enables extracting information about the diabatic states and thereby charge transport parameters. The approach is demonstrated on model systems against constrained density functional theory charge transport and then tested on intramolecular hole transport properties for polyethylene. This work demonstrates that the NcQeq approach is compatible with the charge equilibration schemes for AimNet2 and the latent charge predictions of OrbMol-V2. After calibration to reference data, the method enables estimation of the electronic coupling, reorganization energy, and the free energy difference.

## Provider details
- **Doi:** 10.1021/acsomega.6c04842
- **Journal:** ACS Omega
- **Publisher:** American Chemical Society (ACS)
- **Type:** journal-article

## AI enrichment
- **Concise summary:** Neural constrained charge equilibration extracts charge-transport information from AimNet2 and OrbMol-V2, estimating electronic couplings, reorganization energies, and free-energy differences after calibration.
- **Why it matters:** It extends the use of learned atomic models beyond energy/force prediction toward parameters needed for organic charge-transport calculations.
- **Caveat:** The abstract describes model systems and polyethylene hole transport; compatibility with two models and calibration dependence do not establish universal transport accuracy.
- **Evidence:** [Captured source](https://doi.org/10.1021/acsomega.6c04842); analysis based only on captured metadata, not independently verified full text.
