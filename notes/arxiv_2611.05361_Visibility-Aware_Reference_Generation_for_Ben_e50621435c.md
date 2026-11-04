---
title: Visibility-Aware Reference Generation for Benchmarking Visual 3D Reconstruction
  in Vegetation-Rich Environments
type: arxiv
source: https://arxiv.org/abs/2611.05361
canonical_url: https://arxiv.org/abs/2611.05361
captured_by: auto-scanner
date: '2026-11-04'
captured_at: '2026-11-04T12:44:30+00:00'
last_requested: '2026-11-04T12:44:30+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Zhipeng Zhong
- Matthew Coombes
- Cunjia Liu
published: '2026-11-03'
abstract: Reliable evaluation of visual 3D reconstruction and depth estimation in
  vegetation-rich outdoor environments is limited by the scarcity of geometric ground-truth
  data and the cost of complete scanner surveys. We present a LiDARbased reference-generation
  pipeline for evaluating the zero-shot performance of feed-forward visual-geometry
  models alongside conventional structure-from-motion (SfM) methods. The pipeline
  reuses camera images, LiDAR scans, and reference poses from existing multi-sensor
  localization datasets to generate per-view depth maps and visible reference point
  clouds. To address visibility errors in accumulated LiDAR scans, we introduce the
  LargeDepth-Gap Visibility Score (LDGVS) for point-wise visibility filtering and
  automatic scale selection in Hidden Point Removal(HPR). Experiments on TartanAirV2
  and TartanGround show that, compared with Poisson surface reconstruction, which
  is an approach suited to completed scan surveys, the combined HPR and LDGVS filtering
  retains approximately three times the point density at comparable absolute relative
  error. We also apply the pipeline to the BotanicGarden dataset to systematically
  compare depth estimation and 3D reconstruction methods. Feedforward methods produce
  dense depth predictions efficiently, but their 3D reconstructions can contain duplicated
  structures. Conventional SfM generally produces more coherent geometry, but its
  reconstructions remain sparse and more prone to failure in challenging vegetated
  scenes. The benchmark toolkit and datasets will be released.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.05361'
  categories:
  - cs.CV
  - cs.RO
---

# Visibility-Aware Reference Generation for Benchmarking Visual 3D Reconstruction in Vegetation-Rich Environments

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.05361
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Zhipeng Zhong, Matthew Coombes, Cunjia Liu
- **Published:** 2026-11-03

## Summary
Reliable evaluation of visual 3D reconstruction and depth estimation in vegetation-rich outdoor environments is limited by the scarcity of geometric ground-truth data and the cost of complete scanner surveys. We present a LiDARbased reference-generation pipeline for evaluating the zero-shot performance of feed-forward visual-geometry models alongside conventional structure-from-motion (SfM) methods. The pipeline reuses camera images, LiDAR scans, and reference poses from existing multi-sensor localization datasets to generate per-view depth maps and visible reference point clouds. To address visibility errors in accumulated LiDAR scans, we introduce the LargeDepth-Gap Visibility Score (LDGVS) for point-wise visibility filtering and automatic scale selection in Hidden Point Removal(HPR). Experiments on TartanAirV2 and TartanGround show that, compared with Poisson surface reconstruction, which is an approach suited to completed scan surveys, the combined HPR and LDGVS filtering retains approximately three times the point density at comparable absolute relative error. We also apply the pipeline to the BotanicGarden dataset to systematically compare depth estimation and 3D reconstruction methods. Feedforward methods produce dense depth predictions efficiently, but their 3D reconstructions can contain duplicated structures. Conventional SfM generally produces more coherent geometry, but its reconstructions remain sparse and more prone to failure in challenging vegetated scenes. The benchmark toolkit and datasets will be released.

## Provider details
- **Arxiv Id:** 2611.05361
- **Categories:** ["cs.CV", "cs.RO"]
