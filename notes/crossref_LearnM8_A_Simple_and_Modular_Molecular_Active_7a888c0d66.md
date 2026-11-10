---
title: 'LearnM8: A Simple and Modular Molecular Active Learning Framework for any
  Oracle'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011895/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011895/v1
captured_by: auto-scanner
date: '2026-11-10'
captured_at: '2026-11-10T13:12:34+00:00'
last_requested: '2026-11-10T13:12:34+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Antoine Lacour
- Maximilian Bähr
- Andrea Volkamer
published: '2026-11-10'
abstract: Make-on-demand chemical spaces contain more than 10 11 compounds, which
  makes exhaustive virtual screening by docking or another costly scoring method (the
  oracle) impractical. Active learning reduces this cost by training a surrogate model
  (learner) on labeled compounds and using an acquisition strategy to select the next
  batch to evaluate. However, available implementations are built around particular
  docking programs and need new code for each oracle, learner and acquisition strategy.
  Here, we present LearnM8 1.0, an open-source Python package for modular active learning
  in which the oracle is a replaceable function, such that docking, free-energy calculations,
  precomputed scores or laboratory measurements can drive the same workflow. LearnM8
  provides 19 learners, 7 acquisition strategies and 39 featurizers, together with
  user-defined cycle schedules, removal of compounds from later cycles that scored
  worst (pruning), per-cycle diversity metrics, saved per-cycle predictions and a
  persistent feature cache. In retrospective benchmarks on precomputed docking scores,
  LearnM8 recovered 98% of the best-scoring 0.1% of compounds in AmpC libraries of
  1 to 96 million compounds after evaluating 10% of each library. On a 116-million-compound
  D4 library the same protocol recovered 91%. In the same study, random selection
  recovered 9.4% of the 1-millioncompound AmpC library. Smaller batch sizes per cycle
  improved recovery at higher computational cost, and pruning reduced prediction workload
  while slightly reducing recovery. LearnM8 is released under the MIT license at https://github.com/drugm8/LearnM8.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011895/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# LearnM8: A Simple and Modular Molecular Active Learning Framework for any Oracle

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011895/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Antoine Lacour, Maximilian Bähr, Andrea Volkamer
- **Published:** 2026-11-10

## Summary
Make-on-demand chemical spaces contain more than 10 11 compounds, which makes exhaustive virtual screening by docking or another costly scoring method (the oracle) impractical. Active learning reduces this cost by training a surrogate model (learner) on labeled compounds and using an acquisition strategy to select the next batch to evaluate. However, available implementations are built around particular docking programs and need new code for each oracle, learner and acquisition strategy. Here, we present LearnM8 1.0, an open-source Python package for modular active learning in which the oracle is a replaceable function, such that docking, free-energy calculations, precomputed scores or laboratory measurements can drive the same workflow. LearnM8 provides 19 learners, 7 acquisition strategies and 39 featurizers, together with user-defined cycle schedules, removal of compounds from later cycles that scored worst (pruning), per-cycle diversity metrics, saved per-cycle predictions and a persistent feature cache. In retrospective benchmarks on precomputed docking scores, LearnM8 recovered 98% of the best-scoring 0.1% of compounds in AmpC libraries of 1 to 96 million compounds after evaluating 10% of each library. On a 116-million-compound D4 library the same protocol recovered 91%. In the same study, random selection recovered 9.4% of the 1-millioncompound AmpC library. Smaller batch sizes per cycle improved recovery at higher computational cost, and pruning reduced prediction workload while slightly reducing recovery. LearnM8 is released under the MIT license at https://github.com/drugm8/LearnM8.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011895/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
