---
title: 'Machine Learning for Ionic Conductivity Prediction in Polymer Electrolytes:
  A Benchmark on Lithium Systems and a Feasibility Study on the Data-Scarce Multivalent
  (Mg, Zn, Na) Frontier'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010742/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15010742/v1
captured_by: auto-scanner
date: '2026-10-21'
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [polymer-electrolytes, ionic-conductivity, materials-ml]
captured_at: '2026-10-21T09:47:36+00:00'
last_requested: '2026-10-21T09:47:36+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Meghanadh Singh Yadav Dokku
published: '2026-10-21'
abstract: 'Solid and gel polymer electrolytes are central to safer, more flexible
  batteries, and machine learning has been used to predict their ionic conductivity
  directly from composition and processing variables. Almost all of this work targets
  lithium-ion systems, for which large, curated datasets exist. Polymer electrolytes
  conducting multivalent or non-lithium cations (magnesium, zinc, sodium) are promising
  lower-cost alternatives but remain comparably underexplored, in part because no
  public, ML-ready dataset of their measured ionic conductivities exists. Here we
  validate a standard composition-to-conductivity pipeline (Random Forest and XGBoost
  regression) on OBELiX, a published dataset of 599 lithium solid-state electrolytes,
  reaching R2 = 0.79 against a mean-predicting baseline near zero. We then construct,
  to our knowledge, the first ML-ready dataset of Mg-, Zn-, and Na-conducting polymer
  electrolytes, systematically mined from the primary and review literature: 135 data
  points across 105 distinct host-polymer/salt systems. Applying the same pipeline
  to this new dataset, a tuned Random Forest reaches R2 = 0.47 under leave-one-out
  cross-validation, or 0.36 under a more conservative 5-fold estimate, well below
  the lithium benchmark. Through chemistry-informed feature engineering and a nested
  cross-validation check, we show this gap is driven primarily by data scarcity and
  literature measurement heterogeneity, not by model or feature choice. We argue the
  scarcity is itself the central finding: it puts a number, for the first time, on
  how far behind the multivalent and non-lithium polymer electrolyte literature sits
  relative to the lithium-ion mainstream. We release the curated dataset and pipeline
  to support future community data collection.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010742/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Machine Learning for Ionic Conductivity Prediction in Polymer Electrolytes: A Benchmark on Lithium Systems and a Feasibility Study on the Data-Scarce Multivalent (Mg, Zn, Na) Frontier

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010742/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Meghanadh Singh Yadav Dokku
- **Published:** 2026-10-21

## Summary
Solid and gel polymer electrolytes are central to safer, more flexible batteries, and machine learning has been used to predict their ionic conductivity directly from composition and processing variables. Almost all of this work targets lithium-ion systems, for which large, curated datasets exist. Polymer electrolytes conducting multivalent or non-lithium cations (magnesium, zinc, sodium) are promising lower-cost alternatives but remain comparably underexplored, in part because no public, ML-ready dataset of their measured ionic conductivities exists. Here we validate a standard composition-to-conductivity pipeline (Random Forest and XGBoost regression) on OBELiX, a published dataset of 599 lithium solid-state electrolytes, reaching R2 = 0.79 against a mean-predicting baseline near zero. We then construct, to our knowledge, the first ML-ready dataset of Mg-, Zn-, and Na-conducting polymer electrolytes, systematically mined from the primary and review literature: 135 data points across 105 distinct host-polymer/salt systems. Applying the same pipeline to this new dataset, a tuned Random Forest reaches R2 = 0.47 under leave-one-out cross-validation, or 0.36 under a more conservative 5-fold estimate, well below the lithium benchmark. Through chemistry-informed feature engineering and a nested cross-validation check, we show this gap is driven primarily by data scarcity and literature measurement heterogeneity, not by model or feature choice. We argue the scarcity is itself the central finding: it puts a number, for the first time, on how far behind the multivalent and non-lithium polymer electrolyte literature sits relative to the lithium-ion mainstream. We release the curated dataset and pipeline to support future community data collection.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010742/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment
- **Concise summary:** The preprint benchmarks machine-learning prediction of ionic conductivity in lithium polymer electrolytes and explores data-scarce multivalent and sodium systems.
- **Why it matters:** It addresses how far composition- and processing-based prediction may extend beyond better-studied lithium materials.
- **Caveat:** This is a ChemRxiv preprint; the abstract does not establish model reliability outside the reported data.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15010742/v1); analysis based only on captured metadata, not independently verified full text.
