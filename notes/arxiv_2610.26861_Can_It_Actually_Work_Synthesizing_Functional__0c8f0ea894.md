---
title: Can It Actually Work? Synthesizing Functional CAD Mechanisms
type: arxiv
source: https://arxiv.org/abs/2610.26861
canonical_url: https://arxiv.org/abs/2610.26861
captured_by: auto-scanner
date: '2026-10-20'
captured_at: '2026-10-20T09:46:32+00:00'
last_requested: '2026-10-20T09:46:32+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Wenqian Zhang
- Yangyi Huang
- Zigeng Xu
- Weiyang Liu
- Zhen Liu
published: '2026-10-19'
abstract: 'While LLM agents can generate visually plausible CAD assemblies, these
  designs often fail to fulfill their intended physical functions. We study functional
  CAD design, a setting where agents interpret underspecified requests to construct
  and iteratively revise mechanisms that satisfy functional requirements in physical
  simulation. Verifying these requirements is nontrivial: different candidate mechanisms
  may realize the same function through entirely different components, controls, and
  operating sequences. To bridge this gap, we propose FunCAD-Harness, a framework
  that translates abstract requirements into candidate-specific physical tests and
  uses simulation feedback to guide design revisions. To systematically evaluate this
  capability, we introduce FunCADBench, a benchmark spanning 46 mechanism families
  with interdependent and multi-step operations. Experiments across frontier LLM agents
  show that FunCAD-Harness exposes subtle mechanical failures invisible to visual
  inspection, substantially improving functional success rates over standard simulation-augmented
  baselines. Ultimately, our work marks a step toward CAD agents capable of translating
  human intent into working mechanisms.'
metadata_provider: arXiv
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: AI agents and retrieval
enrichment_tags: [cad-agents, physical-simulation, functional-verification]
provider_data:
  arxiv_id: '2610.26861'
  categories:
  - cs.CV
  - cs.CL
  - cs.GR
---

# Can It Actually Work? Synthesizing Functional CAD Mechanisms

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.26861
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Wenqian Zhang, Yangyi Huang, Zigeng Xu, Weiyang Liu, Zhen Liu
- **Published:** 2026-10-19

## Summary
While LLM agents can generate visually plausible CAD assemblies, these designs often fail to fulfill their intended physical functions. We study functional CAD design, a setting where agents interpret underspecified requests to construct and iteratively revise mechanisms that satisfy functional requirements in physical simulation. Verifying these requirements is nontrivial: different candidate mechanisms may realize the same function through entirely different components, controls, and operating sequences. To bridge this gap, we propose FunCAD-Harness, a framework that translates abstract requirements into candidate-specific physical tests and uses simulation feedback to guide design revisions. To systematically evaluate this capability, we introduce FunCADBench, a benchmark spanning 46 mechanism families with interdependent and multi-step operations. Experiments across frontier LLM agents show that FunCAD-Harness exposes subtle mechanical failures invisible to visual inspection, substantially improving functional success rates over standard simulation-augmented baselines. Ultimately, our work marks a step toward CAD agents capable of translating human intent into working mechanisms.

## Provider details
- **Arxiv Id:** 2610.26861
- **Categories:** ["cs.CV", "cs.CL", "cs.GR"]

## AI enrichment

- **Concise summary:** FunCAD-Harness translates underspecified mechanism requirements into candidate-specific simulation tests and iterative revisions. FunCADBench covers 46 mechanism families with interdependent operations.
- **Why it matters:** Functional testing can reject visually convincing but mechanically ineffective agent-generated designs.
- **Caveat:** Simulated success is not manufacturing or real-world validation, and the captured preprint gives no independently checked effect size.
- **Evidence:** [Captured source](https://arxiv.org/abs/2610.26861); analysis based only on captured metadata, not independently verified full text.
