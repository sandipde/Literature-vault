---
title: 'Learning to Disassemble: Safety-Aware Simulation-Based Reinforcement Learning
  for Robotic Re-Manufacturing'
type: paper
source: https://doi.org/10.1115/msec2026-182806
canonical_url: https://doi.org/10.1115/msec2026-182806
captured_by: auto-scanner
date: '2026-11-05'
captured_at: '2026-11-05T12:53:59+00:00'
last_requested: '2026-11-05T12:53:59+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Safkat Shahrier Swapnil
- Sara Behdad
published: '2026-06-14'
abstract: Abstract Remanufacturing operations face uncertainty in incoming products
  due to variations in wear, geometry, and assembly conditions. Robotic remanufacturing
  provides a promising solution to improve consistency and worker safety; however,
  it requires systems that can process diverse and unpredictable product states. To
  address this challenge, this work presents a physics-informed reinforcement learning
  (RL) framework in Py-Bullet for a UR5e manipulator equipped with a suction end-effector
  that learns safe electronic part extraction and binning under physical uncertainty.
  The task is modeled as a continuous-control Markov Decision Process (MDP) with a
  compact 10-D observation and a 4-D Cartesian delta action with suction activation.
  To operationalize safety, this study introduces a composite reward that penalizes
  shear force, force-rate, and collisions, in addition to preserving a sparse success
  bonus that requires actual bond fracture and placement. Robustness is promoted through
  procedural PCB generation and material-property domain randomization that injects
  damage zones, representing oily contamination (low friction) and corrosion (higher
  break force). A shrinking-tolerance curriculum mitigates exploration paralysis by
  guiding policies from coarse approach to sub-millimeter alignment before full fracture
  difficulty. We benchmark three RL algorithms including Proximal Policy Optimization
  (PPO), Soft Actor-Critic (SAC), and Twin Delayed Deep Deterministic Policy Gradient
  (TD3). Results show that the simulator reproduces elastic loading followed by detachment-induced
  recoil. Safety shaping improves both success and interaction quality, and domain
  randomization provides consistent high success for nominal and degraded environments.
  Local, sliding-window perception supports the same policy to scale from sparse boards
  to cluttered boards with many electronic parts without increasing observation size.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1115/msec2026-182806
  journal: 'Volume 2: Manufacturing Equipment and Automation; Manufacturing Processes;
    Manufacturing Systems; Nano/Micro/Meso Manufacturing; Quality and Reliability'
  publisher: American Society of Mechanical Engineers
  type: proceedings-article
  subjects: []
---

# Learning to Disassemble: Safety-Aware Simulation-Based Reinforcement Learning for Robotic Re-Manufacturing

- **Type:** paper
- **Source:** https://doi.org/10.1115/msec2026-182806
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Safkat Shahrier Swapnil, Sara Behdad
- **Published:** 2026-06-14

## Summary
Abstract Remanufacturing operations face uncertainty in incoming products due to variations in wear, geometry, and assembly conditions. Robotic remanufacturing provides a promising solution to improve consistency and worker safety; however, it requires systems that can process diverse and unpredictable product states. To address this challenge, this work presents a physics-informed reinforcement learning (RL) framework in Py-Bullet for a UR5e manipulator equipped with a suction end-effector that learns safe electronic part extraction and binning under physical uncertainty. The task is modeled as a continuous-control Markov Decision Process (MDP) with a compact 10-D observation and a 4-D Cartesian delta action with suction activation. To operationalize safety, this study introduces a composite reward that penalizes shear force, force-rate, and collisions, in addition to preserving a sparse success bonus that requires actual bond fracture and placement. Robustness is promoted through procedural PCB generation and material-property domain randomization that injects damage zones, representing oily contamination (low friction) and corrosion (higher break force). A shrinking-tolerance curriculum mitigates exploration paralysis by guiding policies from coarse approach to sub-millimeter alignment before full fracture difficulty. We benchmark three RL algorithms including Proximal Policy Optimization (PPO), Soft Actor-Critic (SAC), and Twin Delayed Deep Deterministic Policy Gradient (TD3). Results show that the simulator reproduces elastic loading followed by detachment-induced recoil. Safety shaping improves both success and interaction quality, and domain randomization provides consistent high success for nominal and degraded environments. Local, sliding-window perception supports the same policy to scale from sparse boards to cluttered boards with many electronic parts without increasing observation size.

## Provider details
- **Doi:** 10.1115/msec2026-182806
- **Journal:** Volume 2: Manufacturing Equipment and Automation; Manufacturing Processes; Manufacturing Systems; Nano/Micro/Meso Manufacturing; Quality and Reliability
- **Publisher:** American Society of Mechanical Engineers
- **Type:** proceedings-article
