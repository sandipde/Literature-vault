---
title: 'LigandFF: an open-source implementation of rule-based atom typing, charge
  assignment and parameter assignment by analogy'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15011711/v1
canonical_url: https://doi.org/10.26434/chemrxiv.15011711/v1
captured_by: auto-scanner
date: '2026-11-05'
captured_at: '2026-11-05T12:53:59+00:00'
last_requested: '2026-11-05T12:53:59+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Euihyun Lee
- Carlos R. Baiz
published: '2026-11-05'
abstract: The CHARMM General Force Field (CGenFF) covers drug-like molecules through
  an automated assignment program that types atoms, assigns charges from bond-charge
  increments, and transfers missing bonded parameters from analogous ones with an
  associated penalty. The algorithms are published, but the program and its two hand-built
  rule files are distributed only in binary form. We describe LigandFF, an open-source
  reimplementation built exclusively from the published algorithms and the public
  CGenFF 5.0 topology, parameter and charge-increment files. LigandFF implements the
  published ring, resonance and aromaticity perception, the rule language for atom
  typing, the bond-charge-increment scheme with peratom charge penalties, the penalty-weighted
  analogy search, halogen lone pairs, and writes CHARMM stream files, PSF files and
  OpenMM and GROMACS inputs. Its typing rules were written against the CGenFF training
  molecules, and its substitution-penalty matrices were fitted to 5,787 analogies
  that the official program recorded in the parameter file. On held-out test splits,
  LigandFF types 97.4% and 97.8% of two sets of CGenFF training molecules with every
  atom correct (99.7% and 99.6% of atoms). Replaying the analogies recorded in the
  parameter file against the database they were made from, it recovers the official
  program’s choice of source parameter for 92.1% of 1,447 held-out cases. It reproduces
  the program-5.0 charges and penalties printed in the CGenFF 5.0 supporting information
  exactly, and all 2,074 benchmark molecules produce systems that build in OpenMM.
  All references are CGenFF training molecules or outputs of the official program
  that are already public; agreement with the official program on new drug-like molecules
  has not been measured. LigandFF is not the official CGenFF program, and its outputs
  are labelled accordingly.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15011711/v1
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# LigandFF: an open-source implementation of rule-based atom typing, charge assignment and parameter assignment by analogy

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15011711/v1
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Euihyun Lee, Carlos R. Baiz
- **Published:** 2026-11-05

## Summary
The CHARMM General Force Field (CGenFF) covers drug-like molecules through an automated assignment program that types atoms, assigns charges from bond-charge increments, and transfers missing bonded parameters from analogous ones with an associated penalty. The algorithms are published, but the program and its two hand-built rule files are distributed only in binary form. We describe LigandFF, an open-source reimplementation built exclusively from the published algorithms and the public CGenFF 5.0 topology, parameter and charge-increment files. LigandFF implements the published ring, resonance and aromaticity perception, the rule language for atom typing, the bond-charge-increment scheme with peratom charge penalties, the penalty-weighted analogy search, halogen lone pairs, and writes CHARMM stream files, PSF files and OpenMM and GROMACS inputs. Its typing rules were written against the CGenFF training molecules, and its substitution-penalty matrices were fitted to 5,787 analogies that the official program recorded in the parameter file. On held-out test splits, LigandFF types 97.4% and 97.8% of two sets of CGenFF training molecules with every atom correct (99.7% and 99.6% of atoms). Replaying the analogies recorded in the parameter file against the database they were made from, it recovers the official program’s choice of source parameter for 92.1% of 1,447 held-out cases. It reproduces the program-5.0 charges and penalties printed in the CGenFF 5.0 supporting information exactly, and all 2,074 benchmark molecules produce systems that build in OpenMM. All references are CGenFF training molecules or outputs of the official program that are already public; agreement with the official program on new drug-like molecules has not been measured. LigandFF is not the official CGenFF program, and its outputs are labelled accordingly.

## Provider details
- **Doi:** 10.26434/chemrxiv.15011711/v1
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
