---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Other and possible scan noise
enrichment_tags: [marine-hydrodynamics, learned-surrogates, actuator-line-models]
title: ONRT Hull–Propeller–Rudder Interaction using Machine-Learned Actuator Line
  Propeller Model
type: paper
source: https://doi.org/10.2139/ssrn.7615936
canonical_url: https://doi.org/10.2139/ssrn.7615936
captured_by: auto-scanner
date: '2026-10-15'
captured_at: '2026-10-15T20:09:48+00:00'
last_requested: '2026-10-15T20:09:48+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Joshua Bowman
- Shanti Bhushan
- Shawn Aram
published: '2026-10-15'
abstract: 'A machine-learned actuator line model (ML-ALM) is developed and validated
  for marine propellers as a computationally efficient tool for maneuvering applications.
  The ML-ALM is developed using a deep neural network trained on an open-water, oblique-flow
  solution database and is validated using simulations of UNSEEN open-water flow conditions
  and the ONRT appended hull with rotated rudders. For the open-water simulations,
  ML-ALM predictions agree with the blade-resolved simulations to within 3%, and the
  largest error of 6% was obtained for the swirl predictions. For the appended hull
  cases, the average errors in propeller performance, rudder forces and moment, and
  propeller and rudder wake profiles were around 6%, 2%, and 1.5%, respectively. Further,
  the ML-ALM simulations allowed a fourfold increase in time-step size without any
  significant loss in accuracy, reduced the grid-cell requirements, and achieved faster
  solution convergence, thereby resulting in about a fivefold simulation speed-up
  compared to blade-resolved simulations. ML-ALM models show some deficiencies: they
  introduce unsteadiness in blade forces and moments because individual blade-element
  forces are queried independently; they also do not modulate the upstream propeller
  flow in the same way as blade-resolved simulations. Overall, the study validates
  that ML-ALM can be a viable model for marine propellers.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.2139/ssrn.7615936
  journal: ''
  publisher: Elsevier BV
  type: posted-content
  subjects: []
---

# ONRT Hull–Propeller–Rudder Interaction using Machine-Learned Actuator Line Propeller Model

- **Type:** paper
- **Source:** https://doi.org/10.2139/ssrn.7615936
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Joshua Bowman, Shanti Bhushan, Shawn Aram
- **Published:** 2026-10-15

## Summary
A machine-learned actuator line model (ML-ALM) is developed and validated for marine propellers as a computationally efficient tool for maneuvering applications. The ML-ALM is developed using a deep neural network trained on an open-water, oblique-flow solution database and is validated using simulations of UNSEEN open-water flow conditions and the ONRT appended hull with rotated rudders. For the open-water simulations, ML-ALM predictions agree with the blade-resolved simulations to within 3%, and the largest error of 6% was obtained for the swirl predictions. For the appended hull cases, the average errors in propeller performance, rudder forces and moment, and propeller and rudder wake profiles were around 6%, 2%, and 1.5%, respectively. Further, the ML-ALM simulations allowed a fourfold increase in time-step size without any significant loss in accuracy, reduced the grid-cell requirements, and achieved faster solution convergence, thereby resulting in about a fivefold simulation speed-up compared to blade-resolved simulations. ML-ALM models show some deficiencies: they introduce unsteadiness in blade forces and moments because individual blade-element forces are queried independently; they also do not modulate the upstream propeller flow in the same way as blade-resolved simulations. Overall, the study validates that ML-ALM can be a viable model for marine propellers.

## Provider details
- **Doi:** 10.2139/ssrn.7615936
- **Publisher:** Elsevier BV
- **Type:** posted-content

## AI enrichment
- **Concise summary:** A neural actuator-line propeller model trained on oblique-flow simulations is tested on unseen conditions and hull-rudder interactions, with reported speedups relative to blade-resolved simulations.
- **Why it matters:** It illustrates physics-surrogate tradeoffs at engineering scale, including timestep and grid savings beyond inference cost.
- **Caveat:** The preprint's accuracy and fivefold speedup are unverified; the abstract notes spurious force unsteadiness and imperfect upstream-flow modulation, and this is not atomistic modeling.
- **Evidence:** [Captured source](https://doi.org/10.2139/ssrn.7615936); analysis based only on captured metadata, not independently verified full text.
