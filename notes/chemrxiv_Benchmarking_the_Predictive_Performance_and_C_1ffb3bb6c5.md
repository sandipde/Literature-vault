---
title: Benchmarking the Predictive Performance and Computational Cost of Machine Learning
  Models for Functional Group Identification from Experimental Infrared Spectra
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15012296/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15012296/v1
captured_by: auto-scanner
date: '2026-11-17'
captured_at: '2026-11-17T14:04:00+00:00'
last_requested: '2026-11-17T14:04:00+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Yitian Kong
published: '2026-11-17'
abstract: Automated functional group identification from infrared (IR) spectra has
  attracted a wide range of machine learning architectures, but differences in datasets,
  training protocols, and reported metrics hinder direct comparison. Here, we systematically
  benchmark 11 model configurations across five experimental IR benchmarks derived
  from NIST gas-phase, liquid-phase, solid-phase, and pooled spectra, together with
  an independent Chemotion collection. All models are evaluated using consistent spectral
  preprocessing, structure-derived functional group annotations, shared data partitions
  within each benchmark, and five-fold cross-validation with validation-based model
  selection. Predictive performance is assessed with Macro-F1 and exact match ratio,
  and computational cost with parameter count, inference computation, and estimated
  training computation. Despite differences in spectral sources and physical phases,
  model rankings remain highly consistent across benchmarks, with pairwise Spearman
  correlations of 0.945 to 0.991. One-dimensional CNNs lead in every benchmark and
  stay within 5 percentage points of the best score, whereas the gap between the best
  and worst configurations widens from 12--13 percentage points on the two largest
  benchmarks to 34--42 points on the smaller collections. Computational requirements
  differ by orders of magnitude, even among models with comparable predictive performance.
  A multilayer perceptron (Fine MLP) and the DualHeadCNN family form the performance--cost
  Pareto frontier in every benchmark, joined by IRCNN in four of the five. Fine MLP
  offers competitive accuracy at less than 1/500 of the inference computation of DualHeadCNN.
  Together, these findings provide a standardized assessment of predictive performance
  and computational efficiency, offering practical guidance for selecting machine
  learning models for experimental IR functional group identification.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15012296/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Benchmarking the Predictive Performance and Computational Cost of Machine Learning Models for Functional Group Identification from Experimental Infrared Spectra

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15012296/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Yitian Kong
- **Published:** 2026-11-17

## Summary
Automated functional group identification from infrared (IR) spectra has attracted a wide range of machine learning architectures, but differences in datasets, training protocols, and reported metrics hinder direct comparison. Here, we systematically benchmark 11 model configurations across five experimental IR benchmarks derived from NIST gas-phase, liquid-phase, solid-phase, and pooled spectra, together with an independent Chemotion collection. All models are evaluated using consistent spectral preprocessing, structure-derived functional group annotations, shared data partitions within each benchmark, and five-fold cross-validation with validation-based model selection. Predictive performance is assessed with Macro-F1 and exact match ratio, and computational cost with parameter count, inference computation, and estimated training computation. Despite differences in spectral sources and physical phases, model rankings remain highly consistent across benchmarks, with pairwise Spearman correlations of 0.945 to 0.991. One-dimensional CNNs lead in every benchmark and stay within 5 percentage points of the best score, whereas the gap between the best and worst configurations widens from 12--13 percentage points on the two largest benchmarks to 34--42 points on the smaller collections. Computational requirements differ by orders of magnitude, even among models with comparable predictive performance. A multilayer perceptron (Fine MLP) and the DualHeadCNN family form the performance--cost Pareto frontier in every benchmark, joined by IRCNN in four of the five. Fine MLP offers competitive accuracy at less than 1/500 of the inference computation of DualHeadCNN. Together, these findings provide a standardized assessment of predictive performance and computational efficiency, offering practical guidance for selecting machine learning models for experimental IR functional group identification.

## Provider details
- **Doi:** 10.26434/chemrxiv.15012296/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
