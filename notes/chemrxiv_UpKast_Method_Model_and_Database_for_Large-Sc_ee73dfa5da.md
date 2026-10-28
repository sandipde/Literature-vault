---
title: 'UpKast: Method, Model, and Database for Large-Scale Cross-Solvent Determination
  of pKa Values'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010254/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15010254/v1
captured_by: auto-scanner
date: '2026-10-12'
captured_at: '2026-10-12T12:41:12+00:00'
last_requested: '2026-10-12T12:41:12+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Jonathan Wenyuan Zheng
- William H. Green
published: '2026-10-12'
abstract: 'The acid dissociation constant, commonly written as p K a , plays a key
  role in chemistry. However, most p K a measurements have been conducted in only
  a handful of solvents, resulting in data scarcity for many relevant solvent systems.
  Herein, we introduce the UpKast-DB, which comprises of p K a estimates for around
  3,000 acids and bases in 29 solvents. We constructed UpKast-DB using a quantum-chemical
  method that integrates solvation free energy calculations with experimental data.
  Furthermore, we trained a surrogate machine learning model UpKast-ML on the computed
  values, allowing for rapid and accurate prediction of p K a values beyond the acids
  and bases presented in UpKast-DB. The quantum-chemical and machine learning methods
  result in RMSEs of approximately 1 p K a unit relative to experimental values, slightly
  higher than the typical aleatoric uncertainty of underlying experimental data, but
  more accurate than many existing experimental measurements (which can have uncertainties
  up to, and sometimes beyond, 3 p K a units). The data and modeling approaches provide
  a means of productively augmenting existing p K a data sources, and represent a
  significant step toward general determination of p K a in any solvent. The dataset
  and models can be found on Zenodo: doi:10.5281/zenodo.23239570'
metadata_provider: Crossref
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [pka-prediction, solvent-effects, surrogate-models]
provider_data:
  doi: 10.26434/chemrxiv.15010254/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# UpKast: Method, Model, and Database for Large-Scale Cross-Solvent Determination of pKa Values

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010254/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Jonathan Wenyuan Zheng, William H. Green
- **Published:** 2026-10-12

## Summary
The acid dissociation constant, commonly written as p K a , plays a key role in chemistry. However, most p K a measurements have been conducted in only a handful of solvents, resulting in data scarcity for many relevant solvent systems. Herein, we introduce the UpKast-DB, which comprises of p K a estimates for around 3,000 acids and bases in 29 solvents. We constructed UpKast-DB using a quantum-chemical method that integrates solvation free energy calculations with experimental data. Furthermore, we trained a surrogate machine learning model UpKast-ML on the computed values, allowing for rapid and accurate prediction of p K a values beyond the acids and bases presented in UpKast-DB. The quantum-chemical and machine learning methods result in RMSEs of approximately 1 p K a unit relative to experimental values, slightly higher than the typical aleatoric uncertainty of underlying experimental data, but more accurate than many existing experimental measurements (which can have uncertainties up to, and sometimes beyond, 3 p K a units). The data and modeling approaches provide a means of productively augmenting existing p K a data sources, and represent a significant step toward general determination of p K a in any solvent. The dataset and models can be found on Zenodo: doi:10.5281/zenodo.23239570

## Provider details
- **Doi:** 10.26434/chemrxiv.15010254/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment

- **Concise summary:** UpKast combines solvation-free-energy calculations with experimental data to estimate pKa for about 3,000 acids and bases in 29 solvents. A surrogate learns these computed values for faster prediction.
- **Why it matters:** Expanding solvent coverage addresses a practical limitation of acidity databases concentrated in a few common media.
- **Caveat:** Computed estimates are not new measurements; surrogate errors inherit reference-method uncertainty, and broad any-solvent applicability remains an aspiration in the captured preprint.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15010254/v1); analysis based only on captured metadata, not independently verified full text.
