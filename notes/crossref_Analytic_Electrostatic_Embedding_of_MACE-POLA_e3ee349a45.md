---
title: Analytic Electrostatic Embedding of MACE-POLAR for Fixed-Charge ML/MM
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011059/v2
canonical_url: https://doi.org/10.26434/chemrxiv.15011059/v2
captured_by: auto-scanner
date: '2026-11-19'
captured_at: '2026-11-19T14:04:33+00:00'
last_requested: '2026-11-19T14:04:33+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Jianxin Cheng
published: '2026-11-19'
abstract: Electrostatic embedding allows a local machine-learning potential to respond
  to an extended molecular environment without including every environmental atom
  in its message-passing graph. We construct a fixed-charge machine-learning/molecular-mechanics
  (ML/MM) interface for the pretrained MACE-POLAR-1-M model. Analytic Gaussian monopole
  and dipole operators supply the environmental potential, the internal electrostatic
  features, and the interaction energy. Differentiation through both field-conditioned
  density updates gives forces on the model fragment and the environment, which are
  combined with a subtractive classical energy and exact link-atom force redistribution.
  A reciprocal-space extension treats three-dimensional periodicity at fixed cell.
  We assess the implementation using fixed-geometry numerical checks and 24 matched
  QM/MM reference calculations for a 2589-atom rhodopsin model, with 54 atoms in the
  neural-network graph. The analytic model gives a relative-energy root-mean-square
  error of 8.62 kJ mol−1 after one constant energy shift, and force-component errors
  of 0.07345 and 0.00797 eV Å−1 on the 53 real high-level atoms and 2536 environmental
  atoms, respectively. Analytic operators substantially reduce rotational errors while
  leaving the QM/MM accuracy essentially unchanged. A nearby water accounts for approximately
  74% of the environmental squared force error. Matched charge-density and frozen-density
  force comparisons identify limitations of both the local multipole representation
  and its predicted coefficients. The results establish the numerical consistency
  of the embedding implementation and delimit the single-point accuracy of the transferred
  pretrained model.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011059/v2
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Analytic Electrostatic Embedding of MACE-POLAR for Fixed-Charge ML/MM

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011059/v2
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Jianxin Cheng
- **Published:** 2026-11-19

## Summary
Electrostatic embedding allows a local machine-learning potential to respond to an extended molecular environment without including every environmental atom in its message-passing graph. We construct a fixed-charge machine-learning/molecular-mechanics (ML/MM) interface for the pretrained MACE-POLAR-1-M model. Analytic Gaussian monopole and dipole operators supply the environmental potential, the internal electrostatic features, and the interaction energy. Differentiation through both field-conditioned density updates gives forces on the model fragment and the environment, which are combined with a subtractive classical energy and exact link-atom force redistribution. A reciprocal-space extension treats three-dimensional periodicity at fixed cell. We assess the implementation using fixed-geometry numerical checks and 24 matched QM/MM reference calculations for a 2589-atom rhodopsin model, with 54 atoms in the neural-network graph. The analytic model gives a relative-energy root-mean-square error of 8.62 kJ mol−1 after one constant energy shift, and force-component errors of 0.07345 and 0.00797 eV Å−1 on the 53 real high-level atoms and 2536 environmental atoms, respectively. Analytic operators substantially reduce rotational errors while leaving the QM/MM accuracy essentially unchanged. A nearby water accounts for approximately 74% of the environmental squared force error. Matched charge-density and frozen-density force comparisons identify limitations of both the local multipole representation and its predicted coefficients. The results establish the numerical consistency of the embedding implementation and delimit the single-point accuracy of the transferred pretrained model.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011059/v2
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
