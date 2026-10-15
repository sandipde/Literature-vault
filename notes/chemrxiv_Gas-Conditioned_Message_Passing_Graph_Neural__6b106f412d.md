---
title: Gas-Conditioned Message Passing Graph Neural Network for Permeability Prediction
  in Polymeric Membranes
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010381/v2
canonical_url: https://doi.org/10.26434/chemrxiv.15010381/v2
captured_by: auto-scanner
date: '2026-10-15'
captured_at: '2026-10-15T09:34:27+00:00'
last_requested: '2026-10-15T09:34:27+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Krishnendu Mukherjee
- Zidan Zhang
- Mohammed Alshammasi
- Mohammed G. Hashim
- Hussain H. Naji
- Zainab A. Aithan
- Jihad A. Badra
- Jalal Yagoubi
- Hussain B. Tuwailib
- Ali Hayek
- Venkat Ganesan
published: '2026-10-15'
abstract: Designing polymeric membranes for diverse gas-separation applications remains
  a critical challenge. Machine learning (ML) models can significantly accelerate
  this effort by capturing complex relationships between polymer-gas pairs and enabling
  permeability prediction over an extended chemical space of gases and polymers. In
  this work, we present a novel ML framework, the gas-conditioned message passing
  neural network (GC-MPNN), that jointly combines gas descriptors and polymer chemistry
  in a fused neural network model. Polymers are represented at the monomer level and
  encoded as molecular graphs, where node and edge information is propagated through
  message-passing layers. Six gas species (He, H2, N2, O2, CH4, and CO2) are represented
  using multiple descriptor sets spanning thermodynamic, kinetic, and electrostatic
  properties, along with one-hot encodings and combined feature sets that include
  kinetic plus thermodynamic descriptors and the full physicochemical descriptor set.
  For each descriptor combination, model hyperparameters are optimized using Bayesian
  optimization within a leave-one-gas-out (LOGO) validation framework. Test performance
  is then evaluated on the gas species excluded entirely from the corresponding training
  fold (out-of-training set) and compared across descriptor sets. For most gas species,
  the model achieves strong predictive performance (R2 ∼ 0.86–0.96), while CO2 remains
  more challenging in terms of absolute prediction accuracy (R2 ∼ 0.44). Active learning
  sampling further improves model performance by adding a few labeled samples from
  the test gas species into the training set. Among the three strategies tested, deep
  ensemble-based sampling and random sampling show strong improvement, with R2 reaching
  approximately ∼ 0.95 for all gas species, while evidential regression shows less
  consistent improvement. The model is further evaluated on a smaller polymer-gas
  dataset containing hydrocarbon species (C2H4, C2H6, C3H6, C3H8, and n-C4H10) using
  the GC-MPNN trained only on the six base gases, achieving moderate to strong Pearson
  correlations (r ∼ 0.77–0.89) for these out-of-training gases. Overall, this work
  presents a machine learning model that can learn transferable polymer-gas relationships
  from known gas species and extend them to previously unseen gases.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010381/v2
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Gas-Conditioned Message Passing Graph Neural Network for Permeability Prediction in Polymeric Membranes

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010381/v2
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Krishnendu Mukherjee, Zidan Zhang, Mohammed Alshammasi, Mohammed G. Hashim, Hussain H. Naji, Zainab A. Aithan, Jihad A. Badra, Jalal Yagoubi, Hussain B. Tuwailib, Ali Hayek, Venkat Ganesan
- **Published:** 2026-10-15

## Summary
Designing polymeric membranes for diverse gas-separation applications remains a critical challenge. Machine learning (ML) models can significantly accelerate this effort by capturing complex relationships between polymer-gas pairs and enabling permeability prediction over an extended chemical space of gases and polymers. In this work, we present a novel ML framework, the gas-conditioned message passing neural network (GC-MPNN), that jointly combines gas descriptors and polymer chemistry in a fused neural network model. Polymers are represented at the monomer level and encoded as molecular graphs, where node and edge information is propagated through message-passing layers. Six gas species (He, H2, N2, O2, CH4, and CO2) are represented using multiple descriptor sets spanning thermodynamic, kinetic, and electrostatic properties, along with one-hot encodings and combined feature sets that include kinetic plus thermodynamic descriptors and the full physicochemical descriptor set. For each descriptor combination, model hyperparameters are optimized using Bayesian optimization within a leave-one-gas-out (LOGO) validation framework. Test performance is then evaluated on the gas species excluded entirely from the corresponding training fold (out-of-training set) and compared across descriptor sets. For most gas species, the model achieves strong predictive performance (R2 ∼ 0.86–0.96), while CO2 remains more challenging in terms of absolute prediction accuracy (R2 ∼ 0.44). Active learning sampling further improves model performance by adding a few labeled samples from the test gas species into the training set. Among the three strategies tested, deep ensemble-based sampling and random sampling show strong improvement, with R2 reaching approximately ∼ 0.95 for all gas species, while evidential regression shows less consistent improvement. The model is further evaluated on a smaller polymer-gas dataset containing hydrocarbon species (C2H4, C2H6, C3H6, C3H8, and n-C4H10) using the GC-MPNN trained only on the six base gases, achieving moderate to strong Pearson correlations (r ∼ 0.77–0.89) for these out-of-training gases. Overall, this work presents a machine learning model that can learn transferable polymer-gas relationships from known gas species and extend them to previously unseen gases.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010381/v2
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
