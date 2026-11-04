---
title: A Machine Learning Approach to logBB Prediction Combining Molecular Docking
  and Quantum-Chemical Descriptors
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011661/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011661/v1
captured_by: auto-scanner
date: '2026-11-04'
captured_at: '2026-11-04T12:44:30+00:00'
last_requested: '2026-11-04T12:44:30+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Lilian Rouille
published: '2026-11-04'
abstract: 'Blood–brain barrier (BBB) permeability is a major challenge in the development
  of drugs targeting the central nervous system (CNS). Computational prediction methods
  can help prioritize candidate compounds and reduce the experimental workload during
  early drug discovery. In this study, machine learning models were developed to predict
  the blood-to-brain concentration ratio expressed as its decimal logarithm (logBB).
  The objective was to investigate whether molecular docking scores obtained with
  AutoDock Vina for P-glycoprotein (P-gp) and breast cancer resistance protein (BCRP),
  together with quantum-chemical descriptors, could provide additional information
  for logBB prediction. The dataset comprised 685 compounds. A linear regression analysis
  identified eight factors associated with logBB: hydrogen bond donors, gas-phase
  electronic energy, electronic energy difference between water and hexane, number
  of heavy atoms, LogP, gas-phase geometry optimization time, number of aromatic rings,
  and fraction of sp3-hybridized carbon atoms. Notably, the electronic energy difference
  between water and hexane showed a stronger association with logBB than the corresponding
  Gibbs free energy difference, suggesting that electronic energy descriptors may
  provide complementary information. Higher-level quantum-chemical calculations will
  be required to investigate this finding further. Twenty-one machine learning models
  were evaluated. The selected support vector regression model using a radial basis
  function kernel (SVR-RBF; C = 0.869, ε = 0.135, γ = 0.165) was trained on 585 compounds
  and evaluated on a held-out validation set of 100 compounds, achieving an R2 of
  0.605, an MAE of 0.368, and an RMSE of 0.459. Finally, the computational time analysis
  showed that descriptor generation was strongly dependent on molecular weight, with
  quantum-chemical calculations and molecular docking accounting for most of the computational
  cost. Overall, this work highlights the potential of combining physicochemical,
  molecular docking, and quantum-chemical descriptors for machine learning-based logBB
  prediction.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011661/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# A Machine Learning Approach to logBB Prediction Combining Molecular Docking and Quantum-Chemical Descriptors

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011661/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Lilian Rouille
- **Published:** 2026-11-04

## Summary
Blood–brain barrier (BBB) permeability is a major challenge in the development of drugs targeting the central nervous system (CNS). Computational prediction methods can help prioritize candidate compounds and reduce the experimental workload during early drug discovery. In this study, machine learning models were developed to predict the blood-to-brain concentration ratio expressed as its decimal logarithm (logBB). The objective was to investigate whether molecular docking scores obtained with AutoDock Vina for P-glycoprotein (P-gp) and breast cancer resistance protein (BCRP), together with quantum-chemical descriptors, could provide additional information for logBB prediction. The dataset comprised 685 compounds. A linear regression analysis identified eight factors associated with logBB: hydrogen bond donors, gas-phase electronic energy, electronic energy difference between water and hexane, number of heavy atoms, LogP, gas-phase geometry optimization time, number of aromatic rings, and fraction of sp3-hybridized carbon atoms. Notably, the electronic energy difference between water and hexane showed a stronger association with logBB than the corresponding Gibbs free energy difference, suggesting that electronic energy descriptors may provide complementary information. Higher-level quantum-chemical calculations will be required to investigate this finding further. Twenty-one machine learning models were evaluated. The selected support vector regression model using a radial basis function kernel (SVR-RBF; C = 0.869, ε = 0.135, γ = 0.165) was trained on 585 compounds and evaluated on a held-out validation set of 100 compounds, achieving an R2 of 0.605, an MAE of 0.368, and an RMSE of 0.459. Finally, the computational time analysis showed that descriptor generation was strongly dependent on molecular weight, with quantum-chemical calculations and molecular docking accounting for most of the computational cost. Overall, this work highlights the potential of combining physicochemical, molecular docking, and quantum-chemical descriptors for machine learning-based logBB prediction.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011661/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
