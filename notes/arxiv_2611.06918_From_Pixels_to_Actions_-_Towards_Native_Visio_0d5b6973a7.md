---
title: From Pixels to Actions - Towards Native Vision-Language-Action Policies
type: arxiv
source: https://arxiv.org/abs/2611.06918
canonical_url: https://arxiv.org/abs/2611.06918
captured_by: auto-scanner
date: '2026-11-05'
captured_at: '2026-11-05T12:53:59+00:00'
last_requested: '2026-11-05T12:53:59+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Weichen Fan
- Haiwen Diao
- Penghao Wu
- Siyuan Hu
- Ziqi Huang
- Tianqi Liu
- Mingze Sun
- Ziyi Wang
- Zhongang Cai
- Hanming Deng
- Quan Wang
- Lei Yang
- Lewei Lu
- Fangzhou Hong
- Zhaoxi Chen
- Dahua Lin
- Ziwei Liu
published: '2026-11-04'
abstract: 'Vision-language-action models are typically built on a simple premise:
  perception is first compressed by visual encoders, and action reasoning begins only
  afterwards. Yet manipulation often hinges on precisely the visual signals most vulnerable
  to this abstraction, e.g., local geometry, boundaries, depth, and subtle state changes.
  This raises a fundamental question: should action policies inherit a fixed visual
  endpoint, or directly access evolving visual computation? We introduce NEO-VLA,
  a structurally encoder-free vision-language-action framework. Images are tokenized
  by lightweight patch convolutional layers and evolve jointly with language throughout
  the backbone, allowing a flow-matching action expert to draw from instruction-conditioned
  visual representations at different depths. This simple change reveals a consistent
  pattern. Native architectures outperform encoder-based counterparts under controlled
  comparisons; full fine-tuning reduces but does not erase the gap, and additional
  scale alone cannot recover it. More strikingly, layer-wise probing shows that the
  action-critical signals often peak well before the final visual representation.
  Across diverse manipulation settings and distribution shifts, NEO-VLA consequently
  achieves stronger and more robust control. Together, these results suggest that
  embodied control benefits from access to visual representations across the computational
  hierarchy, rather than a fixed encoder output.'
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.06918'
  categories:
  - cs.CV
---

# From Pixels to Actions - Towards Native Vision-Language-Action Policies

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.06918
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Weichen Fan, Haiwen Diao, Penghao Wu, Siyuan Hu, Ziqi Huang, Tianqi Liu, Mingze Sun, Ziyi Wang, Zhongang Cai, Hanming Deng, Quan Wang, Lei Yang, Lewei Lu, Fangzhou Hong, Zhaoxi Chen, Dahua Lin, Ziwei Liu
- **Published:** 2026-11-04

## Summary
Vision-language-action models are typically built on a simple premise: perception is first compressed by visual encoders, and action reasoning begins only afterwards. Yet manipulation often hinges on precisely the visual signals most vulnerable to this abstraction, e.g., local geometry, boundaries, depth, and subtle state changes. This raises a fundamental question: should action policies inherit a fixed visual endpoint, or directly access evolving visual computation? We introduce NEO-VLA, a structurally encoder-free vision-language-action framework. Images are tokenized by lightweight patch convolutional layers and evolve jointly with language throughout the backbone, allowing a flow-matching action expert to draw from instruction-conditioned visual representations at different depths. This simple change reveals a consistent pattern. Native architectures outperform encoder-based counterparts under controlled comparisons; full fine-tuning reduces but does not erase the gap, and additional scale alone cannot recover it. More strikingly, layer-wise probing shows that the action-critical signals often peak well before the final visual representation. Across diverse manipulation settings and distribution shifts, NEO-VLA consequently achieves stronger and more robust control. Together, these results suggest that embodied control benefits from access to visual representations across the computational hierarchy, rather than a fixed encoder output.

## Provider details
- **Arxiv Id:** 2611.06918
- **Categories:** ["cs.CV"]
