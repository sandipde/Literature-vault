---
title: Applicability Domain of Universal Machine Learning Interatomic Potentials at
  Solid-State Battery Interfaces
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011777/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011777/v1
captured_by: auto-scanner
date: '2026-11-06'
captured_at: '2026-11-06T12:40:38+00:00'
last_requested: '2026-11-06T12:40:38+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Umang Agarwal
- Mengke Li
- Gopalakrishnan Sai Gautam
- Zeyu Deng
published: '2026-11-06'
abstract: Universal machine learning interatomic potentials (uMLIPs) are trained predominantly
  on bulk systems, yet are increasingly applied to solid-solid interfaces. Evaluating
  six uMLIPs against DFT across 24 Li-metal/solid-electrolyte interfaces, we map their
  applicability domain (AD) and where they break down. Total energies are predicted
  reasonably well (MAE < 15 meV/atom), whereas interatomic forces at the interfaces
  are not. Most models underestimate the interfacial formation energy by 0.32 J/m2
  and overestimate the work of adhesion by 0.26 J/m2, and none reproduces the stability
  ordering of polyanion-containing interfaces. Despite large force errors for the
  interfaces, Li-ion kinetics agree well across models. The errors concentrate on
  the interface atoms and are larger for the polyanion chemistries. Descriptor-based
  analysis traces the higher force errors to interfacial environments that lie outside
  the pretraining data. Fine-tuning can close the accuracy gap, but only with data
  that samples the bonding across the interface, whereas slab data alone degrades
  performance. All models struggle on the same chemistries irrespective of the architecture,
  indicating the coverage of the pretraining data as the primary limitation. Overall,
  pretrained uMLIPs are suitable for qualitative screening of interfaces with simple
  single anion electrolytes, while those containing polyanions require interface-specific
  data.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011777/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Applicability Domain of Universal Machine Learning Interatomic Potentials at Solid-State Battery Interfaces

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011777/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Umang Agarwal, Mengke Li, Gopalakrishnan Sai Gautam, Zeyu Deng
- **Published:** 2026-11-06

## Summary
Universal machine learning interatomic potentials (uMLIPs) are trained predominantly on bulk systems, yet are increasingly applied to solid-solid interfaces. Evaluating six uMLIPs against DFT across 24 Li-metal/solid-electrolyte interfaces, we map their applicability domain (AD) and where they break down. Total energies are predicted reasonably well (MAE < 15 meV/atom), whereas interatomic forces at the interfaces are not. Most models underestimate the interfacial formation energy by 0.32 J/m2 and overestimate the work of adhesion by 0.26 J/m2, and none reproduces the stability ordering of polyanion-containing interfaces. Despite large force errors for the interfaces, Li-ion kinetics agree well across models. The errors concentrate on the interface atoms and are larger for the polyanion chemistries. Descriptor-based analysis traces the higher force errors to interfacial environments that lie outside the pretraining data. Fine-tuning can close the accuracy gap, but only with data that samples the bonding across the interface, whereas slab data alone degrades performance. All models struggle on the same chemistries irrespective of the architecture, indicating the coverage of the pretraining data as the primary limitation. Overall, pretrained uMLIPs are suitable for qualitative screening of interfaces with simple single anion electrolytes, while those containing polyanions require interface-specific data.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011777/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
