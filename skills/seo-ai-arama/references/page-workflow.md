# Page decision, brief and safe publishing

## 1. Decide before writing (K2)

1. Search Console → Performance → filter the query → Pages tab.
2. Decide:
   - **A page already earns clicks for the query:** improve that page. Before rewriting, list the queries that already bring it clicks; the new version must keep answering them.
   - **A page gets impressions but few clicks:** improve it when the query is that page's main intent. If the page only catches the query sideways (a different intent), a separate page may serve it better. This is unsettled: present both options with your reasoning and let the user decide.
   - **The change would cost the page queries it already earns clicks for:** create a new page and leave the old one alone.
   - **No page appears:** create a new page.
   - **Two pages appear for the same query:** not a problem by itself. Propose a merge only when both have the same intent **and** the same angle (same reader, same promise); the user decides (K26).
   - **A new question belongs to an intent an existing page already serves:** answer it on that page. Each main intent gets one official page, not one page per question (K6).
3. **Secondary keywords:** collect the other queries for which the current #1 URL ranks in the top 5.

## 2. Brief

The brief contains:

- create or improve, and which URL
- primary and secondary keywords
- the sections the top 3 results share
- **one thing the top 3 lack**: own data, a tool, a real screenshot, a first-hand verdict. If you cannot find one, stop and ask (K15).
- title: primary keyword first and verbatim, one intent per title (K12); on list, comparison and seasonal pages, include the current year (K30)
- meta description: written to win the click

## 3. Write or update

- Cover the shared sections of the top 3 and add the differentiator from the brief (K15).
- One H1 containing the primary keyword. Keep the title plain with the primary keyword first.
- Phrase each heading as the reader's question and answer it in the first one or two sentences below it (K4).
- Put a short, dated answer at the top: the claims an AI answer would quote (price, duration, feature) in one or two plain, factual and correct sentences, with the date the data refers to. No marketing language (K6).
- **Comparison and "best" pages (K36):** include at least one row where the site loses, and say which buyer the competitor suits better. Don't rank the site first in its own "best X" list, and write the ranking criterion on the page. An AI that cites a self-praising list often recommends the competitor: the page becomes the source, the competitor the answer. If an existing self-ranked page already brings customers from Google, propose a test before rewriting it (section 1).
- **Internal links (K20):** give the target page at least 3-5 in-context links from pages on the same topic.
  - Find candidates by crawling the site or searching `site:example.com "keyword"`, not from the sitemap: pages whose text mentions the target's topic but does not link to it.
  - Take anchor candidates from the target page's own Search Console queries (the query it ranks for, or a close variant), and link only where that phrase already occurs naturally in a sentence. Never rewrite a sentence to fit a keyword. Use one anchor for one target only.
  - Exact query anchors versus varied wording across source pages is unsettled. Where the natural sentences differ, let the anchors differ; if the site already leans on one form, test the other on a few pages and compare in Search Console.
  - Add at most 3-5 new links per source page in one pass, spread through the body text.
  - Show the proposed links as a table (source page, sentence, anchor, target, target's query and position) and change nothing until the user approves. Keep a change list so the batch can be rolled back (K8).
  - When an agent places links in bulk, consider calibrating a confidence threshold on hand-checked samples and sending every link below it to the user (K8).
- Special AI markup and `llms.txt` are not ranking shortcuts (K27).
- Sign and date the page: a real author with their role, plus the publish and update dates, shown on the page. If you add Article or Person markup, keep it identical to the author and dates on the page. Aim for markup that describes only what the page visibly shows; treat it as consistency, not as a lever, and otherwise add it only where it fits a rich result the page qualifies for (K32, K27).

## 4. Separate review (K24)

Review the draft in a fresh session or subagent that sees only the page and the brief, not the conversation that wrote it. It does not rewrite the page. It quotes every problem line verbatim: the title and opening lines against the brief, numbers and prices without a source, filler, broken layout on mobile, unsupported superlatives, wrong dates. It ends with one verdict: publish, fix first, or rewrite.

## 5. Diff gate

Before publishing, list every element present in the old version and missing from the new one (tables, forms, images, links, embeds) and show the list to the user. Do not publish without approval (K8).

## 6. Post-publish check (K25)

Do not trust your own "done" report. Check with a script:

- the URL returns 200;
- the canonical is correct and the URL is in the live sitemap;
- the newest published page appears in the sitemap, because a generated sitemap can stop updating without any warning;
- the page receives at least one internal link;
- the links on the page resolve.

Where the stack allows, run the same checks (title, canonical, structured data, internal links, sitemap) as a build or deploy gate, so a page that fails does not ship.

## 7. Yearly and seasonal pages (K29, K30)

For "best" lists, comparisons and pages tied to a recurring season or campaign:

1. Put the current year in the title, and refresh the same page every year: year, statistics, prices, screenshots (K30). Position the site honestly, as in section 3 (K36).
2. Consider keeping the year out of the URL, so one address collects links year after year. Changing an existing URL is a redirect and needs approval (K8).
3. Publish weeks before the season and link the page from the home page and the strongest pages (K29).
4. State the offer (price, what is included, end date) at the top, as in section 3 (K6).
5. When the season ends, consider switching the page to an archive or a "notify me next year" state instead of deleting it. Deleting is a user decision (K8).

## Pace

Publish hand-written or template pages slowly and steadily: consider at most one a day, and never dozens in one day and then nothing. Never publish pages where only the city or name changes. For catalogs generated from a database, the limit is an indexing criterion, not a page count: see [indexing.md](indexing.md) (K11, K19).
