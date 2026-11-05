---
title: Integrating classical similarity and multitask neural representations
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011713/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011713/v1
captured_by: auto-scanner
date: '2026-11-05'
captured_at: '2026-11-05T12:53:59+00:00'
last_requested: '2026-11-05T12:53:59+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Juan Jesus Padrón Melián
published: '2026-11-05'
abstract: Background. Computational prediction of compound–target associations can
  help prioritize hypotheses for experimental investigation. While deep learning architectures
  are increasingly proposed, their apparent superiority often relies on comparisons
  against untuned classical baselines or evaluation protocols prone to data leakage.
  Objective. We present a scaffold-disjoint evaluation benchmark derived from ChEMBL
  37 to evaluate multitask neural representations against tuned classical similarity
  search, and we investigate whether combining both paradigms yields improved ranking
  performance. Methods. The benchmark comprised 100,000 compounds, 1,979 human single-protein
  targets, and 139,789 positive associations, partitioned by Bemis–Murcko scaffold
  into train (70%), validation (10%), and test (20%) sets. All hyperparameters were
  selected on the validation set. We compared a multitask MLP with a tuned K-Nearest
  Neighbors (KNN-20) baseline, as well as a hybrid model integrating both representations.
  Results. On the held-out test set, the tuned KNN-20 achieved a Hits@10 of 0.9335,
  statistically indistinguishable from the 10-seed multitask MLP ensemble (0.9355;
  Δ = +0.0021, 95% CI [−0.0012,+0.0052]). However, a hybrid model integrating both
  representations (40% KNN, 60% MLP) achieved a significantly higher Hits@10 of 0.9426,
  outperforming both KNN-20 (Δ = +0.0091, 95% CI [+0.0066,+0.0116]) and the MLP alone
  (Δ = +0.0070, 95% CI [+0.0052,+0.0089]). Conclusions. Our results demonstrate that
  while complex neural models do not inherently outperform well-tuned classical baselines,
  they capture complementary information. A hybrid approach combining classical chemical
  similarity and multitask neural representations yields a modest but statistically
  significant improvement in ranking performance within this benchmark. This study
  emphasizes the necessity of rigorous baseline tuning and suggests hybrid architectures
  as a promising direction for compound–target prediction.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011713/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Integrating classical similarity and multitask neural representations

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011713/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Juan Jesus Padrón Melián
- **Published:** 2026-11-05

## Summary
Background. Computational prediction of compound–target associations can help prioritize hypotheses for experimental investigation. While deep learning architectures are increasingly proposed, their apparent superiority often relies on comparisons against untuned classical baselines or evaluation protocols prone to data leakage. Objective. We present a scaffold-disjoint evaluation benchmark derived from ChEMBL 37 to evaluate multitask neural representations against tuned classical similarity search, and we investigate whether combining both paradigms yields improved ranking performance. Methods. The benchmark comprised 100,000 compounds, 1,979 human single-protein targets, and 139,789 positive associations, partitioned by Bemis–Murcko scaffold into train (70%), validation (10%), and test (20%) sets. All hyperparameters were selected on the validation set. We compared a multitask MLP with a tuned K-Nearest Neighbors (KNN-20) baseline, as well as a hybrid model integrating both representations. Results. On the held-out test set, the tuned KNN-20 achieved a Hits@10 of 0.9335, statistically indistinguishable from the 10-seed multitask MLP ensemble (0.9355; Δ = +0.0021, 95% CI [−0.0012,+0.0052]). However, a hybrid model integrating both representations (40% KNN, 60% MLP) achieved a significantly higher Hits@10 of 0.9426, outperforming both KNN-20 (Δ = +0.0091, 95% CI [+0.0066,+0.0116]) and the MLP alone (Δ = +0.0070, 95% CI [+0.0052,+0.0089]). Conclusions. Our results demonstrate that while complex neural models do not inherently outperform well-tuned classical baselines, they capture complementary information. A hybrid approach combining classical chemical similarity and multitask neural representations yields a modest but statistically significant improvement in ranking performance within this benchmark. This study emphasizes the necessity of rigorous baseline tuning and suggests hybrid architectures as a promising direction for compound–target prediction.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011713/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
