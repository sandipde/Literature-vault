---
title: 'Continual-ARC: Measuring Skill Acquisition over a Working Lifetime'
type: arxiv
source: https://arxiv.org/abs/2611.14505
canonical_url: https://arxiv.org/abs/2611.14505
captured_by: auto-scanner
date: '2026-11-11'
captured_at: '2026-11-11T12:22:55+00:00'
last_requested: '2026-11-11T12:22:55+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Daniel Lenton
published: '2026-11-10'
abstract: 'Agent harnesses have emerged as a promising mechanism for continual learning,
  alongside test-time parametric learning. However, the current benchmarks have several
  limitations: they generally focus on a single applied domain, serve each instance
  only once, and assume a single family of learner, so memory-based and weight-based
  systems are rarely compared on the same scale. We propose Continual-ARC, a lifelong
  stream built from the three ARC-AGI editions, whose tasks need no domain knowledge.
  The same tasks return after dormant gaps with fresh instances, while new tasks keep
  arriving. On each instance, the learner may pay for demonstrations, submit answers,
  or act inside the harness, with retries permitted on incorrect submissions, which
  are paid for. Each instance is scored based on the share of this feedback budget
  consumed. Since a learner may keep anything between instances, memory-based and
  weight-based systems are scored on the same scale. After the stream, the learner
  is frozen and tested on fresh instances of the tasks it met, which measures memorization,
  and on unseen tasks, which measures generalization. We run an agent harness with
  frozen weights, with and without persistence, on Qwen3.5-9B and GLM-5.3 Flash, comparing
  them with two prompting floors, a program-induction method and Qwen3.5-9B''s weights
  trained to imitate GLM-5.3 Flash. Persistence in the harness generally does not
  improve memorization unless provided with explicit expert guidance. Most harness-based
  methods still learn less than a floor that simply caches each task''s demonstrations,
  across all models we tested. No harness-based method gains on unseen tasks, whereas
  weight-based learning shows substantial gains. This opens the door to future weight-based
  continual learning that could teach models to drive harnesses in new domains.'
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.14505'
  categories:
  - cs.LG
---

# Continual-ARC: Measuring Skill Acquisition over a Working Lifetime

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.14505
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Daniel Lenton
- **Published:** 2026-11-10

## Summary
Agent harnesses have emerged as a promising mechanism for continual learning, alongside test-time parametric learning. However, the current benchmarks have several limitations: they generally focus on a single applied domain, serve each instance only once, and assume a single family of learner, so memory-based and weight-based systems are rarely compared on the same scale. We propose Continual-ARC, a lifelong stream built from the three ARC-AGI editions, whose tasks need no domain knowledge. The same tasks return after dormant gaps with fresh instances, while new tasks keep arriving. On each instance, the learner may pay for demonstrations, submit answers, or act inside the harness, with retries permitted on incorrect submissions, which are paid for. Each instance is scored based on the share of this feedback budget consumed. Since a learner may keep anything between instances, memory-based and weight-based systems are scored on the same scale. After the stream, the learner is frozen and tested on fresh instances of the tasks it met, which measures memorization, and on unseen tasks, which measures generalization. We run an agent harness with frozen weights, with and without persistence, on Qwen3.5-9B and GLM-5.3 Flash, comparing them with two prompting floors, a program-induction method and Qwen3.5-9B's weights trained to imitate GLM-5.3 Flash. Persistence in the harness generally does not improve memorization unless provided with explicit expert guidance. Most harness-based methods still learn less than a floor that simply caches each task's demonstrations, across all models we tested. No harness-based method gains on unseen tasks, whereas weight-based learning shows substantial gains. This opens the door to future weight-based continual learning that could teach models to drive harnesses in new domains.

## Provider details
- **Arxiv Id:** 2611.14505
- **Categories:** ["cs.LG"]
