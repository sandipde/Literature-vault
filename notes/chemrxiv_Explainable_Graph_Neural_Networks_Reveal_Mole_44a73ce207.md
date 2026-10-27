---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [graph-neural-networks, molecular-attribution, taste-prediction]
title: Explainable Graph Neural Networks Reveal Molecular Features Associated with
  Umami Taste
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010977/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15010977/v1
captured_by: auto-scanner
date: '2026-10-24'
captured_at: '2026-10-24T09:15:55+00:00'
last_requested: '2026-10-24T09:15:55+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Hiroaki Iwata
published: '2026-10-23'
abstract: Umami is one of the five basic tastes, and understanding the relationship
  between molecular structure and umami perception is important for food science.
  Although machine learning models have been developed to predict umami taste, the
  molecular features underlying their predictions remain insufficiently understood.
  In this study, we developed a graph neural network (GNN) model for umami taste prediction
  and investigated the structural features contributing to its predictions using Integrated
  Gradients (IG). Three datasets were constructed from ChemTastesDB, comprising 74
  umami compounds and different sets of non-umami compounds. Under five-fold Murcko
  scaffold-disjoint cross-validation, the model achieved mean receiver operating characteristic
  areas under the curve of 0.935, 0.950, and 0.910 for the strict, full primary, and
  physicochemically matched datasets, respectively. Atom-level IG analysis revealed
  that functional-group prevalence did not necessarily correspond to positive attribution
  toward umami prediction. Notably, carboxylic acids occurred at similar frequencies
  in umami and non-umami compounds but showed significantly greater positive attribution
  in umami compounds. Furthermore, analysis of 31 structurally similar umami–nonumami
  molecular pairs demonstrated that regions specific to umami compounds generally
  received greater positive attribution than the corresponding regions in non-umami
  compounds. These findings suggest that the GNN captures molecular features associated
  with umami taste in a manner that depends on their surrounding structural context.
  Combining scaffold-disjoint prediction with atom-level attribution analysis provides
  an approach for investigating structure–taste relationships and identifying molecular
  features potentially relevant to umami perception.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010977/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Explainable Graph Neural Networks Reveal Molecular Features Associated with Umami Taste

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010977/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Hiroaki Iwata
- **Published:** 2026-10-23

## Summary
Umami is one of the five basic tastes, and understanding the relationship between molecular structure and umami perception is important for food science. Although machine learning models have been developed to predict umami taste, the molecular features underlying their predictions remain insufficiently understood. In this study, we developed a graph neural network (GNN) model for umami taste prediction and investigated the structural features contributing to its predictions using Integrated Gradients (IG). Three datasets were constructed from ChemTastesDB, comprising 74 umami compounds and different sets of non-umami compounds. Under five-fold Murcko scaffold-disjoint cross-validation, the model achieved mean receiver operating characteristic areas under the curve of 0.935, 0.950, and 0.910 for the strict, full primary, and physicochemically matched datasets, respectively. Atom-level IG analysis revealed that functional-group prevalence did not necessarily correspond to positive attribution toward umami prediction. Notably, carboxylic acids occurred at similar frequencies in umami and non-umami compounds but showed significantly greater positive attribution in umami compounds. Furthermore, analysis of 31 structurally similar umami–nonumami molecular pairs demonstrated that regions specific to umami compounds generally received greater positive attribution than the corresponding regions in non-umami compounds. These findings suggest that the GNN captures molecular features associated with umami taste in a manner that depends on their surrounding structural context. Combining scaffold-disjoint prediction with atom-level attribution analysis provides an approach for investigating structure–taste relationships and identifying molecular features potentially relevant to umami perception.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010977/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment

- **Concise summary:** A molecular graph model combines scaffold-disjoint umami prediction with atom-level attribution. The abstract suggests that a functional group's molecular surroundings matter more than its presence alone.
- **Why it matters:** Context-sensitive explanations could help distinguish useful structure-property hypotheses from simple functional-group counting.
- **Caveat:** ChemRxiv v1 preprint with only 74 positive compounds in the captured description; attribution is not evidence of a causal taste mechanism. This is molecular-property modeling, not an interatomic potential.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15010977/v1); analysis based only on captured metadata, not independently verified full text.
