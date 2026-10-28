---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Mathematics and algorithms
enrichment_tags: [fermi-operator-expansion, density-matrices, gpu-computing, finite-temperature]
title: Machine-learned, finite temperature Fermi-operator expansions suitable for
  GPUs and AI-hardware
type: paper
source: https://doi.org/10.1063/5.0347394
canonical_url: https://doi.org/10.1063/5.0347394
captured_by: auto-scanner
date: '2026-10-15'
captured_at: '2026-10-15T09:34:27+00:00'
last_requested: '2026-10-15T09:34:27+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Stanislaw Kowalski
- Christian F. A. Negre
- Anders M. N. Niklasson
- Kipton Barros
- Joshua Finkelstein
published: '2026-10-14'
abstract: We present several finite-temperature recursive Fermi–operator expansion
  schemes based on the second-order spectral projection (SP2) method. Our approach
  builds on a previous observation that the electronic structure problem, as formulated
  through a recursive SP2 expansion, can be mapped onto the architecture of a deep
  neural network. Using this perspective, we generalize SP2 to finite electronic temperatures
  by constructing machine learning models that determine optimized recursive expansion
  coefficients. The same approach is also applied to the prediction of the electronic
  entropy for fractional occupation numbers. The coefficients are trained for a specified
  chemical potential and electronic temperature and are not available in closed analytical
  form. However, by employing an appropriate affine rescaling strategy to the Hamiltonian
  matrix, we eliminate the need to retrain the model for different temperatures and
  chemical potentials. Our approach avoids explicit diagonalization and relies solely
  on highly optimized matrix–matrix multiplication kernels. Compared to state-of-the-art
  diagonalization, we achieve an order-of-magnitude speedup in the single-particle
  finite-temperature density matrix calculation for small and moderately sized matrices
  on modern graphics processing units and dense matrix multiply units.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1063/5.0347394
  journal: The Journal of Chemical Physics
  publisher: AIP Publishing
  type: journal-article
  subjects: []
---

# Machine-learned, finite temperature Fermi-operator expansions suitable for GPUs and AI-hardware

- **Type:** paper
- **Source:** https://doi.org/10.1063/5.0347394
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Stanislaw Kowalski, Christian F. A. Negre, Anders M. N. Niklasson, Kipton Barros, Joshua Finkelstein
- **Published:** 2026-10-14

## Summary
We present several finite-temperature recursive Fermi–operator expansion schemes based on the second-order spectral projection (SP2) method. Our approach builds on a previous observation that the electronic structure problem, as formulated through a recursive SP2 expansion, can be mapped onto the architecture of a deep neural network. Using this perspective, we generalize SP2 to finite electronic temperatures by constructing machine learning models that determine optimized recursive expansion coefficients. The same approach is also applied to the prediction of the electronic entropy for fractional occupation numbers. The coefficients are trained for a specified chemical potential and electronic temperature and are not available in closed analytical form. However, by employing an appropriate affine rescaling strategy to the Hamiltonian matrix, we eliminate the need to retrain the model for different temperatures and chemical potentials. Our approach avoids explicit diagonalization and relies solely on highly optimized matrix–matrix multiplication kernels. Compared to state-of-the-art diagonalization, we achieve an order-of-magnitude speedup in the single-particle finite-temperature density matrix calculation for small and moderately sized matrices on modern graphics processing units and dense matrix multiply units.

## Provider details
- **Doi:** 10.1063/5.0347394
- **Journal:** The Journal of Chemical Physics
- **Publisher:** AIP Publishing
- **Type:** journal-article

## AI enrichment
- **Concise summary:** Learned recursive coefficients extend SP2 Fermi-operator expansions to finite temperature and electronic entropy, using affine Hamiltonian rescaling across temperatures and chemical potentials. The method replaces explicit diagonalization with matrix-multiplication kernels.
- **Why it matters:** Reformulating electronic-structure work for dense matrix hardware can accelerate a solver kernel independently of any force-field surrogate.
- **Caveat:** Reported speedups are unverified and concern small-to-moderate matrices on specified accelerator classes; they do not imply an order-of-magnitude speedup for an entire self-consistent calculation.
- **Evidence:** [Captured source](https://doi.org/10.1063/5.0347394); analysis based only on captured metadata, not independently verified full text.
