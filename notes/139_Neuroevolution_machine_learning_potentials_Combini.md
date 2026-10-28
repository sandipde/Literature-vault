---
title: 'Neuroevolution machine learning potentials: Combining high accuracy and low
  cost in atomistic simulations and application to heat transport'
type: paper
source: https://journals.aps.org/prb/abstract/10.1103/PhysRevB.104.104309
canonical_url: https://doi.org/10.1103/physrevb.104.104309
captured_by: sandipde
date: '2026-10-13'
captured_at: '2026-10-13T18:05:22+00:00'
last_requested: '2026-10-13T18:05:22+00:00'
issue: '139'
status: to-read
authors:
- Zheyong Fan
- Zezhu Zeng
- Cunzhi Zhang
- Yanzhou Wang
- Keke Song
- Haikuan Dong
- Yue Chen
- Tapio Ala-Nissila
published: '2021-09-20'
abstract: ''
metadata_provider: Crossref
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-public-source-recovery
enrichment_category: ML interatomic potentials
enrichment_tags: [neuroevolution, heat-transport, gpu-molecular-dynamics]
recovery_status: recovered
recovery_checked_on: '2026-10-28'
provider_data:
  doi: 10.1103/physrevb.104.104309
  journal: Physical Review B
  publisher: American Physical Society (APS)
  volume: '104'
  issue: '10'
  page: ''
  type: journal-article
  subjects: []
  license:
  - start:
      date-parts:
      - - 2021
        - 9
        - 20
      date-time: '2021-09-20T00:00:00Z'
      timestamp: 1632096000000
    content-version: vor
    delay-in-days: 0
    URL: https://link.aps.org/licenses/aps-default-license
---

# Neuroevolution machine learning potentials: Combining high accuracy and low cost in atomistic simulations and application to heat transport

- **Type:** paper
- **Source:** https://journals.aps.org/prb/abstract/10.1103/PhysRevB.104.104309
- **Captured by:** @sandipde
- **Metadata:** complete (Crossref)
- **Authors:** Zheyong Fan, Zezhu Zeng, Cunzhi Zhang, Yanzhou Wang, Keke Song, Haikuan Dong, Yue Chen, Tapio Ala-Nissila
- **Published:** 2021-09-20

## Provider details
- **Doi:** 10.1103/physrevb.104.104309
- **Journal:** Physical Review B
- **Publisher:** American Physical Society (APS)
- **Volume:** 104
- **Issue:** 10
- **Type:** journal-article
- **License:** [{"start": {"date-parts": [[2021, 9, 20]], "date-time": "2021-09-20T00:00:00Z", "timestamp": 1632096000000}, "content-version": "vor", "delay-in-days": 0, "URL": "https://link.aps.org/licenses/aps-default-license"}]

## Source recovery

- **Checked on:** 2026-10-28.
- **Retrieved source:** https://journals.aps.org/prb/abstract/10.1103/PhysRevB.104.104309
- **Outcome:** The publisher abstract describes evolutionary training of neural potentials with Chebyshev/Legendre descriptors, GPU implementation in GPUMD, and per-atom heat currents for heat-transport simulations.
- **Limitations:** Abstract recovery only; the reported speed exceeding ten million atom-steps per second on a V100 was not benchmarked here.

## AI enrichment

- **Concise summary:** NEP combines evolutionary training of neural interatomic potentials with GPU execution and accessible per-atom heat currents. The recovered abstract emphasizes heat transport in anharmonic or spatially disordered materials.
- **Why it matters:** Heat-current availability connects potential design to a measurable transport workflow, rather than treating force accuracy as the sole criterion.
- **Caveat:** This is a force-field framework, not a generator of amorphous structures; accuracy and throughput remain source-reported.
- **Evidence:** [Captured source](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.104.104309); [recovered publisher abstract](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.104.104309), retrieved 2026-10-28; no independent full-text or performance verification.
