---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [multi-fidelity-learning, autonomous-discovery, transfer-certification]
title: Evaluating transfer across modalities in autonomous materials systems
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15001271/v2
canonical_url: https://doi.org/10.26434/chemrxiv.15001271/v2
captured_by: auto-scanner
date: '2026-10-19'
captured_at: '2026-10-19T21:19:36+00:00'
last_requested: '2026-10-19T21:19:36+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Kinston Ackölf
- Taylor D Sparks
published: '2026-10-19'
abstract: 'A power device needs a wide-gap semiconductor and a heat-treated Al–Mg–Si
  alloy to cool it, and both draw on sources that disagree: band gaps from several
  levels of density functional theory (DFT) and from measurement, alloy formation
  energies from DFT and interatomic potentials. Multi-fidelity methods combine such
  sources only through paired values on a common scale and do not state in advance
  whether one source’s guidance holds in another. We test whether the relative differences
  between candidates, which lead and by how much, are preserved across sources whose
  values disagree. PEGKi infers relative ratings of decision bodies (any rule that
  ranks candidates) from comparison outcomes within each source, and scores every
  donor-to-receiver route with a robustness certificate or a refusal. The evidence
  is 261,053 archived band-gap records from eight sources and an Al–Mg–Si pool where
  every query runs a DFT or molecular-dynamics calculation. Orderings alone recover
  the accuracy ladder of the DFT levels, and experiment spreads material classes about
  twice as widely as the generalised gradient approximation. Transfer follows the
  database of origin more than the functional, and routing learned from measured campaigns
  outperforms the fixed default at every query size. For the alloy, the score picks
  each potential’s room-temperature run as donor at heat-treatment temperatures, the
  best measured choice in five of six cases, and discounts the two potentials that
  predict Mg 2 Si to be unstable. Relative margins therefore transfer where values
  do not, so a campaign can rate whose knowledge to reuse before committing compute
  or instrument time.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15001271/v2
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Evaluating transfer across modalities in autonomous materials systems

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15001271/v2
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Kinston Ackölf, Taylor D Sparks
- **Published:** 2026-10-19

## Summary
A power device needs a wide-gap semiconductor and a heat-treated Al–Mg–Si alloy to cool it, and both draw on sources that disagree: band gaps from several levels of density functional theory (DFT) and from measurement, alloy formation energies from DFT and interatomic potentials. Multi-fidelity methods combine such sources only through paired values on a common scale and do not state in advance whether one source’s guidance holds in another. We test whether the relative differences between candidates, which lead and by how much, are preserved across sources whose values disagree. PEGKi infers relative ratings of decision bodies (any rule that ranks candidates) from comparison outcomes within each source, and scores every donor-to-receiver route with a robustness certificate or a refusal. The evidence is 261,053 archived band-gap records from eight sources and an Al–Mg–Si pool where every query runs a DFT or molecular-dynamics calculation. Orderings alone recover the accuracy ladder of the DFT levels, and experiment spreads material classes about twice as widely as the generalised gradient approximation. Transfer follows the database of origin more than the functional, and routing learned from measured campaigns outperforms the fixed default at every query size. For the alloy, the score picks each potential’s room-temperature run as donor at heat-treatment temperatures, the best measured choice in five of six cases, and discounts the two potentials that predict Mg 2 Si to be unstable. Relative margins therefore transfer where values do not, so a campaign can rate whose knowledge to reuse before committing compute or instrument time.

## Provider details
- **Doi:** 10.26434/chemrxiv.15001271/v2
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment
- **Concise summary:** PEGKi evaluates whether relative candidate rankings and margins transfer between disagreeing information sources, issuing route-specific robustness certificates or refusals. Tests use archived band gaps and an Al-Mg-Si campaign with DFT and molecular-dynamics queries.
- **Why it matters:** Selecting which source to trust before spending compute could be more useful than forcing incompatible numerical values onto one scale.
- **Caveat:** The v2 preprint's transfer and routing results are unverified and domain-specific; a ranking certificate is not a guarantee of absolute property accuracy.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15001271/v2); analysis based only on captured metadata, not independently verified full text.
