# Literature Vault

Save research papers, repositories, and other references to Markdown notes with structured public metadata.

**Open the capture app:** [sandipde.github.io/Literature-vault](https://sandipde.github.io/Literature-vault/)

## First-Time Setup

1. Open the capture app and enter the GitHub owner and repository that should receive references. For this vault, use `sandipde` and `Literature-vault`.
2. Create a fine-grained personal access token scoped only to that repository. Grant **Issues: read and write** to submit references and **Contents: read-only** for the browser's duplicate check.
3. Enter the token and select **Save Settings**. The app keeps these settings in this browser's local storage; they are not written to the repository. Select **Reset settings** to remove them from this browser.

Treat the token like a password. Use a repository-scoped token, avoid setting up the app on a shared browser, and revoke the token from GitHub when it is no longer needed. The Actions workflows use GitHub's separate `GITHUB_TOKEN` to update the repository.

## Capture A Reference

1. Optionally enter a title; metadata from the source may replace it when available.
2. Paste a URL or DOI into the reference field. The page identifies the source type as you type.
3. Select **Save to Repo**. The app checks `sources.json` first. If the source is already captured, it shows a link to the existing note instead of creating another Issue.

The app submits new references as GitHub Issues. The issue workflow then resolves public metadata, writes a Markdown note under [`notes/`](notes/), updates [`sources.json`](sources.json), and closes the Issue. If the browser cannot read the registry, it can still submit; the workflow performs its own duplicate check and comments on and closes a duplicate Issue without adding another note.

You can also create an Issue directly in the configured repository. Put the source URL or DOI in the Issue body. The same metadata and duplicate handling apply.

## Chrome Extension

To install the unpacked extension, open `chrome://extensions`, enable **Developer mode**, choose **Load unpacked**, and select this repository's [`extension/`](extension/) directory. Open the extension's **Settings** and enter the repository owner, repository name, and a fine-grained token with **Issues: read and write** permission. The token is stored in Chrome's local extension storage and is not synced by the extension. Use it only in a trusted browser profile and revoke it when no longer needed. The extension submits the active page's title and URL as an Issue; the existing workflow handles duplicate checks, metadata enrichment, note creation, and Issue closure.

## Browse Results

Open **Results** in the Pages app to browse saved sources or recent scan activity. Search across titles, URLs, providers, and profile names; combine multiple filters by type, provider, and status. Saved sources default to most recently requested and can also be sorted by added date, publication date, last provider update, or title. Scan activity sorts by run time. Open a source or its saved note directly from a result row. Use **Refresh** to reload the current repository indexes.

## Daily Newsletters and AI Enrichment

Read the [latest daily edition](newsletters/2026-10-29.md) or browse the [daily newsletter archive](newsletters/). The first batch covers **187 notes added October 21-27, 2026**, with one retrospective edition per UTC day and an October 28 overview. Coverage is based on the Git commit that first added each note, not the paper's publication date or a file's local modification time.

The [October 28 edition](newsletters/2026-10-28.md) preserves its original two entries and adds **18 newly processed October 28 captures**. Its `note_count: 20` counts the main entries only; the original 187-note overview and retrospective editions remain historical coverage. The [October 29 edition](newsletters/2026-10-29.md) catches up **nine notes first added October 28** after the previous baseline, `79c575426c544d0c4db88fc202264c77957e5964`, and advances coverage through fetched upstream HEAD `a74acefdf15ab0c992b8a3f36b2407e5e91ffd00`. Five new records are title-only; public source checks either exposed no abstract or were blocked. No research-paper full-text review or independent benchmark validation was performed.

Selected notes retain their original source metadata and summaries and gain a separate `## AI enrichment` section with a concise summary, editorial relevance, evidence limitations, and a source link. Frontmatter fields `enriched_on`, `enrichment_method`, `enrichment_category`, and `enrichment_tags` identify the enrichment separately from provider metadata and your `user_*` fields. These topic tags do not replace personal tags or automatically change the Results page's filters.

This batch uses **LLM analysis of captured metadata**, not independently verified web research or full-text review. Performance figures remain source claims; sparse descriptions, possible scan noise, and apparent duplicate/version records are flagged rather than silently discarded. Original records remain intact.

The full-vault backfill enriched the original **471 notes**, including the 284 records outside the first newsletter batch. Two additional upstream arrivals were integrated before that publication, bringing the backfill total to **473 notes**. The October 28 follow-up has now enriched 18 further notes; historical backfill and newsletter counts remain unchanged. Notes with incomplete captures receive a public-source retrieval retry; a separate `## Source recovery` section records the outcome, evidence links, and remaining limitations without overwriting the original capture. `recovery_status` and `recovery_checked_on` identify these retries. Where newly fetched evidence informs the analysis, `enrichment_method: llm-public-source-recovery` distinguishes it from captured-metadata-only enrichment. An unsuccessful retrieval is recorded explicitly; enrichment is not a guarantee of full-text availability or independent verification.

The LUMEN PaperQA collection **`auto-scanner`**, shared with the **`qmml`** group, is the search destination for these enriched Markdown notes. It contains notes and source links, not necessarily full paper PDFs. Upload missing or updated notes, index the collection, and verify exact document coverage and a representative search after each synchronization. Repository commits and collection indexing are separate operations; failures must be reported rather than assuming both succeeded. No automatic synchronization is configured.

For the next edition, pull updates and compare newly added notes against the previous edition's `baseline_commit`, using Git's added-file history (`--diff-filter=A -- notes`) so editorial updates do not count as new captures. Record the new baseline, exact UTC coverage, generation date, and note count in each edition. Link every covered note and its original source, and keep editorial interpretation distinct from verified evidence. The first batch's baseline is `7d56e5d`; notes added after it belong to the next batch. These editions are an on-demand editorial pass; no recurring newsletter job has been configured.

## Personal Notes

Open a saved note from **Results** to add your own rating (1-5), priority, status, tags, and comments. **Save personal notes** submits a `[Note metadata]` Issue; the page never writes repository files itself. The **Update Note Metadata** workflow applies it only when the author is a repository owner, member, or collaborator and the request passes validation (a note under `notes/`, rating 0-5, a known priority and status, at most 20 tags of 40 characters, comments up to 5,000 characters). It stores the values as `user_*` fields in the note's frontmatter, rewrites the note's `## Personal notes` section, comments with the outcome, and closes the Issue. Changes usually appear within a minute; reload the note to see them. The same browser token as for captures is enough: **Issues: read and write** and **Contents: read-only**.

The note and your comments are committed to the repository and the Issue stays in its history, so treat them as visible to anyone who can see the repository. The issue-ingest workflow ignores these requests, and the Results page does not list them as pending references.

## Supported Sources

| Source | Information collected when available |
| --- | --- |
| GitHub repository | Description, language, topics, license, stars, forks, open issues, and recent activity |
| Hugging Face model | Model card description, task, tags, license, downloads, likes, and selected files |
| Hugging Face dataset | Dataset card details, tags, license, downloads, likes, and selected files |
| Hugging Face Space | Space description, SDK, tags, license, likes, and selected files |
| GitLab project | Description, topics, license, stars, forks, visibility, and recent activity |
| arXiv | Title, authors, abstract, publication date, categories, and DOI |
| DOI-linked journal paper | Crossref title, authors, journal, publisher, publication date, abstract, subjects, and license details |
| ChemRxiv paper | OpenAlex metadata for an exact public landing-page match; DOI metadata when submitted as a DOI |
| Other URL | Standard publisher citation metadata when available; DOI/title matches may be enriched through Crossref or OpenAlex. Page body text is not extracted. |

Metadata lookups use public APIs without additional credentials. For general journal URLs, the capture workflow reads standard citation tags when available, then resolves an identified DOI or a high-confidence title match through Crossref or OpenAlex. Some publishers block page metadata requests or omit fields; failed or partial lookups do not prevent the source from being saved.

## Duplicate Handling

Sources are keyed by canonical URL. Known aliases such as arXiv PDF, abstract, and version URLs resolve to one identity; repository subpages resolve to their repository. Common tracking parameters are ignored for ordinary web links. The browser check is for convenience; the issue workflow is authoritative.

The registry is bootstrapped from existing note frontmatter. Historical notes are not deleted or merged, even when they refer to the same source; future captures use the shared identity to avoid adding more duplicates.

## Autoscan Profiles

Open **Scan Settings** in the Pages app to configure searches without editing repository files. Profiles have a source/provider, enabled toggle, one or more queries, a maximum result count, a lookback window in hours (24 by default), and a twice-daily, daily, weekly, or monthly interval. Query syntax depends on the selected provider; the editor gives a short hint. New profiles start disabled unless explicitly enabled.

Saving submits a `[Scan settings]` Issue. The settings workflow applies it only when the author is a repository owner, member, or collaborator and the payload passes validation. It comments with the outcome and closes the request. The issue-ingest workflow ignores marked settings requests, so they are never mistaken for references. The browser token needs **Contents: read-only** to load settings and **Issues: read and write** to submit the request; repository file writes stay with Actions.

The initial configuration in [`monitor_config.json`](monitor_config.json) includes searches for ML interatomic potentials, model families (MACE, NequIP, Allegro, ACE, GAP, MTP, SNAP, CHGNet, M3GNet, SevenNet, MatterSim), equivariant networks, materials foundation models, active/on-the-fly learning, long-range electrostatics, and atomistic catalysis. The same **MLIP developments scan** profile name is configured for arXiv, Crossref, ChemRxiv DOI records, GitHub, GitLab, and Hugging Face models, datasets, and Spaces. Previous arXiv searches remain enabled.

The **Periodic Scanner** workflow runs at 05:00 and 17:00 UTC. Each profile searches only within its configured rolling lookback window, defaulting to the preceding 24 hours; provider timestamps are arXiv submission time, Crossref record creation, repository push/activity, or Hugging Face last modification. It checks each enabled profile's last successful scan and runs it only when its interval is due. Profiles can run twice daily, daily, weekly, or monthly. Result limits apply to the total results collected for a profile across its queries. A failed provider search does not advance that profile's schedule, so it remains due for retry. All results share canonical-source deduplication with manually captured notes and other profiles.

Scans use provider APIs (arXiv Atom, Crossref including the ChemRxiv DOI prefix, GitHub, GitLab, and Hugging Face Hub); they do not scrape publisher pages. To run due profiles immediately, open the repository's **Actions** tab, select **Periodic Scanner**, and choose **Run workflow**. The scanner records successful runs in `scan_state.json`, per-provider outcomes in `scan_history.json`, and legacy arXiv history in `seen_papers.json`. Ensure GitHub Actions is enabled and permitted to write repository contents and Issues.

## GitHub Pages

The hosted app is published by the **Deploy Pages** workflow, which copies only the site's static files (`index.html`, `sw.js`, `manifest.json`, and the icons) and runs when one of them changes, not for every captured note or scan commit. In **Settings → Pages**, set **Source** to **GitHub Actions**. To redeploy without changing a file, run **Deploy Pages** from the **Actions** tab. Notes are not published on the site; the app links to them on GitHub. The expected site address is [https://sandipde.github.io/Literature-vault/](https://sandipde.github.io/Literature-vault/).

## Troubleshooting

- **Duplicate check unavailable:** confirm the token has repository **Contents: read-only** permission. Submission can continue; Actions will check again.
- **Issue submission fails:** confirm the token is valid and has **Issues: read and write** permission for the configured repository.
- **No note appears after submission:** check the repository's **Actions** tab for the issue workflow. Actions must be enabled and allowed to write contents and issues.
- **Personal notes show "Save failed":** the page reports what GitHub returned. A 403 or 404 means the token cannot create Issues in the repository (it needs **Issues: read and write**); a 401 means the token is invalid or expired. If the request is submitted but the note does not change, open the Issue to read the workflow's comment, and check that the **Update Note Metadata** workflow is enabled in the **Actions** tab.
- **Some metadata is missing:** the source may not expose that field through its public API. The original URL is still kept in the note.

## Scanner Rate Limits

The scanner spaces requests per host (arXiv at least three seconds apart, as its API terms ask) and retries `429`, `5xx` and quota-exhausted `403` responses up to three times, honouring `Retry-After`. The workflow passes its `GITHUB_TOKEN` so GitHub search uses the authenticated rate limit. To put Crossref and ChemRxiv lookups in Crossref's polite pool, add a repository variable named `CROSSREF_MAILTO` (Settings → Secrets and variables → Actions → Variables) holding a contact address. If any profile still fails, its error is shown as a warning on the scan step and the run is marked failed after successful results have been committed; the failed profile stays due and is retried on the next run.

## Run Tests Locally

Install dependencies and run the offline regression suite:

```sh
pip install -r requirements.txt
python -m unittest discover -s tests -v
```
