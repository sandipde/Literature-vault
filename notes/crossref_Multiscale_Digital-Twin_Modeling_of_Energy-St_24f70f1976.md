---
title: Multiscale Digital-Twin Modeling of Energy-Storage Materials by Integrating
  First-Principles Calculations and Machine-Learning Interatomic Potentials
type: paper
source: https://doi.org/10.4108/ew.14196
canonical_url: https://doi.org/10.4108/ew.14196
captured_by: auto-scanner
date: '2026-10-14'
captured_at: '2026-10-14T09:53:53+00:00'
last_requested: '2026-10-14T09:53:53+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Yan Li
- Duochang Tang
published: '2026-10-14'
abstract: Conventional modeling of energy-storage materials is constrained by the
  computational cost of first-principles calculations, limited electrochemical-state
  awareness in machine-learning interatomic potentials, and weak coupling between
  materials-scale models and online battery decision-making. This study proposes a
  first-principles-constrained electrochemically conditioned machine-learning interatomic
  potential (FP-EMLP) integrated with a multiscale digital-twin framework (FP-EMLP-DT).
  A multistate configuration space spanning ion concentration, temperature, defects,
  strain, and phase boundaries is combined with active learning based on committee
  uncertainty, structural novelty, and physics-based risk. The equivariant graph model
  incorporates electrochemical-state gating, charge-conserving projection, and differentiable
  long-range electrostatics, and is trained using energies, forces, stresses, equilibrium
  voltages, and migration barriers. Predicted diffusion coefficients, free energies,
  elastic tensors, and chemical expansion coefficients are transferred to an electrochemical-mechanical-thermal-damage
  model. The resulting model is further integrated with a physics-based reduced-order
  network, uncertainty-gated residual learning, online data assimilation, and degradation-aware
  control. FP-EMLP achieves mean absolute errors of 6.5 meV atom−1, 33 meV Å−1, 0.051
  V, and 0.038 eV for energy, force, voltage, and migration barrier, respectively,
  with a 4.8% aggregate relative error across multiscale fields. Active learning reduces
  required first-principles labels by 33.3% while covering 91.2% of high-risk configurations.
  FP-EMLP-DT achieves mean absolute errors of 0.93% for state of charge and 1.21%
  for state of health. Degradation-aware control reduces maximum material stress and
  damage increment by 16.5% and 36.8%, respectively, demonstrating an effective multiscale
  pathway from electronic structure to online battery management.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.4108/ew.14196
  journal: EAI Endorsed Transactions on Energy Web
  publisher: European Alliance for Innovation n.o.
  type: journal-article
  subjects: []
---

# Multiscale Digital-Twin Modeling of Energy-Storage Materials by Integrating First-Principles Calculations and Machine-Learning Interatomic Potentials

- **Type:** paper
- **Source:** https://doi.org/10.4108/ew.14196
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Yan Li, Duochang Tang
- **Published:** 2026-10-14

## Summary
Conventional modeling of energy-storage materials is constrained by the computational cost of first-principles calculations, limited electrochemical-state awareness in machine-learning interatomic potentials, and weak coupling between materials-scale models and online battery decision-making. This study proposes a first-principles-constrained electrochemically conditioned machine-learning interatomic potential (FP-EMLP) integrated with a multiscale digital-twin framework (FP-EMLP-DT). A multistate configuration space spanning ion concentration, temperature, defects, strain, and phase boundaries is combined with active learning based on committee uncertainty, structural novelty, and physics-based risk. The equivariant graph model incorporates electrochemical-state gating, charge-conserving projection, and differentiable long-range electrostatics, and is trained using energies, forces, stresses, equilibrium voltages, and migration barriers. Predicted diffusion coefficients, free energies, elastic tensors, and chemical expansion coefficients are transferred to an electrochemical-mechanical-thermal-damage model. The resulting model is further integrated with a physics-based reduced-order network, uncertainty-gated residual learning, online data assimilation, and degradation-aware control. FP-EMLP achieves mean absolute errors of 6.5 meV atom−1, 33 meV Å−1, 0.051 V, and 0.038 eV for energy, force, voltage, and migration barrier, respectively, with a 4.8% aggregate relative error across multiscale fields. Active learning reduces required first-principles labels by 33.3% while covering 91.2% of high-risk configurations. FP-EMLP-DT achieves mean absolute errors of 0.93% for state of charge and 1.21% for state of health. Degradation-aware control reduces maximum material stress and damage increment by 16.5% and 36.8%, respectively, demonstrating an effective multiscale pathway from electronic structure to online battery management.

## Provider details
- **Doi:** 10.4108/ew.14196
- **Journal:** EAI Endorsed Transactions on Energy Web
- **Publisher:** European Alliance for Innovation n.o.
- **Type:** journal-article
