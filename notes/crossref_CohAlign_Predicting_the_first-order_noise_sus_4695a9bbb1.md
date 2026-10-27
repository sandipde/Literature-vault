---
title: 'CohAlign: Predicting the first-order noise susceptibility of gradients in
  equivariant quantum neural networks'
type: paper
source: https://doi.org/10.1371/journal.pone.0361139
canonical_url: https://doi.org/10.1371/journal.pone.0361139
captured_by: auto-scanner
date: '2026-10-22'
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Mathematics and algorithms
enrichment_tags: [quantum-neural-networks, noise-sensitivity, gradient-analysis]
captured_at: '2026-10-22T20:23:01+00:00'
last_requested: '2026-10-22T20:23:01+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Hassan Ugail
- Newton Howard
published: '2026-10-22'
abstract: Quantum neural networks learn by following gradients, and on real hardware
  those gradients are washed out by noise. Predicting how quickly this happens, before
  any finite noise experiment or circuit sweep is run, remains an open problem. We
  present CohAlign, an open source toolkit that computes the first order noise susceptibility
  of the ensemble second moment of a specified parameter gradient in a charge conserving
  brickwork quantum neural network. The computation needs only a classical description
  of the circuit, the noise model, the prepared state, the readout and the initialisation
  prior. The predicted quantity is distinct from training convergence or final accuracy.
  The key observation is that only the part of the noise that a measurement can actually
  see matters. A purposefully constructed control channel makes this clear, damaging
  the operator carrying a gradient at nearly the maximal rate while the measured gradient
  remains exactly as predicted and untouched. We validate the predictions against
  separately evaluated finite difference slopes across the benchmark suite, including
  a signed coherent case, in exact simulations at eight and ten qubits and on two
  circuit topologies.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1371/journal.pone.0361139
  journal: PLOS One
  publisher: Public Library of Science (PLoS)
  type: journal-article
  subjects: []
---

# CohAlign: Predicting the first-order noise susceptibility of gradients in equivariant quantum neural networks

- **Type:** paper
- **Source:** https://doi.org/10.1371/journal.pone.0361139
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Hassan Ugail, Newton Howard
- **Published:** 2026-10-22

## Summary
Quantum neural networks learn by following gradients, and on real hardware those gradients are washed out by noise. Predicting how quickly this happens, before any finite noise experiment or circuit sweep is run, remains an open problem. We present CohAlign, an open source toolkit that computes the first order noise susceptibility of the ensemble second moment of a specified parameter gradient in a charge conserving brickwork quantum neural network. The computation needs only a classical description of the circuit, the noise model, the prepared state, the readout and the initialisation prior. The predicted quantity is distinct from training convergence or final accuracy. The key observation is that only the part of the noise that a measurement can actually see matters. A purposefully constructed control channel makes this clear, damaging the operator carrying a gradient at nearly the maximal rate while the measured gradient remains exactly as predicted and untouched. We validate the predictions against separately evaluated finite difference slopes across the benchmark suite, including a signed coherent case, in exact simulations at eight and ten qubits and on two circuit topologies.

## Provider details
- **Doi:** 10.1371/journal.pone.0361139
- **Journal:** PLOS One
- **Publisher:** Public Library of Science (PLoS)
- **Type:** journal-article

## AI enrichment
- **Concise summary:** The abstract introduces CohAlign to predict first-order noise susceptibility of gradients in equivariant quantum neural networks.
- **Why it matters:** Estimating gradient degradation could help assess trainability before detailed noisy-hardware experiments.
- **Caveat:** The captured abstract does not establish predictive accuracy on hardware or across model families.
- **Evidence:** [Captured source](https://doi.org/10.1371/journal.pone.0361139); analysis based only on captured metadata, not independently verified full text.
