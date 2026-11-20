---
title: 'AdsNet: A Graph Neural Network for Direct Adsorption Energy Prediction'
type: arxiv
source: https://arxiv.org/abs/2611.25646
canonical_url: https://arxiv.org/abs/2611.25646
captured_by: auto-scanner
date: '2026-11-20'
captured_at: '2026-11-20T22:56:01+00:00'
last_requested: '2026-11-20T22:56:01+00:00'
issue: scan:arxiv-ml-atomistic
status: to-read
authors:
- Changzhi Ai
- Frank Abild-Pedersen
- Johannes Voss
published: '2026-11-19'
abstract: Fast and accurate prediction of adsorption energies is critical for high-throughput
  computational catalyst screening, existing methods compromise either on evaluation
  speed (full-graph machine learning potentials) or geometric sensitivity (coordination-based
  models like the alpha-scheme). Here, we present AdsNet, an equivariant graph neural
  network that directly predicts adsorption energies in a single forward pass, which
  operates on a local graph restricted only to adsorbate atoms and its immediate surface
  neighbors within a cutoff radius. This local graph formulation decouples computational
  complexity from total system size while encoding continuous geometric features (interatomic
  distances and directional vectors) enabling sensitivity to subtle variations in
  local bonding environments. AdsNet adopts a message-passing architecture with scalar
  and vector node features over multiple interaction layers. Trained on AdsTraj, a
  dataset of 33,920 density functional theory (DFT) calculated structures spanning
  26 transition metals and 6 adsorbates (H*, C*, O*, CO*, OH*, HOCO*), the model achieves
  an adsorption energy root-mean-square error (RMSE) of 0.032 eV and a force RMSE
  of 0.047 eV/A. Analytic forces obtained via automatic differentiation enable structure
  relaxation through a projected gradient descent algorithm with adaptive line search,
  eliminating entire geometry optimizations. Additionally, AdsNet uniquely decomposes
  predicted adsorption energies into contributions from individual atoms within the
  local adsorbate graph - an interpretability feature unattainable with conventional
  machine-learning potentials. AdsNet thus establishes an accurate, highly efficient,
  and interpretable framework for large-scale adsorption energy prediction and local
  interface relaxation across various material surfaces.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.25646'
  categories:
  - cond-mat.mtrl-sci
  - cs.LG
  - physics.comp-ph
---

# AdsNet: A Graph Neural Network for Direct Adsorption Energy Prediction

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.25646
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Changzhi Ai, Frank Abild-Pedersen, Johannes Voss
- **Published:** 2026-11-19

## Summary
Fast and accurate prediction of adsorption energies is critical for high-throughput computational catalyst screening, existing methods compromise either on evaluation speed (full-graph machine learning potentials) or geometric sensitivity (coordination-based models like the alpha-scheme). Here, we present AdsNet, an equivariant graph neural network that directly predicts adsorption energies in a single forward pass, which operates on a local graph restricted only to adsorbate atoms and its immediate surface neighbors within a cutoff radius. This local graph formulation decouples computational complexity from total system size while encoding continuous geometric features (interatomic distances and directional vectors) enabling sensitivity to subtle variations in local bonding environments. AdsNet adopts a message-passing architecture with scalar and vector node features over multiple interaction layers. Trained on AdsTraj, a dataset of 33,920 density functional theory (DFT) calculated structures spanning 26 transition metals and 6 adsorbates (H*, C*, O*, CO*, OH*, HOCO*), the model achieves an adsorption energy root-mean-square error (RMSE) of 0.032 eV and a force RMSE of 0.047 eV/A. Analytic forces obtained via automatic differentiation enable structure relaxation through a projected gradient descent algorithm with adaptive line search, eliminating entire geometry optimizations. Additionally, AdsNet uniquely decomposes predicted adsorption energies into contributions from individual atoms within the local adsorbate graph - an interpretability feature unattainable with conventional machine-learning potentials. AdsNet thus establishes an accurate, highly efficient, and interpretable framework for large-scale adsorption energy prediction and local interface relaxation across various material surfaces.

## Provider details
- **Arxiv Id:** 2611.25646
- **Categories:** ["cond-mat.mtrl-sci", "cs.LG", "physics.comp-ph"]
