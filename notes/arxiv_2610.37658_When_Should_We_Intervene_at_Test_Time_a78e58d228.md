---
title: When Should We Intervene at Test Time?
type: arxiv
source: https://arxiv.org/abs/2610.37658
canonical_url: https://arxiv.org/abs/2610.37658
captured_by: auto-scanner
date: '2026-10-28'
captured_at: '2026-10-28T10:56:07+00:00'
last_requested: '2026-10-28T10:56:07+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Jiahao Zhang
- Xinling Wen
- Liangliang Li
- Yu Chen
published: '2026-10-27'
abstract: Test-time adaptation helps a deployed model respond to changing inputs,
  but the same intervention can rescue one batch and damage the next. Updating normalization
  statistics, for example, can improve corrupted images yet fail when a batch contains
  mostly one class. Average accuracy hides these failures and cannot tell a model
  when to use an intervention. Target labels can guide this decision, but they are
  scarce and some choices are already clear. We introduce PORTAL, a controller that
  chooses when to deploy an intervention, which inputs to label, and when to stop
  querying. Each available prediction rule is a candidate, and its predictions are
  fixed before current feedback arrives. Every acquired label therefore evaluates
  all candidates on the same input. PORTAL combines these shared comparisons and directs
  queries toward candidates that can still overtake the current leader. It stops when
  the remaining labels cannot change the choice or when the possible accuracy gain
  no longer justifies another query. Our analysis links the required feedback to accuracy
  gaps and shared mistakes, explaining why some choices need much less evidence. Experiments
  show that this control turns an intervention that loses accuracy overall into a
  useful choice on selected batches. It prevents severe failures caused by changes
  in arrival order and preserves gains across complete corruption streams. When a
  fixed rule already works well, PORTAL uses little feedback to retain its performance.
  Periodic label checks reveal when past evidence needs refreshing and help the controller
  recover as conditions change. The acquired labels also train stronger candidates
  for future batches, and selection brings nearly all of their accuracy gains into
  deployment. The same feedback therefore improves both the choice made now and the
  predictions available to later batches.
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2610.37658'
  categories:
  - cs.LG
---

# When Should We Intervene at Test Time?

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2610.37658
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Jiahao Zhang, Xinling Wen, Liangliang Li, Yu Chen
- **Published:** 2026-10-27

## Summary
Test-time adaptation helps a deployed model respond to changing inputs, but the same intervention can rescue one batch and damage the next. Updating normalization statistics, for example, can improve corrupted images yet fail when a batch contains mostly one class. Average accuracy hides these failures and cannot tell a model when to use an intervention. Target labels can guide this decision, but they are scarce and some choices are already clear. We introduce PORTAL, a controller that chooses when to deploy an intervention, which inputs to label, and when to stop querying. Each available prediction rule is a candidate, and its predictions are fixed before current feedback arrives. Every acquired label therefore evaluates all candidates on the same input. PORTAL combines these shared comparisons and directs queries toward candidates that can still overtake the current leader. It stops when the remaining labels cannot change the choice or when the possible accuracy gain no longer justifies another query. Our analysis links the required feedback to accuracy gaps and shared mistakes, explaining why some choices need much less evidence. Experiments show that this control turns an intervention that loses accuracy overall into a useful choice on selected batches. It prevents severe failures caused by changes in arrival order and preserves gains across complete corruption streams. When a fixed rule already works well, PORTAL uses little feedback to retain its performance. Periodic label checks reveal when past evidence needs refreshing and help the controller recover as conditions change. The acquired labels also train stronger candidates for future batches, and selection brings nearly all of their accuracy gains into deployment. The same feedback therefore improves both the choice made now and the predictions available to later batches.

## Provider details
- **Arxiv Id:** 2610.37658
- **Categories:** ["cs.LG"]
