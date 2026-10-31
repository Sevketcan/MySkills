# Page decision, brief and safe publishing

## 1. Decide before writing (K2)

1. Search Console → Performance → filter the query → Pages tab.
2. Decide:
   - **A page already earns clicks for the query:** improve that page.
   - **A page gets impressions but no clicks:** improve it too.
   - **The change would cost the page queries it already earns clicks for:** create a new page and leave the old one alone.
   - **No page appears:** create a new page.
   - **Two pages appear for the same query:** not a problem by itself. Propose a merge only when both have the same intent **and** the same angle (same reader, same promise); the user decides (K26).
3. **Secondary keywords:** collect the other queries for which the current #1 URL ranks in the top 5.

## 2. Brief

The brief contains:

- create or improve, and which URL
- primary and secondary keywords
- the sections the top 3 results share
- **one thing the top 3 lack**: own data, a tool, a real screenshot, a first-hand verdict. If you cannot find one, stop and ask (K15).
- title: primary keyword first and verbatim, one intent per title (K12)
- meta description: written to win the click

## 3. Write or update

- Cover the shared sections of the top 3 and add the differentiator from the brief (K15).
- One H1 containing the primary keyword. Keep the title plain with the primary keyword first.
- Phrase each heading as the reader's question and answer it in the first one or two sentences below it (K4).
- State the claims an AI answer would quote (price, duration, feature) near the top, in one or two plain, factual and correct sentences. No marketing language (K6).
- **Internal links (K20):** give the target page at least 3-5 in-context links from pages on the same topic.
  - Find candidates by crawling the site or searching `site:example.com "keyword"`, not from the sitemap.
  - Let the sentence decide the anchor, and don't use the same anchor for two different pages.
- Special AI markup and `llms.txt` are not ranking shortcuts. Add structured data only where it fits a rich result the page qualifies for (K27).

## 4. Diff gate

Before publishing, list every element present in the old version and missing from the new one (tables, forms, images, links, embeds) and show the list to the user. Do not publish without approval (K8).

## 5. Post-publish check (K25)

Do not trust your own "done" report. Check with a script:

- the URL returns 200;
- the canonical is correct and the URL is in the sitemap;
- the page receives at least one internal link.

## Pace

Publish hand-written or template pages slowly and steadily: the sources say at most one a day, never dozens in one day and then nothing. Never publish pages where only the city or name changes. For catalogs generated from a database, the limit is an indexing criterion, not a page count: see [indexing.md](indexing.md) (K11, K19).
