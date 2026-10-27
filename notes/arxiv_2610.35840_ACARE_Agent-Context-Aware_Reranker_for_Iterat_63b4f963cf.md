---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: AI agents and retrieval
enrichment_tags: [agentic-search, context-reranking, evidence-retrieval]
title: 'ACARE: Agent-Context-Aware Reranker for Iterative Search'
type: arxiv
source: https://arxiv.org/abs/2610.35840
canonical_url: https://arxiv.org/abs/2610.35840
captured_by: auto-scanner
date: '2026-10-27'
captured_at: '2026-10-27T10:10:23+00:00'
last_requested: '2026-10-27T10:10:23+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Sahel Sharifymoghaddam
- Yauhen Babakhin
- Reza Esfandiarpoor
- Oliver Holworthy
- Jimmy Lin
- Bo Liu
published: '2026-10-26'
abstract: 'In agentic search, a document can match an agent-generated sub-query without
  helping answer the user''s original question. Conventional rerankers score documents
  against the sub-query alone, overlooking the broader task and the agent''s reasoning.
  We introduce the Agent-Context-Aware Reranker (ACARe), a compact 4B LLM trained
  to rerank documents using this context when available. Across multiple benchmarks
  and agent families, ACARe improves retrieval quality over its base reranker while
  reducing search effort. These benefits extend to answer generation: ACARe improves
  accuracy and reduces searches over no reranking, while matching or exceeding the
  base reranker''s mean accuracy with more precise evidence. It also helps smaller
  agents narrow the retrieval-quality gap to larger agents, showing how better retrieval
  tools can make smaller agents more effective. The model, training data, and code
  will be released soon.'
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.35840'
  categories:
  - cs.IR
---

# ACARE: Agent-Context-Aware Reranker for Iterative Search

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.35840
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Sahel Sharifymoghaddam, Yauhen Babakhin, Reza Esfandiarpoor, Oliver Holworthy, Jimmy Lin, Bo Liu
- **Published:** 2026-10-26

## Summary
In agentic search, a document can match an agent-generated sub-query without helping answer the user's original question. Conventional rerankers score documents against the sub-query alone, overlooking the broader task and the agent's reasoning. We introduce the Agent-Context-Aware Reranker (ACARe), a compact 4B LLM trained to rerank documents using this context when available. Across multiple benchmarks and agent families, ACARe improves retrieval quality over its base reranker while reducing search effort. These benefits extend to answer generation: ACARe improves accuracy and reduces searches over no reranking, while matching or exceeding the base reranker's mean accuracy with more precise evidence. It also helps smaller agents narrow the retrieval-quality gap to larger agents, showing how better retrieval tools can make smaller agents more effective. The model, training data, and code will be released soon.

## Provider details
- **Arxiv Id:** 2610.35840
- **Categories:** ["cs.IR"]

## AI enrichment

- **Concise summary:** ACARe reranks search documents using the agent's broader task context rather than only the immediate sub-query, with reported retrieval and search-effort gains.
- **Why it matters:** Context-sensitive ranking could reduce retrieval drift when a plausible local query no longer serves the original question.
- **Caveat:** Preprint results are not independently checked; the abstract promises a future model, data and code release rather than confirming availability.
- **Evidence:** [Captured source](https://arxiv.org/abs/2610.35840); analysis based only on captured metadata, not independently verified full text.
