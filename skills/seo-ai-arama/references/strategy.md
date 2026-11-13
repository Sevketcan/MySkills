# Strategy: keyword patterns that make money

Use this when the question is which keywords or page types to target.

## Steps

1. **Collect seeds.**
   - Use the product type and the names of the main competitors as seeds.
   - Put `*` before, inside and after a seed keyword in Google Suggest to collect variations.
   - Add the queries of pages that already bring leads or sales in Search Console.
2. **Read the live results for each candidate (K1).**
   - If the top 3 are landing, category, product or service pages, the query is commercial: target it.
   - If blog posts and definitions dominate, drop it for now.
   - If the page type Google shows differs from ours (for example a blog post ranks where we have a tool page), tuning will not fix it. A page of the right type is needed.
3. **Match your authority.** Queries where sites of similar or lower authority hold the top 3 are realistic (K28).
4. **Group keywords into patterns (K1).** Narrow, buyer-intent patterns usually rank more easily than the head term, because the searcher has already said what they want, their budget or whom they are comparing:
   - [feature] [product]
   - [product] for [use or audience]
   - "best [product]", and "best [product] for [use]"
   - [product] under [price]
   - [brand] vs [competitor]
   - [competitor] alternative
   - questions about a competitor ("is [competitor] worth it")
   - service + city, category + brand
   - entity name: a club, hotel, store or other place people search for by name
   - tool pattern: "[region] [thing] calculator"

   On comparison and alternative pages, take every price and feature from the vendor's own page and record the URL and date (K24).
5. **Check entity and tool patterns (K31).** If users search for the site's entities by name, or a tool pattern has real searches, plan one page per entity or pattern; the search surface then grows with the catalog.
   - Open only pages with data specific to that entity (prices, availability, history). The rest stay out of the index until they qualify: see the indexing criterion in [indexing.md](indexing.md) (K17, K19).
   - Don't generate every deep combination (region × amount); those pages tend to be discovered but not indexed.
   - Feed the pages with in-context links from parent and guide pages (K20).
   - For free tool pages, plan the bridge to the product (a call to action under the result) from the start, and judge them by sign-ups, not impressions (K10).
6. **Write `keywords.md`** with these columns:

   | pattern | keyword | volume | page type Google ranks | do we have a URL |
   |---|---|---|---|---|

   - If volume data is missing, write "n/a". Never invent it.
   - Label queries that an AI tool suggested but Search Console has never shown as "idea" (K24).

## New domain (K35)

If the domain is new, treat its first weeks as a test: Google weighs a new site early, and a poor first judgement takes long to correct.

- Launch with a few complete pages that carry real, current data, not with thin or mass-generated pages.
- Hold back large generated sections until the indexing criterion in [indexing.md](indexing.md) is in place (K17).
- The bar is value, not volume or method: Google's scaled-content policy applies the same way to pages written by people, by automation or by both.

## Notes

- Patterns are what scale. For pages generated from a database, the next questions are which page types get indexed and when: see [indexing.md](indexing.md) (K11, K17).
- Seasonal pages must be live weeks before the season, because discovery and indexing take time, and need links from the home page and the strongest pages (K29). For titles, URLs and the yearly refresh, see [page-workflow.md](page-workflow.md) (K30).
