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
| Other URL | Canonical source URL and any submitted title; no page scraping is performed |

Metadata lookups use public APIs without additional credentials. Some providers may not expose every field; failed or partial lookups do not prevent the source from being saved.

## Duplicate Handling

Sources are keyed by canonical URL. Known aliases such as arXiv PDF, abstract, and version URLs resolve to one identity; repository subpages resolve to their repository. Common tracking parameters are ignored for ordinary web links. The browser check is for convenience; the issue workflow is authoritative.

The registry is bootstrapped from existing note frontmatter. Historical notes are not deleted or merged, even when they refer to the same source; future captures use the shared identity to avoid adding more duplicates.

## Scheduled arXiv Scan

[`monitor_config.json`](monitor_config.json) contains the search queries. The scanner checks the latest 10 results per query on weekdays at 05:00 UTC and uses the same source registry as manual capture. To change queries, edit that file. To start a scan immediately, open the repository's **Actions** tab, select **Periodic Scanner**, and choose **Run workflow**.

The scanner stores its legacy arXiv ID history in `seen_papers.json` and commits new notes and registry entries to `main`. Ensure GitHub Actions is enabled and permitted to write to the repository.

## GitHub Pages

The hosted app is served from this repository's root on the `main` branch. To verify or change its publishing settings, open **Settings → Pages** and select **Deploy from a branch**, branch `main`, folder `/(root)`. The expected site address is [https://sandipde.github.io/Literature-vault/](https://sandipde.github.io/Literature-vault/).

## Troubleshooting

- **Duplicate check unavailable:** confirm the token has repository **Contents: read-only** permission. Submission can continue; Actions will check again.
- **Issue submission fails:** confirm the token is valid and has **Issues: read and write** permission for the configured repository.
- **No note appears after submission:** check the repository's **Actions** tab for the issue workflow. Actions must be enabled and allowed to write contents and issues.
- **Some metadata is missing:** the source may not expose that field through its public API. The original URL is still kept in the note.

## Run Tests Locally

Install dependencies and run the offline regression suite:

```sh
pip install -r requirements.txt
python -m unittest discover -s tests -v
```
