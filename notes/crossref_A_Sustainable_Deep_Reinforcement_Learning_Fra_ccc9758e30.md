---
title: 'A Sustainable Deep Reinforcement Learning Framework for Personalized Learning:
  Balancing Learning Gains, Resource Efficiency, and Educational Equity: A Simulation
  Study'
type: paper
source: https://doi.org/10.3390/su182211524
canonical_url: https://doi.org/10.3390/su182211524
captured_by: auto-scanner
date: '2026-11-12'
captured_at: '2026-11-12T13:29:56+00:00'
last_requested: '2026-11-12T13:29:56+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Xiaoning Xie
- Norzaini Azman
- Mohamad Nizam Nazarudin
published: '2026-11-12'
abstract: This study is a fully synthetic simulation study; no real-student data are
  used. Personalized learning systems must balance achievement, resource use, and
  equity. We examine a deep reinforcement learning formulation motivated by Sustainable
  Development Goal 4. A shared agent selects among six instructional actions for 500
  synthetic students over 80 timesteps. The student model combines difficulty matching,
  engagement-dependent learning, and forgetting. A five-term reward incorporates learning
  gain, engagement, time cost, resource consumption, and remedial fairness. In the
  main comparison, a Deep Q-Network (DQN) and a Proximal Policy Optimization agent
  trained for 200 episodes are evaluated against tabular Q-learning, a rule-based
  policy, and random selection over 20 episodes. DQN attains the highest composite
  reward (2.428) and the lowest resource use (56.21 simulation units per student).
  Its normalized gain (0.685) is slightly below that of random selection (0.704),
  while its gain and equity per unit of resource are the highest (0.0122 and 0.0141);
  random selection lifts initially low-performing students most. Because the reward
  explicitly penalizes resource use and the learned policy concentrates on low-cost
  actions, the composite-reward ranking should be read together with the underlying
  metrics rather than as an independent achievement advantage. The fairness term optimizes
  a bottom-quartile-to-median gap reduction, which is distinct from the dispersion-based
  equity index used in evaluation; the two measures are reported side by side and
  are not used interchangeably. Further analyses vary the reward, the learner model,
  and the training budget, and show that the rankings shift with the objective and
  with the simulated learning dynamics. A robustness block conducted with a documented
  re-implementation—the primary experimental record of this study—adds independent
  five-seed training runs, stronger static comparators, and reward-definition controls.
  Under repeated training, the three learned policies are descriptively close on learning
  gain, so the original single-run DQN–PPO separation is not reproduced; a myopic
  cost-aware greedy comparator that exploits the same reward information without learning
  attains higher gain, lower resource use, and higher equity than every learned policy.
  In this calibrated simulator the sequential reinforcement learning component therefore
  has no demonstrated advantage over short-sighted exploitation of the same objective.
  The study’s contribution is accordingly the formulation itself—making the learning,
  engagement, time, resource, and fairness trade-offs explicit and measurable—together
  with a reproducible diagnostic record of how strongly the conclusions depend on
  the reward design and the simulated learner dynamics; effectiveness with real students
  remains untested.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.3390/su182211524
  journal: Sustainability
  publisher: MDPI AG
  type: journal-article
  subjects: []
---

# A Sustainable Deep Reinforcement Learning Framework for Personalized Learning: Balancing Learning Gains, Resource Efficiency, and Educational Equity: A Simulation Study

- **Type:** paper
- **Source:** https://doi.org/10.3390/su182211524
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Xiaoning Xie, Norzaini Azman, Mohamad Nizam Nazarudin
- **Published:** 2026-11-12

## Summary
This study is a fully synthetic simulation study; no real-student data are used. Personalized learning systems must balance achievement, resource use, and equity. We examine a deep reinforcement learning formulation motivated by Sustainable Development Goal 4. A shared agent selects among six instructional actions for 500 synthetic students over 80 timesteps. The student model combines difficulty matching, engagement-dependent learning, and forgetting. A five-term reward incorporates learning gain, engagement, time cost, resource consumption, and remedial fairness. In the main comparison, a Deep Q-Network (DQN) and a Proximal Policy Optimization agent trained for 200 episodes are evaluated against tabular Q-learning, a rule-based policy, and random selection over 20 episodes. DQN attains the highest composite reward (2.428) and the lowest resource use (56.21 simulation units per student). Its normalized gain (0.685) is slightly below that of random selection (0.704), while its gain and equity per unit of resource are the highest (0.0122 and 0.0141); random selection lifts initially low-performing students most. Because the reward explicitly penalizes resource use and the learned policy concentrates on low-cost actions, the composite-reward ranking should be read together with the underlying metrics rather than as an independent achievement advantage. The fairness term optimizes a bottom-quartile-to-median gap reduction, which is distinct from the dispersion-based equity index used in evaluation; the two measures are reported side by side and are not used interchangeably. Further analyses vary the reward, the learner model, and the training budget, and show that the rankings shift with the objective and with the simulated learning dynamics. A robustness block conducted with a documented re-implementation—the primary experimental record of this study—adds independent five-seed training runs, stronger static comparators, and reward-definition controls. Under repeated training, the three learned policies are descriptively close on learning gain, so the original single-run DQN–PPO separation is not reproduced; a myopic cost-aware greedy comparator that exploits the same reward information without learning attains higher gain, lower resource use, and higher equity than every learned policy. In this calibrated simulator the sequential reinforcement learning component therefore has no demonstrated advantage over short-sighted exploitation of the same objective. The study’s contribution is accordingly the formulation itself—making the learning, engagement, time, resource, and fairness trade-offs explicit and measurable—together with a reproducible diagnostic record of how strongly the conclusions depend on the reward design and the simulated learner dynamics; effectiveness with real students remains untested.

## Provider details
- **Doi:** 10.3390/su182211524
- **Journal:** Sustainability
- **Publisher:** MDPI AG
- **Type:** journal-article
