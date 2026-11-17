---
title: 'End-to-End Learning from Experimental Data: Integrating the PC-SAFT Equation
  of State into Neural Network Training for Improved Polymer Parameter Estimation'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011908/v3
canonical_url: https://doi.org/10.26434/chemrxiv.15011908/v3
captured_by: auto-scanner
date: '2026-11-17'
captured_at: '2026-11-17T00:38:12+00:00'
last_requested: '2026-11-17T00:38:12+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Hasan Ismaeel
- Eleonora Ricci
- Panagiotis Krokidas
- Vassilis Gkatsis
- George Giannakopoulos
- Maria Grazia De Angelis
published: '2026-11-16'
abstract: Accurate and computationally efficient thermodynamic models are essential
  for the design, optimization, and operation of many (bio)chemical processes involving
  polymer solutions, blends, and membranes. In this work, we combine machine learning
  (ML) with the PC-SAFT equation of state (EoS) to predict the non-associating pure
  component parameters for polymers, enabling the rapid evaluation of the pressure–volume–temperature
  (PVT) behavior of polymer melts and rubbers. Using a dataset of more than 5,400
  PVT measurements for 78 chemically diverse polymers, we systematically evaluate
  the effects of EoS integration in the training process, the molecular representation,
  neural network architecture, and transfer learning. A baseline approach trained
  on pre-fitted PC-SAFT parameters is compared with a physics-informed approach that
  embeds the EoS in the training loop, enabling end-to-end training directly on experimental
  PVT data. Performance is assessed using 6-fold cross-validation. For a feed-forward
  neural network (FNN) using extended-connectivity fingerprints (ECFPs), embedding
  the EoS reduces the average mean absolute percentage error (MAPE) from 8.67% to
  5.57%. Replacing the FNN and ECFP representation with a graph neural network (GNN)
  using cyclic polymer graphs further reduces the average MAPE to 2.58%. Pre-training
  the models on PC-SAFT parameters for small molecules, followed by fine-tuning on
  polymer PVT data, yields additional improvements, reducing the average MAPE to 5.06%
  for the FNN and 2.15% for the GNN. These results demonstrate the benefits of combining
  an embedded EoS with geometric deep learning and transfer learning for accurate
  polymer PVT predictions.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011908/v3
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# End-to-End Learning from Experimental Data: Integrating the PC-SAFT Equation of State into Neural Network Training for Improved Polymer Parameter Estimation

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011908/v3
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Hasan Ismaeel, Eleonora Ricci, Panagiotis Krokidas, Vassilis Gkatsis, George Giannakopoulos, Maria Grazia De Angelis
- **Published:** 2026-11-16

## Summary
Accurate and computationally efficient thermodynamic models are essential for the design, optimization, and operation of many (bio)chemical processes involving polymer solutions, blends, and membranes. In this work, we combine machine learning (ML) with the PC-SAFT equation of state (EoS) to predict the non-associating pure component parameters for polymers, enabling the rapid evaluation of the pressure–volume–temperature (PVT) behavior of polymer melts and rubbers. Using a dataset of more than 5,400 PVT measurements for 78 chemically diverse polymers, we systematically evaluate the effects of EoS integration in the training process, the molecular representation, neural network architecture, and transfer learning. A baseline approach trained on pre-fitted PC-SAFT parameters is compared with a physics-informed approach that embeds the EoS in the training loop, enabling end-to-end training directly on experimental PVT data. Performance is assessed using 6-fold cross-validation. For a feed-forward neural network (FNN) using extended-connectivity fingerprints (ECFPs), embedding the EoS reduces the average mean absolute percentage error (MAPE) from 8.67% to 5.57%. Replacing the FNN and ECFP representation with a graph neural network (GNN) using cyclic polymer graphs further reduces the average MAPE to 2.58%. Pre-training the models on PC-SAFT parameters for small molecules, followed by fine-tuning on polymer PVT data, yields additional improvements, reducing the average MAPE to 5.06% for the FNN and 2.15% for the GNN. These results demonstrate the benefits of combining an embedded EoS with geometric deep learning and transfer learning for accurate polymer PVT predictions.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011908/v3
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
