---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Mathematics and algorithms
enrichment_tags: [reduced-order-models, matched-accuracy, sensitivity-analysis, fluid-mechanics]
title: 'Learned corrections and a second-order sensitivity model for subsonic full-potential
  flow: a matched-accuracy comparison'
type: paper
source: https://doi.org/10.2139/ssrn.7624238
canonical_url: https://doi.org/10.2139/ssrn.7624238
captured_by: auto-scanner
date: '2026-10-17'
captured_at: '2026-10-17T18:59:38+00:00'
last_requested: '2026-10-17T18:59:38+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Doyeol Ahn
published: '2026-10-17'
abstract: Learned operator surrogates are often reported to be faster than classical
  solvers, whereas the comparison is rarely made at matched accuracy against a classical
  configuration that meets the same target. Here, we construct such a comparison for
  two-dimensional subsonic flow of an ideal compressible fluid past a small protuberance
  on a straight wall, governed by the full-potential equation on a finite domain.
  Reference solutions are established by manufactured-solution verification, three-grid
  comparisons of Q2 finite elements with up to 1024 elements across the protuberance,
  and acceptance rules fixed before evaluation. On these references we compare the
  linear solution, one chord iteration, learned nonlinear corrections, and a reduced-order
  model (ROM) that is quadratic in five shape coefficients and whose basis fields
  are obtained from first- and second-order sensitivity equations on the flat wall.
  The ROM requires no online finite-element solve. On two sets of ten randomly drawn
  shapes that were not used in model design, each evaluated at three maximum wall
  slopes up to 0.05, the ROM met the wall-pressure, flux and physical-admissibility
  targets in all 27 accepted conditions at Mach 0.6 and all 23 at Mach 0.75, with
  worst relative RMS errors of the wall pressure coefficient of 0.135% and 0.571%.
  At Mach 0.8 it met the targets in 21 of 26 accepted conditions; the five failures
  occur at the largest slope, where one chord iteration fails in the same conditions
  by nearly the same amount. A rule registered before evaluation, based on the transonic
  similarity parameter κ′ = εM²/β³ with ε the maximum wall slope, M the free-stream
  Mach number and β = √(1 - M²), predicted success in all 47 eligible conditions with
  κ′ ≤ 0.1. On the 23 accepted conditions at Mach 0.75, four frozen learned models
  had mean correction errors of 150–347%, above the 100% of the zero-correction baseline,
  whereas that of the ROM was 7.4%. With coefficients resident in memory, the ROM
  is 48–50 times faster than the cheapest measured classical configuration meeting
  the same target, and its construction cost is recovered after about 56 queries.
  The results are restricted to the stated shape family and finite domain; no conclusion
  on transonic flow with shocks follows.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.2139/ssrn.7624238
  journal: ''
  publisher: Elsevier BV
  type: posted-content
  subjects: []
---

# Learned corrections and a second-order sensitivity model for subsonic full-potential flow: a matched-accuracy comparison

- **Type:** paper
- **Source:** https://doi.org/10.2139/ssrn.7624238
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Doyeol Ahn
- **Published:** 2026-10-17

## Summary
Learned operator surrogates are often reported to be faster than classical solvers, whereas the comparison is rarely made at matched accuracy against a classical configuration that meets the same target. Here, we construct such a comparison for two-dimensional subsonic flow of an ideal compressible fluid past a small protuberance on a straight wall, governed by the full-potential equation on a finite domain. Reference solutions are established by manufactured-solution verification, three-grid comparisons of Q2 finite elements with up to 1024 elements across the protuberance, and acceptance rules fixed before evaluation. On these references we compare the linear solution, one chord iteration, learned nonlinear corrections, and a reduced-order model (ROM) that is quadratic in five shape coefficients and whose basis fields are obtained from first- and second-order sensitivity equations on the flat wall. The ROM requires no online finite-element solve. On two sets of ten randomly drawn shapes that were not used in model design, each evaluated at three maximum wall slopes up to 0.05, the ROM met the wall-pressure, flux and physical-admissibility targets in all 27 accepted conditions at Mach 0.6 and all 23 at Mach 0.75, with worst relative RMS errors of the wall pressure coefficient of 0.135% and 0.571%. At Mach 0.8 it met the targets in 21 of 26 accepted conditions; the five failures occur at the largest slope, where one chord iteration fails in the same conditions by nearly the same amount. A rule registered before evaluation, based on the transonic similarity parameter κ′ = εM²/β³ with ε the maximum wall slope, M the free-stream Mach number and β = √(1 - M²), predicted success in all 47 eligible conditions with κ′ ≤ 0.1. On the 23 accepted conditions at Mach 0.75, four frozen learned models had mean correction errors of 150–347%, above the 100% of the zero-correction baseline, whereas that of the ROM was 7.4%. With coefficients resident in memory, the ROM is 48–50 times faster than the cheapest measured classical configuration meeting the same target, and its construction cost is recovered after about 56 queries. The results are restricted to the stated shape family and finite domain; no conclusion on transonic flow with shocks follows.

## Provider details
- **Doi:** 10.2139/ssrn.7624238
- **Publisher:** Elsevier BV
- **Type:** posted-content

## AI enrichment
- **Concise summary:** A quadratic sensitivity-based reduced-order model is compared with learned corrections and classical methods for subsonic full-potential flow at matched accuracy. Within a small wall-shape family it often meets prescribed targets while the tested learned corrections perform poorly.
- **Why it matters:** Runtime comparisons are more meaningful when both classical and learned alternatives must satisfy the same physical and numerical acceptance rules.
- **Caveat:** The SSRN preprint explicitly restricts results to its shape family and finite domain; failures increase near the higher-Mach, larger-slope regime, and no shock-flow conclusion follows.
- **Evidence:** [Captured source](https://doi.org/10.2139/ssrn.7624238); analysis based only on captured metadata, not independently verified full text.
