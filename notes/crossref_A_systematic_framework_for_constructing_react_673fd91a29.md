---
title: A systematic framework for constructing reactive machine learning interatomic
  potentials
type: paper
source: https://doi.org/10.1063/5.0344922
canonical_url: https://doi.org/10.1063/5.0344922
captured_by: auto-scanner
date: '2026-11-02'
captured_at: '2026-11-02T23:46:24+00:00'
last_requested: '2026-11-02T23:46:24+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Rahul Verma
- Nisarg Joshi
- Jim Pfaendtner
published: '2026-12-01'
abstract: Machine learning interatomic potentials (MLIPs) have emerged as an essential
  tool for extending the reach of atomistic simulations, offering near quantum level
  accuracy at a fraction of the computational cost. However, constructing reactive
  and transferable MLIPs that describe rare events, transition states, and high energy
  intermediates remains a significant challenge. While the active learning (AL) protocol
  has proven effective for iterative MLIP refinement, its integration with enhanced
  sampling techniques has typically been implemented in an ad hoc and problem specific
  manner, which limits its reproducibility and generalizability. Here, we present
  a systematic methodology for automated construction of reactive MLIPs using SPARC,
  an open-source workflow package that integrates AL with enhanced sampling through
  the PLUMED library. SPARC combines (i) query-by-committee uncertainty estimations
  to identify configurations where the ensemble of ML models disagrees, with (ii)
  enhanced sampling methods to access reactive regions of the potential energy surface
  that are otherwise inaccessible in unbiased molecular dynamics. We demonstrate the
  robustness of the workflow across three chemically distinct reactive systems, showing
  that stable and accurate reactive MLIPs can be constructed from minimal initial
  training data. In all cases, the workflow discovers high-energy configurations,
  including transition states.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1063/5.0344922
  journal: APL Machine Learning
  publisher: AIP Publishing
  type: journal-article
  subjects: []
---

# A systematic framework for constructing reactive machine learning interatomic potentials

- **Type:** paper
- **Source:** https://doi.org/10.1063/5.0344922
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Rahul Verma, Nisarg Joshi, Jim Pfaendtner
- **Published:** 2026-12-01

## Summary
Machine learning interatomic potentials (MLIPs) have emerged as an essential tool for extending the reach of atomistic simulations, offering near quantum level accuracy at a fraction of the computational cost. However, constructing reactive and transferable MLIPs that describe rare events, transition states, and high energy intermediates remains a significant challenge. While the active learning (AL) protocol has proven effective for iterative MLIP refinement, its integration with enhanced sampling techniques has typically been implemented in an ad hoc and problem specific manner, which limits its reproducibility and generalizability. Here, we present a systematic methodology for automated construction of reactive MLIPs using SPARC, an open-source workflow package that integrates AL with enhanced sampling through the PLUMED library. SPARC combines (i) query-by-committee uncertainty estimations to identify configurations where the ensemble of ML models disagrees, with (ii) enhanced sampling methods to access reactive regions of the potential energy surface that are otherwise inaccessible in unbiased molecular dynamics. We demonstrate the robustness of the workflow across three chemically distinct reactive systems, showing that stable and accurate reactive MLIPs can be constructed from minimal initial training data. In all cases, the workflow discovers high-energy configurations, including transition states.

## Provider details
- **Doi:** 10.1063/5.0344922
- **Journal:** APL Machine Learning
- **Publisher:** AIP Publishing
- **Type:** journal-article
