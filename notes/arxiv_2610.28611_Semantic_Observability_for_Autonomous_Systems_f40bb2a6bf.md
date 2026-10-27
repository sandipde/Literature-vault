---
title: Semantic Observability for Autonomous Systems Diagnostics
type: arxiv
source: https://arxiv.org/abs/2610.28611
canonical_url: https://arxiv.org/abs/2610.28611
captured_by: auto-scanner
date: '2026-10-21'
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: AI agents and retrieval
enrichment_tags: [observability, autonomous-systems, root-cause-analysis]
captured_at: '2026-10-21T09:47:36+00:00'
last_requested: '2026-10-21T09:47:36+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Jitendra Solanki
- Anand Todkar
- Ziran Min
published: '2026-10-20'
abstract: Modern distributed microservice deployments generate massive volumes of
  heterogeneous, multi-format observability logs across physically and logically partitioned
  infrastructure. Isolating root causes during cascading failures remains an arduous
  task for Site Reliability Engineers (SREs), bottlenecked by manual keyword filtering
  and disjointed temporal correlation across monitoring dashboards. We introduce Semantic
  Observability, an autonomous multi-agent framework that unifies disparate log streams
  into a dynamic, queryable Property Graph Database. By modeling physical infrastructure
  topologies, logical software dependencies, and chronological event sequences as
  attributed nodes and directed relations, it bridges the semantic gap inherent in
  flat, unstructured log repositories. Building on this unified substrate, we deploy
  a stateful multi-agent system orchestrated through Directed Cyclic Graphs (DCGs).
  The system autonomously navigates the topology, applying causal graph algorithms
  and temporal back-traversal to isolate the precise blast radius of anomalies. The
  pruned subgraph is then interpreted by a Large Language Model (LLM) reasoning engine
  to generate contextualized, code-level Root Cause Analyses (RCA) and actionable
  remediations. This paper establishes the foundational system architecture, formal
  relational ontology, and multi-agent control loops of Semantic Observability. We
  show conceptually how the framework eliminates ambient telemetry noise, reduces
  Mean Time to Resolution (MTTR), compresses LLM token consumption, and prevents structural
  hallucinations. We also specify an open-source validation framework on standard
  benchmarks (LogHub and Train-Ticket), laying the groundwork for a forthcoming companion
  paper on exhaustive quantitative evaluation and production benchmarking.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.28611'
  categories:
  - cs.AI
---

# Semantic Observability for Autonomous Systems Diagnostics

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.28611
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Jitendra Solanki, Anand Todkar, Ziran Min
- **Published:** 2026-10-20

## Summary
Modern distributed microservice deployments generate massive volumes of heterogeneous, multi-format observability logs across physically and logically partitioned infrastructure. Isolating root causes during cascading failures remains an arduous task for Site Reliability Engineers (SREs), bottlenecked by manual keyword filtering and disjointed temporal correlation across monitoring dashboards. We introduce Semantic Observability, an autonomous multi-agent framework that unifies disparate log streams into a dynamic, queryable Property Graph Database. By modeling physical infrastructure topologies, logical software dependencies, and chronological event sequences as attributed nodes and directed relations, it bridges the semantic gap inherent in flat, unstructured log repositories. Building on this unified substrate, we deploy a stateful multi-agent system orchestrated through Directed Cyclic Graphs (DCGs). The system autonomously navigates the topology, applying causal graph algorithms and temporal back-traversal to isolate the precise blast radius of anomalies. The pruned subgraph is then interpreted by a Large Language Model (LLM) reasoning engine to generate contextualized, code-level Root Cause Analyses (RCA) and actionable remediations. This paper establishes the foundational system architecture, formal relational ontology, and multi-agent control loops of Semantic Observability. We show conceptually how the framework eliminates ambient telemetry noise, reduces Mean Time to Resolution (MTTR), compresses LLM token consumption, and prevents structural hallucinations. We also specify an open-source validation framework on standard benchmarks (LogHub and Train-Ticket), laying the groundwork for a forthcoming companion paper on exhaustive quantitative evaluation and production benchmarking.

## Provider details
- **Arxiv Id:** 2610.28611
- **Categories:** ["cs.AI"]

## AI enrichment
- **Concise summary:** The captured abstract concerns semantic observability for diagnosing failures across distributed microservices with heterogeneous logs.
- **Why it matters:** A semantic view of fragmented telemetry could help connect symptoms across system boundaries during incident analysis.
- **Caveat:** This is a preprint abstract; the title and abstract do not establish diagnostic accuracy or operational readiness.
- **Evidence:** [Captured source](https://arxiv.org/abs/2610.28611); analysis based only on captured metadata, not independently verified full text.
