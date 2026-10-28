---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Mathematics and algorithms
enrichment_tags: [label-efficiency, active-learning, pseudo-labeling, image-classification]
title: 'Label-Efficient Learning for Ground-Based Sky-Image Classification: A Benchmark
  of Transfer Learning, Active Learning, and Pseudo-Labeling on GCD'
type: paper
source: https://doi.org/10.21203/rs.3.rs-11133214/v1
canonical_url: https://doi.org/10.21203/rs.3.rs-11133214/v1
captured_by: auto-scanner
date: '2026-10-16'
captured_at: '2026-10-16T09:27:31+00:00'
last_requested: '2026-10-16T09:27:31+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Esther Bou Dagher
- Viktoriya Bu-Dager
- Boguslaw Zegarlinski
published: '2026-10-16'
abstract: 'Abstract Accurate ground-based cloud classification is important for atmospheric
  monitoring, solar-energy forecasting, aviation weather assessment, and climate observation
  systems. However, reliable sky-image annotation is time-consuming, especially when
  cloud types are visually similar or mixed. In this work, we study the label efficiency
  of deep learning for ground-based cloud classification using the Ground-based Cloud
  Dataset (GCD). Rather than proposing a new architecture, we benchmark three practical
  learning strategies under limited annotation budgets: supervised transfer learning,
  uncertainty-based active learning, and high-confidence pseudo-labeling. An ImageNet-pretrained
  ResNet50 is used as a common frozen backbone, and experiments are repeated over
  five random seeds for label budgets ranging from \((1%)\) to \((100%)\) of the training
  labels. Supervised transfer learning is already highly label-efficient: test accuracy
  increases from \((0.635 \pm 0.018)\) with \((1%)\) labels to \((0.730 \pm 0.002)\)
  with \((40%)\) labels, approaching the full-label performance of \((0.735 \pm 0.003)\).
  Active learning and pseudo-labeling are competitive with supervised sampling and
  provide small improvements for some metrics and budgets, but neither produces a
  large or consistent aggregate gain. Diagnostic analyses show that accepted pseudo-labels
  are highly reliable, with accuracy ranging from \((0.946)\) to \((0.977)\), but
  are biased toward easier, high-confidence sky-type groups. In contrast, uncertainty
  sampling preferentially queries uncertain samples from visually challenging groups,
  including Mixed and the visually confusable Stratocumulus and Cumulonimbus groups,
  but these targeted acquisitions yield only modest performance improvements. Overall,
  these results show that transfer learning can substantially reduce annotation requirements
  for GCD, while simple active and semi-supervised strategies provide limited additional
  gains over a strong supervised baseline.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.21203/rs.3.rs-11133214/v1
  journal: ''
  publisher: Springer Science and Business Media LLC
  type: posted-content
  subjects: []
---

# Label-Efficient Learning for Ground-Based Sky-Image Classification: A Benchmark of Transfer Learning, Active Learning, and Pseudo-Labeling on GCD

- **Type:** paper
- **Source:** https://doi.org/10.21203/rs.3.rs-11133214/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Esther Bou Dagher, Viktoriya Bu-Dager, Boguslaw Zegarlinski
- **Published:** 2026-10-16

## Summary
Abstract Accurate ground-based cloud classification is important for atmospheric monitoring, solar-energy forecasting, aviation weather assessment, and climate observation systems. However, reliable sky-image annotation is time-consuming, especially when cloud types are visually similar or mixed. In this work, we study the label efficiency of deep learning for ground-based cloud classification using the Ground-based Cloud Dataset (GCD). Rather than proposing a new architecture, we benchmark three practical learning strategies under limited annotation budgets: supervised transfer learning, uncertainty-based active learning, and high-confidence pseudo-labeling. An ImageNet-pretrained ResNet50 is used as a common frozen backbone, and experiments are repeated over five random seeds for label budgets ranging from \((1%)\) to \((100%)\) of the training labels. Supervised transfer learning is already highly label-efficient: test accuracy increases from \((0.635 \pm 0.018)\) with \((1%)\) labels to \((0.730 \pm 0.002)\) with \((40%)\) labels, approaching the full-label performance of \((0.735 \pm 0.003)\). Active learning and pseudo-labeling are competitive with supervised sampling and provide small improvements for some metrics and budgets, but neither produces a large or consistent aggregate gain. Diagnostic analyses show that accepted pseudo-labels are highly reliable, with accuracy ranging from \((0.946)\) to \((0.977)\), but are biased toward easier, high-confidence sky-type groups. In contrast, uncertainty sampling preferentially queries uncertain samples from visually challenging groups, including Mixed and the visually confusable Stratocumulus and Cumulonimbus groups, but these targeted acquisitions yield only modest performance improvements. Overall, these results show that transfer learning can substantially reduce annotation requirements for GCD, while simple active and semi-supervised strategies provide limited additional gains over a strong supervised baseline.

## Provider details
- **Doi:** 10.21203/rs.3.rs-11133214/v1
- **Publisher:** Springer Science and Business Media LLC
- **Type:** posted-content

## AI enrichment
- **Concise summary:** A frozen pretrained ResNet50 benchmarks supervised sampling, uncertainty-based active learning, and pseudo-labeling on ground-based cloud images over five seeds and multiple label budgets. Transfer learning is strong, with only modest or inconsistent additional gains from the other strategies.
- **Why it matters:** A strong pretrained baseline can explain much of apparent label efficiency, so acquisition complexity needs a demonstrated marginal benefit.
- **Caveat:** The preprint's findings are unverified and tied to GCD and a frozen backbone; reliable pseudo-labels are biased toward easy groups and need not improve difficult-class coverage.
- **Evidence:** [Captured source](https://doi.org/10.21203/rs.3.rs-11133214/v1); analysis based only on captured metadata, not independently verified full text.
