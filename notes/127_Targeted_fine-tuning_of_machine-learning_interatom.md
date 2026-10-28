---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: ML interatomic potentials
enrichment_tags: [fine-tuning, phonons, phase-transitions, regularization]
title: Targeted fine-tuning of machine-learning interatomic potentials for phonons
  and phase transitions
type: web
source: https://www.nature.com/articles/s41524-026-02338-w
canonical_url: https://nature.com/articles/s41524-026-02338-w
captured_by: sandipde
date: '2026-10-11'
captured_at: '2026-10-11T20:28:11+00:00'
last_requested: '2026-10-20T16:24:10+00:00'
issue: '127'
status: to-read
authors:
- Grandel, Jonas
- Benner, Philipp
- George, Janine
published: '2026-10-07'
abstract: Machine-learning interatomic potentials are widely used as computationally
  efficient surrogates for density functional theory in atomistic simulations, enabling
  large-scale and long-time modeling of materials systems. Here, we investigate how
  different fine-tuning strategies affect the prediction of harmonic phonon band structures,
  thermal and elastic properties, and the potential-energy surface along unstable
  phonon modes. We show that substantial improvements can be achieved with very limited
  additional data, with as few as 10 material-specific training structures. We investigate
  targeted L2-SP (L2-TSP) for this application, combining regularization toward the
  pre-trained model with selective fine-tuning of the first two representation-building
  layers, alongside transfer learning and multihead fine-tuning, with an additional
  comparison to low-rank LoRA for phonon prediction. Across 53 materials, L2-TSP achieves
  the most consistent overall performance, reducing phonon errors while also improving
  predictions of thermodynamic and elastic properties. Importantly, models with similar
  harmonic phonon accuracy can differ substantially in their prediction of dynamical
  instabilities and phase-transition behavior. Among the investigated approaches,
  L2-TSP shows the best overall agreement in dynamical-stability classification and
  in recovering the associated DFT reference phases, demonstrating improved generalization
  beyond the fine-tuning region. We implement L2-SP and L2-TSP in Equitrain, a model-agnostic
  software package for training and fine-tuning machine-learning interatomic potentials
  that can be applied beyond the MACE architecture considered here.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1038/s41524-026-02338-w
  journal: npj Computational Materials
  publisher: Springer Science and Business Media LLC
  volume: ''
  issue: ''
  page: ''
  type: journal-article
  subjects: []
  license:
  - start:
      date-parts:
      - - 2026
        - 10
        - 7
      date-time: '2026-10-07T00:00:00Z'
      timestamp: 1791331200000
    content-version: tdm
    delay-in-days: 0
    URL: https://creativecommons.org/licenses/by/4.0
  - start:
      date-parts:
      - - 2026
        - 10
        - 7
      date-time: '2026-10-07T00:00:00Z'
      timestamp: 1791331200000
    content-version: am
    delay-in-days: 0
    URL: https://creativecommons.org/licenses/by/4.0
  topics:
  - Machine Learning in Materials Science
  - Advanced Chemical Physics Studies
  - Model Reduction and Neural Networks
  open_access:
    is_oa: true
    oa_status: gold
    oa_url: https://www.nature.com/articles/s41524-026-02338-w_reference.pdf
    any_repository_has_fulltext: false
  cited_by_count: 0
---

# Targeted fine-tuning of machine-learning interatomic potentials for phonons and phase transitions

- **Type:** web
- **Source:** https://www.nature.com/articles/s41524-026-02338-w
- **Captured by:** @sandipde
- **Metadata:** complete (Crossref)
- **Authors:** Grandel, Jonas, Benner, Philipp, George, Janine
- **Published:** 2026-10-07

## Summary
Machine-learning interatomic potentials are widely used as computationally efficient surrogates for density functional theory in atomistic simulations, enabling large-scale and long-time modeling of materials systems. Here, we investigate how different fine-tuning strategies affect the prediction of harmonic phonon band structures, thermal and elastic properties, and the potential-energy surface along unstable phonon modes. We show that substantial improvements can be achieved with very limited additional data, with as few as 10 material-specific training structures. We investigate targeted L2-SP (L2-TSP) for this application, combining regularization toward the pre-trained model with selective fine-tuning of the first two representation-building layers, alongside transfer learning and multihead fine-tuning, with an additional comparison to low-rank LoRA for phonon prediction. Across 53 materials, L2-TSP achieves the most consistent overall performance, reducing phonon errors while also improving predictions of thermodynamic and elastic properties. Importantly, models with similar harmonic phonon accuracy can differ substantially in their prediction of dynamical instabilities and phase-transition behavior. Among the investigated approaches, L2-TSP shows the best overall agreement in dynamical-stability classification and in recovering the associated DFT reference phases, demonstrating improved generalization beyond the fine-tuning region. We implement L2-SP and L2-TSP in Equitrain, a model-agnostic software package for training and fine-tuning machine-learning interatomic potentials that can be applied beyond the MACE architecture considered here.

## Provider details
- **Doi:** 10.1038/s41524-026-02338-w
- **Journal:** npj Computational Materials
- **Publisher:** Springer Science and Business Media LLC
- **Type:** journal-article
- **License:** [{"start": {"date-parts": [[2026, 10, 7]], "date-time": "2026-10-07T00:00:00Z", "timestamp": 1791331200000}, "content-version": "tdm", "delay-in-days": 0, "URL": "https://creativecommons.org/licenses/by/4.0"}, {"start": {"date-parts": [[2026, 10, 7]], "date-time": "2026-10-07T00:00:00Z", "timestamp": 1791331200000}, "content-version": "am", "delay-in-days": 0, "URL": "https://creativecommons.org/licenses/by/4.0"}]
- **Topics:** ["Machine Learning in Materials Science", "Advanced Chemical Physics Studies", "Model Reduction and Neural Networks"]
- **Open Access:** {"is_oa": true, "oa_status": "gold", "oa_url": "https://www.nature.com/articles/s41524-026-02338-w_reference.pdf", "any_repository_has_fulltext": false}
- **Cited By Count:** 0

## AI enrichment
- **Concise summary:** The study compares MLIP adaptation strategies for phonons and related thermal and elastic properties across 53 materials. Its L2-TSP strategy combines regularization toward a pretrained model with selective early-layer fine-tuning, reporting improvements with as few as ten material-specific structures.
- **Why it matters:** The distinction between matching harmonic phonons and recovering unstable modes makes phase-transition behavior a useful stress test beyond a single phonon-error metric.
- **Caveat:** Reported advantages are unverified abstract-level results for the MACE architecture and selected materials; model-agnostic software does not establish architecture-independent performance.
- **Evidence:** [Captured source](https://www.nature.com/articles/s41524-026-02338-w); analysis based only on captured metadata, not independently verified full text.
