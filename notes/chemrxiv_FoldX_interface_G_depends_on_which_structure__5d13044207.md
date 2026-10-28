---
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [protein-stability, structural-uncertainty, variant-interpretation]
title: 'FoldX interface ΔΔG depends on which structure it starts from, and a learned
  predictor does not: a cautionary analysis on glutaryl-CoA dehydrogenase'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15010007/v2
canonical_url: https://doi.org/10.26434/chemrxiv.15010007/v2
captured_by: auto-scanner
date: '2026-10-12'
captured_at: '2026-10-12T12:41:12+00:00'
last_requested: '2026-10-12T12:41:12+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Cumhur Gökhan Ekmekci
- Ceren Aleyna Cengiz
published: '2026-10-12'
abstract: 'FoldX and related methods are widely used to interpret missense variants,
  and their sensitivity to the input structure is documented: repair of the coordinates
  is mandatory, averaging over structural ensembles improves agreement with experiment,
  and the uncertainty of a FoldX folding ΔΔG has been put at roughly ±3 kcal/mol,
  with binding stability worse. What has not been asked is whether that uncertainty
  is spread evenly over a protein. We took 258 ClinVar missense variants in glutaryl-CoA
  dehydrogenase, a homotetramer, verified every reference residue against the 1SIQ
  structure and computed ΔΔG for the 124 classified pathogenic. Eighteen variants
  were then recomputed on three molecular dynamics snapshots of the same complex:
  six interface variants selected on their monomer-to-tetramer difference, six interface
  variants drawn at random, and six at least 10 Å from any contact. The displacement
  between the crystal-based value and the relaxed-frame mean had a median of 1.10,
  1.38 and 0.20 kcal/mol in the three groups (random interface against distant, Mann-Whitney
  p = 0.0130), while frame-to-frame scatter was indistinguishable between them (Kruskal-Wallis
  p = 0.385). The variation is therefore positional, and it is not explained by noise
  in the mean. SAAMBE-3D, a learned interface predictor, run on the same eighteen
  variants and the same four structures, moved by a median of 0.075 kcal/mol at the
  interface and by nothing at all away from it, so the instability is largely a property
  of FoldX. It also depends on magnitude: G171R, scored at +22.53 kcal/mol, moved
  2.7%, whereas A421V moved from +0.18 kcal/mol, which reads as tolerated, to +4.37
  ± 2.22. Along the way we found that ThermoMPNN given a chain selector on a tetramer
  returns values identical to the isolated monomer at all 7,800 scanned positions.
  For variant interpretation the consequence is specific: at a subunit interface,
  in the range where a classification is actually in doubt, a single starting structure
  does not support a single number.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15010007/v2
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# FoldX interface ΔΔG depends on which structure it starts from, and a learned predictor does not: a cautionary analysis on glutaryl-CoA dehydrogenase

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15010007/v2
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Cumhur Gökhan Ekmekci, Ceren Aleyna Cengiz
- **Published:** 2026-10-12

## Summary
FoldX and related methods are widely used to interpret missense variants, and their sensitivity to the input structure is documented: repair of the coordinates is mandatory, averaging over structural ensembles improves agreement with experiment, and the uncertainty of a FoldX folding ΔΔG has been put at roughly ±3 kcal/mol, with binding stability worse. What has not been asked is whether that uncertainty is spread evenly over a protein. We took 258 ClinVar missense variants in glutaryl-CoA dehydrogenase, a homotetramer, verified every reference residue against the 1SIQ structure and computed ΔΔG for the 124 classified pathogenic. Eighteen variants were then recomputed on three molecular dynamics snapshots of the same complex: six interface variants selected on their monomer-to-tetramer difference, six interface variants drawn at random, and six at least 10 Å from any contact. The displacement between the crystal-based value and the relaxed-frame mean had a median of 1.10, 1.38 and 0.20 kcal/mol in the three groups (random interface against distant, Mann-Whitney p = 0.0130), while frame-to-frame scatter was indistinguishable between them (Kruskal-Wallis p = 0.385). The variation is therefore positional, and it is not explained by noise in the mean. SAAMBE-3D, a learned interface predictor, run on the same eighteen variants and the same four structures, moved by a median of 0.075 kcal/mol at the interface and by nothing at all away from it, so the instability is largely a property of FoldX. It also depends on magnitude: G171R, scored at +22.53 kcal/mol, moved 2.7%, whereas A421V moved from +0.18 kcal/mol, which reads as tolerated, to +4.37 ± 2.22. Along the way we found that ThermoMPNN given a chain selector on a tetramer returns values identical to the isolated monomer at all 7,800 scanned positions. For variant interpretation the consequence is specific: at a subunit interface, in the range where a classification is actually in doubt, a single starting structure does not support a single number.

## Provider details
- **Doi:** 10.26434/chemrxiv.15010007/v2
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content

## AI enrichment
- **Concise summary:** In glutaryl-CoA dehydrogenase, FoldX variant effects shift more between crystal and relaxed structures at subunit interfaces than at distant sites. A learned interface predictor changes much less on the same small comparison panel.
- **Why it matters:** A single structural input can create misleading precision precisely for borderline interface variants where interpretation is consequential.
- **Caveat:** The v2 preprint tests one protein and only eighteen variants across the alternative structures; reduced predictor sensitivity is not evidence that the learned values are more accurate.
- **Evidence:** [Captured source](https://doi.org/10.26434/chemrxiv.15010007/v2); analysis based only on captured metadata, not independently verified full text.
