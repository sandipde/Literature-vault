---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Other and possible scan noise
enrichment_tags: [cell-fate, attractor-landscapes, transcriptomic-models]
title: 'Attractor Landscapes and Network Dynamics of iPSC-Derived Neural Stem Cell
  Plasticity: A Complexity-Theoretic Benchmark of Cell-Fate Transitions'
type: paper
source: https://doi.org/10.20944/preprints202610.2330.v1
canonical_url: https://doi.org/10.20944/preprints202610.2330.v1
captured_by: auto-scanner
date: '2026-10-26'
captured_at: '2026-10-26T10:43:25+00:00'
last_requested: '2026-10-26T10:43:25+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Abicumaran Uthamacumaran
published: '2026-10-26'
abstract: Cell fate decisions are often studied as static transcriptomic snapshots
  even though differentiation is intrinsically a complex dynamical, multistable, and
  plastic process. To better elucidate cell fate plasticity dynamics, we developed
  a complexity-theoretic and machine learning framework to model neural stem cell
  state-transitions using a two-time point single-cell RNA-sequencing subset of GSE138121
  (iPSC-derived motor neurons). The primary cohort comprised 1,960 quality-controlled
  cells from the Batch A control iPSC line at days 12 and 18, represented by 815 genes
  and 62 metacells. Ten neural/progenitor states were annotated and contrasted with
  NNMF and Leiden communities. We integrated forward-in-time metacell transport, quasi-potential
  landscapes, basin and dwell-time analysis, Spearman and Kauffman Random Boolean
  Networks, BDM perturbation analysis, and 5-fold cross-validation of classical machine
  learning and deep learning models. Transition kernels showed broad funneling toward
  the neuroblast/immature-neuron state. The continuous attractor landscape resolved
  four basins, while the 180-node, 1,080-edge Boolean Kauffman abstraction produced
  18 attractors, basin entropy of 2.75 bits, and Derrida one-bit sensitivity of 1.69,
  indicating damage amplification rather than directly demonstrated critical point.
  Consensus steering prioritized ONECUT2, ZFP36L1, DCX, HOXB2, TMEM123, TUBA1A, ENO1,
  ELAVL4, MAP1B, and MLLT11. ESN/reservoir computing yielded the lowest latent endpoint
  MAE (0.138), while CTM and Transformer achieved the lowest transition-kernel RMSE
  after validation-selected blending with a training-only state/time prior (0.0402
  and 0.0404). These results support a complex systems view of iPSC-derived neural
  differentiation as trajectories through a multi-basin state-space, linking attractor
  geometry, network topology, and explainable AI to generate testable candidates for
  cell fate control and reprogramming.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.20944/preprints202610.2330.v1
  journal: ''
  publisher: MDPI AG
  type: posted-content
  subjects: []
---

# Attractor Landscapes and Network Dynamics of iPSC-Derived Neural Stem Cell Plasticity: A Complexity-Theoretic Benchmark of Cell-Fate Transitions

- **Type:** paper
- **Source:** https://doi.org/10.20944/preprints202610.2330.v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Abicumaran Uthamacumaran
- **Published:** 2026-10-26

## Summary
Cell fate decisions are often studied as static transcriptomic snapshots even though differentiation is intrinsically a complex dynamical, multistable, and plastic process. To better elucidate cell fate plasticity dynamics, we developed a complexity-theoretic and machine learning framework to model neural stem cell state-transitions using a two-time point single-cell RNA-sequencing subset of GSE138121 (iPSC-derived motor neurons). The primary cohort comprised 1,960 quality-controlled cells from the Batch A control iPSC line at days 12 and 18, represented by 815 genes and 62 metacells. Ten neural/progenitor states were annotated and contrasted with NNMF and Leiden communities. We integrated forward-in-time metacell transport, quasi-potential landscapes, basin and dwell-time analysis, Spearman and Kauffman Random Boolean Networks, BDM perturbation analysis, and 5-fold cross-validation of classical machine learning and deep learning models. Transition kernels showed broad funneling toward the neuroblast/immature-neuron state. The continuous attractor landscape resolved four basins, while the 180-node, 1,080-edge Boolean Kauffman abstraction produced 18 attractors, basin entropy of 2.75 bits, and Derrida one-bit sensitivity of 1.69, indicating damage amplification rather than directly demonstrated critical point. Consensus steering prioritized ONECUT2, ZFP36L1, DCX, HOXB2, TMEM123, TUBA1A, ENO1, ELAVL4, MAP1B, and MLLT11. ESN/reservoir computing yielded the lowest latent endpoint MAE (0.138), while CTM and Transformer achieved the lowest transition-kernel RMSE after validation-selected blending with a training-only state/time prior (0.0402 and 0.0404). These results support a complex systems view of iPSC-derived neural differentiation as trajectories through a multi-basin state-space, linking attractor geometry, network topology, and explainable AI to generate testable candidates for cell fate control and reprogramming.

## Provider details
- **Doi:** 10.20944/preprints202610.2330.v1
- **Publisher:** MDPI AG
- **Type:** posted-content

## AI enrichment

- **Concise summary:** A neural differentiation study combines transcriptomic state modeling, attractor analysis and predictive models to propose candidate regulators of cell-state changes.
- **Why it matters:** Multiple dynamical representations may generate testable hypotheses beyond static cell labels.
- **Caveat:** This off-topic biological preprint uses two sampled time points; inferred trajectories and steering candidates are not observed causal interventions.
- **Evidence:** [Captured source](https://doi.org/10.20944/preprints202610.2330.v1); analysis based only on captured metadata, not independently verified full text.
