---
title: Efficient and Accurate Ligand Strain Calculations in Solution with the AIMNet2
  Neural Network Potential
type: paper
source: https://doi.org/10.1021/acs.jcim.6c02468
canonical_url: https://doi.org/10.1021/acs.jcim.6c02468
captured_by: auto-scanner
date: '2026-10-21'
enriched_on: '2026-10-28'
enrichment_method: llm-captured-metadata
enrichment_category: Atomistic chemistry and materials
enrichment_tags: [ligand-strain, neural-network-potentials, molecular-modeling]
captured_at: '2026-10-21T09:47:36+00:00'
last_requested: '2026-10-21T09:47:36+00:00'
issue: scan:mlip-development-crossref
status: to-read
authors:
- Hatice Gokcan
- Olexandr Isayev
published: '2026-10-21'
abstract: 'Abstract Conformational strain, the energy a ligand pays to adopt its bound
  conformation, contributes to binding affinity but is routinely misestimated. The
  standard estimate references a single gas-phase energy minimum. This ignores solvent
  and mishandles charged ligands: in vacuo their intramolecular electrostatics collapse
  them into compact minima that deflate the unbound reference and inflate the apparent
  strain. We introduce AIMNet2-CPCM, a neural network potential trained to B97-3c
  energies and forces in a conductor-like continuum solvent (CPCM). It treats neutral
  and charged species on the same footing, and its batched GPU inference makes a solvated
  global-minimum search practical across an entire screening library. Across ∼8K PDB
  ligands the solvated strain has a median of 4.0 kcal/mol and rises with net charge.
  The trend is well determined through a net charge of −2. The −3 and −4 polyanions
  dominate the high-strain tail, where continuum solvation is least reliable, and
  their values are reported as upper bounds. Gas-phase force fields reproduce the
  neutral strains but overstate the charged ones, because they collapse the unbound
  minimum that solvent screening keeps open. Adding a continuum solvent to the force
  field removes most of this error and confirms the mechanism. Profiling at this scale
  further shows that the same ligand strains very differently across the targets that
  bind it: ligand strain is a property of the bound pose, not a transferable molecular
  descriptor.'
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.1021/acs.jcim.6c02468
  journal: 'Journal of Chemical Information

    and Modeling'
  publisher: American Chemical Society (ACS)
  type: journal-article
  subjects: []
---

# Efficient and Accurate Ligand Strain Calculations in Solution with the AIMNet2 Neural Network Potential

- **Type:** paper
- **Source:** https://doi.org/10.1021/acs.jcim.6c02468
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Hatice Gokcan, Olexandr Isayev
- **Published:** 2026-10-21

## Summary
Abstract Conformational strain, the energy a ligand pays to adopt its bound conformation, contributes to binding affinity but is routinely misestimated. The standard estimate references a single gas-phase energy minimum. This ignores solvent and mishandles charged ligands: in vacuo their intramolecular electrostatics collapse them into compact minima that deflate the unbound reference and inflate the apparent strain. We introduce AIMNet2-CPCM, a neural network potential trained to B97-3c energies and forces in a conductor-like continuum solvent (CPCM). It treats neutral and charged species on the same footing, and its batched GPU inference makes a solvated global-minimum search practical across an entire screening library. Across ∼8K PDB ligands the solvated strain has a median of 4.0 kcal/mol and rises with net charge. The trend is well determined through a net charge of −2. The −3 and −4 polyanions dominate the high-strain tail, where continuum solvation is least reliable, and their values are reported as upper bounds. Gas-phase force fields reproduce the neutral strains but overstate the charged ones, because they collapse the unbound minimum that solvent screening keeps open. Adding a continuum solvent to the force field removes most of this error and confirms the mechanism. Profiling at this scale further shows that the same ligand strains very differently across the targets that bind it: ligand strain is a property of the bound pose, not a transferable molecular descriptor.

## Provider details
- **Doi:** 10.1021/acs.jcim.6c02468
- **Journal:** Journal of Chemical Information
and Modeling
- **Publisher:** American Chemical Society (ACS)
- **Type:** journal-article

## AI enrichment
- **Concise summary:** The abstract presents AIMNet2-based ligand strain calculations in solution as an alternative to estimates referenced to a single gas-phase minimum.
- **Why it matters:** More context-aware strain estimates could inform computational interpretation of ligand binding and conformation.
- **Caveat:** The captured abstract does not establish how broadly the method generalizes across ligand classes or binding sites.
- **Evidence:** [Captured source](https://doi.org/10.1021/acs.jcim.6c02468); analysis based only on captured metadata, not independently verified full text.
