---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Mathematics and algorithms
enrichment_tags: [quantum-error-correction, conditional-mutual-information, local-noise, phase-stability]
title: Stability of Quantum LDPC States under Local Pauli Noise
type: arxiv
source: https://arxiv.org/abs/2610.22357
canonical_url: https://arxiv.org/abs/2610.22357
captured_by: auto-scanner
date: '2026-10-16'
captured_at: '2026-10-16T09:27:31+00:00'
last_requested: '2026-10-16T09:27:31+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Tai-Hsuan Yang
- Andrew D. Kim
- Akash Vijay
- Jong Yeon Lee
published: '2026-10-15'
abstract: Quantum low-density parity-check (qLDPC) codes have a canonical mixed state---the
  normalized projector onto the code space---that lies at the intersection of quantum
  error correction and quantum many-body physics, yet the stability of its information-theoretic
  structure under local noise remains poorly understood. Recent progress on mixed-state
  phases of matter has identified the spatial decay of conditional mutual information
  (CMI) $I(A:C|B)$ as a key diagnostic of such stability, analogous to the role of
  the spectral gap for quantum ground states. We prove that, for the normalized code-projector
  state of a $\mathbb{Z}_d$ qLDPC stabilizer code under local Pauli noise, the CMI
  across a buffer $B$ separating $A$ from $C$ decays exponentially with the width
  of $B$ in two complementary noise regimes independent of system size. At weak noise,
  this holds for full-system tripartitions, where correlations between the two sides
  require an error cluster to cross the buffer, an exponentially unlikely event. At
  strong noise, exponential decay holds whenever the buffer supports no logical operator,
  since correlations can persist only along rare chains of buffer qudits that remain
  informative. Under an additional space-uniformity assumption, we establish the robustness
  of Levin--Wen topological entropy. On finite-dimensional lattices of size $n$, the
  weak-noise bound further implies a constant-layer quasi-local Petz recovery channel
  of range $O(\poly(\log n)/\varepsilon)$ that recovers the noiseless state within
  trace-distance error $\varepsilon$. Both CMI bounds apply to general qLDPC interaction
  graphs, including geometries where such constant-depth quasi-local recovery need
  not exist. Thus, the exponential decay of the noise-induced CMI provides a general
  criterion for mixed-state phase stability.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.22357'
  categories:
  - quant-ph
---

# Stability of Quantum LDPC States under Local Pauli Noise

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.22357
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Tai-Hsuan Yang, Andrew D. Kim, Akash Vijay, Jong Yeon Lee
- **Published:** 2026-10-15

## Summary
Quantum low-density parity-check (qLDPC) codes have a canonical mixed state---the normalized projector onto the code space---that lies at the intersection of quantum error correction and quantum many-body physics, yet the stability of its information-theoretic structure under local noise remains poorly understood. Recent progress on mixed-state phases of matter has identified the spatial decay of conditional mutual information (CMI) $I(A:C|B)$ as a key diagnostic of such stability, analogous to the role of the spectral gap for quantum ground states. We prove that, for the normalized code-projector state of a $\mathbb{Z}_d$ qLDPC stabilizer code under local Pauli noise, the CMI across a buffer $B$ separating $A$ from $C$ decays exponentially with the width of $B$ in two complementary noise regimes independent of system size. At weak noise, this holds for full-system tripartitions, where correlations between the two sides require an error cluster to cross the buffer, an exponentially unlikely event. At strong noise, exponential decay holds whenever the buffer supports no logical operator, since correlations can persist only along rare chains of buffer qudits that remain informative. Under an additional space-uniformity assumption, we establish the robustness of Levin--Wen topological entropy. On finite-dimensional lattices of size $n$, the weak-noise bound further implies a constant-layer quasi-local Petz recovery channel of range $O(\poly(\log n)/\varepsilon)$ that recovers the noiseless state within trace-distance error $\varepsilon$. Both CMI bounds apply to general qLDPC interaction graphs, including geometries where such constant-depth quasi-local recovery need not exist. Thus, the exponential decay of the noise-induced CMI provides a general criterion for mixed-state phase stability.

## Provider details
- **Arxiv Id:** 2610.22357
- **Categories:** ["quant-ph"]

## AI enrichment
- **Concise summary:** The paper states exponential conditional-mutual-information decay bounds for qLDPC code-projector states under weak and strong local Pauli noise, with different geometric conditions.
- **Why it matters:** Linking correlation decay to mixed-state stability connects quantum coding theory to many-body information diagnostics.
- **Caveat:** The arXiv claims are theorem-level statements with assumptions: strong-noise buffers must support no logical operator, and recovery-channel conclusions require lattice geometry; proofs were not checked.
- **Evidence:** [Captured source](https://arxiv.org/abs/2610.22357); analysis based only on captured metadata, not independently verified full text.
