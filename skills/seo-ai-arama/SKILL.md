---
name: seo-ai-arama
description: "Improve a website's Google and AI-search visibility from Search Console data: choose money keyword patterns, decide whether to optimise or create a page, mine question queries, diagnose indexing and crawl gaps, run weekly reviews and track AI-answer citations."
---

# SEO and AI Search

Work from Search Console data: decide before writing, change one thing, wait for a recrawl, and judge by measured results. A page earns traffic only after it is published, discovered, crawled, indexed, shown and clicked. Find the broken link in that chain before proposing work.

## Before starting

- Get Search Console data (API, MCP or a CSV export from the user). Without it, label every recommendation as an estimate.
- Read the project's own growth, decision and analytics documents first (for example `docs/BUYUME.md`, `docs/DECISIONS.md`). Project decisions override the generic rules here.
- Confirm which analytics the site actually uses (GA4, Cloudflare Web Analytics, PostHog) and whether conversions are tracked as named events. If they are not, propose that first; otherwise nobody can tell whether SEO work paid off (K10).
- Establish how pages are produced: a few dozen hand-written pages, or thousands generated from a database. Publishing pace and indexing rules differ (K11, K17).
- Never write to the live site directly; use a branch, draft or preview.
- Keep a project rules file with three lists:
  - allowed: reading, drafting
  - needs approval: publishing, changing a title that already earns clicks, redirects, merges, deletions, outreach
  - forbidden

  When the user rejects a proposal, append the reason and read the file at the start of the next session (K8).

## Choose the mode

Use only the mode the request needs:

1. **Strategy**: which keyword patterns make money and which page types Google ranks for them. Read [strategy.md](references/strategy.md).
2. **Page decision and rewrite**: optimise an existing page or create a new one, write the brief, publish safely. Read [page-workflow.md](references/page-workflow.md).
3. **Search Console analysis**: question and long-tail queries, the weekly review, "my rankings dropped". Read [search-console.md](references/search-console.md).
4. **Indexing and crawl**: pages are live but missing from Google, or indexed pages lag far behind supply. Read [indexing.md](references/indexing.md).
5. **AI search**: being cited or recommended in AI Overviews, AI Mode, ChatGPT or Perplexity. Read [ai-search.md](references/ai-search.md).

When the problem is unclear:
- If indexed pages are far below published pages, start with mode 4.
- Otherwise start with mode 3.

## Principles

- Target monetising queries first: the ones whose live results are commercial pages (K1).
- Positions 4-20 with impressions are the cheapest wins (K3).
- Measure revenue, not traffic. Pages with impressions but no conversions are traps (K10).
- Make one change per page, then wait. Judge it on 7 days of data after the page has been recrawled, and leave a substantially changed page alone for 60 days (K7, K18).
- Trust Search Console over rank trackers, and ignore one-day collapses (K9).
- Compare numbers, dates and deltas in code, not by eye.

## Guardrails

- **No invention:** never make up volumes, rankings or outcomes. Cite each finding's source (URL, report, date) and mark missing data as missing (K24).
- **Approval:** noindex, URL or structure changes, redirects, deletions and merges need the user's approval. Never delegate these decisions to a model score (K8).
- **Diff gate:** before publishing, list everything present in the old version and missing from the new one (K8).
- **Post-publish check:** verify with a script (status 200, canonical, in sitemap, at least one internal link) instead of trusting your own report (K25).
- **No scraping:** don't scrape Google results with your own scripts; use Search Console, official APIs or web search.
- **Links:** don't recommend buying links or link-exchange schemes. Mark paid placements `rel="sponsored"`, and avoid stacks of exact-match anchors on external links (K14).
- **Indexing API:** don't use the Google Indexing API for product, category or article pages.
- **AI text:** don't publish AI-written text without adding real expertise and data.
- **Secrets:** never print or commit API keys or other secrets.

## Boundaries

- Channel choice (SEO vs Reddit vs ads) and press outreach: `girisim-pazarlama`.
- App Store and Google Play search (ASO): `mobil-yayin-buyume`.
- YouTube titles, descriptions and thumbnails: `video-icerik-uretimi`.

## Completion

End each session with:

- the link in the chain where the site is stuck, with the evidence;
- at most five actions ranked by business value, each with the metric and date that will verify it;
- changes made, listed separately from proposals;
- decisions waiting for the user.

The (Kn) markers point to [kurallar.md](references/kurallar.md) (Turkish), which lists each rule's sources and evidence level. It is compiled from the owner's research notes in Twitter Notes (taslak v0.4).
