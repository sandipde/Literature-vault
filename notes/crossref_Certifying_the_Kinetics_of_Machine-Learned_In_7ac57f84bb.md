---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: ML interatomic potentials
enrichment_tags: [rare-event-kinetics, rate-certification, reactive-paths, energy-errors]
title: Certifying the Kinetics of Machine-Learned Interatomic Potentials from Single-Point
  Energies
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010329/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15010329/v1
captured_by: auto-scanner
date: '2026-10-13'
captured_at: '2026-10-13T12:25:46+00:00'
last_requested: '2026-10-13T12:25:46+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Xiyao Yu
published: '2026-10-13'
abstract: 'Machine-learned interatomic potentials are validated by force errors on
  equilibrium configurations, yet activated rates depend on transition regions that
  equilibrium sampling rarely visits. In a onedimensional metastable double well,
  the worst-case rate sensitivity to force error grows as eβB/2 with barrier height
  B; a path-space bound valid at any friction shows that force error certifies rare-event
  frequencies only to within a factor that grows at the same rate. The leverage density
  weights energy errors by their influence on reactive transport: it is the normalised
  dissipation density of the reactive current. For reversible overdamped dynamics,
  the Dirichlet and Thomson principles give two-sided capacity bounds, converted to
  metastable rate bounds by basin population corrections. A path representation evaluates
  their averages from reactive trajectories, committor values and single-point energies.
  Sampling uses reference paths to assess sampled transitions and model paths to expose
  additional or overpopulated pathways. In alanine dipeptide, closely matched force
  errors produce rate changes from 0.49 to 3.5, consistent with estimated intervals.
  In Li3OCl, mechanism-resolved upper endpoints track six models’ vacancy-hop rates
  with a systematic underestimation of about 7%. Labels selected from both ensembles
  improve kinetics even as force errors rise. We propose reporting the energy-error
  contrast M between the leverage density and the basins, and the spread σν under
  the leverage density, alongside force error; both are independent of the energy
  zero.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010329/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Certifying the Kinetics of Machine-Learned Interatomic Potentials from Single-Point Energies

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010329/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Xiyao Yu
- **Published:** 2026-10-13

## Summary
Machine-learned interatomic potentials are validated by force errors on equilibrium configurations, yet activated rates depend on transition regions that equilibrium sampling rarely visits. In a onedimensional metastable double well, the worst-case rate sensitivity to force error grows as eβB/2 with barrier height B; a path-space bound valid at any friction shows that force error certifies rare-event frequencies only to within a factor that grows at the same rate. The leverage density weights energy errors by their influence on reactive transport: it is the normalised dissipation density of the reactive current. For reversible overdamped dynamics, the Dirichlet and Thomson principles give two-sided capacity bounds, converted to metastable rate bounds by basin population corrections. A path representation evaluates their averages from reactive trajectories, committor values and single-point energies. Sampling uses reference paths to assess sampled transitions and model paths to expose additional or overpopulated pathways. In alanine dipeptide, closely matched force errors produce rate changes from 0.49 to 3.5, consistent with estimated intervals. In Li3OCl, mechanism-resolved upper endpoints track six models’ vacancy-hop rates with a systematic underestimation of about 7%. Labels selected from both ensembles improve kinetics even as force errors rise. We propose reporting the energy-error contrast M between the leverage density and the basins, and the spread σν under the leverage density, alongside force error; both are independent of the energy zero.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010329/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment
- **Concise summary:** The authors derive kinetic bounds based on reactive-current leverage and single-point energy errors, arguing that equilibrium force errors poorly certify activated rates. Alanine-dipeptide and Li3OCl examples motivate reference- and model-path sampling.
- **Why it matters:** Labeling transition-relevant configurations can improve rates even when aggregate force error rises, challenging common MLIP selection criteria.
- **Caveat:** This preprint's certification claims rely on stated dynamical assumptions; the abstract reports systematic underestimation in Li3OCl, so estimated intervals should not be treated as universally validated bounds.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15010329/v1); analysis based only on captured metadata, not independently verified full text.
