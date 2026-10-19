---
title: Provenance records predict which multi-scale conclusions a foundation-potential
  release can change in SiGeC semiconductors
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010670/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15010670/v1
captured_by: auto-scanner
date: '2026-10-19'
captured_at: '2026-10-19T21:19:36+00:00'
last_requested: '2026-10-19T21:19:36+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Kinston Ackölf
- Taylor D. Sparks
published: '2026-10-19'
abstract: 'Multi-scale simulations of semiconductor alloys rest on foundation interatomic
  potentials (machine-learned force models trained on large density-functional databases),
  re-released as training data grow. A release changes defect energies and phonon
  stiffness and, through them, the recipes and design verdicts downstream; recomputing
  everything is costly, and recomputing nothing leaves conclusions that may no longer
  hold. Workflow records list every result downstream of a calculation, not which
  could change a decision. We tested whether the conclusions a release can change
  are predictable from a campaign’s provenance record (a record of which calculation
  fed which result) before any rerun and settled by recomputing only the predicted
  units. The chain served a SiGeC design question (germanium content, carbon content
  and SiC particle size for low lattice thermal conductivity), with MACE-MP-0 replaced
  by MACE-MPA-0 and all predictions and decision rules fixed in advance. From the
  record, 49 of 128 record entries were reached, 24 conclusions were classified by
  their margin to a decision threshold, and four recompute units were named. Recomputing
  those units (70 relaxations, 91 molecular-dynamics runs) settled 20 conclusions:
  none changed outside the predicted set (exact 95% upper bound on the miss rate 0.24),
  eight of nine flagged as at risk held, and one, Ge attraction to the first shell
  around a SiC particle, reversed by less than a millielectronvolt past its threshold,
  while the conclusion it served (no germanium-depleted zone forms) held. Magnitudes
  moved more than assumed: the energy carbon gains by precipitating as SiC grew by
  0.65–0.75 eV against an assumed 0.3 eV; the recipe and the germanium saving held.
  Recomputation cost 3.5 CPU-task-hours and 354 GPU-hours, 2.2 times the GPU estimate
  scaled from the recorded runs. Decisions whose margins exceed a measured release
  shift can be carried across a release with a recorded check; magnitudes need recomputation,
  and explicit records of each result’s inputs and code would make the prediction
  a lookup.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010670/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Provenance records predict which multi-scale conclusions a foundation-potential release can change in SiGeC semiconductors

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010670/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Kinston Ackölf, Taylor D. Sparks
- **Published:** 2026-10-19

## Summary
Multi-scale simulations of semiconductor alloys rest on foundation interatomic potentials (machine-learned force models trained on large density-functional databases), re-released as training data grow. A release changes defect energies and phonon stiffness and, through them, the recipes and design verdicts downstream; recomputing everything is costly, and recomputing nothing leaves conclusions that may no longer hold. Workflow records list every result downstream of a calculation, not which could change a decision. We tested whether the conclusions a release can change are predictable from a campaign’s provenance record (a record of which calculation fed which result) before any rerun and settled by recomputing only the predicted units. The chain served a SiGeC design question (germanium content, carbon content and SiC particle size for low lattice thermal conductivity), with MACE-MP-0 replaced by MACE-MPA-0 and all predictions and decision rules fixed in advance. From the record, 49 of 128 record entries were reached, 24 conclusions were classified by their margin to a decision threshold, and four recompute units were named. Recomputing those units (70 relaxations, 91 molecular-dynamics runs) settled 20 conclusions: none changed outside the predicted set (exact 95% upper bound on the miss rate 0.24), eight of nine flagged as at risk held, and one, Ge attraction to the first shell around a SiC particle, reversed by less than a millielectronvolt past its threshold, while the conclusion it served (no germanium-depleted zone forms) held. Magnitudes moved more than assumed: the energy carbon gains by precipitating as SiC grew by 0.65–0.75 eV against an assumed 0.3 eV; the recipe and the germanium saving held. Recomputation cost 3.5 CPU-task-hours and 354 GPU-hours, 2.2 times the GPU estimate scaled from the recorded runs. Decisions whose margins exceed a measured release shift can be carried across a release with a recorded check; magnitudes need recomputation, and explicit records of each result’s inputs and code would make the prediction a lookup.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010670/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
