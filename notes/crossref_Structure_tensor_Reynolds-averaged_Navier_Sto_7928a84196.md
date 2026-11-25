---
title: Structure tensor Reynolds-averaged Navier–Stokes turbulence models with equivariant
  neural networks
type: paper
source: https://doi.org/10.1017/jfm.2026.12178
canonical_url: https://doi.org/10.1017/jfm.2026.12178
captured_by: auto-scanner
date: '2026-11-25'
captured_at: '2026-11-25T15:15:02+00:00'
last_requested: '2026-11-25T15:15:02+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Aaron Miller
- Sahil Kommalapati
- Robert D. Moser
- Petros Koumoutsakos
published: '2026-11-10'
abstract: Accurate and generalisable Reynolds-averaged Navier–Stokes (RANS) models
  for turbulent flows rely on effective closures, but currently available closures
  are notoriously unreliable. Kassinos et al. ( J. Fluid Mech. , 2001, vol. 428, pp.
  213–248) hypothesised that this unreliability of RANS models was due to an insufficient
  description of the statistical state of the turbulence and proposed a set of structure
  tensors as a candidate for a sufficiently rich description. To test this hypothesis
  for the rapid pressure-strain term, we introduce tensor-based, symmetry-aware closures
  in terms of the structure tensors using equivariant neural networks (ENNs) and present
  an algorithm for enforcing algebraic contraction relations among tensor components.
  Using data from rapid distortion theory, experiments show that such ENNs can effectively
  learn relationships involving high-order tensors. The resulting ENN structure tensor
  models are orders of magnitude more accurate than existing models for the rapid
  pressure-strain correlation, effectively validating the hypothesis of Kassinos et
  al. for this term. Results show that ENNs provide a physically consistent alternative
  to classical tensor basis models, enabling end-to-end learning of unclosed terms
  in RANS and other tensor modelling domains, and rapid exploration of model dependencies.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1017/jfm.2026.12178
  journal: Journal of Fluid Mechanics
  publisher: Cambridge University Press (CUP)
  type: journal-article
  subjects: []
---

# Structure tensor Reynolds-averaged Navier–Stokes turbulence models with equivariant neural networks

- **Type:** paper
- **Source:** https://doi.org/10.1017/jfm.2026.12178
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Aaron Miller, Sahil Kommalapati, Robert D. Moser, Petros Koumoutsakos
- **Published:** 2026-11-10

## Summary
Accurate and generalisable Reynolds-averaged Navier–Stokes (RANS) models for turbulent flows rely on effective closures, but currently available closures are notoriously unreliable. Kassinos et al. ( J. Fluid Mech. , 2001, vol. 428, pp. 213–248) hypothesised that this unreliability of RANS models was due to an insufficient description of the statistical state of the turbulence and proposed a set of structure tensors as a candidate for a sufficiently rich description. To test this hypothesis for the rapid pressure-strain term, we introduce tensor-based, symmetry-aware closures in terms of the structure tensors using equivariant neural networks (ENNs) and present an algorithm for enforcing algebraic contraction relations among tensor components. Using data from rapid distortion theory, experiments show that such ENNs can effectively learn relationships involving high-order tensors. The resulting ENN structure tensor models are orders of magnitude more accurate than existing models for the rapid pressure-strain correlation, effectively validating the hypothesis of Kassinos et al. for this term. Results show that ENNs provide a physically consistent alternative to classical tensor basis models, enabling end-to-end learning of unclosed terms in RANS and other tensor modelling domains, and rapid exploration of model dependencies.

## Provider details
- **Doi:** 10.1017/jfm.2026.12178
- **Journal:** Journal of Fluid Mechanics
- **Publisher:** Cambridge University Press (CUP)
- **Type:** journal-article
