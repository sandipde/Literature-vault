---
title: Geometry Sets the Neutral MLIP-DFT Gap in Non-Covalent Binding, and Charged
  Systems Fail
type: arxiv
source: https://arxiv.org/abs/2611.33830
canonical_url: https://arxiv.org/abs/2611.33830
captured_by: auto-scanner
date: '2026-11-26'
captured_at: '2026-11-26T14:39:56+00:00'
last_requested: '2026-11-26T14:39:56+00:00'
issue: scan:arxiv-mlips
status: to-read
authors:
- Rui Ding
- Zixin Ding
- Rodrigo Pires Ferreira
- Diantong Li
- Junhong Chen
- Yuxin Chen
published: '2026-11-25'
abstract: 'Pretrained universal machine-learning interatomic potentials (MLIPs) are
  widely expected to substitute for explicit quantum chemistry when screening molecular
  interactions. On non-covalent binding we find that this expectation holds for neutral
  chemistry and fails for charged chemistry. We audit the FAIRChem UMA OMol head,
  without task-specific fine-tuning, on 5,567 probe-target dimers from 18 benchmarks
  across nine fidelity arms, using RAPIDS (Rapid Atomistic Probe-target Interaction
  Discovery Scaffold), a training-free inference-time scaffold. First, on neutral
  chemistry RAPIDS reaches a mean absolute error (MAE) of 1.37 kcal/mol, matching
  or beating every explicit DFT single-point fidelity (1.42-1.50 kcal/mol), so the
  remaining MLIP-DFT gap is geometric rather than a learned-surface error. Second,
  charged systems form a qualitatively different regime: MAE jumps to 8.5-22.9 kcal/mol
  across three charged benchmarks; DFT single-point rescoring does not restore accuracy,
  geometry reoptimization restores it for ionic hydrogen bonds and ion-molecule dimers,
  and the failure persists across all three MLIP backbones. Third, the residual failures
  are structured: signed biases cluster by chemistry family, and whether a fidelity
  fails catastrophically transfers across families more reliably than error magnitude,
  enabling cost-aware fidelity selection. RAPIDS-Select, a closed-form rule on cheap
  precomputed features, uses about 37% less compute than a strong static DFT baseline
  at matched accuracy, and on a newly computed charged benchmark cuts the catastrophe
  rate from 68% to 5.7%. On WetSenseBench, a wet-lab-grounded host-guest selectivity
  benchmark from eight sensing studies, RAPIDS without DFT follow-up recovers 82.9%
  pair-level agreement on the seven studies above its ~1 kcal/mol precision floor.'
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.33830'
  categories:
  - physics.chem-ph
  - cond-mat.mtrl-sci
---

# Geometry Sets the Neutral MLIP-DFT Gap in Non-Covalent Binding, and Charged Systems Fail

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.33830
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Rui Ding, Zixin Ding, Rodrigo Pires Ferreira, Diantong Li, Junhong Chen, Yuxin Chen
- **Published:** 2026-11-25

## Summary
Pretrained universal machine-learning interatomic potentials (MLIPs) are widely expected to substitute for explicit quantum chemistry when screening molecular interactions. On non-covalent binding we find that this expectation holds for neutral chemistry and fails for charged chemistry. We audit the FAIRChem UMA OMol head, without task-specific fine-tuning, on 5,567 probe-target dimers from 18 benchmarks across nine fidelity arms, using RAPIDS (Rapid Atomistic Probe-target Interaction Discovery Scaffold), a training-free inference-time scaffold. First, on neutral chemistry RAPIDS reaches a mean absolute error (MAE) of 1.37 kcal/mol, matching or beating every explicit DFT single-point fidelity (1.42-1.50 kcal/mol), so the remaining MLIP-DFT gap is geometric rather than a learned-surface error. Second, charged systems form a qualitatively different regime: MAE jumps to 8.5-22.9 kcal/mol across three charged benchmarks; DFT single-point rescoring does not restore accuracy, geometry reoptimization restores it for ionic hydrogen bonds and ion-molecule dimers, and the failure persists across all three MLIP backbones. Third, the residual failures are structured: signed biases cluster by chemistry family, and whether a fidelity fails catastrophically transfers across families more reliably than error magnitude, enabling cost-aware fidelity selection. RAPIDS-Select, a closed-form rule on cheap precomputed features, uses about 37% less compute than a strong static DFT baseline at matched accuracy, and on a newly computed charged benchmark cuts the catastrophe rate from 68% to 5.7%. On WetSenseBench, a wet-lab-grounded host-guest selectivity benchmark from eight sensing studies, RAPIDS without DFT follow-up recovers 82.9% pair-level agreement on the seven studies above its ~1 kcal/mol precision floor.

## Provider details
- **Arxiv Id:** 2611.33830
- **Categories:** ["physics.chem-ph", "cond-mat.mtrl-sci"]
