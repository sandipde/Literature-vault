---
title: 'SchNet-AL: Data-Driven Atomistic Representation and Uncertainty-Calibrated
  Active Learning for Sodium-Ion Cathode Screening'
type: paper
source: https://doi.org/10.64972/dea.2023.v2i2.3619d:119-133
canonical_url: https://doi.org/10.64972/dea.2023.v2i2.3619d
captured_by: auto-scanner
date: '2026-11-02'
captured_at: '2026-11-02T23:46:24+00:00'
last_requested: '2026-11-02T23:46:24+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Zorana Mladenović
- Danka Cvetković
published: '2023-06-28'
abstract: The search space for sodium-ion battery cathodes has been made relatively
  large by chemistry, but it is still too expensive to test with density-functional
  theory. This paper introduces a SchNet-active learning framework that combines continuous-filter
  atomistic representation learning with calibrated ensemble uncertainty and diversity-aware
  batch acquisition. A curated pool of 18,240 relaxed and partially relaxed inorganic
  structures was screened for formation energy, average sodium extraction voltage,
  theoretical capacity and diffusion-barrier proxy. Start with 1,200 labelled structures
  and add 300 calculations each time in five acquisition rounds. The proposed strategy
  reduced the energy mean absolute error from 92 to 31 meV atom⁻¹ and the voltage
  error from 0.284 to 0.118 V, and random acquisition needed 61% more labels to achieve
  the same energy accuracy. With a fixed budget of 2,700 labelled structures, 86.7%
  of the retrospectively verified top-60 candidates could be recovered. Multi-objective
  filtering found 47 candidates with stability below 45 meV atom⁻¹ above the convex
  hull, voltage between 2.8 and 4.1 V, capacity over 120 mAh g⁻¹, and a diffusion
  proxy below 0.55 eV. The full workflow reduces the projected screening time by 8.4
  times compared with an all-first-principles calculation. Therefore, uncertainly-calibrated
  atomistic learning can focus the cost of calculation on chemically informative candidates
  without reducing screening coverage.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.64972/dea.2023.v2i2.3619d:119-133
  journal: Data Engineering and Applications
  publisher: European Federation of Engineering Associations
  type: journal-article
  subjects: []
---

# SchNet-AL: Data-Driven Atomistic Representation and Uncertainty-Calibrated Active Learning for Sodium-Ion Cathode Screening

- **Type:** paper
- **Source:** https://doi.org/10.64972/dea.2023.v2i2.3619d:119-133
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Zorana Mladenović, Danka Cvetković
- **Published:** 2023-06-28

## Summary
The search space for sodium-ion battery cathodes has been made relatively large by chemistry, but it is still too expensive to test with density-functional theory. This paper introduces a SchNet-active learning framework that combines continuous-filter atomistic representation learning with calibrated ensemble uncertainty and diversity-aware batch acquisition. A curated pool of 18,240 relaxed and partially relaxed inorganic structures was screened for formation energy, average sodium extraction voltage, theoretical capacity and diffusion-barrier proxy. Start with 1,200 labelled structures and add 300 calculations each time in five acquisition rounds. The proposed strategy reduced the energy mean absolute error from 92 to 31 meV atom⁻¹ and the voltage error from 0.284 to 0.118 V, and random acquisition needed 61% more labels to achieve the same energy accuracy. With a fixed budget of 2,700 labelled structures, 86.7% of the retrospectively verified top-60 candidates could be recovered. Multi-objective filtering found 47 candidates with stability below 45 meV atom⁻¹ above the convex hull, voltage between 2.8 and 4.1 V, capacity over 120 mAh g⁻¹, and a diffusion proxy below 0.55 eV. The full workflow reduces the projected screening time by 8.4 times compared with an all-first-principles calculation. Therefore, uncertainly-calibrated atomistic learning can focus the cost of calculation on chemically informative candidates without reducing screening coverage.

## Provider details
- **Doi:** 10.64972/dea.2023.v2i2.3619d:119-133
- **Journal:** Data Engineering and Applications
- **Publisher:** European Federation of Engineering Associations
- **Type:** journal-article
