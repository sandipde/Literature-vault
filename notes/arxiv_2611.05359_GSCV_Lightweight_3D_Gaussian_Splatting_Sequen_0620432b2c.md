---
title: 'GSCV++: Lightweight 3D Gaussian Splatting Sequence Compression via Standard
  Video Codecs'
type: arxiv
source: https://arxiv.org/abs/2611.05359
canonical_url: https://arxiv.org/abs/2611.05359
captured_by: auto-scanner
date: '2026-11-04'
captured_at: '2026-11-04T12:44:30+00:00'
last_requested: '2026-11-04T12:44:30+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Qi Yang
- Yingzhan Xu
- Kai Zhang
- Li Zhang
published: '2026-11-03'
abstract: This paper presents GSCV++, a lightweight pipeline for 3D {G}aussian {S}platting
  (GS) sequences {C}ompression with standard {V}ideo codecs. To meet the requirements
  of low-complexity and hardware compatibility from the industry, GSCV++ jointly improves
  preprocessing, 3D-to-2D mapping, and practical video compression configuration of
  GS compression. First, for preprocessing, energy-adaptive inter-frame spherical
  harmonic (SH) alternative current (AC) dimensionality reduction (EA-SHDR) is proposed
  to produces a compact and stable temporal SH AC feature space. It can reduce the
  data volume of following mapping and practical compression, as well as less complexity
  while eliminating redundant information. Second, for 3D-to-2D mapping, prior-based
  Inter-MiniPLAS (P-MiniPLAS) is designed to generate smooth 2D feature maps through
  prior-based weighting factor inference and small scale remapping. Compared with
  vanilla Parallel Linear Assignment Sorting (PLAS) and Morton scan, P-MiniPLAS ensures
  the generated 2D maps are more suitable for the video codec while maintaining a
  low level of computational complexity. Third, for practical compression, content-aware
  generalized compression (CA-GC) is developed to use a non-uniform bit-depth split
  for coordinate map generation, and a coding unit size selection is introduced for
  efficient compression complexity control, which fully exploits the performance of
  video codecs without involving normative changes. Experiments demonstrate that GSCV++
  reports over 20\% in intra- and 60\% in inter-prediction rate-distortion gains compared
  with state-of-the-art (SOTA) methods. GSCV++ also achieves faster 2D map generation,
  encoding, and decoding than other SOTA methods using the same type of video codecs.
  Ablation studies verify the effectiveness and robustness of the proposed modules
  and provide insights for subsequent research.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.05359'
  categories:
  - cs.CV
---

# GSCV++: Lightweight 3D Gaussian Splatting Sequence Compression via Standard Video Codecs

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.05359
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Qi Yang, Yingzhan Xu, Kai Zhang, Li Zhang
- **Published:** 2026-11-03

## Summary
This paper presents GSCV++, a lightweight pipeline for 3D {G}aussian {S}platting (GS) sequences {C}ompression with standard {V}ideo codecs. To meet the requirements of low-complexity and hardware compatibility from the industry, GSCV++ jointly improves preprocessing, 3D-to-2D mapping, and practical video compression configuration of GS compression. First, for preprocessing, energy-adaptive inter-frame spherical harmonic (SH) alternative current (AC) dimensionality reduction (EA-SHDR) is proposed to produces a compact and stable temporal SH AC feature space. It can reduce the data volume of following mapping and practical compression, as well as less complexity while eliminating redundant information. Second, for 3D-to-2D mapping, prior-based Inter-MiniPLAS (P-MiniPLAS) is designed to generate smooth 2D feature maps through prior-based weighting factor inference and small scale remapping. Compared with vanilla Parallel Linear Assignment Sorting (PLAS) and Morton scan, P-MiniPLAS ensures the generated 2D maps are more suitable for the video codec while maintaining a low level of computational complexity. Third, for practical compression, content-aware generalized compression (CA-GC) is developed to use a non-uniform bit-depth split for coordinate map generation, and a coding unit size selection is introduced for efficient compression complexity control, which fully exploits the performance of video codecs without involving normative changes. Experiments demonstrate that GSCV++ reports over 20\% in intra- and 60\% in inter-prediction rate-distortion gains compared with state-of-the-art (SOTA) methods. GSCV++ also achieves faster 2D map generation, encoding, and decoding than other SOTA methods using the same type of video codecs. Ablation studies verify the effectiveness and robustness of the proposed modules and provide insights for subsequent research.

## Provider details
- **Arxiv Id:** 2611.05359
- **Categories:** ["cs.CV"]
