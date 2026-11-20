---
title: 'Realized versus Population Reliability: Anytime-Valid Self-Consistency Certification
  under Correlated Reasoning'
type: arxiv
source: https://arxiv.org/abs/2611.26592
canonical_url: https://arxiv.org/abs/2611.26592
captured_by: auto-scanner
date: '2026-11-20'
captured_at: '2026-11-20T13:47:16+00:00'
last_requested: '2026-11-20T13:47:16+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Terence D. Agbeyegbe
- Toneukarin G. Agbeyegbe
published: '2026-11-19'
abstract: 'Self-consistency certification treats repeated sampling from a language
  model as sequential evidence accumulation and stops when an anytime-valid e-process
  crosses a threshold, guaranteeing finite-sample Type I error control by Ville''s
  inequality. Prior constructions assume sampled rollouts are conditionally independent.
  We show this assumption fails in practice: reasoning streams are positively correlated
  through shared reasoning prefixes or across-prompt heterogeneity, changing not merely
  certificate efficiency but the hypothesis certified. Modeling dependence via a per-unit
  latent state (the random-effects / intraclass-correlation structure) induces exchangeable,
  equi-correlated increments with correlation $ρ$. Correlation splits the single null
  into a realized null about the drawn belief and a population null about average
  model behavior, which coincide only when $ρ=0$. We show: (i) the standard betting
  e-process remains anytime-valid for the realized null, not the population null;
  (ii) read as a population-null test, a suitable mixture has asymptotic crossing
  probability at least $π=P(μ(Z)>0)$, potentially exceeding nominal $ε$; (iii) the
  within-unit mean''s effective sample size saturates at $1/ρ$, so extra within-unit
  rollouts cannot restore population validity; and (iv) a prompt-level e-process restores
  population validity, with optimal allocation at one rollout per prompt under a pure
  rollout budget. Simulations and Claude Haiku 4.5 rollouts confirm this regime dependence:
  on GSM8K ($\hatρ=0.435$, $\hatθ=+0.96$) the gap is dormant, whereas on AIME ($\hatρ=0.480$,
  $\hatθ=-0.15$) the single-unit rule crosses on 24% of prompts at nominal $ε=0.05$,
  while the prompt-level procedure declines (0.00). This correctness result identifies
  which reliability claim an anytime-valid certificate actually supports under dependence.'
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.26592'
  categories:
  - stat.ME
  - cs.AI
  - cs.LG
---

# Realized versus Population Reliability: Anytime-Valid Self-Consistency Certification under Correlated Reasoning

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.26592
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Terence D. Agbeyegbe, Toneukarin G. Agbeyegbe
- **Published:** 2026-11-19

## Summary
Self-consistency certification treats repeated sampling from a language model as sequential evidence accumulation and stops when an anytime-valid e-process crosses a threshold, guaranteeing finite-sample Type I error control by Ville's inequality. Prior constructions assume sampled rollouts are conditionally independent. We show this assumption fails in practice: reasoning streams are positively correlated through shared reasoning prefixes or across-prompt heterogeneity, changing not merely certificate efficiency but the hypothesis certified. Modeling dependence via a per-unit latent state (the random-effects / intraclass-correlation structure) induces exchangeable, equi-correlated increments with correlation $ρ$. Correlation splits the single null into a realized null about the drawn belief and a population null about average model behavior, which coincide only when $ρ=0$. We show: (i) the standard betting e-process remains anytime-valid for the realized null, not the population null; (ii) read as a population-null test, a suitable mixture has asymptotic crossing probability at least $π=P(μ(Z)>0)$, potentially exceeding nominal $ε$; (iii) the within-unit mean's effective sample size saturates at $1/ρ$, so extra within-unit rollouts cannot restore population validity; and (iv) a prompt-level e-process restores population validity, with optimal allocation at one rollout per prompt under a pure rollout budget. Simulations and Claude Haiku 4.5 rollouts confirm this regime dependence: on GSM8K ($\hatρ=0.435$, $\hatθ=+0.96$) the gap is dormant, whereas on AIME ($\hatρ=0.480$, $\hatθ=-0.15$) the single-unit rule crosses on 24% of prompts at nominal $ε=0.05$, while the prompt-level procedure declines (0.00). This correctness result identifies which reliability claim an anytime-valid certificate actually supports under dependence.

## Provider details
- **Arxiv Id:** 2611.26592
- **Categories:** ["stat.ME", "cs.AI", "cs.LG"]
