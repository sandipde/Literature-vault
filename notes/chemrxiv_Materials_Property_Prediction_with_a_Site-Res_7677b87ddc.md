---
title: Materials Property Prediction with a Site-Resolved Three-Dimensional Voxel
  Convolution Neural Network
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011524/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011524/v1
captured_by: auto-scanner
date: '2026-11-02'
captured_at: '2026-11-02T23:46:24+00:00'
last_requested: '2026-11-02T23:46:24+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Juo Kim
- Kyoungmin Min
published: '2026-11-02'
abstract: Identifying low-energy atomic arrangements is central to the design of multicomponent
  materials such as high-entropy cathodes and perovskites, but the number of possible
  arrangements grows combinatorially with the number of elements. Calculating each
  arrangement with density functional theory (DFT) is impractical, and many machine-learning
  models require relaxed structures that become available only after such calculations.
  This study presents a site-resolved voxel three-dimensional convolutional neural
  network (SiVox) that maps each crystallographic site of a known prototype onto a
  voxel and encodes the occupying element by its physicochemical properties, so that
  only the site assignment is required as input. The model was evaluated on 1,287,000
  configurations of high-entropy Li-rich layered oxides (HE-LLOs) and 18,928 cubic
  ABX3 perovskites. For HE-LLOs, it reached configurational R2 values of 0.989 for
  new configurations of training compositions and 0.993 for compositions excluded
  from training, compared with 0.92–0.93 for descriptor-based models. For perovskites,
  site assignment alone lowered the formation-energy MAE from 0.432 to 0.133 eV/cell
  relative to composition descriptors, and screening about 6% of the candidates recovered
  90% of the lowest-energy 5%. Relaxed lattice parameters and atomic displacements
  reduced the error further and mattered most when the most stable of seven anion
  variants had to be identified. These results indicate that site assignment on a
  known framework is sufficient to narrow a large candidate space before structural
  relaxation.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011524/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Materials Property Prediction with a Site-Resolved Three-Dimensional Voxel Convolution Neural Network

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011524/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Juo Kim, Kyoungmin Min
- **Published:** 2026-11-02

## Summary
Identifying low-energy atomic arrangements is central to the design of multicomponent materials such as high-entropy cathodes and perovskites, but the number of possible arrangements grows combinatorially with the number of elements. Calculating each arrangement with density functional theory (DFT) is impractical, and many machine-learning models require relaxed structures that become available only after such calculations. This study presents a site-resolved voxel three-dimensional convolutional neural network (SiVox) that maps each crystallographic site of a known prototype onto a voxel and encodes the occupying element by its physicochemical properties, so that only the site assignment is required as input. The model was evaluated on 1,287,000 configurations of high-entropy Li-rich layered oxides (HE-LLOs) and 18,928 cubic ABX3 perovskites. For HE-LLOs, it reached configurational R2 values of 0.989 for new configurations of training compositions and 0.993 for compositions excluded from training, compared with 0.92–0.93 for descriptor-based models. For perovskites, site assignment alone lowered the formation-energy MAE from 0.432 to 0.133 eV/cell relative to composition descriptors, and screening about 6% of the candidates recovered 90% of the lowest-energy 5%. Relaxed lattice parameters and atomic displacements reduced the error further and mattered most when the most stable of seven anion variants had to be identified. These results indicate that site assignment on a known framework is sufficient to narrow a large candidate space before structural relaxation.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011524/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
