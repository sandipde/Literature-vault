---
title: 'Where machine learning for enantioselectivity on polysaccharide chiral stationary
  phases actually fails: a leave-one-paper-out reappraisal of 10,525 enantiomer pairs'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011705/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011705/v1
captured_by: auto-scanner
date: '2026-11-05'
captured_at: '2026-11-05T12:53:59+00:00'
last_requested: '2026-11-05T12:53:59+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Lang Cui
published: '2026-11-05'
abstract: Machine-learning models for enantioselectivity on polysaccharide chiral
  stationary phases increasingly report high accuracy, but almost always under random
  data splits. We re-examined this problem on CMRT, the largest public chiral chromatography
  dataset, curating it into 10,525 enantiomer pairs covering 530 DOI groupsand25columns.Underatrueleave-one-paper-outprotocol,elution-orderaccuracyfallsfrom
  66.1 % under a random split to 52.9 %, indistinguishable from a within-paper permutation
  null (52.3 % ± 0.6). Between-paper variance accounts for 38.5 % of the total variance,
  but it cannot be predicted from compositional features, so domain adaptation is
  ineffective. The molecular signal is real within a single paper (median per-paper
  correlation r = +0.185) but falls to r = +0.0009 for an unseen paper, and adding
  trainingpapersdoesnothelp.Avariancedecompositionofasingle-laboratorygridshowsthatonly
  23.05 % of the variance is attributable to additive main effects of molecule and
  condition, the remaining 76.95 % being an unidentifiable molecule × condition interaction
  and noise. We therefore argue that the bottleneck liesnotinmodelcapacityordescriptorqualitybutinthedatastructure:adding
  condition metadata,buildingsystematicmolecule×conditiongrids,introducingreplicatemeasurementsand
  recording failed separations are the prerequisites for improving transferability.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011705/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Where machine learning for enantioselectivity on polysaccharide chiral stationary phases actually fails: a leave-one-paper-out reappraisal of 10,525 enantiomer pairs

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011705/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Lang Cui
- **Published:** 2026-11-05

## Summary
Machine-learning models for enantioselectivity on polysaccharide chiral stationary phases increasingly report high accuracy, but almost always under random data splits. We re-examined this problem on CMRT, the largest public chiral chromatography dataset, curating it into 10,525 enantiomer pairs covering 530 DOI groupsand25columns.Underatrueleave-one-paper-outprotocol,elution-orderaccuracyfallsfrom 66.1 % under a random split to 52.9 %, indistinguishable from a within-paper permutation null (52.3 % ± 0.6). Between-paper variance accounts for 38.5 % of the total variance, but it cannot be predicted from compositional features, so domain adaptation is ineffective. The molecular signal is real within a single paper (median per-paper correlation r = +0.185) but falls to r = +0.0009 for an unseen paper, and adding trainingpapersdoesnothelp.Avariancedecompositionofasingle-laboratorygridshowsthatonly 23.05 % of the variance is attributable to additive main effects of molecule and condition, the remaining 76.95 % being an unidentifiable molecule × condition interaction and noise. We therefore argue that the bottleneck liesnotinmodelcapacityordescriptorqualitybutinthedatastructure:adding condition metadata,buildingsystematicmolecule×conditiongrids,introducingreplicatemeasurementsand recording failed separations are the prerequisites for improving transferability.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011705/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
