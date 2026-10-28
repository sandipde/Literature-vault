---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: ML interatomic potentials
enrichment_tags: [enzyme-reactions, free-energy-barriers, universal-potentials, petase]
title: 'Whole-Enzyme Reactive Free-Energy Simulations with a Universal Machine Learning
  Interatomic Potential: Catalytic Mechanism and Mutational Effects of PETase'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15004671/v2
canonical_url: https://doi.org/10.26434/chemrxiv.15004671/v2
captured_by: auto-scanner
date: '2026-10-16'
captured_at: '2026-10-16T09:27:31+00:00'
last_requested: '2026-10-16T09:27:31+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Masataka Yamauchi
- Makoto Sato
published: '2026-10-16'
abstract: Universal machine learning interatomic potentials (uMLIPs) have emerged
  as powerful tools for atomistic simulations that achieve quantum mechanical accuracy
  at significantly reduced computational cost. Yet, their direct application to complex
  enzymatic reactions remains challenging owing to the immense size of solvated enzyme
  systems and the scarcity of transition-state structures in training data. In this
  study, we demonstrate that PFP (PreFerred Potential), a pretrained uMLIP across
  96 elements in nature, simulates the complete hydrolytic cycle of polyethylene terephthalate
  (PET) catalyzed by PETase as a single reactive domain of approximately 20,000 atoms,
  without multiscale partitioning or system-specific fine-tuning. Umbrella-sampling
  simulations revealed stepwise mechanisms for both acylation and deacylation through
  distinct tetrahedral intermediates. The computed rate-limiting deacylation barrier
  of 20.5 ± 0.3 kcal/mol is in agreement with the range of 18.0–18.7 kcal/mol inferred
  from experimental turnover numbers. The PFP-based simulations further capture catalytic
  consequences of point mutations from loss of function (D177N, M132A) to predicted
  activity enhancement (D157N) and reveal that simultaneous neutralization of three
  distal acidic residues which are located more than 10 Å from the active site raises
  the activation barrier due to a collective long-range electrostatic effect that
  emerges naturally in the partition-free treatment. These findings demonstrate that
  the pretrained uMLIP, PFP, can provide physically plausible free-energy profiles
  for enzymatic reaction mechanisms and capture mutational effects, providing a powerful
  platform for rational enzyme design.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15004671/v2
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Whole-Enzyme Reactive Free-Energy Simulations with a Universal Machine Learning Interatomic Potential: Catalytic Mechanism and Mutational Effects of PETase

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15004671/v2
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Masataka Yamauchi, Makoto Sato
- **Published:** 2026-10-16

## Summary
Universal machine learning interatomic potentials (uMLIPs) have emerged as powerful tools for atomistic simulations that achieve quantum mechanical accuracy at significantly reduced computational cost. Yet, their direct application to complex enzymatic reactions remains challenging owing to the immense size of solvated enzyme systems and the scarcity of transition-state structures in training data. In this study, we demonstrate that PFP (PreFerred Potential), a pretrained uMLIP across 96 elements in nature, simulates the complete hydrolytic cycle of polyethylene terephthalate (PET) catalyzed by PETase as a single reactive domain of approximately 20,000 atoms, without multiscale partitioning or system-specific fine-tuning. Umbrella-sampling simulations revealed stepwise mechanisms for both acylation and deacylation through distinct tetrahedral intermediates. The computed rate-limiting deacylation barrier of 20.5 ± 0.3 kcal/mol is in agreement with the range of 18.0–18.7 kcal/mol inferred from experimental turnover numbers. The PFP-based simulations further capture catalytic consequences of point mutations from loss of function (D177N, M132A) to predicted activity enhancement (D157N) and reveal that simultaneous neutralization of three distal acidic residues which are located more than 10 Å from the active site raises the activation barrier due to a collective long-range electrostatic effect that emerges naturally in the partition-free treatment. These findings demonstrate that the pretrained uMLIP, PFP, can provide physically plausible free-energy profiles for enzymatic reaction mechanisms and capture mutational effects, providing a powerful platform for rational enzyme design.

## Provider details
- **Doi:** 10.26434/chemrxiv.15004671/v2
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment
- **Concise summary:** The preprint uses pretrained PFP for an approximately 20,000-atom PETase reactive domain without multiscale partitioning or system-specific fine-tuning, reporting umbrella-sampled acylation/deacylation pathways and mutation effects.
- **Why it matters:** A partition-free treatment could explore coupling between active-site reactions and distal electrostatics without choosing a separate reactive region.
- **Caveat:** Claims are unverified; the reported 20.5 +/- 0.3 kcal/mol barrier lies above the cited experimental-inference range of 18.0-18.7 kcal/mol despite the abstract's agreement wording, so numerical uncertainty is not total model error.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15004671/v2); analysis based only on captured metadata, not independently verified full text.
