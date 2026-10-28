---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [equivariant-networks, solvation-properties, delta-learning, hydration-free-energy]
title: From Vacuum Geometry to Solution-Phase Electronic Properties and Thermodynamics
  via Equivariant Neural Networks
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010245/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15010245/v1
captured_by: auto-scanner
date: '2026-10-12'
captured_at: '2026-10-12T12:41:12+00:00'
last_requested: '2026-10-12T12:41:12+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Mathias Hilfiker
- Lorenzo D’Amore
- Dries Van Rompaey
- Marco Klähn
- Ola Engkvist
- Alexandre Tkatchenko
- Leonardo Medrano Sandonas
published: '2026-10-12'
abstract: We introduce a general framework for predicting solution-phase quantum-mechanical
  (QM) properties of drug-like molecules directly from gas-phase geometries, without
  solvent-specific structural optimization or property calculations. Using current
  equivariant neural network (ENN) architectures, such as MACE and Allegro, we demonstrate
  that they can also predict extensive and intensive QM properties in implicit water
  at a high level of theory. Direct-and ∆-learning strategies are employed for this
  prediction task using the Aquamarine dataset, which provides QM properties for the
  same molecules in both environments. The developed models are systematically evaluated
  for scalability to larger molecules, transferability across chemical space, and
  generalization to out-of-equilibrium configurations. Our results show that, despite
  substantial differences between gas-and solution-phase conformational ensembles,
  the models can accurately reconstruct ensemble-averaged solution-phase properties
  from gas-phase molecular dynamics. We further integrate the learned QM properties
  into the QUEDsol framework (“QUantum Electronic Descriptors in SOLution”) as electronic
  descriptors for hydration free-energy prediction. A simple and interpretable quadratic
  regression model trained on the FreeSolv dataset achieves state-of-the-art performance
  on the challenging and chemically diverse FlexiSol benchmark, outperforming previously
  reported QM-and ML-based approaches. These results establish ENNs as a versatile
  approach for inter-phase molecular property prediction and demonstrate that environment-specific
  QM descriptors generated from gas-phase geometries can provide transferable inputs
  for complex thermodynamic modeling.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010245/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# From Vacuum Geometry to Solution-Phase Electronic Properties and Thermodynamics via Equivariant Neural Networks

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010245/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Mathias Hilfiker, Lorenzo D’Amore, Dries Van Rompaey, Marco Klähn, Ola Engkvist, Alexandre Tkatchenko, Leonardo Medrano Sandonas
- **Published:** 2026-10-12

## Summary
We introduce a general framework for predicting solution-phase quantum-mechanical (QM) properties of drug-like molecules directly from gas-phase geometries, without solvent-specific structural optimization or property calculations. Using current equivariant neural network (ENN) architectures, such as MACE and Allegro, we demonstrate that they can also predict extensive and intensive QM properties in implicit water at a high level of theory. Direct-and ∆-learning strategies are employed for this prediction task using the Aquamarine dataset, which provides QM properties for the same molecules in both environments. The developed models are systematically evaluated for scalability to larger molecules, transferability across chemical space, and generalization to out-of-equilibrium configurations. Our results show that, despite substantial differences between gas-and solution-phase conformational ensembles, the models can accurately reconstruct ensemble-averaged solution-phase properties from gas-phase molecular dynamics. We further integrate the learned QM properties into the QUEDsol framework (“QUantum Electronic Descriptors in SOLution”) as electronic descriptors for hydration free-energy prediction. A simple and interpretable quadratic regression model trained on the FreeSolv dataset achieves state-of-the-art performance on the challenging and chemically diverse FlexiSol benchmark, outperforming previously reported QM-and ML-based approaches. These results establish ENNs as a versatile approach for inter-phase molecular property prediction and demonstrate that environment-specific QM descriptors generated from gas-phase geometries can provide transferable inputs for complex thermodynamic modeling.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010245/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment
- **Concise summary:** Equivariant networks predict implicit-water quantum properties from gas-phase geometries using paired Aquamarine data and direct or delta learning. Learned solution descriptors feed an interpretable hydration-free-energy regression within QUEDsol.
- **Why it matters:** Cross-environment property prediction could avoid repeating solvent-specific calculations while retaining descriptors relevant to solution thermodynamics.
- **Caveat:** This preprint's transfer and benchmark claims are unverified; using MACE or Allegro architectures does not make these property predictors validated molecular-dynamics force fields.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15010245/v1); analysis based only on captured metadata, not independently verified full text.
