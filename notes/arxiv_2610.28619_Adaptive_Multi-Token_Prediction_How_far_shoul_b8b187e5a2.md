---
title: 'Adaptive Multi-Token Prediction: How far should we go?'
type: arxiv
source: https://arxiv.org/abs/2610.28619
canonical_url: https://arxiv.org/abs/2610.28619
captured_by: auto-scanner
date: '2026-10-21'
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Mathematics and algorithms
enrichment_tags: [language-model-inference, speculative-decoding, adaptive-computation]
captured_at: '2026-10-21T09:47:36+00:00'
last_requested: '2026-10-21T09:47:36+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Emile Anand
- Mohammed Rehan Parwani
- Xinyuan Cao
published: '2026-10-20'
abstract: 'Multi-token prediction (MTP) can accelerate language-model decoding by
  drafting several tokens and verifying them in a single target-model pass. However,
  the best speculation horizon changes with context: longer drafts offer greater amortization
  when reliable, but can waste compute on suffixes discarded after a rejection. Unlike
  autoregressive drafting, where a stopping rule can decide token by token, MTP must
  fix the horizon before drafting, as all heads fire in the same forward pass. We
  therefore formulate horizon selection as an online control problem, using verification
  feedback to learn how far the draft can be trusted in each context, and introduce
  Adaptive Multi-Token Prediction (AMTP): a lightweight controller that requires no
  retraining and leaves the exact verifier unchanged. To guide horizon selection,
  we characterize the expected number of tokens committed at each horizon via acceptance
  survival, the probability that a draft prefix is fully accepted. Before each round,
  AMTP predicts how far the draft is likely to survive and picks the horizon with
  the highest expected tokens per second, learning freely from every verification
  pass. Theoretically, we show that any online learner''s prediction error translates
  into throughput regret against the best horizon for each context, and in turn into
  a bound on wall-clock completion time. With online gradient descent, this regret
  is sublinear. Across five draft-target pairings built on Llama-3.1-8B-Instruct with
  Medusa heads, Meta''s MTP models, and Qwen3-4B-Inst-2507-MTP, evaluated on AIME
  2025 and GSM8K, AMTP decodes up to 4.1x faster than standard decoding and matches
  or outperforms the fixed window in 8 of 10 settings, with throughput gains of up
  to 10%.'
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.28619'
  categories:
  - cs.AI
  - cs.LG
  - eess.SY
---

# Adaptive Multi-Token Prediction: How far should we go?

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.28619
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Emile Anand, Mohammed Rehan Parwani, Xinyuan Cao
- **Published:** 2026-10-20

## Summary
Multi-token prediction (MTP) can accelerate language-model decoding by drafting several tokens and verifying them in a single target-model pass. However, the best speculation horizon changes with context: longer drafts offer greater amortization when reliable, but can waste compute on suffixes discarded after a rejection. Unlike autoregressive drafting, where a stopping rule can decide token by token, MTP must fix the horizon before drafting, as all heads fire in the same forward pass. We therefore formulate horizon selection as an online control problem, using verification feedback to learn how far the draft can be trusted in each context, and introduce Adaptive Multi-Token Prediction (AMTP): a lightweight controller that requires no retraining and leaves the exact verifier unchanged. To guide horizon selection, we characterize the expected number of tokens committed at each horizon via acceptance survival, the probability that a draft prefix is fully accepted. Before each round, AMTP predicts how far the draft is likely to survive and picks the horizon with the highest expected tokens per second, learning freely from every verification pass. Theoretically, we show that any online learner's prediction error translates into throughput regret against the best horizon for each context, and in turn into a bound on wall-clock completion time. With online gradient descent, this regret is sublinear. Across five draft-target pairings built on Llama-3.1-8B-Instruct with Medusa heads, Meta's MTP models, and Qwen3-4B-Inst-2507-MTP, evaluated on AIME 2025 and GSM8K, AMTP decodes up to 4.1x faster than standard decoding and matches or outperforms the fixed window in 8 of 10 settings, with throughput gains of up to 10%.

## Provider details
- **Arxiv Id:** 2610.28619
- **Categories:** ["cs.AI", "cs.LG", "eess.SY"]

## AI enrichment
- **Concise summary:** The abstract studies adapting the speculative decoding horizon in multi-token prediction as context-dependent draft quality changes.
- **Why it matters:** Choosing draft length dynamically is a practical algorithmic lever for balancing inference speed and verification cost.
- **Caveat:** This is a preprint; the captured abstract alone does not establish general speedups or deployment behavior.
- **Evidence:** [Captured source](https://arxiv.org/abs/2610.28619); analysis based only on captured metadata, not independently verified full text.
