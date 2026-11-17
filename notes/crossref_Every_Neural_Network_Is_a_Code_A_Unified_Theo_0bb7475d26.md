---
title: 'Every Neural Network Is a Code: A Unified Theory of Implicit Coding in Neural
  Networks'
type: paper
source: https://doi.org/10.21203/rs.3.rs-11731108/v1
canonical_url: https://doi.org/10.21203/rs.3.rs-11731108/v1
captured_by: auto-scanner
date: '2026-11-17'
captured_at: '2026-11-17T14:04:00+00:00'
last_requested: '2026-11-17T14:04:00+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Luca Eliseo Pavesi
published: '2026-11-17'
abstract: 'Abstract The theory of neural networks lacks a single quantity that is
  defined for every architecture and training procedure, measurable on real pipelines,
  and sufficient to state what a network can and cannot learn. We argue that such
  a quantity exists: the implicit code length, the cumulative log loss incurred when
  each example is predicted before it is trained on. We develop it into a self-contained
  theory with complete proofs: a conservation law (for every learner and every input
  set the code lengths of all labelings satisfy Kraft''s equality, so inductive bias
  is a fixed budget that can be moved but not increased); a representation theorem
  (every learner is the Bayes predictor of its own implicit prior); a compression
  identity (expected code length equals the sum of test risks along the learning curve),
  which constrains plateaus, scaling exponents and double-descent bumps; exact accounting
  for single-pass training, for symmetries of architecture and initialization (including
  a new corollary: breaking a symmetry moves the tax inside the orbit but cannot remove
  it), for pretraining and for in-context learning. We state three falsifiable conjectures
  and a protocol to test them, and report experiments with real numbers. Earlier exact
  enumerations at $n=10$ and $n=16$ and MNIST code lengths are reproduced in part
  and extended by four new experiments. (i) Across standard, NTK, maximal-update ($\mu$P)
  and step-rescaled parametrizations, exact priors on all $2^{12}$ labelings show
  that the concentration of the prior with width reported earlier is a property of
  a step that grows with width: in $\mu$P the entropy is flat ($+0.005\pm0.009$ nats
  per doubling) and the prior converges ($\mathrm{KL}(Q_{2H}\|Q_H)\propto H^{-1.10\pm0.15}$),
  while the revised conjecture that entropy is a function of function-space movement
  alone is refuted ($0.82\pm0.11$ nats between $\mu$P and NTK at equal movement).
  (ii) A centred finite network approaches its neural-tangent-kernel code as $H^{-0.97\pm0.08}$
  in Kullback--Leibler divergence; beyond width about one hundred the departure is
  the randomness of the kernel, not feature learning; and infinite-width gradient
  descent stays $0.37$ nats ($4.5\%$ of $n\ln2$) from the best tempered Gaussian-process
  Bayes code. (iii) Sample-wise double descent of a ridgeless random-features classifier
  is a burst of code rate at the interpolation threshold whose price is $3.9$--$176$
  nats (median). (iv) On sparse parities the plateau of single-pass SGD costs $1{,}495$--$8{,}500$
  nats where the Bayes mixture over the class pays at most $7.04$, and the price is
  not monotone in width. Kraft''s equality holds to $3.3\times10^{-16}$ on all $313$
  new exact codes. The six further experiments of the programme are reported as well.
  (v) The in-context identity holds to $10^{-15}$ on a four-task family; the unavoidable
  term is $0.752$ nats ($H(\pi)=1.280$), and a network pretrained on one task costs
  up to $15.24$ nats on the opposite one against $6.83$ from scratch. (vi) Exact priors
  of convolutional, residual and attention architectures on translation orbits fall
  into two clusters $5$--$15$ nats apart; translation-invariant learners put $0.896$--$0.982$
  of their mass on invariant labelings (MLP: $0.016$), almost all of it on constant
  ones. (vii) On the scikit-learn digits, block-wise code lengths follow power laws
  in $n$ with exponents that order the pipelines as on MNIST, and code-length ratios
  over $30$ tasks stay within a factor $1.38$. (viii) Two presentation orders of the
  same ten examples give priors $0.44$--$0.77$ nats apart, as much as two seeds. (ix)
  An asymmetric initialization redistributes the symmetry tax inside every orbit,
  as the corollary predicts, and makes a naming cheaper than its tax for only $2$
  of some ten million labelings. (x) On the stored $n=12$ priors, multiplicative invariance
  holds labeling-wise with a constant of at most $3.7$ for width-stable parametrizations
  and fails for a fixed-step standard one ($4.1$ at width $64$, $8.1$ at $256$); the
  simplicity envelope survives for a geometry-aware code as an inequality ($\tilde
  K\le2C_A+0.83$ for $n=6$ to $12$) that explains under $5\%$ of the variance. Results
  that contradict our hypotheses are reported as results.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.21203/rs.3.rs-11731108/v1
  journal: ''
  publisher: Springer Science and Business Media LLC
  type: posted-content
  subjects: []
