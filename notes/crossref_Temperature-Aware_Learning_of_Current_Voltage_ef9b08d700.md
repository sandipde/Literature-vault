---
title: 'Temperature-Aware Learning of Current–Voltage Behavior in Schottky Diodes:
  From Classical Machine Learning to Neural Basis-Expansion Models under a Leave-One-Temperature-Out
  Validation Protocol'
type: paper
source: https://doi.org/10.1016/j.mlwa.2026.101039
canonical_url: https://doi.org/10.1016/j.mlwa.2026.101039
captured_by: auto-scanner
date: '2026-10-20'
captured_at: '2026-10-20T09:46:32+00:00'
last_requested: '2026-10-20T09:46:32+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Gökalp Tulum
- İlke Taşçıoğlu
published: 2026-10
abstract: ''
metadata_provider: Crossref
metadata_status: complete
enriched_on: '2026-10-28'
enrichment_method: llm-public-source-recovery
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [schottky-diodes, temperature-transfer, electrical-surrogates]
recovery_status: recovered
recovery_checked_on: '2026-10-28'
provider_data:
  doi: 10.1016/j.mlwa.2026.101039
  journal: Machine Learning with Applications
  publisher: Elsevier BV
  type: journal-article
  subjects: []
---

# Temperature-Aware Learning of Current–Voltage Behavior in Schottky Diodes: From Classical Machine Learning to Neural Basis-Expansion Models under a Leave-One-Temperature-Out Validation Protocol

- **Type:** paper
- **Source:** https://doi.org/10.1016/j.mlwa.2026.101039
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Gökalp Tulum, İlke Taşçıoğlu
- **Published:** 2026-10

## Provider details
- **Doi:** 10.1016/j.mlwa.2026.101039
- **Journal:** Machine Learning with Applications
- **Publisher:** Elsevier BV
- **Type:** journal-article

## Source recovery

- **Checked on:** 2026-10-28.
- **Attempted source:** https://doi.org/10.1016/j.mlwa.2026.101039 returned an Elsevier redirect shell.
- **Retrieved source:** https://api.openalex.org/works/https://doi.org/10.1016/j.mlwa.2026.101039?select=doi,title,abstract_inverted_index
- **Outcome:** The exact-DOI abstract compares seven data-driven models and three baseline methods for Al/CdZnO/p-Si diode current-voltage behavior under eleven leave-one-temperature-out folds. N-BEATS has the lowest reported descriptive mean errors, closely followed by MLP.
- **Limitations:** Indexed abstract only; no device-independent testing or reproduction of error metrics.

## AI enrichment

- **Concise summary:** The recovered abstract benchmarks temperature-conditioned diode surrogates while withholding entire temperatures, including comparison with a thermionic-emission model.
- **Why it matters:** Temperature-level holdouts ask whether a surrogate transfers across measurement conditions rather than memorizing adjacent voltage samples.
- **Caveat:** Held-out temperatures within one studied device system do not establish extrapolation to new devices, materials, or temperature ranges.
- **Evidence:** [Captured source](https://doi.org/10.1016/j.mlwa.2026.101039); [recovered OpenAlex abstract](https://api.openalex.org/works/https://doi.org/10.1016/j.mlwa.2026.101039?select=doi,title,abstract_inverted_index), retrieved 2026-10-28; no independent full-text verification.
