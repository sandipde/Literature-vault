---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [aromaticity, cellular-sheaves, molecular-topology, spectral-descriptors]
title: A Cellular Sheaf Model for Aromaticity in Discrete Molecular Systems
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010344/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15010344/v1
captured_by: auto-scanner
date: '2026-10-13'
captured_at: '2026-10-13T12:25:46+00:00'
last_requested: '2026-10-13T12:25:46+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Roy Han
published: '2026-10-13'
abstract: Aromaticity underpins molecular stability in fields ranging from pharmaceuticals
  to organic semiconductors, yet existing prediction methods are either too computationally
  costly for large-scale screening or too empirically restricted for broad applicability.
  This work introduces the molecular sheaf, a cellular sheaf model free of empirical
  parameters for chemical bonding that generalizes standard molecular graph theory.
  From this the frontier eigengap Δ_F is derived as a spectral approximation of the
  HOMO-LUMO gap requiring only molecular topology and electron count. Δ_F correctly
  classifies the aromaticity and antiaromaticity of the full annulene series, including
  benzene and cyclobutadiene, exactly recovering Hückel theory for regular hydrocarbon
  systems. At scale, it accounts for 62.5% of the variance in DFT HOMO-LUMO gaps across
  17,523 structurally diverse polycyclic aromatic hydrocarbons and 21.7% across 52,000
  heteroaromatic systems, with the reduction reflecting the deliberate cost of parameter
  freedom. This confirms that aromatic character can be approximated from molecular
  connectivity and electron count alone, suggesting that cellular sheaves offer a
  largely unexplored mathematical framework for the modeling of chemical bonding and
  structure. All calculations run at under 1 ms per molecule, over seven orders of
  magnitude faster than corresponding DFT calculations. The molecular sheaf thus also
  enables rapid, parameter-free pre-screening of aromatic character from structural
  data alone.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010344/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# A Cellular Sheaf Model for Aromaticity in Discrete Molecular Systems

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010344/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Roy Han
- **Published:** 2026-10-13

## Summary
Aromaticity underpins molecular stability in fields ranging from pharmaceuticals to organic semiconductors, yet existing prediction methods are either too computationally costly for large-scale screening or too empirically restricted for broad applicability. This work introduces the molecular sheaf, a cellular sheaf model free of empirical parameters for chemical bonding that generalizes standard molecular graph theory. From this the frontier eigengap Δ_F is derived as a spectral approximation of the HOMO-LUMO gap requiring only molecular topology and electron count. Δ_F correctly classifies the aromaticity and antiaromaticity of the full annulene series, including benzene and cyclobutadiene, exactly recovering Hückel theory for regular hydrocarbon systems. At scale, it accounts for 62.5% of the variance in DFT HOMO-LUMO gaps across 17,523 structurally diverse polycyclic aromatic hydrocarbons and 21.7% across 52,000 heteroaromatic systems, with the reduction reflecting the deliberate cost of parameter freedom. This confirms that aromatic character can be approximated from molecular connectivity and electron count alone, suggesting that cellular sheaves offer a largely unexplored mathematical framework for the modeling of chemical bonding and structure. All calculations run at under 1 ms per molecule, over seven orders of magnitude faster than corresponding DFT calculations. The molecular sheaf thus also enables rapid, parameter-free pre-screening of aromatic character from structural data alone.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010344/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment
- **Concise summary:** A parameter-free cellular-sheaf representation derives a frontier eigengap from connectivity and electron count as a proxy for molecular electronic gaps and aromatic character. The abstract reports stronger explained variance for hydrocarbon than heteroaromatic datasets.
- **Why it matters:** A topology-only screening descriptor could cheaply prioritize molecules before electronic-structure calculations while exposing how much chemistry connectivity alone captures.
- **Caveat:** The ChemRxiv v1 results and runtime comparison are unverified; the reported 21.7% variance for heteroaromatics limits any claim of a general HOMO-LUMO predictor.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15010344/v1); analysis based only on captured metadata, not independently verified full text.
