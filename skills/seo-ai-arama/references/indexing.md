# Indexing and crawl diagnosis

Use this when pages are live but missing from Google, or when the number of indexed pages lags far behind what the site publishes. Answer the four questions in order.
- Write each answer from data.
- When data is missing, write "unknown" and say how to measure it.

Search Console labels below are English, with the Turkish UI label in parentheses.

## Question 1: why are the pages not indexed?

1. **Collect the reasons and counts.** Open Indexing → Pages and list each reason with its count. Check the report date; it can lag by days.
2. **Split the reasons into two groups.**
   - **Deliberate exclusions** (not errors; just check they are limited to the expected URLs) (K13):
     - noindex
     - "Alternate page with proper canonical tag"
     - redirects
     - filter and search URLs blocked by robots
   - **Problems:**
     - "Discovered – currently not indexed" (Keşfedildi, şu anda dizine eklenmedi): Google knows the URL but has not crawled it. Look at crawl capacity, internal links and the server.
     - "Crawled – currently not indexed" (Tarandı, şu anda dizine eklenmedi): Google crawled the page but did not keep it. Look at quality, similarity and the missing differentiator.
     - 5xx, soft 404 and redirect errors.
3. **Inspect samples.** Check 3-5 sample URLs from each problem group in URL Inspection: last crawl date, the canonical Google chose, live test result.
4. **Check before interpreting.** Fetch the URL's current response before reading meaning into an old report row.

| Status | Meaning | Look first at |
|---|---|---|
| Discovered – currently not indexed | Known, not crawled | Internal links, crawl capacity, server errors, number of URLs in the sitemap |
| Crawled – currently not indexed | Crawled, not indexed | What does the page offer beyond what Google already knows? Thin or near-duplicate pages, no differentiator |
| Alternate page with proper canonical tag | Deliberate exclusion | Not an error; only the expected URLs? |
| Google chose a different canonical than the user | Conflicting signals | Do canonical, sitemap, internal links and redirects all point to the same URL? |
| Excluded by noindex | Deliberate, or a template bug | Limited to expected types? A sudden jump is a template bug |
| Server error (5xx) | Real problem | Current response, server logs, memory and cache |
| Soft 404 | Empty or "no results" page returns 200 | Empty category and combination pages; redirecting everything to the home page can also count as soft 404 |

- robots.txt controls crawling; noindex controls indexing. A noindex on a robots-blocked page is never seen.
- `site:example.com keyword` is a rough check; URL Inspection is the definitive one. A "main index vs supplemental index" check through Programmable Search is a disputed claim; don't use it for diagnosis.

## Question 2: are sitemaps split by type? (K16, K17)

1. **Split by page type.** List the sitemap index's children. Are they split by page type (product, category, comparison, brand, article)?
2. **Submit each child separately.** Is each major child sitemap submitted to Search Console on its own? If only the index is submitted, the index report is one undivided bucket.
   - Recommend submitting the children separately; this is the user's job in the panel.
   - Then use the "Submitted pages only" filter in the Pages report to get each type's index rate.
3. **Use the right denominator.** Compute the index rate against the URLs we **want** indexed, not all URLs.
4. **Check what the sitemap contains.**
   - Only URLs that return 200, are self-canonical, indexable and meant to appear in search?
   - Do the canonical and the sitemap point to the same URL?
   - Does `lastmod` carry the real change date?
5. **Measure cache delay.** If the sitemap is cached, measure how long a new URL takes to appear in it. Even minutes matter on a fast-publishing site.

## Question 3: are internal links and crawl budget sufficient? (K20, K21)

1. **Orphan pages:** the share of sitemap URLs that receive no internal link (from a site crawl). Are important types on the home → category → child path?
2. **Strong pages:** do internal links flow to the types that index best and earn the most clicks?
3. **Crawl budget:** in server logs (or Search Console → Settings → Crawl stats), how many Googlebot requests per day, and to which URL types? Are parameterised, empty, infinite-filter or duplicate URLs eating the budget?
4. **Rough arithmetic:** compare daily Googlebot requests with the number of URLs in the sitemap and write down "how many days would one full read of the site take?"
5. **Server health:** 5xx, 429 and response time. Google slows crawling when errors rise. Caching and a CDN are the fastest fixes.
6. **Pagination and JavaScript:** are deep pages linked with `<a href>`? Are content and links in the HTML without JavaScript?
7. **Size threshold:** crawl-budget work only matters for large sites (tens of thousands of URLs or more) or very frequently changing ones. Don't spend time on it for a small site.

## Question 4: how and how fast are new pages published? (K11, K17, K19)

1. **Production mode:**
   - Hand-written or template service and blog pages: publish slowly and steadily. The sources say at most one a day, never dozens in one day and then nothing.
   - Catalogs generated from a database: the limit is an indexing criterion, not a page count.
2. **Is the indexing criterion in code?** Use the template below. A page that fails the criterion is either `noindex, follow` or left out of the sitemap, and enters automatically once it qualifies.
3. **Does every page have a differentiator?** A page where only a name or city changes counts as a near-duplicate of something Google already knows and may not be indexed (K19).
4. **How are new URLs discovered?**
   - Do they enter the sitemap immediately?
   - Do they get links from hub pages ("newly added", categories)?
   - Is IndexNow used for Bing and Yandex? Only one source supports this.
   - For Google, the sitemap and internal links are what count. The Google Indexing API is not for product or article pages; that is our note from Google's official scope, not from the sources.
5. **Seasonal pages:** are they live weeks before the season (K29)?

### Indexing criterion template

For sites that generate pages from a database. The thresholds are project-specific; these are examples.

```
Page type: <product / category × brand / comparison / profile>
Indexable AND in the sitemap when:
  - content condition: <at least N results / at least N price records / has a biography>
  - differentiator: <a data field specific to this page is filled>
  - demand: <impressions in Search Console or site search>  (optional)
  - internal link: <linked from at least one hub page>
Otherwise: noindex, follow + left out of the sitemap. Enters automatically once it qualifies.
Alert on sudden changes in indexable count, noindex, 404 and canonicals.
```

Measure "indexed / indexable and in the sitemap" per type, with a separate child sitemap for each type and the "Submitted pages only" filter.

## Google's typical timings

These are Google's own published estimates, not guarantees. They add up along the chain.

| Process | Typical | Bad case |
|---|---|---|
| Discover a new page | ~20 hours | weeks, or never |
| Recrawl an existing page | ~30 days | |
| Process a sitemap | ~24 hours | up to 14 days depending on quality, or never |
| Pick up a robots.txt change | ~24 hours | |
| Adjust crawl capacity | 4 hours to 2 weeks | |
| Finish indexing | ~1.5 hours | months, or never |
| Process links | minutes to 3 weeks | |
| Remove a page from the index | 1-3 weeks | |
| Canonical change | 1-3 weeks | months with conflicting signals |
| Site migration | 1-3 months | 6 months to 1 year |
| Title and description update | 1-2 days | |
| Recover from a core update | 3-6 months | 6 months to 1 year, sometimes the next update |

A page change cannot show any effect until the page is recrawled. Check the last crawl date in URL Inspection before judging.

## Output

- **Findings:** the answers to the four questions and where the chain breaks (crawl / index / impressions / clicks).
- **Actions:** at most five, each with the metric and date that will verify it.
- **Follow-up:** read the index report weekly. Judge an indexing change no earlier than one recrawl cycle (~30 days) later (K18).
- **Approval:** bulk `noindex`, removing URLs from sitemaps, URL structure changes and the indexing criterion are user decisions; present them as proposals.
