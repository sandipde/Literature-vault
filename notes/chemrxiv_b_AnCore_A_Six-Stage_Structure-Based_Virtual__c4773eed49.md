---
title: '<b>AnCore: A Six-Stage Structure-Based Virtual Screening Pipeline Integrating
  Two-Phase Redocking, Reciprocal Rank Fusion Consensus Scoring, and a Contact-Anchored
  Elastic-Network Pose-Persistence Heuristic</b>'
type: chemrxiv
source: https://doi.org/10.26434/chemrxiv.15012010/v2
canonical_url: https://doi.org/10.26434/chemrxiv.15012010/v2
captured_by: auto-scanner
date: '2026-11-17'
captured_at: '2026-11-17T14:04:00+00:00'
last_requested: '2026-11-17T14:04:00+00:00'
issue: scan:mlip-development-chemrxiv
status: to-read
authors:
- Norseen H Abdelhakim
- Ahmed M. Senary
published: '2026-11-17'
abstract: Structure-based virtual screening workflows often keep molecular visualization
  apart from multi-engine consensus rescoring and post-docking triage. We present
  AnCore Scientific Studio (v1.2.0), an open-source macOS workbench that couples a
  Rust/Tauri shell and a 3Dmol.js viewport to a six-stage Python pipeline. The stages
  are (1) receptor curation with AMBER14/GBn2 minimization and a steric clash gate;
  (2) a two-phase co-crystal redocking gate, with local BFGS refinement (Phase A)
  and focused-box Monte Carlo search (Phase B); (3) RDKit ligand preparation; (4)
  consensus rescoring of AutoDock Vina, Vinardo and AutoDock4 by Reciprocal Rank Fusion
  and mean Z-score; (5) 3D radial interaction fingerprinting; and (6) post-docking
  triage, made up of unrestrained full-atom minimization (Mode A), a 3.0 ps contact-anchored
  elastic-network pose-persistence heuristic (Mode B) and export of 100-ns explicit-solvent
  OpenMM/GROMACS packages (Mode C). We tested the pipeline on a five-target development
  benchmark (1IEP, 3ERT, 1UYG, 1M17, 1STP; 50 ligands, 25 literature actives and 25
  presumed-inactive decoys, plus 5 co-crystal references). All five co-crystal ligands
  passed the 2.00 Å redocking gate (mean RMSD 0.906 ± 0.388 Å). Consensus rescoring
  raised the suite-mean ROC-AUC from 0.584 for Vina alone to 0.696 for mean Z-score
  (one-sided paired bootstrap p = 0.0070). A contact-count control that uses no co-crystal
  information reached 0.864, and the Mode B heuristic reached 0.920. Because the Mode
  B parameters were set during development on these same targets, and because its
  inputs overlap with the contact counts it is compared against, we treat these two
  figures as in-sample results. Mode B also rejected 40% of the actives under hard
  cutoffs, so it should be used for ranking and not for rejection. Prospective validation
  on independent DUD-E and LIT-PCBA targets is still needed.
metadata_provider: Crossref
metadata_status: complete
provider_data:
  doi: 10.26434/chemrxiv.15012010/v2
  journal: ''
  publisher: American Chemical Society (ACS)
  type: posted-content
  subjects: []
---

# <b>AnCore: A Six-Stage Structure-Based Virtual Screening Pipeline Integrating Two-Phase Redocking, Reciprocal Rank Fusion Consensus Scoring, and a Contact-Anchored Elastic-Network Pose-Persistence Heuristic</b>

- **Type:** chemrxiv
- **Source:** https://doi.org/10.26434/chemrxiv.15012010/v2
- **Captured by:** @auto-scanner
- **Metadata:** complete (Crossref)
- **Authors:** Norseen H Abdelhakim, Ahmed M. Senary
- **Published:** 2026-11-17

## Summary
Structure-based virtual screening workflows often keep molecular visualization apart from multi-engine consensus rescoring and post-docking triage. We present AnCore Scientific Studio (v1.2.0), an open-source macOS workbench that couples a Rust/Tauri shell and a 3Dmol.js viewport to a six-stage Python pipeline. The stages are (1) receptor curation with AMBER14/GBn2 minimization and a steric clash gate; (2) a two-phase co-crystal redocking gate, with local BFGS refinement (Phase A) and focused-box Monte Carlo search (Phase B); (3) RDKit ligand preparation; (4) consensus rescoring of AutoDock Vina, Vinardo and AutoDock4 by Reciprocal Rank Fusion and mean Z-score; (5) 3D radial interaction fingerprinting; and (6) post-docking triage, made up of unrestrained full-atom minimization (Mode A), a 3.0 ps contact-anchored elastic-network pose-persistence heuristic (Mode B) and export of 100-ns explicit-solvent OpenMM/GROMACS packages (Mode C). We tested the pipeline on a five-target development benchmark (1IEP, 3ERT, 1UYG, 1M17, 1STP; 50 ligands, 25 literature actives and 25 presumed-inactive decoys, plus 5 co-crystal references). All five co-crystal ligands passed the 2.00 Å redocking gate (mean RMSD 0.906 ± 0.388 Å). Consensus rescoring raised the suite-mean ROC-AUC from 0.584 for Vina alone to 0.696 for mean Z-score (one-sided paired bootstrap p = 0.0070). A contact-count control that uses no co-crystal information reached 0.864, and the Mode B heuristic reached 0.920. Because the Mode B parameters were set during development on these same targets, and because its inputs overlap with the contact counts it is compared against, we treat these two figures as in-sample results. Mode B also rejected 40% of the actives under hard cutoffs, so it should be used for ranking and not for rejection. Prospective validation on independent DUD-E and LIT-PCBA targets is still needed.

## Provider details
- **Doi:** 10.26434/chemrxiv.15012010/v2
- **Publisher:** American Chemical Society (ACS)
- **Type:** posted-content
