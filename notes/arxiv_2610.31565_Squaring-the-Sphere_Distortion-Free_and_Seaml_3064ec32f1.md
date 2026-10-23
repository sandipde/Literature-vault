---
title: 'Squaring-the-Sphere: Distortion-Free and Seamless Panorama Generation via
  CubeAtlas'
type: arxiv
source: https://arxiv.org/abs/2610.31565
canonical_url: https://arxiv.org/abs/2610.31565
captured_by: auto-scanner
date: '2026-10-23'
captured_at: '2026-10-23T09:43:13+00:00'
last_requested: '2026-10-23T09:43:13+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Xuhui Zuo
- Chenjie Cao
- Tengfei Wang
- Junta Wu
- Yisu Zhang
- Chunchao Guo
published: '2026-10-22'
abstract: 'Generating 360-degree panoramas requires both local perspective fidelity
  and global spherical continuity. Existing representations face a trade-off: equirectangular
  projection (ERP) enables seamless panorama modeling but suffers from severe distortion
  and a domain gap to pre-trained image generators, whereas cubemaps preserve perspective
  geometry but often produce inconsistent faces and visible seams. We present Squaring-the-Sphere,
  a panoramic image generation framework built on a novel representation CubeAtlas,
  which unfolds all cubemap faces into a single compact canvas. By arranging orientation-aligned,
  rotated polar regions alongside the equatorial faces, this representation preserves
  the perspective geometry of cubemaps while organizing the cross-face relationships
  required for seamless panorama assembly. It further enables a pretrained diffusion
  transformer to model the complete panorama jointly in a single pass, without altering
  the backbone architecture or positional encoding. While CubeAtlas has a token count
  comparable to ERP, its structured layout makes many dense attention interactions
  unnecessary. We therefore introduce a layout-aware sparse attention mask that preserves
  the interactions required for panorama continuity while removing geometrically irrelevant
  token pairs. As a result, CubeAtlas achieves better quality than ERP modeling with
  lower attention computation. Furthermore, we introduce a training-free super-resolution
  technique and a fusion scheme that enhance fine details in distortion-free perspective
  space before achieving the final ERP panorama. Experiments on various benchmarks
  demonstrate that our method improves geometric fidelity, cross-view consistency,
  and high-resolution visual quality over previous methods.'
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.31565'
  categories:
  - cs.CV
---

# Squaring-the-Sphere: Distortion-Free and Seamless Panorama Generation via CubeAtlas

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.31565
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Xuhui Zuo, Chenjie Cao, Tengfei Wang, Junta Wu, Yisu Zhang, Chunchao Guo
- **Published:** 2026-10-22

## Summary
Generating 360-degree panoramas requires both local perspective fidelity and global spherical continuity. Existing representations face a trade-off: equirectangular projection (ERP) enables seamless panorama modeling but suffers from severe distortion and a domain gap to pre-trained image generators, whereas cubemaps preserve perspective geometry but often produce inconsistent faces and visible seams. We present Squaring-the-Sphere, a panoramic image generation framework built on a novel representation CubeAtlas, which unfolds all cubemap faces into a single compact canvas. By arranging orientation-aligned, rotated polar regions alongside the equatorial faces, this representation preserves the perspective geometry of cubemaps while organizing the cross-face relationships required for seamless panorama assembly. It further enables a pretrained diffusion transformer to model the complete panorama jointly in a single pass, without altering the backbone architecture or positional encoding. While CubeAtlas has a token count comparable to ERP, its structured layout makes many dense attention interactions unnecessary. We therefore introduce a layout-aware sparse attention mask that preserves the interactions required for panorama continuity while removing geometrically irrelevant token pairs. As a result, CubeAtlas achieves better quality than ERP modeling with lower attention computation. Furthermore, we introduce a training-free super-resolution technique and a fusion scheme that enhance fine details in distortion-free perspective space before achieving the final ERP panorama. Experiments on various benchmarks demonstrate that our method improves geometric fidelity, cross-view consistency, and high-resolution visual quality over previous methods.

## Provider details
- **Arxiv Id:** 2610.31565
- **Categories:** ["cs.CV"]
