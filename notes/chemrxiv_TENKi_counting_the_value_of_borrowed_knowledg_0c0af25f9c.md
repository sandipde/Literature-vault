---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [knowledge-transfer, active-learning, ranking-priors, compute-budgets]
title: 'TENKi: counting the value of borrowed knowledge to a materials campaign in
  measurements saved'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010673/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15010673/v1
captured_by: auto-scanner
date: '2026-10-19'
captured_at: '2026-10-19T21:19:36+00:00'
last_requested: '2026-10-19T21:19:36+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Kinston Ackölf
- Taylor D. Sparks
published: '2026-10-19'
abstract: 'Materials campaigns draw on data of very different cost: a band gap costs
  almost nothing from a database, core-hours from a hybrid-functional density functional
  theory (DFT) calculation, and instrument time from a measurement. No calibration
  carries values from low-cost to costly sources, and multi-fidelity methods do not
  state how many costly evaluations an imported ordering of the candidates replaces.
  We test whether that ordering, with its margins, reduces the evaluations needed
  to reach a given ranking quality, and whether the saving can be measured for each
  route. TENKi (Transfer-ensemble Knowledge Inheritance) records ranking agreement
  against budget while a ranking model is fitted to queries that order several candidates
  at once, with the donor ordering entered as a prior whose trust is learned from
  incoming results. The evidence is 261,053 archived band-gap records from eight sources,
  171 semiconductors with gaps computed on demand, and an aluminium–magnesium–silicon
  (Al–Mg–Si) alloy pool computed with DFT and molecular dynamics. Queries ranking
  four candidates outperform pairwise comparisons on every source, a donor prior replaces
  nearly half of the early measurement budget, and a trained query-selection policy
  reaches the ranking quality of random selection with fewer evaluations on held-out
  sources, whereas hand-written rules do not. An ordering from the generalised gradient
  approximation cuts hybrid-functional compute about sixfold, while an archived ordering
  that lacks the alloys gives no saving at fixed trust; for Al–Mg–Si, a foundation-potential
  ordering lowers the DFT compute needed to find eight of the ten most stable compounds
  from 19% to 5%. The saving depends on direction and coverage, and the agreement-versus-budget
  curve separates disagreement that further sampling removes from gaps that remain,
  so a campaign can use these curves to decide which source to compute first, how
  far to trust it, and when further evaluations stop improving the ranking.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010673/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# TENKi: counting the value of borrowed knowledge to a materials campaign in measurements saved

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010673/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Kinston Ackölf, Taylor D. Sparks
- **Published:** 2026-10-19

## Summary
Materials campaigns draw on data of very different cost: a band gap costs almost nothing from a database, core-hours from a hybrid-functional density functional theory (DFT) calculation, and instrument time from a measurement. No calibration carries values from low-cost to costly sources, and multi-fidelity methods do not state how many costly evaluations an imported ordering of the candidates replaces. We test whether that ordering, with its margins, reduces the evaluations needed to reach a given ranking quality, and whether the saving can be measured for each route. TENKi (Transfer-ensemble Knowledge Inheritance) records ranking agreement against budget while a ranking model is fitted to queries that order several candidates at once, with the donor ordering entered as a prior whose trust is learned from incoming results. The evidence is 261,053 archived band-gap records from eight sources, 171 semiconductors with gaps computed on demand, and an aluminium–magnesium–silicon (Al–Mg–Si) alloy pool computed with DFT and molecular dynamics. Queries ranking four candidates outperform pairwise comparisons on every source, a donor prior replaces nearly half of the early measurement budget, and a trained query-selection policy reaches the ranking quality of random selection with fewer evaluations on held-out sources, whereas hand-written rules do not. An ordering from the generalised gradient approximation cuts hybrid-functional compute about sixfold, while an archived ordering that lacks the alloys gives no saving at fixed trust; for Al–Mg–Si, a foundation-potential ordering lowers the DFT compute needed to find eight of the ten most stable compounds from 19% to 5%. The saving depends on direction and coverage, and the agreement-versus-budget curve separates disagreement that further sampling removes from gaps that remain, so a campaign can use these curves to decide which source to compute first, how far to trust it, and when further evaluations stop improving the ranking.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010673/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment
- **Concise summary:** TENKi measures how donor rankings reduce the queries needed to reach a target ranking quality, learning trust in the donor as results arrive. Band-gap and Al-Mg-Si studies compare query policies and report route-dependent savings.
- **Why it matters:** Expressing transfer value as evaluations saved makes it actionable for choosing between cheap models and costly calculations.
- **Caveat:** The preprint's savings are unverified and depend on transfer direction and chemical coverage; the abstract itself reports no saving for an alloy-missing archived ordering at fixed trust.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15010673/v1); analysis based only on captured metadata, not independently verified full text.
