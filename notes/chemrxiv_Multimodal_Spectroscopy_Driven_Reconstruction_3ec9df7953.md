---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [spectroscopic-inference, molecular-geometry, conditional-diffusion]
title: Multimodal Spectroscopy–Driven Reconstruction of Three-Dimensional Molecular
  Structures via Conditional Diffusion Model
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011037/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011037/v1
captured_by: auto-scanner
date: '2026-10-26'
captured_at: '2026-10-26T10:43:25+00:00'
last_requested: '2026-10-26T10:43:25+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Wenjie Du
- Xiaohan Qin
- Yixi Shen
- Ledu Wang
- Andreas Burger
- Chuangwei Liu
- Song Wang
- Jun Jiang
- Yang Wang
- Eric Liu
published: '2026-10-26'
abstract: Three-dimensional (3D) molecular structures underpin molecular function
  and dynamics. Spectroscopy can encode rich structural information via energy-level
  transitions, but existing data-driven approaches have largely focused on predicting
  symbolic representations such as SMILES, or molecular topology rather than reconstructing
  full 3D structures. Here, we introduce SpecDiffMol, the first generative framework
  to directly reconstruct full molecular 3D structures from molecular formulae and
  multimodal spectroscopic data, including infrared, Raman, UV–vis, and NMR spectra.
  SpecDiffMol integrates a Transformer-based topology inference module with an E(3)-equivariant
  conditional diffusion model, enabling the inference of molecular connectivity, global
  structure, and fine-grained conformational geometry in a unified framework. Extensive
  experiments on large-scale theoretical spectroscopic benchmarks comprising about
  400,000 molecules systematically elucidate the complementary roles of individual
  spectroscopic modalities in determining molecular connectivity, backbone topology,
  and detailed 3D conformations. By explicitly incorporating spectroscopically informed
  topological priors, the framework substantially constrains the chemical search space
  and enables robust structure generation. Meanwhile, SpecDiffMol remains effective
  under realistic experimental conditions. Using automated experimental spectroscopic
  measurements, we demonstrate its ability to track Z↔E isomerization dynamics in
  bridged azobenzenes, capturing conformational transitions and key dihedral angle
  evolution with high accuracy. As a general and extensible approach for spectroscopically
  driven 3D molecular structure generation, SpecDiffMol opens new avenues for autonomous
  structure–function discovery and real-time in situ molecular analysis across chemistry,
  materials science, and molecular biology.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011037/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Multimodal Spectroscopy–Driven Reconstruction of Three-Dimensional Molecular Structures via Conditional Diffusion Model

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011037/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Wenjie Du, Xiaohan Qin, Yixi Shen, Ledu Wang, Andreas Burger, Chuangwei Liu, Song Wang, Jun Jiang, Yang Wang, Eric Liu
- **Published:** 2026-10-26

## Summary
Three-dimensional (3D) molecular structures underpin molecular function and dynamics. Spectroscopy can encode rich structural information via energy-level transitions, but existing data-driven approaches have largely focused on predicting symbolic representations such as SMILES, or molecular topology rather than reconstructing full 3D structures. Here, we introduce SpecDiffMol, the first generative framework to directly reconstruct full molecular 3D structures from molecular formulae and multimodal spectroscopic data, including infrared, Raman, UV–vis, and NMR spectra. SpecDiffMol integrates a Transformer-based topology inference module with an E(3)-equivariant conditional diffusion model, enabling the inference of molecular connectivity, global structure, and fine-grained conformational geometry in a unified framework. Extensive experiments on large-scale theoretical spectroscopic benchmarks comprising about 400,000 molecules systematically elucidate the complementary roles of individual spectroscopic modalities in determining molecular connectivity, backbone topology, and detailed 3D conformations. By explicitly incorporating spectroscopically informed topological priors, the framework substantially constrains the chemical search space and enables robust structure generation. Meanwhile, SpecDiffMol remains effective under realistic experimental conditions. Using automated experimental spectroscopic measurements, we demonstrate its ability to track Z↔E isomerization dynamics in bridged azobenzenes, capturing conformational transitions and key dihedral angle evolution with high accuracy. As a general and extensible approach for spectroscopically driven 3D molecular structure generation, SpecDiffMol opens new avenues for autonomous structure–function discovery and real-time in situ molecular analysis across chemistry, materials science, and molecular biology.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011037/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment

- **Concise summary:** SpecDiffMol combines topology inference and equivariant diffusion to reconstruct molecular geometry from formulae and multiple spectroscopic modalities.
- **Why it matters:** Combining complementary measurements could constrain structure generation more strongly than any individual spectrum.
- **Caveat:** The preprint relies substantially on theoretical spectra and a described experimental example; broad experimental robustness and priority claims are unverified.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15011037/v1); analysis based only on captured metadata, not independently verified full text.
