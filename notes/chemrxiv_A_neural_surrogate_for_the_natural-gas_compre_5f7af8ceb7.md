---
title: 'A neural surrogate for the natural-gas compressibility factor: reference-equation
  accuracy from synthetic training data alone, benchmarked on 2426 independent laboratory
  measurements'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011889/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011889/v1
captured_by: auto-scanner
date: '2026-11-10'
captured_at: '2026-11-10T13:12:34+00:00'
last_requested: '2026-11-10T13:12:34+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Emir Borovac
published: '2026-11-10'
abstract: 'The compressibility factor z of natural gas is obtained either from inexpensive
  empirical correlations or from reference equations of state that require the full
  molar composition and an iterative density solve. Machine learning has been proposed
  as a bridge, but almost all published studies are trained and tested on values digitised
  from the same 1942 chart, so their gains have never been shown on independent laboratory
  data. We assemble such a test set: 6726 gas-phase measurements from 40 publishedstudiesintheNISTThermoMLarchive,withabsolutepressure,temperatureand
  composition, from which z follows exactly. On its natural-gas domain (2426 points,
  10 laboratories) we evaluate six established methods and a residual neural surrogate
  trained only on synthetic states fromareferenceequation.Thesurrogateattainsanaverageabsolutedeviationof0.789%,
  statisticallyindistinguishablefrom AGA8-DETAIL (0.769%) and ahead ofGERG-2008 (0.917%),
  while reducing the error of the Dranchuk–Abou-Kassem, Hall–Yarborough and Dranchuk–Purvis–Robinson
  correlations by about 1.1 percentage points at all ten laboratories. Replacing the
  teaching equation whileholding states,architecture and seed fixed changes testaccuracy
  from 0.923% to 0.789%: surrogate accuracy is governed by the reference equation
  chosen to generate its labels. A search over 31 functional families shows that fitted
  residual corrections transfer for the empirical correlations but not for the reference
  equations or the surrogate.We also measure the cost such surrogatesassertratherthandemonstrate:thenetworkisslowerperstatethanthereference
  equation, and fastest only when batched on a graphics processor.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011889/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# A neural surrogate for the natural-gas compressibility factor: reference-equation accuracy from synthetic training data alone, benchmarked on 2426 independent laboratory measurements

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011889/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Emir Borovac
- **Published:** 2026-11-10

## Summary
The compressibility factor z of natural gas is obtained either from inexpensive empirical correlations or from reference equations of state that require the full molar composition and an iterative density solve. Machine learning has been proposed as a bridge, but almost all published studies are trained and tested on values digitised from the same 1942 chart, so their gains have never been shown on independent laboratory data. We assemble such a test set: 6726 gas-phase measurements from 40 publishedstudiesintheNISTThermoMLarchive,withabsolutepressure,temperatureand composition, from which z follows exactly. On its natural-gas domain (2426 points, 10 laboratories) we evaluate six established methods and a residual neural surrogate trained only on synthetic states fromareferenceequation.Thesurrogateattainsanaverageabsolutedeviationof0.789%, statisticallyindistinguishablefrom AGA8-DETAIL (0.769%) and ahead ofGERG-2008 (0.917%), while reducing the error of the Dranchuk–Abou-Kassem, Hall–Yarborough and Dranchuk–Purvis–Robinson correlations by about 1.1 percentage points at all ten laboratories. Replacing the teaching equation whileholding states,architecture and seed fixed changes testaccuracy from 0.923% to 0.789%: surrogate accuracy is governed by the reference equation chosen to generate its labels. A search over 31 functional families shows that fitted residual corrections transfer for the empirical correlations but not for the reference equations or the surrogate.We also measure the cost such surrogatesassertratherthandemonstrate:thenetworkisslowerperstatethanthereference equation, and fastest only when batched on a graphics processor.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011889/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
