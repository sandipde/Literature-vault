---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Mathematics and algorithms
enrichment_tags: [reinforcement-learning, quantum-control, entanglement, nonequilibrium-phases]
title: Learning to stabilize nonequilibrium phases of matter with active feedback
  using partial information
type: paper
source: https://doi.org/10.1088/2632-2153/aeb5a1
canonical_url: https://doi.org/10.1088/2632-2153/aeb5a1
captured_by: auto-scanner
date: '2026-10-17'
captured_at: '2026-10-17T08:58:51+00:00'
last_requested: '2026-10-17T08:58:51+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Giovanni Cemin
- Markus Schmitt
- Marin Bukov
published: '2026-10-16'
abstract: Abstract Recent advances in quantum computing experiments have enabled new
  pathways for feedback control. Here, we investigate the role of information in interactive
  quantum many-body dynamics to engineer out-of-equilibrium phases of matter. To this
  end, we train reinforcement learning agents to prevent entanglement spreading in
  $(1{+}1)$-dimensional stabilizer circuits with up to $128$ qubits. We find that,
  above an information threshold, agents learn stochastic near-optimal strategies
  that prevent the system from reaching volume-law entangled states and instead stabilize
  area-law scaling. These strategies rely on bottlenecks that divide the system and
  cap the entanglement in the steady state. Crucially, learned strategies are inherently
  out of equilibrium, require real-time active feedback, and could not be reproduced
  by simple human-designed control rules. This work establishes the foundations for
  information-driven individual control of many interacting quantum degrees of freedom,
  demonstrating the capabilities of reinforcement learning to stabilize and uncover
  novel critical properties of many-body nonequilibrium steady states.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1088/2632-2153/aeb5a1
  journal: 'Machine Learning: Science and Technology'
  publisher: IOP Publishing
  type: journal-article
  subjects: []
---

# Learning to stabilize nonequilibrium phases of matter with active feedback using partial information

- **Type:** paper
- **Source:** https://doi.org/10.1088/2632-2153/aeb5a1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Giovanni Cemin, Markus Schmitt, Marin Bukov
- **Published:** 2026-10-16

## Summary
Abstract Recent advances in quantum computing experiments have enabled new pathways for feedback control. Here, we investigate the role of information in interactive quantum many-body dynamics to engineer out-of-equilibrium phases of matter. To this end, we train reinforcement learning agents to prevent entanglement spreading in $(1{+}1)$-dimensional stabilizer circuits with up to $128$ qubits. We find that, above an information threshold, agents learn stochastic near-optimal strategies that prevent the system from reaching volume-law entangled states and instead stabilize area-law scaling. These strategies rely on bottlenecks that divide the system and cap the entanglement in the steady state. Crucially, learned strategies are inherently out of equilibrium, require real-time active feedback, and could not be reproduced by simple human-designed control rules. This work establishes the foundations for information-driven individual control of many interacting quantum degrees of freedom, demonstrating the capabilities of reinforcement learning to stabilize and uncover novel critical properties of many-body nonequilibrium steady states.

## Provider details
- **Doi:** 10.1088/2632-2153/aeb5a1
- **Journal:** Machine Learning: Science and Technology
- **Publisher:** IOP Publishing
- **Type:** journal-article

## AI enrichment
- **Concise summary:** Reinforcement-learning agents use partial information and active feedback to suppress entanglement spreading in stabilizer circuits of up to 128 qubits.
- **Why it matters:** The reported information threshold and bottleneck strategies connect control policy design to nonequilibrium many-body behavior rather than passive state prediction.
- **Caveat:** Results concern a specified circuit setting and simulated control strategies; the abstract does not establish hardware implementation or general control of arbitrary quantum matter.
- **Evidence:** [Captured source](https://doi.org/10.1088/2632-2153/aeb5a1); analysis based only on captured metadata, not independently verified full text.
