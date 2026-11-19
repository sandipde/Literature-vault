---
title: A GPU-Native Nested Sampling Framework for Finite-Temperature Materials Modelling
  with Machine-Learned Interatomic Potentials
type: arxiv
source: https://arxiv.org/abs/2611.24088
canonical_url: https://arxiv.org/abs/2611.24088
captured_by: auto-scanner
date: '2026-11-19'
captured_at: '2026-11-19T14:04:33+00:00'
last_requested: '2026-11-19T14:04:33+00:00'
issue: scan:arxiv-mlips
status: to-read
authors:
- Nico Unglert
- Alessandro Serafini
- Jesús Carrete
- Georg K. H. Madsen
published: '2026-11-18'
abstract: Modern equivariant machine-learned interatomic potentials (MLIPs) have dramatically
  improved the accuracy of and the scales accessible to atomistic simulation, yet
  the thermodynamic sampling methods needed to turn those potentials into finite-temperature
  phase stability predictions have not kept pace computationally. We present the GPU-native,
  massively parallel nested sampling framework JAXRENS, implemented on top of JAX,
  which removes the practical bottlenecks preventing atomistic nested sampling from
  being combined with state-of-the-art MLIPs. The framework provides distributed multi-GPU
  execution, vectorised ensembles of walkers, and direct interoperability with modern
  force fields. We demonstrate the highly beneficial scaling of JAXRENS on hardware
  accelerators, and apply it to the simulation of the ZnS phase diagram based on a
  MACE foundation model, a procedure previously computationally inaccessible. Despite
  requiring in the order of 10^10 model evaluations, the final converged simulation
  completed within six days on four GPUs, marking an important step towards routine,
  first-principles-quality predictions of finite-temperature phase stability using
  machine-learned interatomic potentials.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.24088'
  categories:
  - cond-mat.mtrl-sci
---

# A GPU-Native Nested Sampling Framework for Finite-Temperature Materials Modelling with Machine-Learned Interatomic Potentials

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.24088
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Nico Unglert, Alessandro Serafini, Jesús Carrete, Georg K. H. Madsen
- **Published:** 2026-11-18

## Summary
Modern equivariant machine-learned interatomic potentials (MLIPs) have dramatically improved the accuracy of and the scales accessible to atomistic simulation, yet the thermodynamic sampling methods needed to turn those potentials into finite-temperature phase stability predictions have not kept pace computationally. We present the GPU-native, massively parallel nested sampling framework JAXRENS, implemented on top of JAX, which removes the practical bottlenecks preventing atomistic nested sampling from being combined with state-of-the-art MLIPs. The framework provides distributed multi-GPU execution, vectorised ensembles of walkers, and direct interoperability with modern force fields. We demonstrate the highly beneficial scaling of JAXRENS on hardware accelerators, and apply it to the simulation of the ZnS phase diagram based on a MACE foundation model, a procedure previously computationally inaccessible. Despite requiring in the order of 10^10 model evaluations, the final converged simulation completed within six days on four GPUs, marking an important step towards routine, first-principles-quality predictions of finite-temperature phase stability using machine-learned interatomic potentials.

## Provider details
- **Arxiv Id:** 2611.24088
- **Categories:** ["cond-mat.mtrl-sci"]
