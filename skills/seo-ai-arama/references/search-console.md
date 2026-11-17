# Search Console analysis

Four jobs: quick wins from question queries, the weekly review, refreshing pages that lost clicks, and diagnosing a ranking drop. Search Console data arrives 2-3 days late. Leave incomplete days out of every comparison (K9).

Work on a weekly rhythm. Rankings move over weeks, so daily or hourly rank checks mostly return "no change" and invite needless edits. One scheduled weekly pass, plus a look when something breaks, is enough (K9).

## Regex filters

Search Console → Performance → Add filter → Query → Custom (regex). Search Console uses RE2 syntax.

| Purpose | Regex | Source | Status |
|---|---|---|---|
| English question queries | `^(how\|what\|why\|which\|can\|is\|does\|do\|are\|should\|when)\b` | VengeonsP | used in the source |
| French question queries | `^(comment\|pourquoi\|quel\|quelle\|quels\|quelles\|combien\|est-ce\|faut-il\|peut-on\|qu'est-ce)\b` | VengeonsP | used in the source |
| Turkish question queries | `(^\|\s)(nasıl\|neden\|niye\|niçin\|hangi\|hangisi\|kaç\|kim\|nerede\|nereden\|nereye\|ne zaman\|nedir\|ne kadar\|mi\|mı\|mu\|mü\|mısın\|midir\|mıdır)(\s\|$)` | our adaptation | tested on 14 sample queries; confirm in Search Console on first use |
| Queries of 7+ words (any language) | `^(\S+\s){6,}\S+$` | denohawari | used in the source |

`\|` is Markdown escaping; paste a plain `|` into Search Console.

## 1. Quick wins: question queries (K4)

1. Filter question and long queries with the regexes above.
2. Sort by impressions and keep average positions 1-20.
3. For each question, find the page it is shown for. Make the question a heading on that page and answer it in the first one or two sentences with something concrete.

## 2. Weekly review

1. **Compare the last 28 days with the previous 28.**
   - Pages whose impressions jumped have entered the top 10: queue them for a brief.
   - Flag pages that lost clicks. Did the position fall (improve the page) or did CTR fall at the same position (improve the title)? Do the arithmetic in code.
2. **Rank the opportunities.**
   - Positions 4-20 with high impressions are the cheapest (K3).
   - At page level, filter the Pages tab to average position 8-20: pages stuck around the bottom of page one and on page two (K3).
   - If CTR is very low (for example 500+ impressions and under 0.5%), look at the snippet and the intent before writing new content.
   - Pages with many impressions and zero conversions are traps: flag them, don't recommend them (K10).
3. **Leave-alone and link rules (K7).**
   - A page whose content was substantially changed, or that received new external links, in the last 60 days: "wait", don't touch it. Adding internal links to it from other pages does not count as touching it.
   - A page edited 90+ days ago from a good brief that still isn't in the top 3 is a link candidate. Most external links naturally point to the home page; for a single inner page, pace them, one or two a month with a few weeks between, rather than a burst (K14).
4. **Judge changes** on 7 days of data, and only if the page has been recrawled since the change. Check the last crawl date in URL Inspection (K18).
5. **Google AI features (K34).** If Search Console shows a generative AI features report, record its impressions as a separate line in the review. The report gives impressions only; clicks from AI answers are not broken out. Don't read that as zero clicks: consider estimating AI's click share by comparing two comparable periods (same length, same season, no other big change), and label the result an estimate.
6. **Output:** at most five actions ranked by business value (not traffic). List changes made separately from proposals.

## 3. Flat traffic: refresh pages that lost clicks (K2)

When traffic is flat, start here before writing new pages. Pages that once earned clicks are already known to Google.

1. Performance → compare the last 3 months with the previous 3 → Pages tab. Sort by click change in code, biggest loss first.
2. Compare the same months with last year too, so a seasonal dip is not mistaken for decay.
3. Take the 10 pages that lost the most. Skip pages changed in the last 60 days (K7).
4. For each page, read the live results for its main query and note what the top 3 cover that the page lacks.
5. Refresh it through the brief in [page-workflow.md](page-workflow.md):
   - rewrite the first two lines to answer the query directly (K4);
   - update years, statistics, prices and screenshots (K30);
   - add the missing sections and one thing only this site can offer (K15).
6. Link the refreshed page from at least 3 related pages (K20), then request indexing in URL Inspection.
7. Judge the result only after the page has been recrawled (K18).

## 4. "My rankings dropped"

1. Compare impressions and average position for the same keywords on the drop day against the previous 7 days.
2. If Search Console is flat but the rank tracker fell, the tracker's data is bad ("poisoned results"). Don't touch the site.
3. Ignore one-day collapses. A real change persists over consecutive days and shows in Search Console.
4. Before calling a change a failure, check the page's last crawl date. Google can take about 30 days to recrawl a page (K18).
5. Check the server: were there 5xx or 429 responses, or slowdowns, during the drop? If so, Google has throttled crawling (K21).
6. Is there a manual action in Search Console? If not, don't recommend disavowing bad links.
7. If the drop coincides with a core update, don't expect a quick fix. Recovery typically takes 3-6 months.
