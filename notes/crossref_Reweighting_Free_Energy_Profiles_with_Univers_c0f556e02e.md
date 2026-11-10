---
title: Reweighting Free Energy Profiles with Universal Machine Learning Interatomic
  Potentials for Fast Consensus Building
type: paper
source: https://doi.org/10.1021/acs.jctc.6c02044
canonical_url: https://doi.org/10.1021/acs.jctc.6c02044
captured_by: auto-scanner
date: '2026-11-10'
captured_at: '2026-11-10T00:31:39+00:00'
last_requested: '2026-11-10T00:31:39+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Sauradeep Majumdar
- Miguel Steiner
- Johannes C. B. Dietschreit
- Swagata Roy
- Daniel Willimetz
- Lukáš Grajciar
- Rafael Gómez-Bombarelli
published: '2026-11-09'
abstract: 'Abstract Universal machine learning interatomic potentials (MLIPs) have
  made density functional theory (DFT)-level molecular dynamics highly affordable.
  However, their rapid proliferation makes it prohibitively expensive to benchmark
  every new model against the potential of mean force (PMF), the bridge between microscopic
  atomic fluctuations and macroscopic thermodynamic and kinetic observables. Reweighting
  the trajectory of a single “source” MLIP onto a suite of target potentials offers
  a cheaper route, but it is hindered by the statistical collapse of exponential free
  energy perturbation when the phase-space overlap between potentials is low. We show
  that for system sizes of practical interest, this collapse is essentially unavoidable,
  and we quantify it with an information-theoretic diagnostic, the reweighting entropy,
  that indicates when reweighting can be trusted. To sidestep the collapse, we introduce
  a systematic, scalable reweighting framework spanning exponential reweighting, the
  Gaussian approximation, and the energy-only estimator. When applied to the intramolecular
  radical cyclization of hexenyl (17 atoms), all three estimators perform well and
  reproduce the target ωB97M-V/def2-TZVP PMF. However, when extended to Li+ transport
  through a water-solvated zeolite (601 atoms), only the energy-only estimator recovers
  the PMFs of a diverse suite of MLIPs from a single source simulation by discarding
  the noisy entropic contribution to the free energy correction. An independent, brute-force
  umbrella sampling of one of the most divergent targets (MACE-MATPES-r2SCAN) for
  this system confirms it: beyond the shape of the PMF, both the reaction and activation
  free energies are recovered within chemical accuracy. The same analysis reveals
  that the studied MLIPs partition into two clusters, one of plain generalized gradient
  approximation (GGA) models (PBE, PBE-sol) and one of meta-GGA and/or dispersion-corrected
  models (PBE-D3, r2SCAN, r2SCAN-D4), reflecting differences in their training data
  and DFT reference. The resulting protocol thus offers an affordable and reliable
  route to cross-model consensus on materials properties, even when exact reweighting
  is statistically intractable.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1021/acs.jctc.6c02044
  journal: 'Journal of Chemical Theory

    and Computation'
  publisher: American Chemical Society (ACS)
  type: journal-article
  subjects: []
---

# Reweighting Free Energy Profiles with Universal Machine Learning Interatomic Potentials for Fast Consensus Building

- **Type:** paper
- **Source:** https://doi.org/10.1021/acs.jctc.6c02044
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Sauradeep Majumdar, Miguel Steiner, Johannes C. B. Dietschreit, Swagata Roy, Daniel Willimetz, Lukáš Grajciar, Rafael Gómez-Bombarelli
- **Published:** 2026-11-09

## Summary
Abstract Universal machine learning interatomic potentials (MLIPs) have made density functional theory (DFT)-level molecular dynamics highly affordable. However, their rapid proliferation makes it prohibitively expensive to benchmark every new model against the potential of mean force (PMF), the bridge between microscopic atomic fluctuations and macroscopic thermodynamic and kinetic observables. Reweighting the trajectory of a single “source” MLIP onto a suite of target potentials offers a cheaper route, but it is hindered by the statistical collapse of exponential free energy perturbation when the phase-space overlap between potentials is low. We show that for system sizes of practical interest, this collapse is essentially unavoidable, and we quantify it with an information-theoretic diagnostic, the reweighting entropy, that indicates when reweighting can be trusted. To sidestep the collapse, we introduce a systematic, scalable reweighting framework spanning exponential reweighting, the Gaussian approximation, and the energy-only estimator. When applied to the intramolecular radical cyclization of hexenyl (17 atoms), all three estimators perform well and reproduce the target ωB97M-V/def2-TZVP PMF. However, when extended to Li+ transport through a water-solvated zeolite (601 atoms), only the energy-only estimator recovers the PMFs of a diverse suite of MLIPs from a single source simulation by discarding the noisy entropic contribution to the free energy correction. An independent, brute-force umbrella sampling of one of the most divergent targets (MACE-MATPES-r2SCAN) for this system confirms it: beyond the shape of the PMF, both the reaction and activation free energies are recovered within chemical accuracy. The same analysis reveals that the studied MLIPs partition into two clusters, one of plain generalized gradient approximation (GGA) models (PBE, PBE-sol) and one of meta-GGA and/or dispersion-corrected models (PBE-D3, r2SCAN, r2SCAN-D4), reflecting differences in their training data and DFT reference. The resulting protocol thus offers an affordable and reliable route to cross-model consensus on materials properties, even when exact reweighting is statistically intractable.

## Provider details
- **Doi:** 10.1021/acs.jctc.6c02044
- **Journal:** Journal of Chemical Theory
and Computation
- **Publisher:** American Chemical Society (ACS)
- **Type:** journal-article
