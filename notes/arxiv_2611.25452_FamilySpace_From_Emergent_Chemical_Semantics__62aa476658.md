---
title: 'FamilySpace: From Emergent Chemical Semantics to Controllable Crystal Generation'
type: arxiv
source: https://arxiv.org/abs/2611.25452
canonical_url: https://arxiv.org/abs/2611.25452
captured_by: auto-scanner
date: '2026-11-20'
captured_at: '2026-11-20T22:56:01+00:00'
last_requested: '2026-11-20T22:56:01+00:00'
issue: scan:arxiv-ml-atomistic
status: to-read
authors:
- Haowei Hua
- Irwin King
- Wanyu Lin
published: '2026-11-19'
abstract: Latent crystal generative models typically combine a variational autoencoder
  (VAE) for learning atom-wise representations with a flow model that transports a
  simple source distribution to the learned latent distribution. However, previous
  studies have mainly focused on the quality of generated crystals, leaving the structure
  and generative utility of the atom-wise latent space largely unexplored. In this
  work, we show that even a vanilla crystal VAE implicitly organizes atom-wise latent
  representations according to elemental families, with different families occupying
  largely separated regions of the latent space. We term this phenomenon emergent
  chemical semantics. This structure suggests that sampling from a family-specific
  latent region can bias the decoder toward atoms from the corresponding elemental
  family. Building on this insight, we propose FamilySpace, a framework for controlling
  the elemental-family composition of generated crystals. FamilySpace assigns each
  elemental family a distinct source component, forming a family-indexed multi-source
  distribution, and trains a flow model using source-target pairs matched by family.
  In inference, a user-specified family template selects the source component for
  each atom-wise representation, enabling direct control over the family composition
  of generated crystals. Experiments on MP-20 and MPTS-52 show that FamilySpace achieves
  competitive crystal-generation performance while matching prescribed elemental-family
  compositions. Moreover, selected family templates increase the fraction of generated
  crystals predicted to be stable or metastable, demonstrating that latent-space composition
  control can support targeted exploration of promising chemical regions without additional
  optimization techniques such as reinforcement learning. Code is available at https://github.com/hhw11/FamilySpace
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.25452'
  categories:
  - cs.LG
  - cond-mat.mtrl-sci
---

# FamilySpace: From Emergent Chemical Semantics to Controllable Crystal Generation

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.25452
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Haowei Hua, Irwin King, Wanyu Lin
- **Published:** 2026-11-19

## Summary
Latent crystal generative models typically combine a variational autoencoder (VAE) for learning atom-wise representations with a flow model that transports a simple source distribution to the learned latent distribution. However, previous studies have mainly focused on the quality of generated crystals, leaving the structure and generative utility of the atom-wise latent space largely unexplored. In this work, we show that even a vanilla crystal VAE implicitly organizes atom-wise latent representations according to elemental families, with different families occupying largely separated regions of the latent space. We term this phenomenon emergent chemical semantics. This structure suggests that sampling from a family-specific latent region can bias the decoder toward atoms from the corresponding elemental family. Building on this insight, we propose FamilySpace, a framework for controlling the elemental-family composition of generated crystals. FamilySpace assigns each elemental family a distinct source component, forming a family-indexed multi-source distribution, and trains a flow model using source-target pairs matched by family. In inference, a user-specified family template selects the source component for each atom-wise representation, enabling direct control over the family composition of generated crystals. Experiments on MP-20 and MPTS-52 show that FamilySpace achieves competitive crystal-generation performance while matching prescribed elemental-family compositions. Moreover, selected family templates increase the fraction of generated crystals predicted to be stable or metastable, demonstrating that latent-space composition control can support targeted exploration of promising chemical regions without additional optimization techniques such as reinforcement learning. Code is available at https://github.com/hhw11/FamilySpace

## Provider details
- **Arxiv Id:** 2611.25452
- **Categories:** ["cs.LG", "cond-mat.mtrl-sci"]
