---
title: Assessment of honey samples from Nigerian markets using FTIR spectroscopy and
  machine learning
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011888/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011888/v1
captured_by: auto-scanner
date: '2026-11-10'
captured_at: '2026-11-10T13:12:34+00:00'
last_requested: '2026-11-10T13:12:34+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Godwill Charles
published: '2026-11-10'
abstract: Honey adulteration with cheaper sugars is a concern in Nigerian markets,
  where conventional tests are slow, costly, and not widely accessible. This study
  assessed whether Fourier-transform infrared (FTIR) spectroscopy combined with machine
  learning can screen honey for added sugar, and whether such a model can be applied
  to honey sold in Nigerian markets. A Random Forest classifier was trained on a public
  FTIR dataset of 16 honeys, each measured pure and with 10, 20, and 40% added sugar.
  It was compared with PLS-DA, logistic regression, and a support vector machine.
  Models were tested by leave-one-honey-out cross-validation, so each honey was always
  predicted by a model that had never seen it. ATR-FTIR spectra were also recorded
  for 11 honeys purchased from Nigerian markets. Random Forest reached balanced accuracy
  of 0.70–0.71 and AUC of 0.80–0.87 across three pre-processing methods; Random Forest
  and PLS-DA together ranged from 0.64 to 0.76 (balanced accuracy) and 0.72 to 0.87
  (AUC). Most adulterated spectra were detected, even at 10% added sugar, but about
  half of the pure honeys were also flagged. The amount of added sugar could not be
  estimated (RMSECV 12.2 percentage points). The most informative bands lay in the
  carbohydrate fingerprint region (near 1365, 1031, 902, and 818 cm-1, stable across
  validation rounds). After ATR and baseline correction, the market honeys closely
  resembled the training honeys (r = 0.965), but they lay outside the range of spectra
  the model was trained on, so they could not be classified reliably. A leakage-prone
  test, with augmentation before a random split, gave 0.87 balanced accuracy, against
  0.70 when augmentation was kept inside the training data and each honey was held
  out, showing how test design can inflate reported results. These results support
  further evaluation of FTIR with machine learning as a rapid screen, but a local
  calibration set of Nigerian honeys is needed before market samples can be judged.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011888/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Assessment of honey samples from Nigerian markets using FTIR spectroscopy and machine learning

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011888/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Godwill Charles
- **Published:** 2026-11-10

## Summary
Honey adulteration with cheaper sugars is a concern in Nigerian markets, where conventional tests are slow, costly, and not widely accessible. This study assessed whether Fourier-transform infrared (FTIR) spectroscopy combined with machine learning can screen honey for added sugar, and whether such a model can be applied to honey sold in Nigerian markets. A Random Forest classifier was trained on a public FTIR dataset of 16 honeys, each measured pure and with 10, 20, and 40% added sugar. It was compared with PLS-DA, logistic regression, and a support vector machine. Models were tested by leave-one-honey-out cross-validation, so each honey was always predicted by a model that had never seen it. ATR-FTIR spectra were also recorded for 11 honeys purchased from Nigerian markets. Random Forest reached balanced accuracy of 0.70–0.71 and AUC of 0.80–0.87 across three pre-processing methods; Random Forest and PLS-DA together ranged from 0.64 to 0.76 (balanced accuracy) and 0.72 to 0.87 (AUC). Most adulterated spectra were detected, even at 10% added sugar, but about half of the pure honeys were also flagged. The amount of added sugar could not be estimated (RMSECV 12.2 percentage points). The most informative bands lay in the carbohydrate fingerprint region (near 1365, 1031, 902, and 818 cm-1, stable across validation rounds). After ATR and baseline correction, the market honeys closely resembled the training honeys (r = 0.965), but they lay outside the range of spectra the model was trained on, so they could not be classified reliably. A leakage-prone test, with augmentation before a random split, gave 0.87 balanced accuracy, against 0.70 when augmentation was kept inside the training data and each honey was held out, showing how test design can inflate reported results. These results support further evaluation of FTIR with machine learning as a rapid screen, but a local calibration set of Nigerian honeys is needed before market samples can be judged.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011888/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
