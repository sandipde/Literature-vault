---
title: 'From Natural Language to Exact Cover: A Neuro-Symbolic Approach to Zebra Puzzles'
type: arxiv
source: https://arxiv.org/abs/2611.03641
canonical_url: https://arxiv.org/abs/2611.03641
captured_by: auto-scanner
date: '2026-11-03'
captured_at: '2026-11-03T12:34:47+00:00'
last_requested: '2026-11-03T12:34:47+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Paulius Skaisgiris
- Thomas Pammer
- Veronika Semmelrock
- Mykyta Ielanskyi
- Maximilian Heisinger
- Erich Kobler
published: '2026-11-02'
abstract: Chain-of-Thought (CoT) generation has substantially improved the performance
  of Large Language Models (LLMs) on complex reasoning tasks, including code generation,
  data analysis, and exam-style question answering. Despite these advances, purely
  neural LLMs continue to struggle with elementary logical reasoning problems and
  lack the determinism, soundness, and reliability characteristic of symbolic reasoning
  systems. Conversely, classical symbolic methods such as SAT solving and exact cover
  guarantee correctness and completeness, but require problems to be expressed in
  highly specialized formal encodings, limiting their applicability to natural language
  inputs. In this work, we present a synergistic neuro-symbolic framework that bridges
  this gap by combining neural semantic parsing with deterministic exact cover reasoning.
  Given a Zebra-style logic puzzle in natural language, an LLM translates entities
  and constraints into structured tool calls that construct an exact cover instance.
  A symbolic solver then computes the solution and provides feedback to iteratively
  refine invalid, under- or overconstrained encodings, exploiting the uniqueness property
  of Zebra puzzles. We conduct a comprehensive empirical evaluation across multiple
  parameter scales, post-training paradigms, and LLM families. The results demonstrate
  that our hybrid approach consistently outperforms strong plain neural baselines,
  including CoT prompting, as well as recent neuro-symbolic methods.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.03641'
  categories:
  - cs.AI
---

# From Natural Language to Exact Cover: A Neuro-Symbolic Approach to Zebra Puzzles

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.03641
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Paulius Skaisgiris, Thomas Pammer, Veronika Semmelrock, Mykyta Ielanskyi, Maximilian Heisinger, Erich Kobler
- **Published:** 2026-11-02

## Summary
Chain-of-Thought (CoT) generation has substantially improved the performance of Large Language Models (LLMs) on complex reasoning tasks, including code generation, data analysis, and exam-style question answering. Despite these advances, purely neural LLMs continue to struggle with elementary logical reasoning problems and lack the determinism, soundness, and reliability characteristic of symbolic reasoning systems. Conversely, classical symbolic methods such as SAT solving and exact cover guarantee correctness and completeness, but require problems to be expressed in highly specialized formal encodings, limiting their applicability to natural language inputs. In this work, we present a synergistic neuro-symbolic framework that bridges this gap by combining neural semantic parsing with deterministic exact cover reasoning. Given a Zebra-style logic puzzle in natural language, an LLM translates entities and constraints into structured tool calls that construct an exact cover instance. A symbolic solver then computes the solution and provides feedback to iteratively refine invalid, under- or overconstrained encodings, exploiting the uniqueness property of Zebra puzzles. We conduct a comprehensive empirical evaluation across multiple parameter scales, post-training paradigms, and LLM families. The results demonstrate that our hybrid approach consistently outperforms strong plain neural baselines, including CoT prompting, as well as recent neuro-symbolic methods.

## Provider details
- **Arxiv Id:** 2611.03641
- **Categories:** ["cs.AI"]