---

# Every Neural Network Is a Code: A Unified Theory of Implicit Coding in Neural Networks

- **Type:** paper
- **Source:** https://doi.org/10.21203/rs.3.rs-11731108/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Luca Eliseo Pavesi
- **Published:** 2026-11-17

## Summary
Abstract The theory of neural networks lacks a single quantity that is defined for every architecture and training procedure, measurable on real pipelines, and sufficient to state what a network can and cannot learn. We argue that such a quantity exists: the implicit code length, the cumulative log loss incurred when each example is predicted before it is trained on. We develop it into a self-contained theory with complete proofs: a conservation law (for every learner and every input set the code lengths of all labelings satisfy Kraft's equality, so inductive bias is a fixed budget that can be moved but not increased); a representation theorem (every learner is the Bayes predictor of its own implicit prior); a compression identity (expected code length equals the sum of test risks along the learning curve), which constrains plateaus, scaling exponents and double-descent bumps; exact accounting for single-pass training, for symmetries of architecture and initialization (including a new corollary: breaking a symmetry moves the tax inside the orbit but cannot remove it), for pretraining and for in-context learning. We state three falsifiable conjectures and a protocol to test them, and report experiments with real numbers. Earlier exact enumerations at $n=10$ and $n=16$ and MNIST code lengths are reproduced in part and extended by four new experiments. (i) Across standard, NTK, maximal-update ($\mu$P) and step-rescaled parametrizations, exact priors on all $2^{12}$ labelings show that the concentration of the prior with width reported earlier is a property of a step that grows with width: in $\mu$P the entropy is flat ($+0.005\pm0.009$ nats per doubling) and the prior converges ($\mathrm{KL}(Q_{2H}\|Q_H)\propto H^{-1.10\pm0.15}$), while the revised conjecture that entropy is a function of function-space movement alone is refuted ($0.82\pm0.11$ nats between $\mu$P and NTK at equal movement). (ii) A centred finite network approaches its neural-tangent-kernel code as $H^{-0.97\pm0.08}$ in Kullback--Leibler divergence; beyond width about one hundred the departure is the randomness of the kernel, not feature learning; and infinite-width gradient descent stays $0.37$ nats ($4.5\%$ of $n\ln2$) from the best tempered Gaussian-process Bayes code. (iii) Sample-wise double descent of a ridgeless random-features classifier is a burst of code rate at the interpolation threshold whose price is $3.9$--$176$ nats (median). (iv) On sparse parities the plateau of single-pass SGD costs $1{,}495$--$8{,}500$ nats where the Bayes mixture over the class pays at most $7.04$, and the price is not monotone in width. Kraft's equality holds to $3.3\times10^{-16}$ on all $313$ new exact codes. The six further experiments of the programme are reported as well. (v) The in-context identity holds to $10^{-15}$ on a four-task family; the unavoidable term is $0.752$ nats ($H(\pi)=1.280$), and a network pretrained on one task costs up to $15.24$ nats on the opposite one against $6.83$ from scratch. (vi) Exact priors of convolutional, residual and attention architectures on translation orbits fall into two clusters $5$--$15$ nats apart; translation-invariant learners put $0.896$--$0.982$ of their mass on invariant labelings (MLP: $0.016$), almost all of it on constant ones. (vii) On the scikit-learn digits, block-wise code lengths follow power laws in $n$ with exponents that order the pipelines as on MNIST, and code-length ratios over $30$ tasks stay within a factor $1.38$. (viii) Two presentation orders of the same ten examples give priors $0.44$--$0.77$ nats apart, as much as two seeds. (ix) An asymmetric initialization redistributes the symmetry tax inside every orbit, as the corollary predicts, and makes a naming cheaper than its tax for only $2$ of some ten million labelings. (x) On the stored $n=12$ priors, multiplicative invariance holds labeling-wise with a constant of at most $3.7$ for width-stable parametrizations and fails for a fixed-step standard one ($4.1$ at width $64$, $8.1$ at $256$); the simplicity envelope survives for a geometry-aware code as an inequality ($\tilde K\le2C_A+0.83$ for $n=6$ to $12$) that explains under $5\%$ of the variance. Results that contradict our hypotheses are reported as results.

## Provider details
- **Doi:** 10.21203/rs.3.rs-11731108/v1
- **Publisher:** Springer Science and Business Media LLC
- **Type:** posted-content
