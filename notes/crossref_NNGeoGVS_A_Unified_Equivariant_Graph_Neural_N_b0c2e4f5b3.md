---
title: 'NNGeoGVS: A Unified Equivariant Graph Neural Network Framework for Integrated
  Structure and Ligand-based Virtual Screening'
type: paper
source: https://doi.org/10.2174/0115734099527526261007151436
canonical_url: https://doi.org/10.2174/0115734099527526261007151436
captured_by: auto-scanner
date: '2026-10-14'
captured_at: '2026-10-14T20:24:05+00:00'
last_requested: '2026-10-14T20:24:05+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Suresh Chand Yadam
- Phani Kumar Singamsetty
published: '2026-10-09'
abstract: 'Introduction: Virtual screening (VS) is a widely used computational strategy
  in early- stage drug discovery for identifying bioactive compounds from large chemical
  libraries. Although structure-based and ligand-based approaches have demonstrated
  success individually, their integration into a unified deep learning framework remains
  limited. This study presents NNGeoGVS (Neural Network Geometric Graph-based Virtual
  Screening), an Equivariant Graph Neural Network (EGNN)-based framework that integrates
  ligand molecular topology and protein active-site geometry for activity prediction.
  Methods: NNGeoGVS represents ligands and protein binding sites as molecular graphs
  and learns structure–activity relationships through end-to-end message passing using
  PyTorch Geometric. The framework combines node-level atomic features, edge-level
  bond descriptors, and global geometric and pharmacophore descriptors. Active-site
  geometry is characterized using Ultra-Fast Shape Recognition (USR) and convex hull
  algorithms. These features are integrated through a multi-branch GNN architecture
  with late fusion, while focal loss optimization and graph-level augmentation address
  class imbalance. Results: NNGeoGVS was evaluated on the DUD-E dataset (8 kinase
  targets) and the LITPCBA benchmark (15 targets). Compared with NNGeoAS and other
  GNN-based methods, it achieved average EF1% values of 35.92 and 17.03 and ROC-AUC
  scores of 0.98 and 0.77 on DUD-E and LIT-PCBA, respectively. Discussion: The integration
  of ligand topology with protein active-site geometry improves enrichment and classification
  performance, demonstrating the effectiveness of combining complementary structural
  information within a unified EGNN framework. Conclusion: We proposed NNGeoGVS, a
  robust framework for virtual screening that integrates structural information of
  both proteins and ligands and demonstrated robust predictive performance on benchmark
  datasets.'
metadata_provider: Crossref
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [virtual-screening, equivariant-graphs, protein-ligand-features]
provider_data:
  doi: 10.2174/0115734099527526261007151436
  journal: Current Computer-Aided Drug Design
  publisher: Bentham Science Publishers Ltd.
  type: journal-article
  subjects: []
---

# NNGeoGVS: A Unified Equivariant Graph Neural Network Framework for Integrated Structure and Ligand-based Virtual Screening

- **Type:** paper
- **Source:** https://doi.org/10.2174/0115734099527526261007151436
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Suresh Chand Yadam, Phani Kumar Singamsetty
- **Published:** 2026-10-09

## Summary
Introduction: Virtual screening (VS) is a widely used computational strategy in early- stage drug discovery for identifying bioactive compounds from large chemical libraries. Although structure-based and ligand-based approaches have demonstrated success individually, their integration into a unified deep learning framework remains limited. This study presents NNGeoGVS (Neural Network Geometric Graph-based Virtual Screening), an Equivariant Graph Neural Network (EGNN)-based framework that integrates ligand molecular topology and protein active-site geometry for activity prediction. Methods: NNGeoGVS represents ligands and protein binding sites as molecular graphs and learns structure–activity relationships through end-to-end message passing using PyTorch Geometric. The framework combines node-level atomic features, edge-level bond descriptors, and global geometric and pharmacophore descriptors. Active-site geometry is characterized using Ultra-Fast Shape Recognition (USR) and convex hull algorithms. These features are integrated through a multi-branch GNN architecture with late fusion, while focal loss optimization and graph-level augmentation address class imbalance. Results: NNGeoGVS was evaluated on the DUD-E dataset (8 kinase targets) and the LITPCBA benchmark (15 targets). Compared with NNGeoAS and other GNN-based methods, it achieved average EF1% values of 35.92 and 17.03 and ROC-AUC scores of 0.98 and 0.77 on DUD-E and LIT-PCBA, respectively. Discussion: The integration of ligand topology with protein active-site geometry improves enrichment and classification performance, demonstrating the effectiveness of combining complementary structural information within a unified EGNN framework. Conclusion: We proposed NNGeoGVS, a robust framework for virtual screening that integrates structural information of both proteins and ligands and demonstrated robust predictive performance on benchmark datasets.

## Provider details
- **Doi:** 10.2174/0115734099527526261007151436
- **Journal:** Current Computer-Aided Drug Design
- **Publisher:** Bentham Science Publishers Ltd.
- **Type:** journal-article

## AI enrichment

- **Concise summary:** NNGeoGVS combines ligand topology and protein-site geometry through a multi-branch equivariant graph framework with late fusion. The abstract reports enrichment and classification results on DUD-E and LIT-PCBA.
- **Why it matters:** Combining complementary ligand and site representations targets a practical gap between ligand-only and structure-based screening.
- **Caveat:** The large difference between reported benchmark ROC-AUC values cautions against universal performance claims; activity prediction is not experimental hit confirmation.
- **Evidence:** [Captured source](https://doi.org/10.2174/0115734099527526261007151436); analysis based only on captured metadata, not independently verified full text.
