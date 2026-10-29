---
title: Correcting the Liquid Densities of Universal Machine-Learning Interatomic Potentials
  Using Local-Number-Density Repulsion
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011258/v2
canonical_url: https://doi.org/10.26434/chemrxiv.15011258/v2
captured_by: auto-scanner
date: '2026-10-29'
captured_at: '2026-10-29T21:30:21+00:00'
last_requested: '2026-10-29T21:30:21+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Shunsuke Mieda
published: '2026-10-29'
abstract: Universal machine-learning interatomic potentials (MLIPs) such as UMA, trained
  on reference data from meta-generalized gradient approximation or hybrid functionals
  that incorporate dispersion interactions, often overestimate molecular-liquid densities,
  thereby placing every property computed at constant pressure at the wrong state
  point. This study proposes a correction that adds to the MLIP a repulsive energy
  quadratic in the local number density of each atom, with two coefficients fitted
  only to the equations of state of water and ethanol; the forces and stresses follow
  analytically, so neither electronic-structure calculations nor retraining is required.
  For UMA, the correction reduces the density mean absolute error (MAE) of 22 liquids
  from 10.8% to 2.5%, lowering the error for every liquid and bringing 20 of them
  within ±5% of experiment, while improving the bulk modulus (MAE from 71.6% to 22.1%),
  heat of vaporization, and second hydration shell of water, none of which was calibrated.
  Applied to SevenNet-Omni without recalibration, the same coefficients reduce the
  density MAE from 8.2% to 1.8%, with 21 of 22 liquids within ±5% of experiment.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011258/v2
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Correcting the Liquid Densities of Universal Machine-Learning Interatomic Potentials Using Local-Number-Density Repulsion

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011258/v2
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Shunsuke Mieda
- **Published:** 2026-10-29

## Summary
Universal machine-learning interatomic potentials (MLIPs) such as UMA, trained on reference data from meta-generalized gradient approximation or hybrid functionals that incorporate dispersion interactions, often overestimate molecular-liquid densities, thereby placing every property computed at constant pressure at the wrong state point. This study proposes a correction that adds to the MLIP a repulsive energy quadratic in the local number density of each atom, with two coefficients fitted only to the equations of state of water and ethanol; the forces and stresses follow analytically, so neither electronic-structure calculations nor retraining is required. For UMA, the correction reduces the density mean absolute error (MAE) of 22 liquids from 10.8% to 2.5%, lowering the error for every liquid and bringing 20 of them within ±5% of experiment, while improving the bulk modulus (MAE from 71.6% to 22.1%), heat of vaporization, and second hydration shell of water, none of which was calibrated. Applied to SevenNet-Omni without recalibration, the same coefficients reduce the density MAE from 8.2% to 1.8%, with 21 of 22 liquids within ±5% of experiment.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011258/v2
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
