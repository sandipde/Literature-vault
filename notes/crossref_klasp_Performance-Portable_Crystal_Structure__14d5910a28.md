---
title: 'klasp: Performance-Portable Crystal Structure Prediction with Distributed
  Multipoles and Machine-Learned Interatomic Potentials'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15012881/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15012881/v1
captured_by: auto-scanner
date: '2026-11-27'
captured_at: '2026-11-27T14:38:01+00:00'
last_requested: '2026-11-27T14:38:01+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Peter R. Spackman
- James R. Brookes
published: '2026-11-27'
abstract: Crystal structure prediction (CSP) of molecular crystals commonly begins
  with the lattice energy minimisation of very large numbers of trial structures,
  treating molecules as rigid bodies interacting through distributed multipoles and
  an empirical repulsion–dispersion potential. Here we present klasp, a batched lattice
  energy minimiser and complete CSP program, which runs from a single performanceportable
  source on CPUs and on GPUs from different vendors. Generation, minimisation, deduplication
  and refinement with a machine-learned interatomic potential run within one program,
  with no file or process for each structure. With the same energy model as existing
  implementations, klasp reproduces their lattice energies to within a few hundredths
  of a kJmol−1, completes a full search in minutes on a single GPU node, and scales
  efficiently to many GPUs. On 13 targets from the CCDC blind tests, complete searches
  on CPUs need 9.5 to 17 times fewer core-hours than the minimisation steps alone
  of an established workflow, and all 13 searches together take 3 node-hours on GPUs.
  The force field alone finds the experimental structure for 10 of the 12 targets
  with a Z′ = 1 reference, and refinement for 11, seven of them at rank 1.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15012881/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# klasp: Performance-Portable Crystal Structure Prediction with Distributed Multipoles and Machine-Learned Interatomic Potentials

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15012881/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Peter R. Spackman, James R. Brookes
- **Published:** 2026-11-27

## Summary
Crystal structure prediction (CSP) of molecular crystals commonly begins with the lattice energy minimisation of very large numbers of trial structures, treating molecules as rigid bodies interacting through distributed multipoles and an empirical repulsion–dispersion potential. Here we present klasp, a batched lattice energy minimiser and complete CSP program, which runs from a single performanceportable source on CPUs and on GPUs from different vendors. Generation, minimisation, deduplication and refinement with a machine-learned interatomic potential run within one program, with no file or process for each structure. With the same energy model as existing implementations, klasp reproduces their lattice energies to within a few hundredths of a kJmol−1, completes a full search in minutes on a single GPU node, and scales efficiently to many GPUs. On 13 targets from the CCDC blind tests, complete searches on CPUs need 9.5 to 17 times fewer core-hours than the minimisation steps alone of an established workflow, and all 13 searches together take 3 node-hours on GPUs. The force field alone finds the experimental structure for 10 of the 12 targets with a Z′ = 1 reference, and refinement for 11, seven of them at rank 1.

## Provider details
- **Doi:** 10.26434/chemrxiv.15012881/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
