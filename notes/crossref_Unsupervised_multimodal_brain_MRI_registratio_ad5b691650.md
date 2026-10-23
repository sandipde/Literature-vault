---
title: Unsupervised multimodal brain MRI registration with complementary learned and
  structural descriptors.
type: paper
source: https://doi.org/10.21203/rs.3.rs-11462321/v1
canonical_url: https://doi.org/10.21203/rs.3.rs-11462321/v1
captured_by: auto-scanner
date: '2026-10-23'
captured_at: '2026-10-23T09:43:13+00:00'
last_requested: '2026-10-23T09:43:13+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- DM BAPPY
- Hyeongboo Baek
published: '2026-10-23'
abstract: Abstract Deformable registration of T1- and T2-weighted brain magnetic resonance
  images is difficult because tissue intensities differ across contrasts. We investigate
  whether learned and hand-crafted descriptors provide complementary similarity information
  for unsupervised registration. A Cross-Modal Descriptor Network learns contrast-invariant
  voxel embeddings through self-supervised contrastive training on aligned same-subject
  pairs. These embeddings are combined with the modality-independent neighbourhood
  descriptor with self-similarity context (MIND-SSC) to train a compact diffeomorphic
  attention U-Net without anatomical labels. In inter-subject T1-to-T2 registration
  on the IXI dataset (n=45), the hybrid achieved a mean Dice coefficient of 0.700
  and a 95th-percentile Hausdorff distance of 3.21 mm, with no observed folded voxels.
  It outperformed the evaluated classical, learned, structural-descriptor, transformer,
  and foundation-model baselines (p<0.05, paired Wilcoxon tests). Gains were largest
  for small deep gray-matter structures, and the hybrid also performed best in the
  evaluated unseen-scanner and BraTS glioma experiments. Descriptors are used only
  during training; inference requires one 83 ms forward pass of a 0.247 M-parameter
  network. These results support combining learned and structural descriptors for
  accurate and computationally efficient multimodal brain registration.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.21203/rs.3.rs-11462321/v1
  journal: ''
  publisher: Springer Science and Business Media LLC
  type: posted-content
  subjects: []
---

# Unsupervised multimodal brain MRI registration with complementary learned and structural descriptors.

- **Type:** paper
- **Source:** https://doi.org/10.21203/rs.3.rs-11462321/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** DM BAPPY, Hyeongboo Baek
- **Published:** 2026-10-23

## Summary
Abstract Deformable registration of T1- and T2-weighted brain magnetic resonance images is difficult because tissue intensities differ across contrasts. We investigate whether learned and hand-crafted descriptors provide complementary similarity information for unsupervised registration. A Cross-Modal Descriptor Network learns contrast-invariant voxel embeddings through self-supervised contrastive training on aligned same-subject pairs. These embeddings are combined with the modality-independent neighbourhood descriptor with self-similarity context (MIND-SSC) to train a compact diffeomorphic attention U-Net without anatomical labels. In inter-subject T1-to-T2 registration on the IXI dataset (n=45), the hybrid achieved a mean Dice coefficient of 0.700 and a 95th-percentile Hausdorff distance of 3.21 mm, with no observed folded voxels. It outperformed the evaluated classical, learned, structural-descriptor, transformer, and foundation-model baselines (p<0.05, paired Wilcoxon tests). Gains were largest for small deep gray-matter structures, and the hybrid also performed best in the evaluated unseen-scanner and BraTS glioma experiments. Descriptors are used only during training; inference requires one 83 ms forward pass of a 0.247 M-parameter network. These results support combining learned and structural descriptors for accurate and computationally efficient multimodal brain registration.

## Provider details
- **Doi:** 10.21203/rs.3.rs-11462321/v1
- **Publisher:** Springer Science and Business Media LLC
- **Type:** posted-content
