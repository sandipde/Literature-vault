---
title: A BAYESIAN PHYSICS-DRIVEN NEURAL NETWORK FOR ELASTIC LOG PREDICTION VIA CROSS-BASIN
  TRANSFER LEARNING
type: paper
source: https://doi.org/10.22541/essoar.15011385/v1
canonical_url: https://doi.org/10.22541/essoar.15011385/v1
captured_by: auto-scanner
date: '2026-11-01'
captured_at: '2026-11-01T11:37:28+00:00'
last_requested: '2026-11-01T11:37:28+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Vivek Thomas
- Shib Sankar Ganguli
- Prakash Kumar
published: '2026-11-01'
abstract: Driven by the demands of reservoir characterization, accurate elastic log
  prediction remains a critical research priority that bridges rock physical properties
  with seismic responses for hydrocarbon exploration. Elastic logs are conventionally
  estimated using rock physics models (RPMs) or, more recently, machine learning (ML)
  frameworks. However, these RPMs are constrained by idealized assumptions and fail
  to account for uncertainty, whereas existing ML approaches often lack physical constraints.
  To address this, Bayesian Neural Networks (BNNs) have proven successful in quantitative
  log prediction by simultaneously enhancing accuracy and quantifying model uncertainty.
  We introduce a novel BNN framework designed for the quantitative estimation of elastic
  properties from well logs. By integrating rock physics constraints via a physics-based
  loss term derived from synthetic velocity realizations, the proposed method ensures
  physically consistent predictions and calibrated uncertainty. Using variational
  inference (VI) governed by the Kullback-Leibler divergence objective function, the
  framework approximates the neural network’s posterior distribution to generate ensemble
  predictions that closely align with the target logs. To bridge the gap between velocity
  measurements and rock physical properties, the network incorporates a physics-dependent
  loss term derived from various combinations of velocity realizations. Furthermore,
  we employ cross-domain adaptation via a two-stage fine-tuning transfer learning
  strategy to predict seismic velocities in an unseen basin. By utilizing selective
  layer updates and regularization on a limited subset of target well data, the framework
  adapts the pre-trained BNN without sacrificing prior knowledge, ensuring physically
  meaningful predictions and physically consistent trends despite domain shift. When
  tested on field datasets from the Canning Basin (Western Australia) and the Sichuan
  Basin (China), our proposed approach outperformed the standard BNN, delivering higher
  correlation coefficients, lower prediction errors, and lower uncertainties. Remarkably,
  this framework offers a scalable, robust paradigm for subsurface characterization
  in complex, data-limited regimes by synthesizing physics-informed constraints with
  cross-domain transfer learning.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.22541/essoar.15011385/v1
  journal: ''
  publisher: Wiley
  type: posted-content
  subjects: []
---

# A BAYESIAN PHYSICS-DRIVEN NEURAL NETWORK FOR ELASTIC LOG PREDICTION VIA CROSS-BASIN TRANSFER LEARNING

- **Type:** paper
- **Source:** https://doi.org/10.22541/essoar.15011385/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Vivek Thomas, Shib Sankar Ganguli, Prakash Kumar
- **Published:** 2026-11-01

## Summary
Driven by the demands of reservoir characterization, accurate elastic log prediction remains a critical research priority that bridges rock physical properties with seismic responses for hydrocarbon exploration. Elastic logs are conventionally estimated using rock physics models (RPMs) or, more recently, machine learning (ML) frameworks. However, these RPMs are constrained by idealized assumptions and fail to account for uncertainty, whereas existing ML approaches often lack physical constraints. To address this, Bayesian Neural Networks (BNNs) have proven successful in quantitative log prediction by simultaneously enhancing accuracy and quantifying model uncertainty. We introduce a novel BNN framework designed for the quantitative estimation of elastic properties from well logs. By integrating rock physics constraints via a physics-based loss term derived from synthetic velocity realizations, the proposed method ensures physically consistent predictions and calibrated uncertainty. Using variational inference (VI) governed by the Kullback-Leibler divergence objective function, the framework approximates the neural network’s posterior distribution to generate ensemble predictions that closely align with the target logs. To bridge the gap between velocity measurements and rock physical properties, the network incorporates a physics-dependent loss term derived from various combinations of velocity realizations. Furthermore, we employ cross-domain adaptation via a two-stage fine-tuning transfer learning strategy to predict seismic velocities in an unseen basin. By utilizing selective layer updates and regularization on a limited subset of target well data, the framework adapts the pre-trained BNN without sacrificing prior knowledge, ensuring physically meaningful predictions and physically consistent trends despite domain shift. When tested on field datasets from the Canning Basin (Western Australia) and the Sichuan Basin (China), our proposed approach outperformed the standard BNN, delivering higher correlation coefficients, lower prediction errors, and lower uncertainties. Remarkably, this framework offers a scalable, robust paradigm for subsurface characterization in complex, data-limited regimes by synthesizing physics-informed constraints with cross-domain transfer learning.

## Provider details
- **Doi:** 10.22541/essoar.15011385/v1
- **Publisher:** Wiley
- **Type:** posted-content
