---
title: Unconstrained learning of equivariant atomistic properties
type: arxiv
source: https://arxiv.org/abs/2610.31183
canonical_url: https://arxiv.org/abs/2610.31183
captured_by: auto-scanner
date: '2026-10-23'
captured_at: '2026-10-23T09:43:13+00:00'
last_requested: '2026-10-23T09:43:13+00:00'
issue: scan:arxiv-mlips
status: to-read
authors:
- Joseph W. Abbott
- Paolo Pegolo
- Pol Febrer
- Michelangelo Domina
- Sandra Saade
- Matthias Kellner
- Filippo Bigi
- Philip Loche
- Michele Ceriotti
published: '2026-10-22'
abstract: Machine-learned interatomic potentials based on graph neural networks (GNNs)
  have made first-principles accuracy routine for the potential energy surface (PES).
  Their backbones, often O(3)-equivariant by design, are increasingly used to learn
  other atomistic properties. Many of these are of high angular order or pseudotensorial
  character, defined per atom, or expanded on large atom-centered basis sets. Such
  targets strain equivariant GNNs, whose tensor products grow steeply in cost with
  angular order and can fail to represent the target if truncated, forcing difficult
  trade-offs between hyperparameters. Unconstrained models like the Point-Edge Transformer
  (PET) instead replace explicit O(3) algebra with edge-to-edge attention and learn
  equivariance from data, so that the same backbone can in principle learn any equivariant
  property. We demonstrate how to use PET to learn molecular dipoles and polarizabilities,
  NMR chemical shielding tensors, and auxiliary-basis expansions of the electron density.
  Increasing the backbone size systematically improves both accuracy and equivariance
  error, and targeted architectural and training choices reduce the symmetry breaking
  further. PET matches or improves on the released reference models at lower inference
  cost and, compared with equivariant models, a smaller memory footprint. The predictions
  give accurate IR and Raman spectra and isotropic shieldings; the predicted densities
  accelerate self-consistent field calculations and give one-shot ground-state properties,
  and pretrained density models transfer to higher levels of theory by fine-tuning
  on little data. The impact of approximate equivariance is small for most observables,
  further validating this approach to train fast, accurate, and useful surrogate models
  for properties beyond the PES.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.31183'
  categories:
  - physics.chem-ph
---

# Unconstrained learning of equivariant atomistic properties

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.31183
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Joseph W. Abbott, Paolo Pegolo, Pol Febrer, Michelangelo Domina, Sandra Saade, Matthias Kellner, Filippo Bigi, Philip Loche, Michele Ceriotti
- **Published:** 2026-10-22

## Summary
Machine-learned interatomic potentials based on graph neural networks (GNNs) have made first-principles accuracy routine for the potential energy surface (PES). Their backbones, often O(3)-equivariant by design, are increasingly used to learn other atomistic properties. Many of these are of high angular order or pseudotensorial character, defined per atom, or expanded on large atom-centered basis sets. Such targets strain equivariant GNNs, whose tensor products grow steeply in cost with angular order and can fail to represent the target if truncated, forcing difficult trade-offs between hyperparameters. Unconstrained models like the Point-Edge Transformer (PET) instead replace explicit O(3) algebra with edge-to-edge attention and learn equivariance from data, so that the same backbone can in principle learn any equivariant property. We demonstrate how to use PET to learn molecular dipoles and polarizabilities, NMR chemical shielding tensors, and auxiliary-basis expansions of the electron density. Increasing the backbone size systematically improves both accuracy and equivariance error, and targeted architectural and training choices reduce the symmetry breaking further. PET matches or improves on the released reference models at lower inference cost and, compared with equivariant models, a smaller memory footprint. The predictions give accurate IR and Raman spectra and isotropic shieldings; the predicted densities accelerate self-consistent field calculations and give one-shot ground-state properties, and pretrained density models transfer to higher levels of theory by fine-tuning on little data. The impact of approximate equivariance is small for most observables, further validating this approach to train fast, accurate, and useful surrogate models for properties beyond the PES.

## Provider details
- **Arxiv Id:** 2610.31183
- **Categories:** ["physics.chem-ph"]
