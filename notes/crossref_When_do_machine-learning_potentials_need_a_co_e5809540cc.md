---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: ML interatomic potentials
enrichment_tags: [long-range-interactions, fourier-operators, environment-screening]
title: When do machine-learning potentials need a configuration-dependent kernel?
  Learning long-range interactions with Fourier neural operators
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011048/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011048/v1
captured_by: auto-scanner
date: '2026-10-26'
captured_at: '2026-10-26T10:43:25+00:00'
last_requested: '2026-10-26T10:43:25+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Wei Chen
- Gian-Marco Rignanese
published: '2026-10-26'
abstract: Long-range interactions in machine-learning interatomic potentials are commonly
  treated by coupling learned sources through either a prescribed electrostatic kernel
  or a learned but configurationindependent one. Whether such a kernel suffices depends
  on the underlying screened interaction. We address this question by using Fourier
  neural operators (FNOs) to learn how latent source fields, built from the descriptors
  of a local backbone (here MACE), interact across the simulation cell. For a synthetic
  ionic system with tunable screening, a prescribed Coulomb kernel underestimates
  the longwavelength charge fluctuations by 43% under strong screening, whereas the
  FNO reproduces them within 3% and recovers 95–99% of the variance of the residual
  left by the local backbone. A linear FNO, which learns a configuration-independent
  kernel, performs equally well in the homogeneous case. Under inhomogeneous screening,
  rearranging the remote medium modulates the coupling between distant ions, a dependence
  that no configuration-independent kernel can represent. Among the models tested,
  only the nonlinear FNO responds to this modulation, and its force errors are 27–41%
  lower than those of configuration-independent models. In first-principles benchmarks
  of liquid water, lithium lanthanum zirconate, and Au 2 /MgO(001), MACE–FNO is comparable
  to a prescribed-kernel model for the bulk systems and more accurate for the interface.
  It further captures the reversal of the Au 2 wetting preference induced by remote
  Al dopants, with deviations below 5meV per cell from density functional theory.
  These results indicate that a configuration-dependent kernel becomes necessary once
  the screening medium varies, even though the energy remains quadratic in the charges
  for a fixed medium. Nonlinear FNOs, which learn such a kernel from energies and
  forces alone, offer a flexible route to environment-dependent long-range interactions.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011048/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# When do machine-learning potentials need a configuration-dependent kernel? Learning long-range interactions with Fourier neural operators

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011048/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Wei Chen, Gian-Marco Rignanese
- **Published:** 2026-10-26

## Summary
Long-range interactions in machine-learning interatomic potentials are commonly treated by coupling learned sources through either a prescribed electrostatic kernel or a learned but configurationindependent one. Whether such a kernel suffices depends on the underlying screened interaction. We address this question by using Fourier neural operators (FNOs) to learn how latent source fields, built from the descriptors of a local backbone (here MACE), interact across the simulation cell. For a synthetic ionic system with tunable screening, a prescribed Coulomb kernel underestimates the longwavelength charge fluctuations by 43% under strong screening, whereas the FNO reproduces them within 3% and recovers 95–99% of the variance of the residual left by the local backbone. A linear FNO, which learns a configuration-independent kernel, performs equally well in the homogeneous case. Under inhomogeneous screening, rearranging the remote medium modulates the coupling between distant ions, a dependence that no configuration-independent kernel can represent. Among the models tested, only the nonlinear FNO responds to this modulation, and its force errors are 27–41% lower than those of configuration-independent models. In first-principles benchmarks of liquid water, lithium lanthanum zirconate, and Au 2 /MgO(001), MACE–FNO is comparable to a prescribed-kernel model for the bulk systems and more accurate for the interface. It further captures the reversal of the Au 2 wetting preference induced by remote Al dopants, with deviations below 5meV per cell from density functional theory. These results indicate that a configuration-dependent kernel becomes necessary once the screening medium varies, even though the energy remains quadratic in the charges for a fixed medium. Nonlinear FNOs, which learn such a kernel from energies and forces alone, offer a flexible route to environment-dependent long-range interactions.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011048/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment

- **Concise summary:** MACE-based Fourier neural operators learn long-range coupling, with nonlinear configuration-dependent kernels outperforming fixed kernels when the screening environment varies.
- **Why it matters:** The distinction identifies a physical reason to add model complexity rather than choosing a flexible kernel by default.
- **Caveat:** The preprint's necessity argument concerns its modeled screening setup; reported synthetic and first-principles tests do not establish universal superiority.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15011048/v1); analysis based only on captured metadata, not independently verified full text.
