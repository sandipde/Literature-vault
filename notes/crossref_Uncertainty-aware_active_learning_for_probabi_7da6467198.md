---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [high-entropy-alloys, corrosion-screening, uncertainty-aware-search, active-learning]
title: Uncertainty-aware active learning for probability-guided screening of high-entropy
  alloys with high corrosion potential
type: paper
source: https://doi.org/10.2139/ssrn.7624632
canonical_url: https://doi.org/10.2139/ssrn.7624632
captured_by: auto-scanner
date: '2026-10-18'
captured_at: '2026-10-18T09:18:02+00:00'
last_requested: '2026-10-18T09:18:02+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Zuoshan Zhang
- Gongbin Tang
- Tianjun Cui
- Lingli Jiang
- Zhongwei Liang
published: '2026-10-17'
abstract: High-entropy alloy screening is difficult because available corrosion datasets
  are small and heterogeneous. This study develops an uncertainty-aware active learning
  framework for probability-guided screening of alloys with high corrosion potential.
  After data standardization, descriptor construction, and feature selection, support
  vector regression achieved an initial test coefficient of determination of 0.629.
  Predicted corrosion potential, probability of high corrosion potential, predictive
  uncertainty, candidate diversity, and extrapolation risk were jointly considered
  during three active learning iterations, with three alloys experimentally tested
  in each round. Neither corrosion potential nor global regression accuracy increased
  monotonically. However, real experimental feedback gradually produced localized
  enrichment of high-corrosion-potential samples in the descriptor space. Three probability-guided
  follow-up alloys were then selected from this region. Two exceeded the highest corrosion
  potential in the original dataset, and the best alloy reached 66.6 millivolts versus
  the saturated calomel electrode, which was 116.6 millivolts more positive than the
  previous maximum. X-ray photoelectron spectroscopy and electrochemical impedance
  spectroscopy further revealed differences in surface oxidation states and interfacial
  impedance responses. Comparison with synthetic data augmentation showed that improved
  internal predictive performance did not necessarily translate into reliable prediction
  of newly measured alloys. These results show that active learning is more useful
  for progressively building a probability-guided experimental search space than for
  continuously improving global regression accuracy.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.2139/ssrn.7624632
  journal: ''
  publisher: Elsevier BV
  type: posted-content
  subjects: []
---

# Uncertainty-aware active learning for probability-guided screening of high-entropy alloys with high corrosion potential

- **Type:** paper
- **Source:** https://doi.org/10.2139/ssrn.7624632
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Zuoshan Zhang, Gongbin Tang, Tianjun Cui, Lingli Jiang, Zhongwei Liang
- **Published:** 2026-10-17

## Summary
High-entropy alloy screening is difficult because available corrosion datasets are small and heterogeneous. This study develops an uncertainty-aware active learning framework for probability-guided screening of alloys with high corrosion potential. After data standardization, descriptor construction, and feature selection, support vector regression achieved an initial test coefficient of determination of 0.629. Predicted corrosion potential, probability of high corrosion potential, predictive uncertainty, candidate diversity, and extrapolation risk were jointly considered during three active learning iterations, with three alloys experimentally tested in each round. Neither corrosion potential nor global regression accuracy increased monotonically. However, real experimental feedback gradually produced localized enrichment of high-corrosion-potential samples in the descriptor space. Three probability-guided follow-up alloys were then selected from this region. Two exceeded the highest corrosion potential in the original dataset, and the best alloy reached 66.6 millivolts versus the saturated calomel electrode, which was 116.6 millivolts more positive than the previous maximum. X-ray photoelectron spectroscopy and electrochemical impedance spectroscopy further revealed differences in surface oxidation states and interfacial impedance responses. Comparison with synthetic data augmentation showed that improved internal predictive performance did not necessarily translate into reliable prediction of newly measured alloys. These results show that active learning is more useful for progressively building a probability-guided experimental search space than for continuously improving global regression accuracy.

## Provider details
- **Doi:** 10.2139/ssrn.7624632
- **Publisher:** Elsevier BV
- **Type:** posted-content

## AI enrichment
- **Concise summary:** An uncertainty-aware alloy-screening loop combines predicted corrosion potential, target probability, diversity, and extrapolation risk with experimental feedback. The abstract reports localized enrichment of promising compositions despite nonmonotonic regression accuracy.
- **Why it matters:** Discovery success and global prediction metrics can diverge, so a campaign should be judged by measured candidates as well as held-out regression scores.
- **Caveat:** The SSRN preprint reports few experimental rounds and unverified outcomes; a more positive corrosion potential alone does not establish universally superior corrosion resistance.
- **Evidence:** [Captured source](https://doi.org/10.2139/ssrn.7624632); analysis based only on captured metadata, not independently verified full text.
