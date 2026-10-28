---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [electronic-structure, orbital-learning, band-energies, delta-learning]
title: Beyond DFT electronic band structures via dual-space orbital learning
type: arxiv
source: https://arxiv.org/abs/2610.19919
canonical_url: https://arxiv.org/abs/2610.19919
captured_by: auto-scanner
date: '2026-10-15'
captured_at: '2026-10-15T09:34:27+00:00'
last_requested: '2026-10-20T09:32:08+00:00'
issue: scan:arxiv-ml-atomistic
status: to-read
authors:
- Minhyuk Kang
- Beom Seok Kang
- Nikolai Argatoff
- Miguel Nouman
- Danish Khan
- William A. Goddard
- Anima Anandkumar
published: '2026-10-14'
abstract: Accurate electronic band structures are essential for predicting material
  properties, but high-fidelity calculations are computationally demanding. We introduce
  O-kRystal, a dual-space orbital-learning framework that uses a lower-cost Perdew-Burke-Ernzerhof
  (PBE) calculation as both an energy baseline and a source of structured orbital
  information. Combining PBE band energies with real- and reciprocal-space orbital
  matrices, O-kRystal predicts higher-level corrections for individual electronic
  states as a function of crystal momentum and spin. For states within 5 eV of the
  band-edge midpoint, it predicts Heyd-Scuseria-Ernzerhof (HSE06) band energies with
  a mean absolute error of $0.171 \pm 0.009$ eV across nearly 6,000 three-dimensional
  materials spanning insulating, metallic, magnetic, and nonmagnetic systems. On a
  separate benchmark of six strongly correlated materials, it reduces the corresponding
  PBE band-energy MAE by 68.7% and resolves orbital-dependent changes in the relative
  placement of transition-metal d and ligand p states. Despite training only at high-symmetry
  points, it maintains comparable accuracy at unseen points along band paths and reconstructs
  HSE06 densities of states from dense Brillouin-zone predictions. Finally, training
  O-kRystal on $G_0W_0$ quasiparticle energies for two-dimensional materials demonstrates
  its applicability across levels of theory and the potential of orbital learning
  for higher-fidelity, momentum-resolved electronic-structure prediction beyond density
  functional theory.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.19919'
  categories:
  - cs.LG
  - cond-mat.mtrl-sci
---

# Beyond DFT electronic band structures via dual-space orbital learning

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.19919
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Minhyuk Kang, Beom Seok Kang, Nikolai Argatoff, Miguel Nouman, Danish Khan, William A. Goddard, Anima Anandkumar
- **Published:** 2026-10-14

## Summary
Accurate electronic band structures are essential for predicting material properties, but high-fidelity calculations are computationally demanding. We introduce O-kRystal, a dual-space orbital-learning framework that uses a lower-cost Perdew-Burke-Ernzerhof (PBE) calculation as both an energy baseline and a source of structured orbital information. Combining PBE band energies with real- and reciprocal-space orbital matrices, O-kRystal predicts higher-level corrections for individual electronic states as a function of crystal momentum and spin. For states within 5 eV of the band-edge midpoint, it predicts Heyd-Scuseria-Ernzerhof (HSE06) band energies with a mean absolute error of $0.171 \pm 0.009$ eV across nearly 6,000 three-dimensional materials spanning insulating, metallic, magnetic, and nonmagnetic systems. On a separate benchmark of six strongly correlated materials, it reduces the corresponding PBE band-energy MAE by 68.7% and resolves orbital-dependent changes in the relative placement of transition-metal d and ligand p states. Despite training only at high-symmetry points, it maintains comparable accuracy at unseen points along band paths and reconstructs HSE06 densities of states from dense Brillouin-zone predictions. Finally, training O-kRystal on $G_0W_0$ quasiparticle energies for two-dimensional materials demonstrates its applicability across levels of theory and the potential of orbital learning for higher-fidelity, momentum-resolved electronic-structure prediction beyond density functional theory.

## Provider details
- **Arxiv Id:** 2610.19919
- **Categories:** ["cs.LG", "cond-mat.mtrl-sci"]

## AI enrichment
- **Concise summary:** O-kRystal learns momentum- and spin-resolved corrections to PBE band energies from real- and reciprocal-space orbital information, targeting HSE06 and demonstrating a separate GW application.
- **Why it matters:** Retaining orbital information may support higher-fidelity band predictions beyond scalar energy corrections; this is electronic-structure learning, not an interatomic force field.
- **Caveat:** The arXiv abstract's 0.171 ± 0.009 eV error is restricted to states within 5 eV of the band-edge midpoint, and its correlated-material benchmark contains only six systems.
- **Evidence:** [Captured source](https://arxiv.org/abs/2610.19919); analysis based only on captured metadata, not independently verified full text.
