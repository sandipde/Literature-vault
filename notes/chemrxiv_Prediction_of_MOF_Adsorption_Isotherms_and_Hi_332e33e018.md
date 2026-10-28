---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [mof-adsorption, pressure-conditioning, graph-neural-networks, surrogate-models]
title: Prediction of MOF Adsorption Isotherms and High-Throughput Screening Using
  a Physics-Informed Membranes Graph Neural Network
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010295/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15010295/v1
captured_by: auto-scanner
date: '2026-10-12'
captured_at: '2026-10-12T23:25:53+00:00'
last_requested: '2026-10-12T23:25:53+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Li Linfeng
- Xingshuo Fan
- Ning Zhang
published: '2026-10-12'
abstract: Metal-organic frameworks (MOFs) are prime CO 2 -capture candidates, but
  grand canonical Monte Carlo (GCMC) screening is costly when full isotherms, not
  single uptakes, are required; machine learning surrogates rarely resolve the continuous
  pressure response. We report a physics-informed pressure-aware multi-task graph
  neural network (PI-MGNN) to predict CO 2 uptake at arbitrary pressure and reconstruct
  isotherms from structure. From ~130,000 candidates, PCA and K-means select 5,023
  representative MOFs, each simulated by GCMC at five pressures spanning 0.1-5.0 MPa,
  enforcing a continuous pressure response. Crystal graphs are processed by decoupled
  geometric and electrostatic graph-attention branches with auxiliary supervision,
  while a Gaussian-expanded pressure query is fused by cross-attention. PI-MGNN attains
  R 2 = 0.977 and MAE = 0.291 mol kg -1 ; isotherm MAEs are 0.428/0.312/0.330 mol
  kg -1 for high/medium/low-uptake MOFs, and cross-attention improves accuracy by
  6.3%. Attention weights recover the pressure-resolved physics, enabling accurate
  and interpretable high-throughput screening.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010295/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Prediction of MOF Adsorption Isotherms and High-Throughput Screening Using a Physics-Informed Membranes Graph Neural Network

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010295/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Li Linfeng, Xingshuo Fan, Ning Zhang
- **Published:** 2026-10-12

## Summary
Metal-organic frameworks (MOFs) are prime CO 2 -capture candidates, but grand canonical Monte Carlo (GCMC) screening is costly when full isotherms, not single uptakes, are required; machine learning surrogates rarely resolve the continuous pressure response. We report a physics-informed pressure-aware multi-task graph neural network (PI-MGNN) to predict CO 2 uptake at arbitrary pressure and reconstruct isotherms from structure. From ~130,000 candidates, PCA and K-means select 5,023 representative MOFs, each simulated by GCMC at five pressures spanning 0.1-5.0 MPa, enforcing a continuous pressure response. Crystal graphs are processed by decoupled geometric and electrostatic graph-attention branches with auxiliary supervision, while a Gaussian-expanded pressure query is fused by cross-attention. PI-MGNN attains R 2 = 0.977 and MAE = 0.291 mol kg -1 ; isotherm MAEs are 0.428/0.312/0.330 mol kg -1 for high/medium/low-uptake MOFs, and cross-attention improves accuracy by 6.3%. Attention weights recover the pressure-resolved physics, enabling accurate and interpretable high-throughput screening.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010295/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment
- **Concise summary:** PI-MGNN combines geometric and electrostatic crystal-graph branches with pressure queries to predict CO2 uptake and isotherms from GCMC data for 5,023 selected MOFs.
- **Why it matters:** Pressure conditioning targets an adsorption curve rather than a single uptake value, making the surrogate more directly relevant to operating-condition screening.
- **Caveat:** The v1 abstract's accuracy is against simulation data sampled at five pressures; arbitrary-pressure reliability and physical interpretation of attention weights are not independently established.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15010295/v1); analysis based only on captured metadata, not independently verified full text.
