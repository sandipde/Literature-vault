---
title: Building a grain-boundary machine-learning force field by reactive sampling
  and data curation, and its application to large-scale grain-boundary transport in
  Li6PS5X (X =Cl, Br)
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15012608/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15012608/v1
captured_by: auto-scanner
date: '2026-11-23'
captured_at: '2026-11-23T15:38:12+00:00'
last_requested: '2026-11-23T15:38:12+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Hiroya Nakata
- Shogo Kadota
- Buichiro Ena
published: '2026-11-23'
abstract: General-purpose machine-learning interatomic potentials (MLIPs) achieve
  near-DFT accuracy for equilibrium properties, yet their reliability for rare, non-equilibrium
  events—such as Li migration in grain-boundary (GB) corescannot be judged from static
  error metrics alone. Here we present a datageneration, curation, and validation
  framework that turns this judgment into a routine check, demonstrated on argyrodite
  Li6PS5X. Reactive-path sampling (ODPMD) concentrated in the transition region yields
  configurations far from the existing data (44% novel vs. 4% for intact-phase frames),
  which are screened by a physical-consistency filter and selected by stratified sampling
  in a MatterSim descriptor space. Fine-tuning MatterSim on this compact, regime-balanced
  data set reduces held-out DFT Li-migration barrier errors from 44meV to 32meV MAE
  (median 25meV), mainly in the rate-limiting high-barrier tail, while retaining bulk
  properties. MD on GB models of up to 4344 atoms shows, for both models, a mild activation
  penalty (∆Ea = +50–80 meV) that suppresses Li diffusion mainly at low temperature
  (DGB/Dbulk ≈ 0.46 at 500 K vs. 0.59 for the universal model at the ordered boundary)
  but is nearly invisible at the 700–800 K commonly simulated; electric-field-driven
  non-equilibrium MD corroborates this weak blocking. The universal model thus captures
  the qualitative physics, but its quantitative reliability can be established only
  by validating local barri-
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15012608/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Building a grain-boundary machine-learning force field by reactive sampling and data curation, and its application to large-scale grain-boundary transport in Li6PS5X (X =Cl, Br)

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15012608/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Hiroya Nakata, Shogo Kadota, Buichiro Ena
- **Published:** 2026-11-23

## Summary
General-purpose machine-learning interatomic potentials (MLIPs) achieve near-DFT accuracy for equilibrium properties, yet their reliability for rare, non-equilibrium events—such as Li migration in grain-boundary (GB) corescannot be judged from static error metrics alone. Here we present a datageneration, curation, and validation framework that turns this judgment into a routine check, demonstrated on argyrodite Li6PS5X. Reactive-path sampling (ODPMD) concentrated in the transition region yields configurations far from the existing data (44% novel vs. 4% for intact-phase frames), which are screened by a physical-consistency filter and selected by stratified sampling in a MatterSim descriptor space. Fine-tuning MatterSim on this compact, regime-balanced data set reduces held-out DFT Li-migration barrier errors from 44meV to 32meV MAE (median 25meV), mainly in the rate-limiting high-barrier tail, while retaining bulk properties. MD on GB models of up to 4344 atoms shows, for both models, a mild activation penalty (∆Ea = +50–80 meV) that suppresses Li diffusion mainly at low temperature (DGB/Dbulk ≈ 0.46 at 500 K vs. 0.59 for the universal model at the ordered boundary) but is nearly invisible at the 700–800 K commonly simulated; electric-field-driven non-equilibrium MD corroborates this weak blocking. The universal model thus captures the qualitative physics, but its quantitative reliability can be established only by validating local barri-

## Provider details
- **Doi:** 10.26434/chemrxiv.15012608/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
