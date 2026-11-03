---
title: Evaluating the Dimensionality of Molecular Ensembles Using Deep Neural Network
  Stochastic Autoencoders
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011591/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011591/v1
captured_by: auto-scanner
date: '2026-11-03'
captured_at: '2026-11-03T22:11:07+00:00'
last_requested: '2026-11-03T22:11:07+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Joseph A. DePaolo-Boisvert
- Thitipun Srinarmwong
- Aryan Bahl
- Soohaeng Yoo Willow
- Lulu Kang
- David D. L. Minh
published: '2026-11-03'
abstract: Stochastic autoencoders (SAEs), which omit the Kullback–Leibler prior-matching
  term of variational autoencoders and are therefore suited to reconstruction rather
  than generative sampling, offer a nonlinear route to reducing the dimensionality
  of molecular ensembles, but their behavior across systems of differing size and
  flexibility is poorly characterized. Training SAEs on molecular dynamics trajectories
  of oxycodone, deca-alanine, crambin, a bromodomain–JQ1 complex, and HIV-1 protease,
  we find that reconstruction error plateaus at a system- and model-dependent latent
  dimensionality, that the effects of dropout and batch normalization are system-specific,
  and that SAEs yield more distinct clusters than principal component analysis (PCA)
  at very low dimensionality and reconstruct large data sets more accurately than
  the deterministic autoencoder CompressTraj at low dimensionality. With two to four
  latent variables, SAE reconstructions of crambin and HIV-1 protease are as accurate
  as PCA with 6–18 components, two latent variables span their leading principal subspace
  as well as 9–15 components, and a single SAE coordinate recovers the end-to-end
  distance of deca-alanine (R2 = 0.97, versus 0.04 for the first principal component),
  whereas PCA is more accurate at higher dimensionality and for the near-rigid bromodomain
  ensemble. Latent-space perturbations show that SAE latent variables encode nonlinear,
  position-dependent collective motions that vary across the learned manifold.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011591/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# Evaluating the Dimensionality of Molecular Ensembles Using Deep Neural Network Stochastic Autoencoders

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011591/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Joseph A. DePaolo-Boisvert, Thitipun Srinarmwong, Aryan Bahl, Soohaeng Yoo Willow, Lulu Kang, David D. L. Minh
- **Published:** 2026-11-03

## Summary
Stochastic autoencoders (SAEs), which omit the Kullback–Leibler prior-matching term of variational autoencoders and are therefore suited to reconstruction rather than generative sampling, offer a nonlinear route to reducing the dimensionality of molecular ensembles, but their behavior across systems of differing size and flexibility is poorly characterized. Training SAEs on molecular dynamics trajectories of oxycodone, deca-alanine, crambin, a bromodomain–JQ1 complex, and HIV-1 protease, we find that reconstruction error plateaus at a system- and model-dependent latent dimensionality, that the effects of dropout and batch normalization are system-specific, and that SAEs yield more distinct clusters than principal component analysis (PCA) at very low dimensionality and reconstruct large data sets more accurately than the deterministic autoencoder CompressTraj at low dimensionality. With two to four latent variables, SAE reconstructions of crambin and HIV-1 protease are as accurate as PCA with 6–18 components, two latent variables span their leading principal subspace as well as 9–15 components, and a single SAE coordinate recovers the end-to-end distance of deca-alanine (R2 = 0.97, versus 0.04 for the first principal component), whereas PCA is more accurate at higher dimensionality and for the near-rigid bromodomain ensemble. Latent-space perturbations show that SAE latent variables encode nonlinear, position-dependent collective motions that vary across the learned manifold.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011591/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
