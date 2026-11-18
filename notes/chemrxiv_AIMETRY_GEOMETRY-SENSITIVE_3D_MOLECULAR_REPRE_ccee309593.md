---
title: 'AIMETRY: GEOMETRY-SENSITIVE 3D MOLECULAR REPRESENTATIONS FROM QUANTUM MECHANICAL
  LEARNED FEATURES'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15012428/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15012428/v1
captured_by: auto-scanner
date: '2026-11-18'
captured_at: '2026-11-18T13:38:13+00:00'
last_requested: '2026-11-18T13:38:13+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Sheng Shu
- Kaiya Taura
- Shuhao Zhang
- Olexandr Isayev
published: '2026-11-18'
abstract: Quantifying molecular similarity depends on both chemical composition and
  3D structure, which are difficult to capture in a single fixed-length representation.
  Contrastive learning is a common machine learning approach to generate such representations
  (molecular embeddings), pulling each molecule toward a positive anchor of itself.
  These anchors typically come from graph augmentations that alter chemical identity
  or from other conformers of the same molecule. However, using conformers as positive
  anchors in standard contrastive learning suppresses geometric distinctions and graded
  structural relationships. Here, we introduce AIMetry, a geometry-sensitive representation
  learning scheme in which a graph transformer aggregates spatially and chemically
  aware atomic features from AIMNet2, a machine-learned interatomic potential trained
  on quantum-chemical data, into a molecular embedding. We guide standard contrastive
  learning using fingerprint similarity, which modulates embedding similarity between
  different-molecule pairs, and root-mean-square deviation, which modulates embedding
  similarity between conformer pairs. Trained on approximately 44 million conformers
  of 2.8 million ChEMBL molecules, AIMetry demonstrates higher retention of fingerprint-defined
  structural relationships and greater geometric sensitivity than a reference model
  pretrained with standard contrastive learning. AIMetry also improves linear-probe
  performance relative to the reference model across the evaluated datasets, while
  benefits under nonlinear readout and fine-tuning are task-specific. Chemical and
  conformational analyses provide complementary evidence about the information retained
  in the representation.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15012428/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# AIMETRY: GEOMETRY-SENSITIVE 3D MOLECULAR REPRESENTATIONS FROM QUANTUM MECHANICAL LEARNED FEATURES

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15012428/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Sheng Shu, Kaiya Taura, Shuhao Zhang, Olexandr Isayev
- **Published:** 2026-11-18

## Summary
Quantifying molecular similarity depends on both chemical composition and 3D structure, which are difficult to capture in a single fixed-length representation. Contrastive learning is a common machine learning approach to generate such representations (molecular embeddings), pulling each molecule toward a positive anchor of itself. These anchors typically come from graph augmentations that alter chemical identity or from other conformers of the same molecule. However, using conformers as positive anchors in standard contrastive learning suppresses geometric distinctions and graded structural relationships. Here, we introduce AIMetry, a geometry-sensitive representation learning scheme in which a graph transformer aggregates spatially and chemically aware atomic features from AIMNet2, a machine-learned interatomic potential trained on quantum-chemical data, into a molecular embedding. We guide standard contrastive learning using fingerprint similarity, which modulates embedding similarity between different-molecule pairs, and root-mean-square deviation, which modulates embedding similarity between conformer pairs. Trained on approximately 44 million conformers of 2.8 million ChEMBL molecules, AIMetry demonstrates higher retention of fingerprint-defined structural relationships and greater geometric sensitivity than a reference model pretrained with standard contrastive learning. AIMetry also improves linear-probe performance relative to the reference model across the evaluated datasets, while benefits under nonlinear readout and fine-tuning are task-specific. Chemical and conformational analyses provide complementary evidence about the information retained in the representation.

## Provider details
- **Doi:** 10.26434/chemrxiv.15012428/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
