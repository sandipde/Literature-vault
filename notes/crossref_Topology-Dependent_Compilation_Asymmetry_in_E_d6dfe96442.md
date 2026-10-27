---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Mathematics and algorithms
enrichment_tags: [quantum-compilation, equivariance, graph-symmetry]
title: 'Topology-Dependent Compilation Asymmetry in Equivariant Quantum Neural Networks:
  A Compile-Once-and-Relabel Solution'
type: paper
source: https://doi.org/10.1088/2058-9565/aeb8ef
canonical_url: https://doi.org/10.1088/2058-9565/aeb8ef
captured_by: auto-scanner
date: '2026-10-24'
captured_at: '2026-10-24T09:15:55+00:00'
last_requested: '2026-10-24T09:15:55+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Hassan Ugail
- Newton Howard
published: '2026-10-23'
abstract: Abstract Equivariant quantum neural networks are designed to preserve symmetries
  in quantum machine-learning data, but this property is usually verified only before
  hardware compilation. We show that a transpiler can preserve the expected unitary
  symmetry relation while compiling symmetry-related inputs into circuits with different
  two-qubit gate counts and physical-qubit layouts, so ideal-circuit equivariance
  does not guarantee symmetry at the level of compiled circuit structure. We formalise
  this gap with a three-level compliance hierarchy and a taxonomy separating topology-input
  ansätze, where the symmetry changes the gate topology the compiler sees, from parameter-input
  ansätze, where it changes only numerical gate parameters and provably leaves controlled-Z
  counts unchanged under topology-based transpilation. Auditing four published ansatz
  families, we observe the effect only in the topology-input case. For the Skolik
  permutation-equivariant weighted-graph ansatz compiled to the IBM Heron Fez simulator
  target at twelve qubits, sparse graph inputs produce a mean relative controlled-Z
  asymmetry of 7.3\% across fifty random vertex permutations, with a worst case of
  22.5\%. The effect persists across all four Qiskit optimisation levels and is not
  removed by matched-layout compilation, implicating routing-stage sensitivity to
  the ordered sparse-edge gate sequence. A density sweep shows that the asymmetry
  is comparable across intermediate graph densities and vanishes for complete graphs,
  where the ansatz degenerates into the parameter-input class, and stochastic baselines
  attribute the realised differences to heuristic routing sensitivity rather than
  to differing optimal compiled costs. Finally, we propose compile-once-and-relabel,
  a deployment pattern that removes controlled-Z count asymmetry by construction and
  reduces compilation cost for orbit-based workflows.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1088/2058-9565/aeb8ef
  journal: Quantum Science and Technology
  publisher: IOP Publishing
  type: journal-article
  subjects: []
---

# Topology-Dependent Compilation Asymmetry in Equivariant Quantum Neural Networks: A Compile-Once-and-Relabel Solution

- **Type:** paper
- **Source:** https://doi.org/10.1088/2058-9565/aeb8ef
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Hassan Ugail, Newton Howard
- **Published:** 2026-10-23

## Summary
Abstract Equivariant quantum neural networks are designed to preserve symmetries in quantum machine-learning data, but this property is usually verified only before hardware compilation. We show that a transpiler can preserve the expected unitary symmetry relation while compiling symmetry-related inputs into circuits with different two-qubit gate counts and physical-qubit layouts, so ideal-circuit equivariance does not guarantee symmetry at the level of compiled circuit structure. We formalise this gap with a three-level compliance hierarchy and a taxonomy separating topology-input ansätze, where the symmetry changes the gate topology the compiler sees, from parameter-input ansätze, where it changes only numerical gate parameters and provably leaves controlled-Z counts unchanged under topology-based transpilation. Auditing four published ansatz families, we observe the effect only in the topology-input case. For the Skolik permutation-equivariant weighted-graph ansatz compiled to the IBM Heron Fez simulator target at twelve qubits, sparse graph inputs produce a mean relative controlled-Z asymmetry of 7.3\% across fifty random vertex permutations, with a worst case of 22.5\%. The effect persists across all four Qiskit optimisation levels and is not removed by matched-layout compilation, implicating routing-stage sensitivity to the ordered sparse-edge gate sequence. A density sweep shows that the asymmetry is comparable across intermediate graph densities and vanishes for complete graphs, where the ansatz degenerates into the parameter-input class, and stochastic baselines attribute the realised differences to heuristic routing sensitivity rather than to differing optimal compiled costs. Finally, we propose compile-once-and-relabel, a deployment pattern that removes controlled-Z count asymmetry by construction and reduces compilation cost for orbit-based workflows.

## Provider details
- **Doi:** 10.1088/2058-9565/aeb8ef
- **Journal:** Quantum Science and Technology
- **Publisher:** IOP Publishing
- **Type:** journal-article

## AI enrichment

- **Concise summary:** The captured abstract distinguishes ideal quantum-model equivariance from symmetry of compiled circuit costs. It reports topology-sensitive routing differences and proposes compiling once before relabeling symmetry-related inputs.
- **Why it matters:** Symmetry-aware algorithms may need deployment-level audits, not just mathematical invariance checks.
- **Caveat:** Reported results concern specified ansatz families and a simulator target, not a universal hardware guarantee. Three same-title peer-review records added on October 25 belong to this DOI's version family and are not independent studies.
- **Evidence:** [Captured source](https://doi.org/10.1088/2058-9565/aeb8ef); analysis based only on captured metadata, not independently verified full text.
