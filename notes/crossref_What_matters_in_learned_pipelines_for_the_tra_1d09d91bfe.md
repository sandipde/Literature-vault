---
title: 'What matters in learned pipelines for the traveling salesman problem with
  drone: search objective, start diversity, and learned priors'
type: paper
source: https://doi.org/10.2139/ssrn.7657722
canonical_url: https://doi.org/10.2139/ssrn.7657722
captured_by: auto-scanner
date: '2026-10-23'
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Mathematics and algorithms
enrichment_tags: [traveling-salesperson, learned-heuristics, algorithm-evaluation]
captured_at: '2026-10-23T09:43:13+00:00'
last_requested: '2026-10-23T09:43:13+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Abdelouahed Ben Mhamed
- Assia Kamal-Idrissi
- Amal El Fallah Seghrouchni
published: '2026-10-22'
abstract: Learned construction policies for the traveling salesman problem with drone
  (TSP-D) are rarely evaluated in a way that isolates the source of solution quality.
  In a controlled design, one pipeline receives customer orders from an operation-level
  Generative Flow Network (GFlowNet), an order-level policy trained with policy optimization
  with multiple optima (POMO), a published deep reinforcement learning policy, and
  classical constructions from random orders to perturbed Lin–Kernighan–Helsgaun (LKH)
  tours. An exact dynamic program partitions each order, and a restricted version
  prices each search move. Experiments cover the uniform Agatz benchmark and synthetic
  instances with 50 to 200 customers. First, the search objective and start diversity
  determine quality. Pricing moves by makespan rather than truck length improves every
  method by 9.8–12.8%. Sixteen diverse starts converge 4.0–6.6 percentage points below
  a single nearest-neighbor start, whereas screening thousands of samples adds at
  most 0.4 percentage points and can reduce quality. Second, every stochastic method
  improves on the best published benchmark averages at 50 and 100 nodes and drone
  speed ratios 1–3. The best method improves on a recent hybrid genetic algorithm
  by 1.55–4.15% at similar run time. Third, under small budgets and up to 100 customers,
  learned policies reach the reference quality with 1.8–3.7 times fewer evaluations
  than random or nearest-neighbor multi-starts. After full search, learned and diverse
  classical starts show no significant difference up to 100 customers, and perturbed
  LKH tours lead at 200. In wall-clock time, a single LKH tour reaches near-converged
  quality fastest.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.2139/ssrn.7657722
  journal: ''
  publisher: Elsevier BV
  type: posted-content
  subjects: []
---

# What matters in learned pipelines for the traveling salesman problem with drone: search objective, start diversity, and learned priors

- **Type:** paper
- **Source:** https://doi.org/10.2139/ssrn.7657722
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Abdelouahed Ben Mhamed, Assia Kamal-Idrissi, Amal El Fallah Seghrouchni
- **Published:** 2026-10-22

## Summary
Learned construction policies for the traveling salesman problem with drone (TSP-D) are rarely evaluated in a way that isolates the source of solution quality. In a controlled design, one pipeline receives customer orders from an operation-level Generative Flow Network (GFlowNet), an order-level policy trained with policy optimization with multiple optima (POMO), a published deep reinforcement learning policy, and classical constructions from random orders to perturbed Lin–Kernighan–Helsgaun (LKH) tours. An exact dynamic program partitions each order, and a restricted version prices each search move. Experiments cover the uniform Agatz benchmark and synthetic instances with 50 to 200 customers. First, the search objective and start diversity determine quality. Pricing moves by makespan rather than truck length improves every method by 9.8–12.8%. Sixteen diverse starts converge 4.0–6.6 percentage points below a single nearest-neighbor start, whereas screening thousands of samples adds at most 0.4 percentage points and can reduce quality. Second, every stochastic method improves on the best published benchmark averages at 50 and 100 nodes and drone speed ratios 1–3. The best method improves on a recent hybrid genetic algorithm by 1.55–4.15% at similar run time. Third, under small budgets and up to 100 customers, learned policies reach the reference quality with 1.8–3.7 times fewer evaluations than random or nearest-neighbor multi-starts. After full search, learned and diverse classical starts show no significant difference up to 100 customers, and perturbed LKH tours lead at 200. In wall-clock time, a single LKH tour reaches near-converged quality fastest.

## Provider details
- **Doi:** 10.2139/ssrn.7657722
- **Publisher:** Elsevier BV
- **Type:** posted-content

## AI enrichment
- **Concise summary:** The abstract uses a controlled design to examine search objectives, start diversity, and learned priors in learned construction policies for the traveling-salesperson problem with a drone.
- **Why it matters:** Isolating pipeline components helps clarify what contributes to solution quality in learned heuristics.
- **Caveat:** This is posted content; the abstract's study findings are not independently evaluated.
- **Evidence:** [Captured source](https://doi.org/10.2139/ssrn.7657722); analysis based only on captured metadata, not independently verified full text.
