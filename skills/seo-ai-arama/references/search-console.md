# Search Console analysis

Three jobs: quick wins from question queries, the weekly review, and diagnosing a ranking drop. Search Console data arrives 2-3 days late. Leave incomplete days out of every comparison (K9).

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
   - If CTR is very low (for example 500+ impressions and under 0.5%), look at the snippet and the intent before writing new content.
   - Pages with many impressions and zero conversions are traps: flag them, don't recommend them (K10).
3. **Leave-alone and link rules (K7).**
   - A page edited or given links in the last 60 days: "wait", don't touch it.
   - A page edited 90+ days ago from a good brief that still isn't in the top 3 is a link candidate.
4. **Judge changes** on 7 days of data, and only if the page has been recrawled since the change. Check the last crawl date in URL Inspection (K18).
5. **Output:** at most five actions ranked by business value (not traffic). List changes made separately from proposals.

## 3. "My rankings dropped"

1. Compare impressions and average position for the same keywords on the drop day against the previous 7 days.
2. If Search Console is flat but the rank tracker fell, the tracker's data is bad ("poisoned results"). Don't touch the site.
3. Ignore one-day collapses. A real change persists over consecutive days and shows in Search Console.
4. Before calling a change a failure, check the page's last crawl date. Google can take about 30 days to recrawl a page (K18).
5. Check the server: were there 5xx or 429 responses, or slowdowns, during the drop? If so, Google has throttled crawling (K21).
6. Is there a manual action in Search Console? If not, don't recommend disavowing bad links.
7. If the drop coincides with a core update, don't expect a quick fix. Recovery typically takes 3-6 months.
