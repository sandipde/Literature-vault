---
title: Autonomous phase diagram mapping of polymer blends through SAXS-guided active
  learning
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15012310/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15012310/v1
captured_by: auto-scanner
date: '2026-11-17'
captured_at: '2026-11-17T14:04:00+00:00'
last_requested: '2026-11-17T14:04:00+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Saroj Upreti
- Kailash Adhikari
- Sabin Baral
- Yunfei Wang
- Boran Ma
- Chenhui Zhu
- Marcus Noack
- Xiaodan Gu
published: '2026-11-17'
abstract: Autonomous phase behavior mapping from multicomponent copolymer formulation
  requires feedback that connects scattering measurements to experimental decisions.
  We couple robotic polymer formulation, automated small-angle X-ray scattering (SAXS)
  analysis, and Gaussian-process active learning using structure factor to autonomously
  map complex phase behavior of multiblock copolymer/homopolymer blends. This dimensionless
  descriptor, based on secondary and primary scattering peak ratio q2/q1, captures
  relative reciprocal-space geometry while removing a common structural length scale
  when the same reflections are tracked. An ordering model identifies compositions
  with sharp scattering features, and a conditional regressor learns the ratio surface.
  An acquisition function weighted by ordering probability combines predicted ratio
  gradients with length-scale-adjusted uncertainty to direct measurements towards
  candidate structural transitions. Ternary blends of poly(1,4-isoprene-block-styrene-block-2-vinylpyridine),
  polystyrene and poly(2-vinylpyridine) provide the experimental test system. Starting
  from 15 initial formulations, the algorithm progressively refines an irregular phase
  map over 10 additional rounds with 5 experiments for each additional round. Across
  iterations 9-11, the mean absolute change in predicted q2/q1 between successive
  maps decreases from 0.044 to 0.012 over their common predicted ordered region, while
  mean predictive uncertainty remains approximately 0.08, indicating Gaussian-process
  active learning captured the unknown phase map of ternary blend system. The active
  learning uses only 1.26% of the formulations in a complete ternary grid at 1% composition
  increments. The resulting phase maps reveal regions consistent with BCC-packed spheres,
  hexagonally packed cylinders, and lamellae. Weakly ordered structures appear at
  high PS loading, while boundary samples show signatures of coexistence or network
  morphologies. The workflow is adaptable to other periodically ordered materials
  by using resolved scattering-peak ratios as feedback and training the model on measurements
  from each system. This will enable autonomous phase mapping for ordered material
  with different structure factors before every region has a definitive morphology
  label, while retaining the evidence needed for materials-specific interpretation.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15012310/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Autonomous phase diagram mapping of polymer blends through SAXS-guided active learning

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15012310/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Saroj Upreti, Kailash Adhikari, Sabin Baral, Yunfei Wang, Boran Ma, Chenhui Zhu, Marcus Noack, Xiaodan Gu
- **Published:** 2026-11-17

## Summary
Autonomous phase behavior mapping from multicomponent copolymer formulation requires feedback that connects scattering measurements to experimental decisions. We couple robotic polymer formulation, automated small-angle X-ray scattering (SAXS) analysis, and Gaussian-process active learning using structure factor to autonomously map complex phase behavior of multiblock copolymer/homopolymer blends. This dimensionless descriptor, based on secondary and primary scattering peak ratio q2/q1, captures relative reciprocal-space geometry while removing a common structural length scale when the same reflections are tracked. An ordering model identifies compositions with sharp scattering features, and a conditional regressor learns the ratio surface. An acquisition function weighted by ordering probability combines predicted ratio gradients with length-scale-adjusted uncertainty to direct measurements towards candidate structural transitions. Ternary blends of poly(1,4-isoprene-block-styrene-block-2-vinylpyridine), polystyrene and poly(2-vinylpyridine) provide the experimental test system. Starting from 15 initial formulations, the algorithm progressively refines an irregular phase map over 10 additional rounds with 5 experiments for each additional round. Across iterations 9-11, the mean absolute change in predicted q2/q1 between successive maps decreases from 0.044 to 0.012 over their common predicted ordered region, while mean predictive uncertainty remains approximately 0.08, indicating Gaussian-process active learning captured the unknown phase map of ternary blend system. The active learning uses only 1.26% of the formulations in a complete ternary grid at 1% composition increments. The resulting phase maps reveal regions consistent with BCC-packed spheres, hexagonally packed cylinders, and lamellae. Weakly ordered structures appear at high PS loading, while boundary samples show signatures of coexistence or network morphologies. The workflow is adaptable to other periodically ordered materials by using resolved scattering-peak ratios as feedback and training the model on measurements from each system. This will enable autonomous phase mapping for ordered material with different structure factors before every region has a definitive morphology label, while retaining the evidence needed for materials-specific interpretation.

## Provider details
- **Doi:** 10.26434/chemrxiv.15012310/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
