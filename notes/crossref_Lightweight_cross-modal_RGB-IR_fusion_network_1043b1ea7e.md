---
title: Lightweight cross-modal RGB-IR fusion network for real-time aerial surveillance
type: paper
source: https://doi.org/10.1007/s00521-026-12529-7
canonical_url: https://doi.org/10.1007/s00521-026-12529-7
captured_by: auto-scanner
date: '2026-11-09'
captured_at: '2026-11-09T13:33:43+00:00'
last_requested: '2026-11-09T13:33:43+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Nadin Habash
- Ahmad Abu Alqumsan
- Tao Zhou
published: 2026-11
abstract: Abstract Real-time onboard object detection is essential for autonomous
  UAV applications requiring rapid and reliable decision-making in dynamic environments.
  Most existing onboard detectors rely on RGB imagery due to its computational efficiency;
  however, RGB-based models suffer significant performance degradation under low-illumination
  conditions. Although recent RGB–infrared (RGB–IR) fusion approaches enhance detection
  by leveraging complementary thermal information, they often employ complex architectures
  that introduce feature redundancy, and high computational overhead, limiting their
  suitability for real-time edge deployment. To address these limitations, this paper
  proposes a lightweight RGB–IR object detection framework for real-time onboard aerial
  applications. A guided difference-based fusion mechanism is introduced to adaptively
  balance RGB and IR contributions while reducing cross-modal redundancy. Additionally,
  a lightweight variant of the FasterNet module is developed to improve feature extraction
  efficiency, particularly within the backbone, which dominates inference cost. The
  results demonstrate its efficiency on three aerial multimodal datasets, DroneVehicle,
  VEDAI and RGBT-Tiny for small objects for surveillance applications. The proposed
  model achieves 93.0% mAP50 on VEDAI and 78% mAP50 on DroneVehicle. With only 2.74M
  parameters, it runs at 2.9 ms per image on an RTX 4080 and achieves 35.71 FPS on
  Jetson Orin AGX and 26.3 FPS on Jetson Orin Nano, with 5.6 MB network size, validating
  its effectiveness for edge UAV deployment.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1007/s00521-026-12529-7
  journal: Neural Computing and Applications
  publisher: Springer Science and Business Media LLC
  type: journal-article
  subjects: []
---

# Lightweight cross-modal RGB-IR fusion network for real-time aerial surveillance

- **Type:** paper
- **Source:** https://doi.org/10.1007/s00521-026-12529-7
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Nadin Habash, Ahmad Abu Alqumsan, Tao Zhou
- **Published:** 2026-11

## Summary
Abstract Real-time onboard object detection is essential for autonomous UAV applications requiring rapid and reliable decision-making in dynamic environments. Most existing onboard detectors rely on RGB imagery due to its computational efficiency; however, RGB-based models suffer significant performance degradation under low-illumination conditions. Although recent RGB–infrared (RGB–IR) fusion approaches enhance detection by leveraging complementary thermal information, they often employ complex architectures that introduce feature redundancy, and high computational overhead, limiting their suitability for real-time edge deployment. To address these limitations, this paper proposes a lightweight RGB–IR object detection framework for real-time onboard aerial applications. A guided difference-based fusion mechanism is introduced to adaptively balance RGB and IR contributions while reducing cross-modal redundancy. Additionally, a lightweight variant of the FasterNet module is developed to improve feature extraction efficiency, particularly within the backbone, which dominates inference cost. The results demonstrate its efficiency on three aerial multimodal datasets, DroneVehicle, VEDAI and RGBT-Tiny for small objects for surveillance applications. The proposed model achieves 93.0% mAP50 on VEDAI and 78% mAP50 on DroneVehicle. With only 2.74M parameters, it runs at 2.9 ms per image on an RTX 4080 and achieves 35.71 FPS on Jetson Orin AGX and 26.3 FPS on Jetson Orin Nano, with 5.6 MB network size, validating its effectiveness for edge UAV deployment.

## Provider details
- **Doi:** 10.1007/s00521-026-12529-7
- **Journal:** Neural Computing and Applications
- **Publisher:** Springer Science and Business Media LLC
- **Type:** journal-article
