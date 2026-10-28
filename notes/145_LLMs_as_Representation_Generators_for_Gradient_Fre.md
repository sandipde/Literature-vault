---
title: 'LLMs as Representation Generators for Gradient‐Free Scientific Optimization:
  A Case Study in Battery Fast Charging'
type: paper
source: https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.78012
canonical_url: https://doi.org/10.1002/advs.78012
captured_by: sandipde
date: '2026-10-15'
captured_at: '2026-10-15T17:12:54+00:00'
last_requested: '2026-10-15T17:12:54+00:00'
issue: '145'
status: to-read
authors:
- Ge Lei
- Ferran Brosa Planella
- Sterling G. Baird
- Samuel J. Cooper
published: '2026-10-11'
abstract: 'ABSTRACT Scientific optimization problems are often characterized by slow,
  expensive, and non‐differentiable evaluations, which severely limit efficient exploration
  of rich design spaces. In these settings, performance depends not only on the optimizer
  itself, but also on whether the chosen search space can represent good solutions
  and whether important design requirements are effectively incorporated into the
  search. Here, we introduce a gradient‐free optimization framework based on large
  language models (LLMs) that enables the generation and refinement of executable
  control policies directly from natural language. We propose two complementary paradigms:
  Prompt‐to‐Optimizer (P2O), which combines LLM‐based structural generation with gradient‐free
  parameter optimization, and Prompt‐to‐Protocol (P2P), which directly synthesizes
  fully specified control policies. We apply this framework to battery fast‐charging
  protocol design, a representative slow‐feedback optimization problem. Across multiple
  case studies, our methods outperform conventional approaches restricted to predefined
  functional forms. In a realistic fast‐charging scenario, both approaches improve
  battery state of health by approximately 4.2% over a representative baseline, with
  P2P achieving this under matched evaluation budgets. More broadly, our results suggest
  that LLMs can serve as representation generators that expand the hypothesis space
  of scientific optimization, enabling efficient search in domains where evaluations
  are costly, and gradients are unavailable.'
metadata_provider: Crossref
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Mathematics and algorithms
enrichment_tags: [gradient-free-optimization, control-policies, battery-charging]
provider_data:
  doi: 10.1002/advs.78012
  journal: Advanced Science
  publisher: Wiley
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
        - 11
      date-time: '2026-10-11T00:00:00Z'
      timestamp: 1791676800000
    content-version: vor
    delay-in-days: 0
    URL: http://creativecommons.org/licenses/by/4.0/
  - start:
      date-parts:
      - - 2026
        - 10
        - 11
      date-time: '2026-10-11T00:00:00Z'
      timestamp: 1791676800000
    content-version: tdm
    delay-in-days: 0
    URL: http://doi.wiley.com/10.1002/tdm_license_1.1
---

# LLMs as Representation Generators for Gradient‐Free Scientific Optimization: A Case Study in Battery Fast Charging

- **Type:** paper
- **Source:** https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.78012
- **Captured by:** @sandipde
- **Metadata:** complete (Crossref)
- **Authors:** Ge Lei, Ferran Brosa Planella, Sterling G. Baird, Samuel J. Cooper
- **Published:** 2026-10-11

## Summary
ABSTRACT Scientific optimization problems are often characterized by slow, expensive, and non‐differentiable evaluations, which severely limit efficient exploration of rich design spaces. In these settings, performance depends not only on the optimizer itself, but also on whether the chosen search space can represent good solutions and whether important design requirements are effectively incorporated into the search. Here, we introduce a gradient‐free optimization framework based on large language models (LLMs) that enables the generation and refinement of executable control policies directly from natural language. We propose two complementary paradigms: Prompt‐to‐Optimizer (P2O), which combines LLM‐based structural generation with gradient‐free parameter optimization, and Prompt‐to‐Protocol (P2P), which directly synthesizes fully specified control policies. We apply this framework to battery fast‐charging protocol design, a representative slow‐feedback optimization problem. Across multiple case studies, our methods outperform conventional approaches restricted to predefined functional forms. In a realistic fast‐charging scenario, both approaches improve battery state of health by approximately 4.2% over a representative baseline, with P2P achieving this under matched evaluation budgets. More broadly, our results suggest that LLMs can serve as representation generators that expand the hypothesis space of scientific optimization, enabling efficient search in domains where evaluations are costly, and gradients are unavailable.

## Provider details
- **Doi:** 10.1002/advs.78012
- **Journal:** Advanced Science
- **Publisher:** Wiley
- **Type:** journal-article
- **License:** [{"start": {"date-parts": [[2026, 10, 11]], "date-time": "2026-10-11T00:00:00Z", "timestamp": 1791676800000}, "content-version": "vor", "delay-in-days": 0, "URL": "http://creativecommons.org/licenses/by/4.0/"}, {"start": {"date-parts": [[2026, 10, 11]], "date-time": "2026-10-11T00:00:00Z", "timestamp": 1791676800000}, "content-version": "tdm", "delay-in-days": 0, "URL": "http://doi.wiley.com/10.1002/tdm_license_1.1"}]

## AI enrichment

- **Concise summary:** P2O uses LLM-generated policy structures with gradient-free parameter search, while P2P directly generates complete charging policies. The abstract reports roughly 4.2% better battery state of health over a selected baseline.
- **Why it matters:** The central intervention is expanding the policy representation, offering an alternative to optimizing parameters inside a fixed functional family.
- **Caveat:** Battery-health gains depend on the stated scenarios and evaluation budgets; experimental deployment and broader superiority are not established by this capture.
- **Evidence:** [Captured source](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.78012); analysis based only on captured metadata, not independently verified full text.
