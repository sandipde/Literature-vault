---
title: "Dielectric Response of Short and Long Range Models of Nonuniform Liquids and Implications for Machine Learned Interatomic Potentials"
source: "https://arxiv.org/pdf/2610.04224"
captured_by: "sandipde"
date: 2026-10-09
issue: 4
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: ML interatomic potentials
enrichment_tags: [dielectric-response, long-range-electrostatics, confined-water]
---

# Dielectric Response of Short and Long Range Models of Nonuniform Liquids and Implications for Machine Learned Interatomic Potentials

- **Captured by:** @sandipde
- **Source:** https://arxiv.org/pdf/2610.04224

## Abstract
Dielectric screening of electric fields is modified by interfaces and confinement, and any accurate description of interfacial chemistry necessitates properly modeling the nonuniform dielectric tensor. However, models with short range interactions, such as local machine learned interatomic potentials (MLIPs), are increasingly used in simulations of molecular interfaces without quantitative understanding of their nonuniform dielectric response. To build this understanding, we use the framework provided by local molecular field (LMF) theory to quantify the roles of short and long range electrostatics in confined water. Short and long range models predict the same transverse dielectric profile but short range models predict qualitatively different longitudinal dielectric profiles than their long range counterparts. To understand these differences, we develop a Landau theory that shows that long range interactions stiffen polarization fluctuations by a factor of the bulk dielectric constant and reduce the interfacial polarization correlation length by an order of magnitude. LMF theory, which captures long range interactions with an averaged field, can correct the structure and dielectric response, but the standard fluctuation relation no longer holds. We derive a fluctuation relation and integral equation for LMF theory and demonstrate their accuracy for predicting longitudinal dielectric response. MLIPs that incorporate interfacial configurations in their training essentially learn a static mean field correction at the interface, such that the integral equation can be used to predict their nonuniform dielectric profile from polarization fluctuations. We also show that short range MLIPs can be combined with symmetry preserving mean field (SPMF) theory to provide a linear-scaling alternative for long range interactions and predicting nonuniform dielectric functions.

## AI enrichment

- **Concise summary:** The abstract distinguishes transverse and longitudinal dielectric responses of confined water under short- and long-range interactions. It develops local-molecular-field fluctuation relations and discusses mean-field corrections for short-range MLIPs.
- **Why it matters:** Matching local interfacial structure need not imply correct polarization fluctuations, a concrete limitation for evaluating local potentials.
- **Caveat:** These are preprint-level theoretical and simulation claims; the capture does not establish accuracy across other liquids or geometries.
- **Evidence:** [Captured source](https://arxiv.org/pdf/2610.04224); analysis based only on captured metadata, not independently verified full text.
