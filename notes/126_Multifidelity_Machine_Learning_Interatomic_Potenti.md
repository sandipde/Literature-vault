---
title: Multifidelity Machine Learning Interatomic Potentials for Charged Point Defects
type: paper
source: https://journals.aps.org/prxenergy/abstract/10.1103/tzwd-cl3y
canonical_url: https://doi.org/10.1103/tzwd-cl3y
captured_by: sandipde
date: '2026-10-11'
captured_at: '2026-10-11T19:25:16+00:00'
last_requested: '2026-10-11T19:25:16+00:00'
issue: '126'
status: to-read
authors:
- Xinwei Wang
- Irea Mosquera-Lois
- Aron Walsh
published: '2026-10-08'
abstract: Machine learning interatomic potentials (MLIPs) can now reproduce the energy,
  forces, and stresses of bulk materials with high accuracy compared to first-principles
  calculations. The description of imperfections, where coordination environments
  and electron counts deviate from those found in pristine reference structures, remains
  a challenge. We find that the current generation of foundation MLIPs does not describe
  the defect physics of the photovoltaic absorber Sb 2 Se 3 . We introduce global
  defect charge embeddings that distinguish the bonding characteristics of different
  charge states. We further employ a multifidelity approach that combines low-cost
  (semilocal exchange-correlation functional) reference data with high-quality (nonlocal
  hybrid functional) energies and forces that describe well the subtleties of the
  defect energy landscape. The resulting defect-capable force fields can find stable
  structural configurations and predict defect thermodynamics in quantitative agreement
  with direct quantum mechanical calculations, at a fraction of the computational
  cost.
metadata_provider: Crossref
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: ML interatomic potentials
enrichment_tags: [charged-defects, multifidelity-learning, charge-embeddings]
provider_data:
  doi: 10.1103/tzwd-cl3y
  journal: PRX Energy
  publisher: American Physical Society (APS)
  volume: '5'
  issue: '4'
  page: ''
  type: journal-article
  subjects: []
  license:
  - start:
      date-parts:
      - - 2026
        - 10
        - 8
      date-time: '2026-10-08T00:00:00Z'
      timestamp: 1791417600000
    content-version: vor
    delay-in-days: 0
    URL: https://creativecommons.org/licenses/by/4.0/
---

# Multifidelity Machine Learning Interatomic Potentials for Charged Point Defects

- **Type:** paper
- **Source:** https://journals.aps.org/prxenergy/abstract/10.1103/tzwd-cl3y
- **Captured by:** @sandipde
- **Metadata:** complete (Crossref)
- **Authors:** Xinwei Wang, Irea Mosquera-Lois, Aron Walsh
- **Published:** 2026-10-08

## Summary
Machine learning interatomic potentials (MLIPs) can now reproduce the energy, forces, and stresses of bulk materials with high accuracy compared to first-principles calculations. The description of imperfections, where coordination environments and electron counts deviate from those found in pristine reference structures, remains a challenge. We find that the current generation of foundation MLIPs does not describe the defect physics of the photovoltaic absorber Sb 2 Se 3 . We introduce global defect charge embeddings that distinguish the bonding characteristics of different charge states. We further employ a multifidelity approach that combines low-cost (semilocal exchange-correlation functional) reference data with high-quality (nonlocal hybrid functional) energies and forces that describe well the subtleties of the defect energy landscape. The resulting defect-capable force fields can find stable structural configurations and predict defect thermodynamics in quantitative agreement with direct quantum mechanical calculations, at a fraction of the computational cost.

## Provider details
- **Doi:** 10.1103/tzwd-cl3y
- **Journal:** PRX Energy
- **Publisher:** American Physical Society (APS)
- **Volume:** 5
- **Issue:** 4
- **Type:** journal-article
- **License:** [{"start": {"date-parts": [[2026, 10, 8]], "date-time": "2026-10-08T00:00:00Z", "timestamp": 1791417600000}, "content-version": "vor", "delay-in-days": 0, "URL": "https://creativecommons.org/licenses/by/4.0/"}]

## AI enrichment

- **Concise summary:** The captured abstract combines global defect-charge embeddings with semilocal and hybrid-functional training data to model charged defects in Sb2Se3. It reports improved defect configurations and thermodynamics relative to existing foundation MLIPs.
- **Why it matters:** Charge state and reference-data fidelity are explicit design choices here, not problems solved merely by increasing a neutral bulk training set.
- **Caveat:** Reported agreement is material- and reference-dependent; transferability and cost claims have not been independently checked.
- **Evidence:** [Captured source](https://journals.aps.org/prxenergy/abstract/10.1103/tzwd-cl3y); analysis based only on captured metadata, not independently verified full text.
