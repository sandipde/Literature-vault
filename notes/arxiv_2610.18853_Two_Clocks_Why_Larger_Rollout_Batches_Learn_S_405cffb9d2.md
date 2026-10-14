---
title: 'Two Clocks: Why Larger Rollout Batches Learn Slower but Fail on Schedule in
  Reinforcement Learning with Verifiable Rewards'
type: arxiv
source: https://arxiv.org/abs/2610.18853
canonical_url: https://arxiv.org/abs/2610.18853
captured_by: auto-scanner
date: '2026-10-14'
captured_at: '2026-10-14T09:53:53+00:00'
last_requested: '2026-10-14T09:53:53+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Yuante Li
- Junwei Quan
- Kai Qiu
- Kate Zhang
- Yicheng Tao
published: '2026-10-13'
abstract: 'Reinforcement learning with verifiable rewards (RLVR) relies on costly
  model-generated responses, motivating larger rollout batches and square-root learning-rate
  scaling. Reported to approximately preserve progress per sample with one optimizer
  step per rollout, this rule is less understood in practical multi-step training.
  We develop a two-clock framework that separates the samples needed to make progress
  from those consumed before collapse. Under a local quadratic model, the square-root
  rule preserves first-order drift per sample but not progress: larger batches take
  fewer, longer updates and lose more to curvature, yielding a learning-rate-dependent
  critical batch beyond which sample efficiency degrades. A drift-threshold hypothesis
  predicts a complementary failure clock whose sample count remains approximately
  invariant along the square-root rule. Controlled GRPO experiments on Qwen2.5-Math-1.5B
  across a $16\times$ batch range support both predictions. Ratio clipping delays
  failure, especially for larger batches, but the progress gap persists without it.
  Widening the clip trades stability for a transient speed gain. The progress gap
  reappears on another dataset, a general-purpose checkpoint, and a 7B model. Finally,
  we use the two-clock framework to derive a simple multi-step RLVR schedule: start
  below the critical batch and switch to a larger batch before failure. Our code is
  available at: https://github.com/WinstonLiyt/two-clocks-rlvr.'
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.18853'
  categories:
  - cs.LG
  - cs.AI
---

# Two Clocks: Why Larger Rollout Batches Learn Slower but Fail on Schedule in Reinforcement Learning with Verifiable Rewards

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.18853
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Yuante Li, Junwei Quan, Kai Qiu, Kate Zhang, Yicheng Tao
- **Published:** 2026-10-13

## Summary
Reinforcement learning with verifiable rewards (RLVR) relies on costly model-generated responses, motivating larger rollout batches and square-root learning-rate scaling. Reported to approximately preserve progress per sample with one optimizer step per rollout, this rule is less understood in practical multi-step training. We develop a two-clock framework that separates the samples needed to make progress from those consumed before collapse. Under a local quadratic model, the square-root rule preserves first-order drift per sample but not progress: larger batches take fewer, longer updates and lose more to curvature, yielding a learning-rate-dependent critical batch beyond which sample efficiency degrades. A drift-threshold hypothesis predicts a complementary failure clock whose sample count remains approximately invariant along the square-root rule. Controlled GRPO experiments on Qwen2.5-Math-1.5B across a $16\times$ batch range support both predictions. Ratio clipping delays failure, especially for larger batches, but the progress gap persists without it. Widening the clip trades stability for a transient speed gain. The progress gap reappears on another dataset, a general-purpose checkpoint, and a 7B model. Finally, we use the two-clock framework to derive a simple multi-step RLVR schedule: start below the critical batch and switch to a larger batch before failure. Our code is available at: https://github.com/WinstonLiyt/two-clocks-rlvr.

## Provider details
- **Arxiv Id:** 2610.18853
- **Categories:** ["cs.LG", "cs.AI"]
