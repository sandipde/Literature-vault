---
title: Machine-learned syndrome post-selection for reliable quantum error correction
type: paper
source: https://doi.org/10.1088/2632-2153/aec2a3
canonical_url: https://doi.org/10.1088/2632-2153/aec2a3
captured_by: auto-scanner
date: '2026-11-17'
captured_at: '2026-11-17T00:38:12+00:00'
last_requested: '2026-11-17T00:38:12+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Tobias Haug
- Askery Canabarro
- Leandro Aolita
published: '2026-11-16'
abstract: "Abstract Quantum error correction can be enhanced\rby post-selecting out\r\
  runs that are likely to produce a logical failure, but the most accurate measures\
  \ for that \rrequire costly decoder-level information. We introduce a practical,\
  \ decoder-agnostic post-selection method that learns directly from syndrome data.\
  \ The method trains a supervised classifier to distinguish between syndromes from\
  \ low- and high-noise regimes, and then uses the classifier's output as an abort\
  \ score for new runs, without requiring logical-error labels, correction operators,\
  \ or code-specific likelihood calculations. We validate\rthe approach in three complementary\
  \ settings: circuit-level simulations of the Gross bivariate-bicycle code, code-capacity\
  \ simulations of the surface code, and experimental logical magic-state distillation\
  \ data from the QuEra neutral-atom processor [Nature 645 (2025)]. In the Gross and\
  \ surface codes, learned syndrome post-selection reduces the conditional logical\
  \ error rate at a fixed acceptance rate, with performance comparable to syndrome-weight\
  \ filtering. For the surface code, the learned classifier reveals a post-selection\
  \ transition distinct from the conventional decoding threshold. In the experimental\
  \ data, the machine-learning score outperforms syndrome-weight post-selection and,\
  \ when combined with logical-gap filtering, improves the output fidelity beyond\
  \ using the logical gap alone. These results show that syndrome-only learning provides\
  \ a scalable and hardware-compatible route to improving the reliability of quantum\
  \ error correction."
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1088/2632-2153/aec2a3
  journal: 'Machine Learning: Science and Technology'
  publisher: IOP Publishing
  type: journal-article
  subjects: []
---

# Machine-learned syndrome post-selection for reliable quantum error correction

- **Type:** paper
- **Source:** https://doi.org/10.1088/2632-2153/aec2a3
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Tobias Haug, Askery Canabarro, Leandro Aolita
- **Published:** 2026-11-16

## Summary
Abstract Quantum error correction can be enhancedby post-selecting outruns that are likely to produce a logical failure, but the most accurate measures for that require costly decoder-level information. We introduce a practical, decoder-agnostic post-selection method that learns directly from syndrome data. The method trains a supervised classifier to distinguish between syndromes from low- and high-noise regimes, and then uses the classifier's output as an abort score for new runs, without requiring logical-error labels, correction operators, or code-specific likelihood calculations. We validatethe approach in three complementary settings: circuit-level simulations of the Gross bivariate-bicycle code, code-capacity simulations of the surface code, and experimental logical magic-state distillation data from the QuEra neutral-atom processor [Nature 645 (2025)]. In the Gross and surface codes, learned syndrome post-selection reduces the conditional logical error rate at a fixed acceptance rate, with performance comparable to syndrome-weight filtering. For the surface code, the learned classifier reveals a post-selection transition distinct from the conventional decoding threshold. In the experimental data, the machine-learning score outperforms syndrome-weight post-selection and, when combined with logical-gap filtering, improves the output fidelity beyond using the logical gap alone. These results show that syndrome-only learning provides a scalable and hardware-compatible route to improving the reliability of quantum error correction.

## Provider details
- **Doi:** 10.1088/2632-2153/aec2a3
- **Journal:** Machine Learning: Science and Technology
- **Publisher:** IOP Publishing
- **Type:** journal-article
