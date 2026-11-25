---
title: Inferring Experimental Objectives in Microscopy Experiments from Decision Traces
type: arxiv
source: https://arxiv.org/abs/2611.29814
canonical_url: https://arxiv.org/abs/2611.29814
captured_by: auto-scanner
date: '2026-11-25'
captured_at: '2026-11-25T01:13:37+00:00'
last_requested: '2026-11-25T01:13:37+00:00'
issue: scan:arxiv-ml-atomistic
status: to-read
authors:
- Kamyar Barakati
- Boris N. Slautin
- Aditya Raghavan
- Babita Babita
- Surya Prakash Reddy
- Jordan Marshall
- Munireach Nannory
- Stephen Puplampu
- Alla Slautina
- Faith M. Hines
- Newsha Javanmardi
- Sergei V. Kalinin
published: '2026-11-22'
abstract: Modern microscopes can acquire, analyze and act on data far faster than
  human operators can decide what to measure next. Exploiting this speed in automated
  experiments requires the instrument to follow the scientific logic of the operator,
  and one way to encode that logic is through reward functions that become part of
  the operation process. Here we explore whether such reward functions can be learned
  from the decision histories of microscope operators. We propose multiple frameworks
  in which recorded choices among alternative measurement locations serve as comparative
  evidence about the operator's preferences, and we compare several algorithms for
  reconstructing the reward including interpretable linear models built on physically
  meaningful image descriptors, nonlinear functions of the same descriptors, an unsupervised
  image representation followed by preference modeling, and a preference trained deep
  kernel inspired model. The result of this analysis is a spatial field of reward
  functions over the sample that can be used to run the instrument. We also propose
  a way to benchmark these approaches, based on withheld decisions and on decision
  histories generated with known objectives. We then examine the possibility that
  a decision history contains changing priorities throughout the experiment. A hidden
  Markov model assigns distinct rewards to recurring selection strategies, whereas
  a continuous-state model tracks smoothly varying preference weights. Controlled
  sequences generated over real microscopy candidate sets show that both concealed
  switches and gradual drift can be recovered. These reward functions, learned directly
  from recorded decisions, provide candidate objectives for future automated microscopy
  experiments.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.29814'
  categories:
  - cond-mat.mtrl-sci
  - cs.LG
---

# Inferring Experimental Objectives in Microscopy Experiments from Decision Traces

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.29814
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Kamyar Barakati, Boris N. Slautin, Aditya Raghavan, Babita Babita, Surya Prakash Reddy, Jordan Marshall, Munireach Nannory, Stephen Puplampu, Alla Slautina, Faith M. Hines, Newsha Javanmardi, Sergei V. Kalinin
- **Published:** 2026-11-22

## Summary
Modern microscopes can acquire, analyze and act on data far faster than human operators can decide what to measure next. Exploiting this speed in automated experiments requires the instrument to follow the scientific logic of the operator, and one way to encode that logic is through reward functions that become part of the operation process. Here we explore whether such reward functions can be learned from the decision histories of microscope operators. We propose multiple frameworks in which recorded choices among alternative measurement locations serve as comparative evidence about the operator's preferences, and we compare several algorithms for reconstructing the reward including interpretable linear models built on physically meaningful image descriptors, nonlinear functions of the same descriptors, an unsupervised image representation followed by preference modeling, and a preference trained deep kernel inspired model. The result of this analysis is a spatial field of reward functions over the sample that can be used to run the instrument. We also propose a way to benchmark these approaches, based on withheld decisions and on decision histories generated with known objectives. We then examine the possibility that a decision history contains changing priorities throughout the experiment. A hidden Markov model assigns distinct rewards to recurring selection strategies, whereas a continuous-state model tracks smoothly varying preference weights. Controlled sequences generated over real microscopy candidate sets show that both concealed switches and gradual drift can be recovered. These reward functions, learned directly from recorded decisions, provide candidate objectives for future automated microscopy experiments.

## Provider details
- **Arxiv Id:** 2611.29814
- **Categories:** ["cond-mat.mtrl-sci", "cs.LG"]
