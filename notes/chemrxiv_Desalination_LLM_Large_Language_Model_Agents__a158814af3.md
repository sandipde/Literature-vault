---
title: 'Desalination LLM: Large Language Model Agents Design Efficient Graphene Membranes
  for Water Desalination'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011905/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011905/v1
captured_by: auto-scanner
date: '2026-11-10'
captured_at: '2026-11-10T13:12:34+00:00'
last_requested: '2026-11-10T13:12:34+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Omid Barati Farimani
- Amir Barati Farimani
published: '2026-11-10'
abstract: 'Graphene nanopores can, in principle, combine high water permeability with
  strong salt rejection, but finding pore geometries that do both usually requires
  many molecular dynamics (MD) simulations. We describe a design framework in which
  a large language model (LLM) grows a nanopore atom by atom, using pretrained predictors
  of water flux and ion rejection to judge each candidate. Two recent models, Claude
  Opus 5.5 and GPT-6.1 Sol, were tested with the same prompt and the same design protocol
  (30 steps, up to 30 trials per step, at most three atoms removed per trial, and
  a 90% ion-rejection floor). We wanted to know how much of an agent’s performance
  comes from the model and how much from the surrounding scaffold, so each model was
  run twice: once as a tool-using agent with access to the predictors, and once in
  conversation only, where it chose atoms and estimated performance without any feedback.
  Three scaffold-only baselines that contain no language model were run for comparison.
  With tools, both models stayed above the rejection floor at every step. Claude Opus
  5.5 produced a single, island-free pore with a predicted flux of 122.3 ns−1 at 93.2%
  rejection, and GPT-6.1 Sol reached 131.7 ns−1 at 90.2%. Without tools the two models
  erred in opposite directions. Claude Opus 5.5 overestimated rejection and removed
  too many atoms, ending at 64.3% rejection, whereas GPT-6.1 Sol was overly cautious
  and recovered only 30% of the flux reached by its scaffold. A greedy search restricted
  by simple manufacturability rules matched or exceeded both agents in flux. Compared
  with the MD dataset and the deep reinforcement learning (DRL) designs of earlier
  work, the agents placed a larger share of their high-rejection pores above 120 ns−1.
  Taken together, the results indicate that predictor feedback, rather than the language
  model on its own, is what keeps LLM-guided pore design on target, and the six-condition
  protocol gives a simple way to make that attribution for other models.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011905/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Desalination LLM: Large Language Model Agents Design Efficient Graphene Membranes for Water Desalination

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011905/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Omid Barati Farimani, Amir Barati Farimani
- **Published:** 2026-11-10

## Summary
Graphene nanopores can, in principle, combine high water permeability with strong salt rejection, but finding pore geometries that do both usually requires many molecular dynamics (MD) simulations. We describe a design framework in which a large language model (LLM) grows a nanopore atom by atom, using pretrained predictors of water flux and ion rejection to judge each candidate. Two recent models, Claude Opus 5.5 and GPT-6.1 Sol, were tested with the same prompt and the same design protocol (30 steps, up to 30 trials per step, at most three atoms removed per trial, and a 90% ion-rejection floor). We wanted to know how much of an agent’s performance comes from the model and how much from the surrounding scaffold, so each model was run twice: once as a tool-using agent with access to the predictors, and once in conversation only, where it chose atoms and estimated performance without any feedback. Three scaffold-only baselines that contain no language model were run for comparison. With tools, both models stayed above the rejection floor at every step. Claude Opus 5.5 produced a single, island-free pore with a predicted flux of 122.3 ns−1 at 93.2% rejection, and GPT-6.1 Sol reached 131.7 ns−1 at 90.2%. Without tools the two models erred in opposite directions. Claude Opus 5.5 overestimated rejection and removed too many atoms, ending at 64.3% rejection, whereas GPT-6.1 Sol was overly cautious and recovered only 30% of the flux reached by its scaffold. A greedy search restricted by simple manufacturability rules matched or exceeded both agents in flux. Compared with the MD dataset and the deep reinforcement learning (DRL) designs of earlier work, the agents placed a larger share of their high-rejection pores above 120 ns−1. Taken together, the results indicate that predictor feedback, rather than the language model on its own, is what keeps LLM-guided pore design on target, and the six-condition protocol gives a simple way to make that attribution for other models.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011905/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
