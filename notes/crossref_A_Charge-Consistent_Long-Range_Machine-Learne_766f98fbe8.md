---
title: A Charge-Consistent Long-Range Machine-Learned Interatomic Potential Compatible
  with Quantum Linear System Algorithms
type: paper
source: https://doi.org/10.1021/acs.jctc.6c01621
canonical_url: https://doi.org/10.1021/acs.jctc.6c01621
captured_by: auto-scanner
date: '2026-11-12'
captured_at: '2026-11-12T13:29:56+00:00'
last_requested: '2026-11-12T13:29:56+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Da Bean Han
- Hyun Woo Kim
published: '2026-11-12'
abstract: Abstract Charge equilibration in machine-learned interatomic potentials
  (MLIPs) requires repeatedly solving linear systems, providing a promising target
  for quantum linear-system algorithms (QLSAs). However, conventional electronegativity
  equalization schemes suffer from spurious fractional charges between neutral fragments
  at large separations. To address this limitation, we incorporate atom-condensed
  Kohn–Sham density functional theory approximated to second order (ACKS2) into a
  long-range equivariant neural-network MLIP. Across benchmark systems, the ACKS2-based
  model improves energy, force, and charge predictions. At a molecule–metal interface,
  ACKS2 restores molecular fragments to near-neutral charge states upon separation
  while preserving local charge redistribution near adsorption. Because ACKS2 charge
  equilibration reduces to solving a linear system, the classical solver can be directly
  replaced with the Harrow–Hassidim–Lloyd algorithm during inference, demonstrating
  compatibility with quantum linear-system solvers. These results indicate that ACKS2
  provides a promising framework for charge-aware MLIPs and highlight a potential
  pathway toward atomistic simulations based on QLSAs.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1021/acs.jctc.6c01621
  journal: 'Journal of Chemical Theory

    and Computation'
  publisher: American Chemical Society (ACS)
  type: journal-article
  subjects: []
---

# A Charge-Consistent Long-Range Machine-Learned Interatomic Potential Compatible with Quantum Linear System Algorithms

- **Type:** paper
- **Source:** https://doi.org/10.1021/acs.jctc.6c01621
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Da Bean Han, Hyun Woo Kim
- **Published:** 2026-11-12

## Summary
Abstract Charge equilibration in machine-learned interatomic potentials (MLIPs) requires repeatedly solving linear systems, providing a promising target for quantum linear-system algorithms (QLSAs). However, conventional electronegativity equalization schemes suffer from spurious fractional charges between neutral fragments at large separations. To address this limitation, we incorporate atom-condensed Kohn–Sham density functional theory approximated to second order (ACKS2) into a long-range equivariant neural-network MLIP. Across benchmark systems, the ACKS2-based model improves energy, force, and charge predictions. At a molecule–metal interface, ACKS2 restores molecular fragments to near-neutral charge states upon separation while preserving local charge redistribution near adsorption. Because ACKS2 charge equilibration reduces to solving a linear system, the classical solver can be directly replaced with the Harrow–Hassidim–Lloyd algorithm during inference, demonstrating compatibility with quantum linear-system solvers. These results indicate that ACKS2 provides a promising framework for charge-aware MLIPs and highlight a potential pathway toward atomistic simulations based on QLSAs.

## Provider details
- **Doi:** 10.1021/acs.jctc.6c01621
- **Journal:** Journal of Chemical Theory
and Computation
- **Publisher:** American Chemical Society (ACS)
- **Type:** journal-article
