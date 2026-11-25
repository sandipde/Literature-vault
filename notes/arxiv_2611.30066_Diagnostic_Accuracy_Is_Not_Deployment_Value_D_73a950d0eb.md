---
title: 'Diagnostic Accuracy Is Not Deployment Value: Decision-Aligned Reliability
  Evaluation for Foundation MLIPs in Materials Discovery'
type: arxiv
source: https://arxiv.org/abs/2611.30066
canonical_url: https://arxiv.org/abs/2611.30066
captured_by: auto-scanner
date: '2026-11-25'
captured_at: '2026-11-25T01:13:37+00:00'
last_requested: '2026-11-25T01:13:37+00:00'
issue: scan:arxiv-mlips
status: to-read
authors:
- Harry Sevi
- Joonatan E. M. Laulainen
published: '2026-11-23'
abstract: 'In AI-guided materials discovery, machine-learning models increasingly
  decide which candidate materials should receive expensive first-principles or experimental
  evaluation. Standard reliability metrics such as uncertainty, calibration, novelty,
  and ranking accuracy evaluate properties of the predictions, but success on these
  metrics does not necessarily imply a better downstream screening decision. We study
  this mismatch for foundation machine-learned interatomic potentials (MACE-MP, CHGNet,
  Orb V3) used to rank candidate crystal structures before DFT verification. We evaluate
  three representative reliability interventions (novelty detection, sparse DFT calibration,
  and chemistry-level ranking audits) using a deployment objective that measures how
  much DFT can be avoided while maintaining a required recall of near-hull candidates.
  Across all three, a reliability signal can succeed on its immediate target without
  improving the final screening decision: novelty detects distribution shift but weakly
  ranks failure severity; calibration can improve pooled ranking metrics while leaving
  screening unchanged or degrading it; and sparse audits identify MLIP-chemistry combinations
  with poor ranking reliability without yielding a robustly beneficial routing policy.
  A two-oracle analysis further shows that the source of failure depends on the screening
  decision itself: under formation-energy screening, even perfect knowledge of average
  ranking reliability can select the wrong model, whereas in the evaluated hull-aligned
  variant the oracle target becomes decision-aligned but finite-budget audits still
  fail to realize the value. Reliability should be evaluated relative to the decision
  it supports: the relevant question is not whether a model is uncertain or inaccurate,
  but whether acquiring and acting on additional information will improve the final
  discovery decision enough to justify its cost.'
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.30066'
  categories:
  - cs.LG
  - cond-mat.mtrl-sci
---

# Diagnostic Accuracy Is Not Deployment Value: Decision-Aligned Reliability Evaluation for Foundation MLIPs in Materials Discovery

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.30066
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Harry Sevi, Joonatan E. M. Laulainen
- **Published:** 2026-11-23

## Summary
In AI-guided materials discovery, machine-learning models increasingly decide which candidate materials should receive expensive first-principles or experimental evaluation. Standard reliability metrics such as uncertainty, calibration, novelty, and ranking accuracy evaluate properties of the predictions, but success on these metrics does not necessarily imply a better downstream screening decision. We study this mismatch for foundation machine-learned interatomic potentials (MACE-MP, CHGNet, Orb V3) used to rank candidate crystal structures before DFT verification. We evaluate three representative reliability interventions (novelty detection, sparse DFT calibration, and chemistry-level ranking audits) using a deployment objective that measures how much DFT can be avoided while maintaining a required recall of near-hull candidates. Across all three, a reliability signal can succeed on its immediate target without improving the final screening decision: novelty detects distribution shift but weakly ranks failure severity; calibration can improve pooled ranking metrics while leaving screening unchanged or degrading it; and sparse audits identify MLIP-chemistry combinations with poor ranking reliability without yielding a robustly beneficial routing policy. A two-oracle analysis further shows that the source of failure depends on the screening decision itself: under formation-energy screening, even perfect knowledge of average ranking reliability can select the wrong model, whereas in the evaluated hull-aligned variant the oracle target becomes decision-aligned but finite-budget audits still fail to realize the value. Reliability should be evaluated relative to the decision it supports: the relevant question is not whether a model is uncertain or inaccurate, but whether acquiring and acting on additional information will improve the final discovery decision enough to justify its cost.

## Provider details
- **Arxiv Id:** 2611.30066
- **Categories:** ["cs.LG", "cond-mat.mtrl-sci"]
