---
title: Temporal Exploration and Rendezvous via Weisfeiler-Leman Colorings
type: arxiv
source: https://arxiv.org/abs/2610.30123
canonical_url: https://arxiv.org/abs/2610.30123
captured_by: auto-scanner
date: '2026-10-22'
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Mathematics and algorithms
enrichment_tags: [temporal-graphs, graph-coloring, exploration-algorithms]
captured_at: '2026-10-22T09:48:39+00:00'
last_requested: '2026-10-22T09:48:39+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Frank Kammer
- Sandra Kiefer
- Johannes Meintrup
published: '2026-10-21'
abstract: Temporal graphs are graphs whose edge relation changes in discrete time
  steps. The Temporal Exploration Problem (TEXP) asks for a temporal walk that visits
  all vertices. We show that every connected temporal graph with $n$ vertices can
  be explored in $O(qn\log^3(n))$ time steps, where $q$ is the number of vertex color
  classes induced by the 2-dimensional Weisfeiler-Leman (2-WL) coloring. For small
  $q$, our bound substantially improves on the known worst-case bound of $Θ(n^2)$
  in general connected temporal graphs. A corresponding walk can be constructed in
  deterministic polynomial time. The upper bound is complemented by lower bounds of
  $Ω(n\log(n))$ when $q$ is constant and $Ω(qn)$ when $1 \leq q \leq n$. We also apply
  our techniques to the Temporal Rendezvous Problem (TRP), in which two agents that
  do not communicate have to meet on a vertex of the temporal graph. Our exploration
  algorithm yields that, with only polynomial-time computational power, the agents
  can meet in $O(n\log^3(n))$ time steps, leaving a gap of only $\log^2(n)$ to the
  known lower bound. Dogeas, Erlebach, Kammer, Meintrup, and Moses Jr. [ICALP'24]
  have shown an $O(rn^{1+ε})$ bound for TEXP, for every fixed $ε> 0$, where $r$ is
  the number of orbits, and an $O(n^{1+ε})$ bound for TRP. Both results require superpolynomial
  computation time. Our contribution improves upon these results in several ways.
  First, the dependence on $n$ in the upper bounds on the number of time steps is
  decreased from $n^{1+ε}$ to $n\log^3(n)$ for both TEXP and TRP. Second, for TEXP,
  we bound the number of time steps linearly by the parameter q, which is efficiently
  computable and upper bounded by $r$. Third, we provide novel deterministic polynomial-time
  algorithms for both TEXP and TRP.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.30123'
  categories:
  - cs.DS
  - cs.CC
  - cs.DM
  - math.CO
---

# Temporal Exploration and Rendezvous via Weisfeiler-Leman Colorings

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.30123
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Frank Kammer, Sandra Kiefer, Johannes Meintrup
- **Published:** 2026-10-21

## Summary
Temporal graphs are graphs whose edge relation changes in discrete time steps. The Temporal Exploration Problem (TEXP) asks for a temporal walk that visits all vertices. We show that every connected temporal graph with $n$ vertices can be explored in $O(qn\log^3(n))$ time steps, where $q$ is the number of vertex color classes induced by the 2-dimensional Weisfeiler-Leman (2-WL) coloring. For small $q$, our bound substantially improves on the known worst-case bound of $Θ(n^2)$ in general connected temporal graphs. A corresponding walk can be constructed in deterministic polynomial time. The upper bound is complemented by lower bounds of $Ω(n\log(n))$ when $q$ is constant and $Ω(qn)$ when $1 \leq q \leq n$. We also apply our techniques to the Temporal Rendezvous Problem (TRP), in which two agents that do not communicate have to meet on a vertex of the temporal graph. Our exploration algorithm yields that, with only polynomial-time computational power, the agents can meet in $O(n\log^3(n))$ time steps, leaving a gap of only $\log^2(n)$ to the known lower bound. Dogeas, Erlebach, Kammer, Meintrup, and Moses Jr. [ICALP'24] have shown an $O(rn^{1+ε})$ bound for TEXP, for every fixed $ε> 0$, where $r$ is the number of orbits, and an $O(n^{1+ε})$ bound for TRP. Both results require superpolynomial computation time. Our contribution improves upon these results in several ways. First, the dependence on $n$ in the upper bounds on the number of time steps is decreased from $n^{1+ε}$ to $n\log^3(n)$ for both TEXP and TRP. Second, for TEXP, we bound the number of time steps linearly by the parameter q, which is efficiently computable and upper bounded by $r$. Third, we provide novel deterministic polynomial-time algorithms for both TEXP and TRP.

## Provider details
- **Arxiv Id:** 2610.30123
- **Categories:** ["cs.DS", "cs.CC", "cs.DM", "math.CO"]

## AI enrichment
- **Concise summary:** The preprint studies temporal graph exploration and rendezvous using Weisfeiler-Leman colorings.
- **Why it matters:** It brings graph-structural tools to algorithms where edges and paths change over discrete time steps.
- **Caveat:** This is a preprint; the abstract's stated results and assumptions are not independently verified.
- **Evidence:** [Captured source](https://arxiv.org/abs/2610.30123); analysis based only on captured metadata, not independently verified full text.
