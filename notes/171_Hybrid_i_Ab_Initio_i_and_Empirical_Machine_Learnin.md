---
title: "Hybrid\n                    <i>Ab Initio</i>\n                    and Empirical\
  \ Machine Learning Models for the Potential Energy Surface"
type: paper
source: https://journals.aps.org/prl/abstract/10.1103/x3hc-52cp
canonical_url: https://doi.org/10.1103/x3hc-52cp
captured_by: sandipde
date: '2026-10-20'
captured_at: '2026-10-20T16:24:26+00:00'
last_requested: '2026-10-20T16:24:26+00:00'
issue: '171'
status: to-read
authors:
- Pablo Peña-Cano
- Pablo M. Piaggi
published: '2026-10-14'
abstract: ''
metadata_provider: Crossref
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-public-source-recovery
enrichment_category: ML interatomic potentials
enrichment_tags: [hybrid-training, experimental-observables, ensemble-reweighting]
recovery_status: recovered
recovery_checked_on: '2026-10-28'
provider_data:
  doi: 10.1103/x3hc-52cp
  journal: Physical Review Letters
  publisher: American Physical Society (APS)
  volume: '137'
  issue: '16'
  page: ''
  type: journal-article
  subjects: []
  license:
  - start:
      date-parts:
      - - 2026
        - 10
        - 14
      date-time: '2026-10-14T00:00:00Z'
      timestamp: 1791936000000
    content-version: vor
    delay-in-days: 0
    URL: https://link.aps.org/licenses/aps-default-license
---

# Hybrid
                    <i>Ab Initio</i>
                    and Empirical Machine Learning Models for the Potential Energy Surface

- **Type:** paper
- **Source:** https://journals.aps.org/prl/abstract/10.1103/x3hc-52cp
- **Captured by:** @sandipde
- **Metadata:** complete (Crossref)
- **Authors:** Pablo Peña-Cano, Pablo M. Piaggi
- **Published:** 2026-10-14

## Provider details
- **Doi:** 10.1103/x3hc-52cp
- **Journal:** Physical Review Letters
- **Publisher:** American Physical Society (APS)
- **Volume:** 137
- **Issue:** 16
- **Type:** journal-article
- **License:** [{"start": {"date-parts": [[2026, 10, 14]], "date-time": "2026-10-14T00:00:00Z", "timestamp": 1791936000000}, "content-version": "vor", "delay-in-days": 0, "URL": "https://link.aps.org/licenses/aps-default-license"}]

## Source recovery

- **Checked on:** 2026-10-28.
- **Retrieved source:** https://journals.aps.org/prl/abstract/10.1103/x3hc-52cp
- **Outcome:** The publisher abstract describes simultaneous fitting to ab initio energies/forces and experimental static observables using ensemble reweighting during training. Water density maxima and radial distribution functions are the stated demonstrations.
- **Limitations:** Recovered abstract only; no independent assessment of simulation convergence or predictive transfer.

## AI enrichment

- **Concise summary:** The recovered abstract proposes hybrid potential training against electronic-structure data and experimental thermodynamic or structural observables. On-the-fly reweighting supplies ensemble averages for the observable-based loss.
- **Why it matters:** It directly targets the gap between microscopic reference accuracy and experimentally meaningful ensemble behavior.
- **Caveat:** Agreement for water observables used in model development does not establish broader transferability or an unbiased reference potential.
- **Evidence:** [Captured source](https://journals.aps.org/prl/abstract/10.1103/x3hc-52cp); [recovered publisher abstract](https://journals.aps.org/prl/abstract/10.1103/x3hc-52cp), retrieved 2026-10-28; no independent full-text verification.
