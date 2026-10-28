---
title: Sorption Molecular Dynamics of Point Defects in 2D Materials with a Machine
  Learning Potential
type: arxiv
source: https://arxiv.org/abs/2610.20063
canonical_url: https://arxiv.org/abs/2610.20063
captured_by: auto-scanner
date: '2026-10-15'
captured_at: '2026-10-15T09:34:27+00:00'
last_requested: '2026-10-15T09:34:27+00:00'
issue: scan:arxiv-mlips
status: to-read
authors:
- Nils-Ruben Skogemyr
- Albin Sjöstedt
- Isak Wernroth
- Isak Häggqvist
- Isac Ljungwald
- Hans-Ove Åkesson
- Henricus R. A. ten Eikelder
- Rickard Armiento
- Joel Davidsson
published: '2026-10-14'
abstract: Defect engineering is a crucial tool for tuning and tailoring the properties
  of two-dimensional (2D) materials. A key challenge is identifying which defects
  are kinetically stable at room temperature and sufficiently promising to warrant
  further investigation. However, identifying stable defects with suitable properties
  using first-principles calculations, such as density functional theory (DFT) is
  computationally demanding, effectively limiting the scope of high-throughput studies.
  In this work, we investigate whether the machine learning interatomic potential
  MACE can reproduce sorption trends (adsorption vs. absorption) previously obtained
  from high-throughput DFT calculations and extend the analysis to elevated temperatures.
  A total of 17,624 defect structures from the ADAQ database are simulated using MACE-accelerated
  molecular dynamics (MD) at both 0 K and 300 K. The results show that MACE successfully
  reproduces the overall sorption trends observed in DFT calculations at 0 K at a
  fraction of the computational cost. Simulations performed at 300 K further indicate
  that the qualitative sorption trends remain largely the same when including finite-temperature
  effects. These findings demonstrate that MACE-driven MD can be used as an effective
  high-throughput prescreening tool for defect-related studies in 2D materials, specially
  related to sorption. While conventional first-principles methods, such as DFT, remain
  necessary for accurate and quantitative validation, the use of MLIPs enables MD
  simulations of finite-temperature defect behavior at a fraction of the computational
  cost of DFT-based MD.
metadata_provider: arXiv
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: ML interatomic potentials
enrichment_tags: [point-defects, sorption, two-dimensional-materials]
provider_data:
  arxiv_id: '2610.20063'
  categories:
  - cond-mat.mtrl-sci
---

# Sorption Molecular Dynamics of Point Defects in 2D Materials with a Machine Learning Potential

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.20063
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Nils-Ruben Skogemyr, Albin Sjöstedt, Isak Wernroth, Isak Häggqvist, Isac Ljungwald, Hans-Ove Åkesson, Henricus R. A. ten Eikelder, Rickard Armiento, Joel Davidsson
- **Published:** 2026-10-14

## Summary
Defect engineering is a crucial tool for tuning and tailoring the properties of two-dimensional (2D) materials. A key challenge is identifying which defects are kinetically stable at room temperature and sufficiently promising to warrant further investigation. However, identifying stable defects with suitable properties using first-principles calculations, such as density functional theory (DFT) is computationally demanding, effectively limiting the scope of high-throughput studies. In this work, we investigate whether the machine learning interatomic potential MACE can reproduce sorption trends (adsorption vs. absorption) previously obtained from high-throughput DFT calculations and extend the analysis to elevated temperatures. A total of 17,624 defect structures from the ADAQ database are simulated using MACE-accelerated molecular dynamics (MD) at both 0 K and 300 K. The results show that MACE successfully reproduces the overall sorption trends observed in DFT calculations at 0 K at a fraction of the computational cost. Simulations performed at 300 K further indicate that the qualitative sorption trends remain largely the same when including finite-temperature effects. These findings demonstrate that MACE-driven MD can be used as an effective high-throughput prescreening tool for defect-related studies in 2D materials, specially related to sorption. While conventional first-principles methods, such as DFT, remain necessary for accurate and quantitative validation, the use of MLIPs enables MD simulations of finite-temperature defect behavior at a fraction of the computational cost of DFT-based MD.

## Provider details
- **Arxiv Id:** 2610.20063
- **Categories:** ["cond-mat.mtrl-sci"]

## AI enrichment

- **Concise summary:** The preprint uses MACE molecular dynamics on 17,624 ADAQ defect structures to compare adsorption and absorption trends at 0 K and 300 K. It reports qualitative agreement with earlier DFT trends.
- **Why it matters:** A large defect-screening workflow provides a task-specific test of MLIP usefulness beyond aggregate force errors.
- **Caveat:** Qualitative prescreening is not quantitative defect validation; the abstract explicitly retains a role for first-principles checks.
- **Evidence:** [Captured source](https://arxiv.org/abs/2610.20063); analysis based only on captured metadata, not independently verified full text.
