---
title: Fast contracted Clebsch-Gordan tensor products for equivariant graph neural
  networks
type: paper
source: https://doi.org/10.1088/2632-2153/aec40f
canonical_url: https://doi.org/10.1088/2632-2153/aec40f
captured_by: auto-scanner
date: '2026-11-19'
captured_at: '2026-11-19T14:04:33+00:00'
last_requested: '2026-11-19T14:04:33+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Anton Bochkarev
- Yury Vyatcheslavovich Lysogorskiy
- Ralf Drautz
published: '2026-11-18'
abstract: Abstract We present an algorithm with an O(L3) operation count for evaluating
  contracted Clebsch–Gordan tensor products in O(3)-equivariant machine learning potentials
  at fixed Canonical Polyadic (CP) rank. Mapping the angular integral to a structured
  Gauss–Legendre and Fourier tensor-product grid decouples the radial channel contractions
  from the angular transforms. The antisymmetric parity- odd Clebsch–Gordan channels,
  unreachable by the symmetric pointwise product on a scalar S2 grid, are recovered
  through the surface-curl pairing ˆ r·[∇S2 A×∇S2 B], the spherical Poisson bracket,
  which supplies the L = 1 angular momentum on the grid while preserving rotational
  equivariance. The construction extends to parity-aware equivariant message passing
  in architectures of the atomic cluster expansion family and is verified by direct
  numerical quadrature. The full uncontracted Clebsch–Gordan tensor product remains
  subject to the O(L4) output-size lower bound. Benchmarks show wall-clock scaling
  approximately as L2 for both operations over the whole range measured, with the
  runtime on the tested GPU set by data movement on the L2-sized grid tensors rather
  than by the L3 arithmetic.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1088/2632-2153/aec40f
  journal: 'Machine Learning: Science and Technology'
  publisher: IOP Publishing
  type: journal-article
  subjects: []
---

# Fast contracted Clebsch-Gordan tensor products for equivariant graph neural networks

- **Type:** paper
- **Source:** https://doi.org/10.1088/2632-2153/aec40f
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Anton Bochkarev, Yury Vyatcheslavovich Lysogorskiy, Ralf Drautz
- **Published:** 2026-11-18

## Summary
Abstract We present an algorithm with an O(L3) operation count for evaluating contracted Clebsch–Gordan tensor products in O(3)-equivariant machine learning potentials at fixed Canonical Polyadic (CP) rank. Mapping the angular integral to a structured Gauss–Legendre and Fourier tensor-product grid decouples the radial channel contractions from the angular transforms. The antisymmetric parity- odd Clebsch–Gordan channels, unreachable by the symmetric pointwise product on a scalar S2 grid, are recovered through the surface-curl pairing ˆ r·[∇S2 A×∇S2 B], the spherical Poisson bracket, which supplies the L = 1 angular momentum on the grid while preserving rotational equivariance. The construction extends to parity-aware equivariant message passing in architectures of the atomic cluster expansion family and is verified by direct numerical quadrature. The full uncontracted Clebsch–Gordan tensor product remains subject to the O(L4) output-size lower bound. Benchmarks show wall-clock scaling approximately as L2 for both operations over the whole range measured, with the runtime on the tested GPU set by data movement on the L2-sized grid tensors rather than by the L3 arithmetic.

## Provider details
- **Doi:** 10.1088/2632-2153/aec40f
- **Journal:** Machine Learning: Science and Technology
- **Publisher:** IOP Publishing
- **Type:** journal-article
