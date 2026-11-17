# AI search: being cited and recommended

AI answers mostly reuse what classic search already finds. Good SEO, crawlable and indexed pages and plain answers come first. There is no special AI shortcut; `llms.txt` and markup are not one (K27). Server logs show crawlers fetching `robots.txt` constantly and `llms.txt` almost never, so treat the file as a cheap bet at most: keep an existing one, but never report it as visibility work or rank it ahead of the steps below. Any markup should mirror only what the page visibly shows (K32).

## Steps

1. **Check access first (K33).** Report what you find; changing bot rules or settings is the owner's decision.
   - Fetch the live `robots.txt` as served, not the file in the repository, and read the CDN's bot settings. A CDN can add its own rules to the top of the file, or turn a bot away before it reaches the server.
   - Google has no separate AI crawler. Blocking Googlebot also removes the site from AI Overviews and AI Mode, so never propose it as a way to manage AI. `Google-Extended` is not a crawler: it is a control token, written as a user-agent line in `robots.txt`, for the use of content in Google's AI training. It does not affect Search; AI Overviews and AI Mode follow the Googlebot rules.
   - For other engines, treat search crawlers (OAI-SearchBot, Claude-SearchBot, PerplexityBot) and training crawlers (GPTBot, ClaudeBot) as separate decisions. Blocking a search crawler removes the site from that engine's search answers; blocking a training crawler does not stop citations. Whether to block training depends on the business model (a publisher living off its content may block it; a site selling products usually keeps it open).
   - Request the key pages without JavaScript, using the crawler's user agent, and confirm that price, documentation and comparison facts are in the raw HTML. A crawler that does not run JavaScript sees a client-rendered page as empty.
   - Consider requesting the home page and one key page with each AI crawler's user agent, following redirects, and noting the final status code. A final 403, 429 or 5xx, or a challenge page, means that crawler is turned away.
   - If server logs are available, report AI crawler requests separately: which pages, how often. A user-agent test cannot reveal an IP-based block; logs can.
2. **Check Google's AI-features setting (K34).** In Search Console settings, see whether the site has opted out of Google's AI features (AI Overviews, AI Mode, Discover AI summaries). Google says the setting is not a ranking signal for normal results. Before anyone opts out, look at the site's AI-feature impressions, and don't argue for opting out on the assumption that AI answers send no clicks. The AI-features report shows impressions only; clicks from AI answers are not broken out. For estimating them, see [search-console.md](search-console.md).
3. **Check the official pages (K6).** AI answers about a brand tend to come from the brand's own pages: ChatGPT builds its shortlist from brands it knows and then reads each one's pricing and documentation pages.
   - For each money offer, open the site's own pricing, plan and documentation pages. Are prices, plans and limits stated plainly near the top, current, dated, and present in the raw HTML?
   - Give each main intent one official page (pricing, policies, specs), not one page per question.
   - Consider checking whether the business can claim its listing in ChatGPT (OpenAI's Business Hub), which lets it supply basic facts and a price and stock feed directly. Availability outside the US is unclear; claiming and verification are the owner's job.
4. **Build the queries.**
   - For the top 5 commercial keywords, form "best + keyword + year" and its variants ("best X for [use]", "best X for [audience]"), in the site's language, for example "en iyi … 2026" (K5).
   - Add the buyers' own questions for each money offer: a few offers, 5-10 questions each, written in the buyer's words and situation ("I need X this week, will the price drop?"), not as keywords (K23).
5. **Collect the cited lists.**
   - Ask in a logged-out or temporary session with web search on; a logged-in account personalises answers from its history. Run each question a few times per engine (K23).
   - Open and record the cited sources, not only the answer text. Gather the list articles that appear for these queries in AI Overviews, AI Mode and ChatGPT sources.
   - Note each source's type (list article, review site, forum, video, the brand's own page). It shows where the site can appear and feeds steps 7 and 8.
   - Repeat for at least 7 days and keep the ones that keep appearing.
   - Record date, country, device, engine and mode (K5, K23).
6. **Measure three things separately:** the brand being mentioned, a link to the site, and the brand being recommended.
   - Keep the dashboard per engine × offer × question and follow it over time.
   - A run that returned no answer is missing data, not "not mentioned".
   - One answer is one observation (K23). Cited sources change from day to day, so ask the same questions on the same weekday and decide on the trend, never on one screenshot.
7. **Draft outreach** for the lists the site is missing from: short and personal. The user sends them.
   - Back every claim in an email with a primary-source URL.
   - Drop what cannot be verified.
   - Being mentioned by others counts for more than praise on the site's own pages. Find the review platforms the AI cites for the category (Google Business Profile for a local business; G2, Capterra or Trustpilot for software) and suggest collecting reviews on one of them rather than spreading thin. Asking customers is the owner's job (K5).
8. **Check whether Google's AI surfaces cite video (K37).** For commercial and "[competitor] review" queries, count the YouTube videos among the AI Overview and AI Mode sources. Where they appear and nobody has covered the query, a plain single-take review or tutorial can become a source; hand production to `video-icerik-uretimi`. ChatGPT, Perplexity and Claude cite video rarely, so judge each engine separately.
9. **Propose a statistics or report page** built from data the site owns (prices, its own measurements, test results). It is the cleanest way to earn links and citations (K22).
10. **Suggest "best" and the current year** in the titles of suitable commercial and list pages, with a stable URL and a yearly refresh: see "Yearly and seasonal pages" in [page-workflow.md](page-workflow.md) (K30).
11. **Track AI traffic** as its own channel in the site's analytics, and follow it to conversions and, where there is one, the CRM (K10).
    - ChatGPT visits usually carry `utm_source=chatgpt.com`. Segment it, or those visits look like direct traffic. The tag can disappear for a while, so also segment by referrer (`chatgpt.com`, `perplexity.ai`) and consider a measurement problem before reading a sudden drop as lost traffic.
    - Consider adding a "how did you hear about us" question with ChatGPT, Perplexity and Google AI options to sign-up or order forms: some AI apps send no referrer, so their visits land in direct traffic.
    - Add the site and its sitemap to Bing Webmaster Tools. Once Bing indexes the site, its AI Performance report shows cited pages, the queries the AI ran, intent groups, citation share and a period comparison. For a site missing from Bing's index the report is empty (K23).

## Notes

- On the page itself, put a short, dated answer at the top: the claims an AI would quote (price, duration, feature) in plain factual sentences (K6).
- On comparison and "best" pages, position the site honestly: see section 3 of [page-workflow.md](page-workflow.md) (K36).
- AI traffic is small but tends to convert better. Most customers still come from Google, so classic SEO keeps priority.
