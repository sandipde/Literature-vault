---
title: Completing analytical conversion scheme among DH, Hayati, CPC and POE models
  for manipulator calibration
type: arxiv
source: https://arxiv.org/abs/2611.31054
canonical_url: https://arxiv.org/abs/2611.31054
captured_by: auto-scanner
date: '2026-11-24'
captured_at: '2026-11-24T15:29:01+00:00'
last_requested: '2026-11-24T15:29:01+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Oleg Yu. Sumenkov
- Danil D. Kulminskiy
- Sergei V. Gusev
published: '2026-11-23'
abstract: 'Building on Mooring''s decomposition of the calibration procedure into
  four stages - modeling, measurement, identification, and correction - this paper
  investigates the role of analytical kinematic model conversion algorithms within
  the calibration framework and their potential to improve calibration performance.
  Four prominent and widely cited kinematic models: Denavit-Hartenberg (DH), Hayati
  (HAY), Complete and Parametrically Continuous (CPC), and Product of Exponentials
  (POE), - are considered. A systematic analysis of the existing conversion relationships
  reveals that, although most conversions among these models have already been established
  in the literature, a direct analytical conversion between POE and HAY, and CPC and
  HAY remains unavailable. Relying instead on a sequential combination of the existing
  POE-DH and DH-HAY conversions, for example, introduces several limitations. To address
  this gap, we develop a constructive analytical conversion between POE-HAY and HAY-CPC
  models based on Lie group theory, formally established through a set of lemmas and
  propositions. The proposed algorithms are illustrated using an RRRP SCARA robot
  and an RRHHHH Puma 560 manipulator. The direct POE-HAY conversion is compared with
  the sequential POE-DH-HAY approach, as well as HAY-CPC in terms of several relevant
  criteria, demonstrating the advantages of the proposed solution. Finally, we demonstrate
  the practical significance of the completed analytical conversion framework in an
  open-loop kinematic calibration experiment on an ABB IRB 1600 manipulator, using
  an API Radian EMSD3 Laser Tracker for measurements. The experimental results demonstrate
  that proper model selection combined with completed analytical conversion scheme
  directly improves calibration accuracy.'
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.31054'
  categories:
  - cs.RO
---

# Completing analytical conversion scheme among DH, Hayati, CPC and POE models for manipulator calibration

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.31054
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Oleg Yu. Sumenkov, Danil D. Kulminskiy, Sergei V. Gusev
- **Published:** 2026-11-23

## Summary
Building on Mooring's decomposition of the calibration procedure into four stages - modeling, measurement, identification, and correction - this paper investigates the role of analytical kinematic model conversion algorithms within the calibration framework and their potential to improve calibration performance. Four prominent and widely cited kinematic models: Denavit-Hartenberg (DH), Hayati (HAY), Complete and Parametrically Continuous (CPC), and Product of Exponentials (POE), - are considered. A systematic analysis of the existing conversion relationships reveals that, although most conversions among these models have already been established in the literature, a direct analytical conversion between POE and HAY, and CPC and HAY remains unavailable. Relying instead on a sequential combination of the existing POE-DH and DH-HAY conversions, for example, introduces several limitations. To address this gap, we develop a constructive analytical conversion between POE-HAY and HAY-CPC models based on Lie group theory, formally established through a set of lemmas and propositions. The proposed algorithms are illustrated using an RRRP SCARA robot and an RRHHHH Puma 560 manipulator. The direct POE-HAY conversion is compared with the sequential POE-DH-HAY approach, as well as HAY-CPC in terms of several relevant criteria, demonstrating the advantages of the proposed solution. Finally, we demonstrate the practical significance of the completed analytical conversion framework in an open-loop kinematic calibration experiment on an ABB IRB 1600 manipulator, using an API Radian EMSD3 Laser Tracker for measurements. The experimental results demonstrate that proper model selection combined with completed analytical conversion scheme directly improves calibration accuracy.

## Provider details
- **Arxiv Id:** 2611.31054
- **Categories:** ["cs.RO"]
