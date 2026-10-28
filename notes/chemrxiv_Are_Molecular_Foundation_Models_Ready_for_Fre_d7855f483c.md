---
title: Are Molecular Foundation Models Ready for Free Energy Simulations?
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010593/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15010593/v1
captured_by: auto-scanner
date: '2026-10-17'
captured_at: '2026-10-17T08:58:51+00:00'
last_requested: '2026-10-17T08:58:51+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Nils Gönnheimer
- Karsten Reuter
- Johannes T. Margraf
published: '2026-10-16'
abstract: 'Foundation models for atomistic simulations offer broadly applicable potentialenergy
  surfaces that can either be applied in a zero-shot manner (without domainspecific
  retraining) or fine-tuned to the task at hand. Their accuracy is typically judged
  by energy and force errors on near-equilibrium data, yet it remains largely unclear
  whether these metrics translate into reliable free-energy landscapes. Here, enhanced
  sampling can be a particularly demanding test: simulations are driven far from equilibrium
  into sparsely trained regions and held there over long trajectories, so that small
  systematic errors in forces or relative energies can accumulate and distort predicted
  populations, transition pathways, and barriers. We assess several molecular foundation
  models trained on different dataset sizes and architectures (including models with
  explicit long-range electrostatics) in prototypical metadynamics and umbrella sampling
  simulations. Our results show that recent foundation models can reproduce simple
  gas-phase free-energy profiles with near-reference accuracy, while more complex
  multidimensional and solvated free-energy landscapes remain challenging. However,
  assessing their performance in these systems is further complicated by limitations
  in current sampling protocols and the lack of well-defined reference data. These
  findings highlight the need for more rigorous sampling protocols and reliable benchmarks
  to systematically assess the accuracy of future molecular foundation models in free-energy
  calculations.'
metadata_provider: Crossref
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: ML interatomic potentials
enrichment_tags: [free-energy, enhanced-sampling, foundation-potentials]
provider_data:
  doi: 10.26434/chemrxiv.15010593/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Are Molecular Foundation Models Ready for Free Energy Simulations?

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010593/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Nils Gönnheimer, Karsten Reuter, Johannes T. Margraf
- **Published:** 2026-10-16

## Summary
Foundation models for atomistic simulations offer broadly applicable potentialenergy surfaces that can either be applied in a zero-shot manner (without domainspecific retraining) or fine-tuned to the task at hand. Their accuracy is typically judged by energy and force errors on near-equilibrium data, yet it remains largely unclear whether these metrics translate into reliable free-energy landscapes. Here, enhanced sampling can be a particularly demanding test: simulations are driven far from equilibrium into sparsely trained regions and held there over long trajectories, so that small systematic errors in forces or relative energies can accumulate and distort predicted populations, transition pathways, and barriers. We assess several molecular foundation models trained on different dataset sizes and architectures (including models with explicit long-range electrostatics) in prototypical metadynamics and umbrella sampling simulations. Our results show that recent foundation models can reproduce simple gas-phase free-energy profiles with near-reference accuracy, while more complex multidimensional and solvated free-energy landscapes remain challenging. However, assessing their performance in these systems is further complicated by limitations in current sampling protocols and the lack of well-defined reference data. These findings highlight the need for more rigorous sampling protocols and reliable benchmarks to systematically assess the accuracy of future molecular foundation models in free-energy calculations.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010593/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment

- **Concise summary:** The abstract assesses molecular foundation potentials in metadynamics and umbrella sampling, reporting stronger results for simple gas-phase profiles than for solvated multidimensional landscapes.
- **Why it matters:** Rare-region force biases can distort populations and barriers even when near-equilibrium regression metrics look good.
- **Caveat:** The preprint also flags sampling and reference-data limitations, so observed discrepancies cannot automatically be attributed only to the potentials.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15010593/v1); analysis based only on captured metadata, not independently verified full text.
