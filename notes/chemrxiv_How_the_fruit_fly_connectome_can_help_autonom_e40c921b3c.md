---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: AI agents and retrieval
enrichment_tags: [autonomous-laboratories, connectome-models, instrument-control, edge-inference]
title: How the fruit fly connectome can help autonomous materials discovery
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010667/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15010667/v1
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
abstract: 'Autonomous laboratories for two-dimensional semiconductors pair a recipe
  planner with instruments that return in situ spectra every few seconds. Some decisions
  are too fast for the planner: stop a failing selenization anneal, flag a flake that
  is not the logged material, or end an ion irradiation at a set vacancy density,
  from a few examples, on a small computer at the instrument. The fruit fly takes
  decisions of this form with two structures whose wiring is measured at synapse level:
  the mushroom body, a one-shot memory for odours, and the ventral nerve cord, which
  turns a few descending commands into local reflexes. We asked which instrument jobs
  models wired from these connectomes do better than engineered tools. A mushroom-body
  model of 685 projection neurons and 5,177 Kenyon cells read one Raman band per glomerulus;
  over 20 paired seeds, on simulated selenization Raman streams and on Ar + irradiation
  anchored in published in situ spectra, it lost the fewest flakes when one failed
  run taught a stop rule (3.3 of 30, against 3.9 for a nearest neighbour), read vacancy
  density from its sparse code with less error than from the raw spectrum (5.5 % against
  6.4 %), and ran in 0.30 ms on a Raspberry Pi 5 within 152 kB. A stop decided at
  the furnace, as the nerve cord decides reflexes, prevented the losses of a planner
  that needed 60 s per turn (0.15 against 10.7 flakes of 30). It did not choose recipes.
  In three animals and after training, measured wiring matched a degree-preserving
  shuffle, and the nerve-cord wiring matched a ridge regression: the connectome contributes
  an architecture and wiring statistics, not a partner map. As hardware, the fixed
  wiring can be binary and each plastic synapse needs about 64 levels. The connectome
  supplies a low-cost reflex layer under the planner, not a replacement.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010667/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# How the fruit fly connectome can help autonomous materials discovery

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010667/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Kinston Ackölf, Taylor D. Sparks
- **Published:** 2026-10-19

## Summary
Autonomous laboratories for two-dimensional semiconductors pair a recipe planner with instruments that return in situ spectra every few seconds. Some decisions are too fast for the planner: stop a failing selenization anneal, flag a flake that is not the logged material, or end an ion irradiation at a set vacancy density, from a few examples, on a small computer at the instrument. The fruit fly takes decisions of this form with two structures whose wiring is measured at synapse level: the mushroom body, a one-shot memory for odours, and the ventral nerve cord, which turns a few descending commands into local reflexes. We asked which instrument jobs models wired from these connectomes do better than engineered tools. A mushroom-body model of 685 projection neurons and 5,177 Kenyon cells read one Raman band per glomerulus; over 20 paired seeds, on simulated selenization Raman streams and on Ar + irradiation anchored in published in situ spectra, it lost the fewest flakes when one failed run taught a stop rule (3.3 of 30, against 3.9 for a nearest neighbour), read vacancy density from its sparse code with less error than from the raw spectrum (5.5 % against 6.4 %), and ran in 0.30 ms on a Raspberry Pi 5 within 152 kB. A stop decided at the furnace, as the nerve cord decides reflexes, prevented the losses of a planner that needed 60 s per turn (0.15 against 10.7 flakes of 30). It did not choose recipes. In three animals and after training, measured wiring matched a degree-preserving shuffle, and the nerve-cord wiring matched a ridge regression: the connectome contributes an architecture and wiring statistics, not a partner map. As hardware, the fixed wiring can be binary and each plastic synapse needs about 64 levels. The connectome supplies a low-cost reflex layer under the planner, not a replacement.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010667/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment
- **Concise summary:** Connectome-inspired models are evaluated as low-latency instrument reflex layers for Raman-based materials workflows, beneath a slower recipe planner.
- **Why it matters:** Local stopping decisions address a different autonomy bottleneck from recipe selection, and the reported matched-shuffle results distinguish architectural value from specific biological wiring.
- **Caveat:** The v1 study uses simulated streams and irradiation data anchored in published spectra; its abstract explicitly does not claim recipe planning or a unique advantage of exact synaptic maps.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15010667/v1); analysis based only on captured metadata, not independently verified full text.
