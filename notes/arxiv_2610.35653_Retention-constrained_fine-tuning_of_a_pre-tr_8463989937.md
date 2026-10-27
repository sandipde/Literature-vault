---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: ML interatomic potentials
enrichment_tags: [active-learning, potential-fine-tuning, mechanical-retention]
title: Retention-constrained fine-tuning of a pre-trained aluminium MACE potential
  for non-equilibrium defect dynamics and plasticity
type: arxiv
source: https://arxiv.org/abs/2610.35653
canonical_url: https://arxiv.org/abs/2610.35653
captured_by: auto-scanner
date: '2026-10-27'
captured_at: '2026-10-27T10:10:23+00:00'
last_requested: '2026-10-27T10:10:23+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Yue Wu
- Yuan Tian
- Deng Pan
- Mingwei Chen
published: '2026-10-26'
abstract: 'Adapting a pre-trained machine-learning interatomic potential for non-equilibrium
  defect dynamics and plasticity requires improving defect accuracy without degrading
  the near-equilibrium elastic and vibrational response. Here we achieve this balance
  for the aluminium MACE potential QP17 by integrating conditional readout uncertainty,
  iterative full-parameter updates and protocol-compatible relative-energy anchoring.
  Sensitivities over 144 linear readout weights guide acquisition, with within-batch
  covariance updates and evolving neural representations. After four active-learning
  rounds (32 acquired configurations and 400 gradient updates), force-uncertainty
  acquisition reduces mean development force error from 22.43 to 21.52 meV/Angstrom,
  outperforming random sampling (22.70), geometry-diversity selection (22.46) and
  uniform training across all 104 candidate labels (22.71) under the same update budget.
  All three force-uncertainty runs satisfy bulk-mechanical retention criteria: historical
  relative-energy error decreases from 0.375 to 0.207 meV/atom, while harmonic phonon
  root-mean-square drift remains below 0.05 THz. Matched objective ablations reveal
  that relative-energy anchoring suppresses harmonic drift. Out-of-sample evaluations
  across planar faults, twin boundaries and grain boundaries demonstrate transferable
  gains in defect energies and deviatoric stresses, even though virial stresses are
  never fitted. A closed-loop molecular dynamics and density functional theory (MD-DFT)
  pilot confirms that automated acceptance gating intercepts updates that violate
  historical elastic-group energy or vibrational tolerances. Together, these components
  establish a retention-constrained fine-tuning protocol for improving plastic-deformation
  observables while preserving the tested bulk mechanical response.'
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.35653'
  categories:
  - cond-mat.mtrl-sci
---

# Retention-constrained fine-tuning of a pre-trained aluminium MACE potential for non-equilibrium defect dynamics and plasticity

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.35653
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Yue Wu, Yuan Tian, Deng Pan, Mingwei Chen
- **Published:** 2026-10-26

## Summary
Adapting a pre-trained machine-learning interatomic potential for non-equilibrium defect dynamics and plasticity requires improving defect accuracy without degrading the near-equilibrium elastic and vibrational response. Here we achieve this balance for the aluminium MACE potential QP17 by integrating conditional readout uncertainty, iterative full-parameter updates and protocol-compatible relative-energy anchoring. Sensitivities over 144 linear readout weights guide acquisition, with within-batch covariance updates and evolving neural representations. After four active-learning rounds (32 acquired configurations and 400 gradient updates), force-uncertainty acquisition reduces mean development force error from 22.43 to 21.52 meV/Angstrom, outperforming random sampling (22.70), geometry-diversity selection (22.46) and uniform training across all 104 candidate labels (22.71) under the same update budget. All three force-uncertainty runs satisfy bulk-mechanical retention criteria: historical relative-energy error decreases from 0.375 to 0.207 meV/atom, while harmonic phonon root-mean-square drift remains below 0.05 THz. Matched objective ablations reveal that relative-energy anchoring suppresses harmonic drift. Out-of-sample evaluations across planar faults, twin boundaries and grain boundaries demonstrate transferable gains in defect energies and deviatoric stresses, even though virial stresses are never fitted. A closed-loop molecular dynamics and density functional theory (MD-DFT) pilot confirms that automated acceptance gating intercepts updates that violate historical elastic-group energy or vibrational tolerances. Together, these components establish a retention-constrained fine-tuning protocol for improving plastic-deformation observables while preserving the tested bulk mechanical response.

## Provider details
- **Arxiv Id:** 2610.35653
- **Categories:** ["cond-mat.mtrl-sci"]

## AI enrichment

- **Concise summary:** The study fine-tunes an aluminium MACE potential for defect behavior while using relative-energy anchoring and acceptance gates to retain tested bulk responses.
- **Why it matters:** Treating retention as an explicit constraint addresses the risk that specialization damages already useful material properties.
- **Caveat:** Preprint evidence concerns one starting potential and selected aluminium tests; reported force-error improvements are modest and broader transfer is unproven.
- **Evidence:** [Captured source](https://arxiv.org/abs/2610.35653); analysis based only on captured metadata, not independently verified full text.
