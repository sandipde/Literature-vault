---
title: 'ML-COHP: predicting bond descriptors using latent space of a universal interatomic
  potentials'
type: arxiv
source: https://arxiv.org/abs/2610.40445
canonical_url: https://arxiv.org/abs/2610.40445
captured_by: auto-scanner
date: '2026-10-30'
captured_at: '2026-10-30T11:09:08+00:00'
last_requested: '2026-10-30T11:09:08+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Daniil S. Alekseev
- Ilya V. Chepkasov
- Alexander G. Kvashnin
published: '2026-10-29'
abstract: The integrated crystal orbital Hamilton population (ICOHP) is the standard
  measure of bond strength in a DFT calculation, but every structure needs its own
  DFT single point and LOBSTER projection, which takes days for a cell of a hundred
  atoms, such as a grain boundary or a catalytic nanoparticle. We predict ICOHP from
  the frozen descriptors of a MACE foundation model. A symmetric pair head reads the
  scalar and bond-projected vector channels of the two atoms and corrects a pair baseline
  built from the element embeddings of the same model. We tested the model on the
  high-entropy diboride (Hf,Zr,Ti,Nb,Ta)B$_2$, Pt clusters on defective graphene and
  Pt/Pd nanoparticles with adsorbed O$_2$. The error on bonds stronger than 0.5 eV
  is 1.6-4.1%, about half that of the Gaussian-process model of Ferreira et al. trained
  on the same data. Trained only on high-temperature HEB$_2$ snapshots, the model
  reproduces the LOBSTER ICOHP of relaxed grain boundary cells to 0.06 eV in about
  a second, against 5-51 hours of LOBSTER. The vector channels halve the error compared
  to the scalar ones, and the baseline keeps the model usable with two training structures.
  With geometries from a fine-tuned MACE potential, the model gives the bonding of
  Pt/Pd particles over a continuous O$_2$ coverage, and DFT on these particles shows
  that O$_2$ costs a Pt-rich shell several times more metal--metal bonding than a
  Pd shell.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.40445'
  categories:
  - physics.comp-ph
  - cond-mat.mtrl-sci
---

# ML-COHP: predicting bond descriptors using latent space of a universal interatomic potentials

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.40445
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Daniil S. Alekseev, Ilya V. Chepkasov, Alexander G. Kvashnin
- **Published:** 2026-10-29

## Summary
The integrated crystal orbital Hamilton population (ICOHP) is the standard measure of bond strength in a DFT calculation, but every structure needs its own DFT single point and LOBSTER projection, which takes days for a cell of a hundred atoms, such as a grain boundary or a catalytic nanoparticle. We predict ICOHP from the frozen descriptors of a MACE foundation model. A symmetric pair head reads the scalar and bond-projected vector channels of the two atoms and corrects a pair baseline built from the element embeddings of the same model. We tested the model on the high-entropy diboride (Hf,Zr,Ti,Nb,Ta)B$_2$, Pt clusters on defective graphene and Pt/Pd nanoparticles with adsorbed O$_2$. The error on bonds stronger than 0.5 eV is 1.6-4.1%, about half that of the Gaussian-process model of Ferreira et al. trained on the same data. Trained only on high-temperature HEB$_2$ snapshots, the model reproduces the LOBSTER ICOHP of relaxed grain boundary cells to 0.06 eV in about a second, against 5-51 hours of LOBSTER. The vector channels halve the error compared to the scalar ones, and the baseline keeps the model usable with two training structures. With geometries from a fine-tuned MACE potential, the model gives the bonding of Pt/Pd particles over a continuous O$_2$ coverage, and DFT on these particles shows that O$_2$ costs a Pt-rich shell several times more metal--metal bonding than a Pd shell.

## Provider details
- **Arxiv Id:** 2610.40445
- **Categories:** ["physics.comp-ph", "cond-mat.mtrl-sci"]
