---
title: 'ZENN: A thermodynamics-inspired computational framework for heterogeneous
  data–driven modeling'
type: paper
source: https://www.pnas.org/doi/10.1073/pnas.2511227122
canonical_url: https://doi.org/10.1073/pnas.2511227122
captured_by: sandipde
date: '2026-10-16'
captured_at: '2026-10-16T07:02:43+00:00'
last_requested: '2026-10-16T07:02:43+00:00'
issue: '151'
status: to-read
authors:
- Shun Wang
- Shun-Li Shang
- Zi-Kui Liu
- Wenrui Hao
published: '2026-01-06'
abstract: Traditional entropy-based methods—such as cross-entropy loss in classification
  problems—have long been essential tools for representing the information uncertainty
  and physical disorder in data and for developing artificial intelligence algorithms.
  However, the rapid growth of data across various domains has introduced new challenges,
  particularly the integration of heterogeneous datasets with intrinsic disparities.
  To address this, we introduce a zentropy-enhanced neural network (ZENN), extending
  zentropy theory into the data science domain via intrinsic entropy, enabling more
  effective learning from heterogeneous data sources. ZENN simultaneously learns both
  energy and intrinsic entropy components, capturing the underlying structure of multisource
  data. To support this, we redesign the neural network architecture to better reflect
  the intrinsic properties and variability inherent in diverse datasets. We demonstrate
  the effectiveness of ZENN on classification tasks and energy landscape reconstructions,
  showing its superior generalization capabilities and robustness-particularly in
  predicting high-order derivatives. In image and text classification tasks, ZENN
  demonstrates superior generalization by introducing a learnable temperature variable
  that models latent multisource heterogeneity, allowing it to surpass state-of-the-art
  models on CIFAR-10/100, BBC News, and AG News. As a practical application in materials
  science, we employ ZENN to reconstruct the Helmholtz energy landscape of Fe 3 Pt
  using data generated from density functional theory and capture key material behaviors,
  including negative thermal expansion and the critical point in the temperature–pressure
  space. Overall, this work presents a zentropy-grounded framework for data-driven
  machine learning, positioning ZENN as a versatile and robust approach for scientific
  problems involving complex, heterogeneous datasets.
metadata_provider: Crossref
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Mathematics and algorithms
enrichment_tags: [heterogeneous-data, zentropy, energy-landscapes]
provider_data:
  doi: 10.1073/pnas.2511227122
  journal: Proceedings of the National Academy of Sciences
  publisher: National Academy of Sciences
  volume: '123'
  issue: '1'
  page: ''
  type: journal-article
  subjects: []
  license:
  - start:
      date-parts:
      - - 2026
        - 1
        - 2
      date-time: '2026-01-02T00:00:00Z'
      timestamp: 1767312000000
    content-version: vor
    delay-in-days: 0
    URL: https://creativecommons.org/licenses/by-nc-nd/4.0/
---

# ZENN: A thermodynamics-inspired computational framework for heterogeneous data–driven modeling

- **Type:** paper
- **Source:** https://www.pnas.org/doi/10.1073/pnas.2511227122
- **Captured by:** @sandipde
- **Metadata:** complete (Crossref)
- **Authors:** Shun Wang, Shun-Li Shang, Zi-Kui Liu, Wenrui Hao
- **Published:** 2026-01-06

## Summary
Traditional entropy-based methods—such as cross-entropy loss in classification problems—have long been essential tools for representing the information uncertainty and physical disorder in data and for developing artificial intelligence algorithms. However, the rapid growth of data across various domains has introduced new challenges, particularly the integration of heterogeneous datasets with intrinsic disparities. To address this, we introduce a zentropy-enhanced neural network (ZENN), extending zentropy theory into the data science domain via intrinsic entropy, enabling more effective learning from heterogeneous data sources. ZENN simultaneously learns both energy and intrinsic entropy components, capturing the underlying structure of multisource data. To support this, we redesign the neural network architecture to better reflect the intrinsic properties and variability inherent in diverse datasets. We demonstrate the effectiveness of ZENN on classification tasks and energy landscape reconstructions, showing its superior generalization capabilities and robustness-particularly in predicting high-order derivatives. In image and text classification tasks, ZENN demonstrates superior generalization by introducing a learnable temperature variable that models latent multisource heterogeneity, allowing it to surpass state-of-the-art models on CIFAR-10/100, BBC News, and AG News. As a practical application in materials science, we employ ZENN to reconstruct the Helmholtz energy landscape of Fe 3 Pt using data generated from density functional theory and capture key material behaviors, including negative thermal expansion and the critical point in the temperature–pressure space. Overall, this work presents a zentropy-grounded framework for data-driven machine learning, positioning ZENN as a versatile and robust approach for scientific problems involving complex, heterogeneous datasets.

## Provider details
- **Doi:** 10.1073/pnas.2511227122
- **Journal:** Proceedings of the National Academy of Sciences
- **Publisher:** National Academy of Sciences
- **Volume:** 123
- **Issue:** 1
- **Type:** journal-article
- **License:** [{"start": {"date-parts": [[2026, 1, 2]], "date-time": "2026-01-02T00:00:00Z", "timestamp": 1767312000000}, "content-version": "vor", "delay-in-days": 0, "URL": "https://creativecommons.org/licenses/by-nc-nd/4.0/"}]

## AI enrichment

- **Concise summary:** ZENN learns energy and intrinsic-entropy components to represent heterogeneous datasets using a zentropy-inspired neural architecture. The abstract connects classification experiments to reconstruction of the Fe3Pt Helmholtz-energy landscape.
- **Why it matters:** Learning heterogeneity explicitly may link multisource statistical modeling to thermodynamic derivative prediction, rather than merely borrowing physical terminology.
- **Caveat:** Reported robustness, generalization, and high-order derivative quality are abstract-level claims without independently examined comparisons.
- **Evidence:** [Captured source](https://www.pnas.org/doi/10.1073/pnas.2511227122); analysis based only on captured metadata, not independently verified full text.
