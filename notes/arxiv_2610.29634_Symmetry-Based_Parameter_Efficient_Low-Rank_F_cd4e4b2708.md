---
title: Symmetry-Based Parameter Efficient Low-Rank Fine-Tuning for High-Throughput
  Calculation of Lattice Thermal Conductivity
type: arxiv
source: https://arxiv.org/abs/2610.29634
canonical_url: https://arxiv.org/abs/2610.29634
captured_by: auto-scanner
date: '2026-10-22'
captured_at: '2026-10-22T09:48:39+00:00'
last_requested: '2026-10-22T09:48:39+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Rustam Arabov
- Konstantin Sozykin
- Nikita Rybin
- Alexander Shapeev
published: '2026-10-21'
abstract: Accurate and efficient prediction of lattice thermal conductivity (LTC)
  is essential for developing materials for thermoelectric, microelectronic, and photovoltaic
  applications. Here, we present a methodology for high-throughput calculation of
  LTC across large datasets of compounds sharing a common crystal symmetry. Our approach
  combines fine-tuning of the MatterSim 1M universal machine-learned interatomic potential
  with LTC calculations based on the solution of the Boltzmann transport equation.
  We introduce a symmetry-based few-shot fine-tuning strategy (SBFS-FT) based on low-rank
  adaptation. In this approach, MatterSim 1M is fine-tuned on a small, carefully selected
  set of compounds that share a common crystal symmetry. The resulting potential is
  then applicable for accurate LTC calculations for compounds with this crystal symmetry,
  even if they were not included in the fine-tuning set. We tested our methodology
  on datasets of half-Heusler compounds (space group 216), materials with space group
  225, and spinels (space group 227). We demonstrated that LTC calculations with MatterSim
  1M fine-tuned using SBFS-FT exhibited a mean absolute relative difference from the
  reference results (obtained using moment tensor potentials and polyMLPs) 2-3 times
  smaller than that achieved with the non-fine-tuned MatterSim 1M potential. Moreover,
  the accuracy of LTC calculations with MatterSim 1M after SBFS-FT was comparable
  to that achieved using the MatterSim 1M potentials individually fine-tuned for each
  compound. Importantly, SBFS-FT enabled generation of the potential suitable for
  accurate LTC calculations across large compound datasets substantially faster than
  fine-tuning of MatterSim 1M for each compound individually, reducing the computational
  time by approximately a factor of 5-7 for a dataset of 100 compounds.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.29634'
  categories:
  - cond-mat.mtrl-sci
---

# Symmetry-Based Parameter Efficient Low-Rank Fine-Tuning for High-Throughput Calculation of Lattice Thermal Conductivity

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.29634
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Rustam Arabov, Konstantin Sozykin, Nikita Rybin, Alexander Shapeev
- **Published:** 2026-10-21

## Summary
Accurate and efficient prediction of lattice thermal conductivity (LTC) is essential for developing materials for thermoelectric, microelectronic, and photovoltaic applications. Here, we present a methodology for high-throughput calculation of LTC across large datasets of compounds sharing a common crystal symmetry. Our approach combines fine-tuning of the MatterSim 1M universal machine-learned interatomic potential with LTC calculations based on the solution of the Boltzmann transport equation. We introduce a symmetry-based few-shot fine-tuning strategy (SBFS-FT) based on low-rank adaptation. In this approach, MatterSim 1M is fine-tuned on a small, carefully selected set of compounds that share a common crystal symmetry. The resulting potential is then applicable for accurate LTC calculations for compounds with this crystal symmetry, even if they were not included in the fine-tuning set. We tested our methodology on datasets of half-Heusler compounds (space group 216), materials with space group 225, and spinels (space group 227). We demonstrated that LTC calculations with MatterSim 1M fine-tuned using SBFS-FT exhibited a mean absolute relative difference from the reference results (obtained using moment tensor potentials and polyMLPs) 2-3 times smaller than that achieved with the non-fine-tuned MatterSim 1M potential. Moreover, the accuracy of LTC calculations with MatterSim 1M after SBFS-FT was comparable to that achieved using the MatterSim 1M potentials individually fine-tuned for each compound. Importantly, SBFS-FT enabled generation of the potential suitable for accurate LTC calculations across large compound datasets substantially faster than fine-tuning of MatterSim 1M for each compound individually, reducing the computational time by approximately a factor of 5-7 for a dataset of 100 compounds.

## Provider details
- **Arxiv Id:** 2610.29634
- **Categories:** ["cond-mat.mtrl-sci"]
