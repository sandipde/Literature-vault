---
title: Learned Image Coding With Generative Reference of Conditional Latents
type: paper
source: https://doi.org/10.1109/tpami.2026.3744812
canonical_url: https://doi.org/10.1109/tpami.2026.3744812
captured_by: auto-scanner
date: '2026-10-19'
captured_at: '2026-10-19T21:19:36+00:00'
last_requested: '2026-10-19T21:19:36+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Siqi Wu
- Yinda Chen
- Weiming Chen
- Dong Liu
- K. C. Ho
- Zhihai He
published: '2026'
abstract: ''
metadata_provider: Crossref
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-public-source-recovery
enrichment_category: Mathematics and algorithms
enrichment_tags: [image-compression, conditional-latents, generative-references]
recovery_status: recovered
recovery_checked_on: '2026-10-28'
provider_data:
  doi: 10.1109/tpami.2026.3744812
  journal: IEEE Transactions on Pattern Analysis and Machine Intelligence
  publisher: Institute of Electrical and Electronics Engineers (IEEE)
  type: journal-article
  subjects: []
---

# Learned Image Coding With Generative Reference of Conditional Latents

- **Type:** paper
- **Source:** https://doi.org/10.1109/tpami.2026.3744812
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Siqi Wu, Yinda Chen, Weiming Chen, Dong Liu, K. C. Ho, Zhihai He
- **Published:** 2026

## Provider details
- **Doi:** 10.1109/tpami.2026.3744812
- **Journal:** IEEE Transactions on Pattern Analysis and Machine Intelligence
- **Publisher:** Institute of Electrical and Electronics Engineers (IEEE)
- **Type:** journal-article

## Source recovery

- **Checked on:** 2026-10-28.
- **Attempted source:** https://doi.org/10.1109/tpami.2026.3744812 yielded no usable IEEE page content.
- **Retrieved source:** https://api.openalex.org/works/https://doi.org/10.1109/tpami.2026.3744812?select=doi,title,abstract_inverted_index
- **Outcome:** The exact-DOI indexed abstract describes learned compression using external-image references in conditional latent maps. Reference sources include local retrieval, web search, and diffusion generation; it reports gains up to 1.5 dB PSNR with about 0.005 bits/pixel overhead.
- **Limitations:** Indexed abstract only; coding comparisons, synchronization, and reference-acquisition costs were not independently tested.

## AI enrichment

- **Concise summary:** GRCL uses semantically related external images to construct conditional latent references for image compression, synchronizing generation between encoder and decoder.
- **Why it matters:** Retrieval and generation become compression-side information rather than merely tools for synthesizing the final image.
- **Caveat:** Reported peak PSNR gains depend on datasets and baselines; this is image coding, not atomistic or amorphous-material generation.
- **Evidence:** [Captured source](https://doi.org/10.1109/tpami.2026.3744812); [recovered OpenAlex abstract](https://api.openalex.org/works/https://doi.org/10.1109/tpami.2026.3744812?select=doi,title,abstract_inverted_index), retrieved 2026-10-28; no independent full-text verification.
