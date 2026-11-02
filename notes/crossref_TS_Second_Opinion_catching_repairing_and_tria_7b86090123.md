---
title: 'TS Second Opinion: catching, repairing and triaging mirror-image errors in
  machine-learned transition states'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011459/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011459/v1
captured_by: auto-scanner
date: '2026-11-02'
captured_at: '2026-11-02T13:02:05+00:00'
last_requested: '2026-11-02T13:02:05+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Tamana Sisodiya
published: '2026-11-02'
abstract: 'Generative models now predict a reaction’s transition state (TS) in milliseconds,
  but they cannot say when a guess is wrong. On the RDB7 benchmark, 17.7% of the TS
  guesses from GoFlow, a flow-matching TS generator, have a stereocentre the wrong
  way round, and 85% of those still count as accurate by the usual distance-based
  score. 90% of these errors are whole mirror images, which have the same energy and
  vibrational frequencies as the correct TS, so they also pass a frequency check.
  We present TS Second Opinion, a model-agnostic layer that runs after generation.
  Chemists state checks in plain English; a large language model (Claude) writes each
  check as Python, and a gate keeps it only if it accepts at least 99% of 9,540 reference
  DFT transition states, never crashes, and still catches mirrored or distorted ones.
  The accepted checks then test every guess, repair whole mirror images by reflection,
  and assign each reaction a verdict (trust, check with DFT, or re-generate); conformal
  selection turns the ranking into a set of trusted reactions with a stated average
  error rate. On 1,194 held-out RDB7 reactions with eight GoFlow models, two LLM-written
  stereo checks catch 93% of wrong-handed guesses at 0.2% false alarms, wrong-handed
  final answers fall from 17.7% to 2.3%, and 80% of reactions can be trusted at a
  5% average geometry-error rate. New ωB97X/def2-SVP transition-state optimisations
  on 16 reactions support both the symmetry argument and the verdicts: an unrepaired
  mirror image converges to a first-order saddle point 0.0006 kcal/mol from the repaired
  one, all six trusted guesses reach the reference TS, and none of the six re-generate
  guesses do, although five of them still pass a DFT frequency check. The results
  are mostly retrospective, on one dataset and one model family; code, data and a
  browser app are openly available.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011459/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# TS Second Opinion: catching, repairing and triaging mirror-image errors in machine-learned transition states

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011459/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Tamana Sisodiya
- **Published:** 2026-11-02

## Summary
Generative models now predict a reaction’s transition state (TS) in milliseconds, but they cannot say when a guess is wrong. On the RDB7 benchmark, 17.7% of the TS guesses from GoFlow, a flow-matching TS generator, have a stereocentre the wrong way round, and 85% of those still count as accurate by the usual distance-based score. 90% of these errors are whole mirror images, which have the same energy and vibrational frequencies as the correct TS, so they also pass a frequency check. We present TS Second Opinion, a model-agnostic layer that runs after generation. Chemists state checks in plain English; a large language model (Claude) writes each check as Python, and a gate keeps it only if it accepts at least 99% of 9,540 reference DFT transition states, never crashes, and still catches mirrored or distorted ones. The accepted checks then test every guess, repair whole mirror images by reflection, and assign each reaction a verdict (trust, check with DFT, or re-generate); conformal selection turns the ranking into a set of trusted reactions with a stated average error rate. On 1,194 held-out RDB7 reactions with eight GoFlow models, two LLM-written stereo checks catch 93% of wrong-handed guesses at 0.2% false alarms, wrong-handed final answers fall from 17.7% to 2.3%, and 80% of reactions can be trusted at a 5% average geometry-error rate. New ωB97X/def2-SVP transition-state optimisations on 16 reactions support both the symmetry argument and the verdicts: an unrepaired mirror image converges to a first-order saddle point 0.0006 kcal/mol from the repaired one, all six trusted guesses reach the reference TS, and none of the six re-generate guesses do, although five of them still pass a DFT frequency check. The results are mostly retrospective, on one dataset and one model family; code, data and a browser app are openly available.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011459/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
