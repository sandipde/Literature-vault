---
title: 'Orbitol: Crystal Generation on Wyckoff Orbits'
type: arxiv
source: https://arxiv.org/abs/2610.30086
canonical_url: https://arxiv.org/abs/2610.30086
captured_by: sandipde
date: '2026-11-19'
captured_at: '2026-11-19T13:40:33+00:00'
last_requested: '2026-11-19T13:40:33+00:00'
issue: '207'
status: to-read
authors:
- Ivan Žugec
- Joshua Rosenthal
- Ivor Lončarić
- Jan-Willem van de Meent
- Tin Hadži Veljković
published: '2026-10-21'
abstract: Generative models propose crystalline materials by learning composition
  and geometry, but unconditional sampling gives no direct control over the space
  group, which constrains whether responses such as piezoelectricity are symmetry-allowed.
  We present Orbitol, a crystal generator built on the Crystalite diffusion Transformer
  that replaces atom tokens with Wyckoff-orbit tokens. Given a space group and a collection
  of occupied Wyckoff positions, Orbitol generates the atom type and free coordinates
  of each orbit together with a compatible lattice, so every valid structure is invariant
  under the operations of the requested group. It generates structures two to three
  orders of magnitude faster than the symmetry-aware baselines at the evaluated settings.
  On MP-20, 13.8% of Orbitol's attempts yielded stable or metastable, unique and novel
  structures that retained the requested space group after relaxation, compared with
  10.8% for SGFM, the next best model. We also introduce SPARC, a score that combines
  retention of the raw detected space group with agreement between the retained-group
  and training distributions. Finally, we used Orbitol to generate candidates in piezoelectric
  crystal classes. Of the structures selected by internal screening, 89% passed our
  density functional theory checks, and 79% also matched no Materials Project or Alexandria
  entry with the same space group. Their median figure of merit was nine times that
  of the piezoelectric materials computed in the Materials Project, and 24% of the
  new candidates ranked in that set's top 10%.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.30086'
  categories:
  - cs.LG
  primary_category: cs.LG
  updated: '2026-11-05T17:03:59Z'
  doi: ''
---

# Orbitol: Crystal Generation on Wyckoff Orbits

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.30086
- **Captured by:** @sandipde
- **Metadata:** complete (arXiv)
- **Authors:** Ivan Žugec, Joshua Rosenthal, Ivor Lončarić, Jan-Willem van de Meent, Tin Hadži Veljković
- **Published:** 2026-10-21

## Summary
Generative models propose crystalline materials by learning composition and geometry, but unconditional sampling gives no direct control over the space group, which constrains whether responses such as piezoelectricity are symmetry-allowed. We present Orbitol, a crystal generator built on the Crystalite diffusion Transformer that replaces atom tokens with Wyckoff-orbit tokens. Given a space group and a collection of occupied Wyckoff positions, Orbitol generates the atom type and free coordinates of each orbit together with a compatible lattice, so every valid structure is invariant under the operations of the requested group. It generates structures two to three orders of magnitude faster than the symmetry-aware baselines at the evaluated settings. On MP-20, 13.8% of Orbitol's attempts yielded stable or metastable, unique and novel structures that retained the requested space group after relaxation, compared with 10.8% for SGFM, the next best model. We also introduce SPARC, a score that combines retention of the raw detected space group with agreement between the retained-group and training distributions. Finally, we used Orbitol to generate candidates in piezoelectric crystal classes. Of the structures selected by internal screening, 89% passed our density functional theory checks, and 79% also matched no Materials Project or Alexandria entry with the same space group. Their median figure of merit was nine times that of the piezoelectric materials computed in the Materials Project, and 24% of the new candidates ranked in that set's top 10%.

## Provider details
- **Arxiv Id:** 2610.30086
- **Categories:** ["cs.LG"]
- **Primary Category:** cs.LG
- **Updated:** 2026-11-05T17:03:59Z
