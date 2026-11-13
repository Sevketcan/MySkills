# E-commerce and marketplace seller tooling

Use this for a seller's own tools on a store or marketplace platform, API access and test modes, bulk listing work, marketplace AI policy, competitor ad creative, orders from AI search, discount or urgency wording, and moving a store to a new platform.

## 1. Own seller tool (E1, E3, E11, E13, E15, E17)

1. Build the seller's own tool on the platform's API or CLI with AI, instead of renting a monthly tool for the job (for example Etsy Open API v3, Shopify CLI or AI Toolkit) (E1).
2. When a model writes the API code, include an instruction such as: "Don't invent endpoints or fields; use the current official documentation." (E3)
3. Request only the permissions the job needs (E3).
4. **Don't assume access (E15).** Read the app's own row in the platform's developer dashboard for its rate limits and granted permissions, and build within them. Commercial or upgraded access reportedly doesn't unlock everything: buyer addresses can be a separate permission, and some actions (for example adding tracking numbers with new keys) can be restricted by country. Check the platform's naming rules before registering the app.
5. **Keep tests away from the live shop (E13).** Before turning on a developer or test mode on a shop that sells, read what the mode does to visibility. On Etsy it reportedly hides the shop's listings from search, and leaving it takes a request to Etsy. Consider a separate test shop.
6. **Competitor and search data (E11, E14).** The store-management API writes to the seller's own data. Public listing data (search results, tags, prices, favourites) may also be readable through the official API, but the API terms reportedly restrict using it for analytics, machine learning or AI without written permission. Check the intended use against the current terms with the user before building competitor research on it; otherwise consider a browser-based research tool, within that tool's terms.
7. **Tools that write in bulk (E17).** Consider:
   - generating titles and tags deterministically (same input, same output), so that checking a sample says something about the rest;
   - enforcing platform limits (length, allowed characters, tag count) while generating, not afterwards;
   - retrying a request the platform rejected for rate limits, but not blindly retrying a write that may have gone through when the API has no idempotency key: report it as uncertain instead;
   - logging bulk uploads so an interrupted run resumes without creating duplicates.

## 2. Approval gate for bulk changes (E2)

Prepare → show the change as a list → the user checks it → apply only after the user says "apply". Nothing is written to the store before that.

- Default to drafts. Publishing, editing a live listing and anything that reaches buyers (for example a tracking number that triggers an email) are live changes and go through the gate.
- Don't ask for delete permission unless the job needs it.

## 3. Listing scoring (E4)

Consider scoring each listing out of 100 against the user's own rules document, with the broken fields and the top 5 fixes.

## 4. Marketplace AI policy (E6, E14)

If any design, text or image is AI-generated, have the user open the marketplace's current policy and check against it. Points reported for one marketplace, to confirm in the official text:

- disclose AI use;
- the seller's own role is visible;
- at least one real photo;
- no bot-driven, one-click bulk listing;
- other sellers' content (titles, tags, descriptions) is not fed to an AI to produce derivatives; the terms reportedly forbid it explicitly from a coming date. Use competitors as inspiration, not as text to rewrite (E14).

Rely on the official text, not on a social post about it. Terms-of-use questions go to a lawyer.

## 5. Competitor ad creative (E7)

1. Consider tagging competitors' running ads by hook, format, offer, CTA and awareness stage.
2. When adapting, never copy an ad verbatim, and tell the user about the brand and copyright risk.
3. Producing variants with the user's product: `video-icerik-uretimi`.

## 6. Orders from AI search (E10)

Consider measuring ChatGPT and Perplexity visits as a separate channel and comparing their conversion with Google. Setup steps: `seo-ai-arama`.

## 7. Discount and urgency claims (E12, G32)

Check this before writing "% off", "price dropped" or urgency text in ads, listings, posts or video templates.

1. **Reference price:** compare against an old price you can prove from your own records. Sources report that in Turkey the old price in a discount claim must be the lowest price of a legally set period before the discount, must appear in the ad, and that misleading discount ads are fined heavily. Have a lawyer verify the current period, wording and penalties before publishing.
2. **Urgency:** don't write "last item", "last hours" or "running out" unless the stock or deadline is confirmed by the store.
3. **Ratings and discounts from other sources:** don't repeat them as is; see [offer-and-ads.md](offer-and-ads.md), section 8.
4. **Questions for the lawyer:** does the rule apply to the user as the advertiser, for example a comparison or affiliate site that sends traffic to stores? Which wording is safe for the user's claims?

## 8. Moving to a new platform or URL structure (E16)

Consider this checklist when a store moves platform or changes its URL structure, and adapt it to the move:

1. **Redirects:** map each old URL to its new one with a 301; don't send everything to the home page.
2. **SEO fields:** keep the title, meta description, H1, product and category text, internal links and image alt text of the top-traffic pages.
3. **Data:** import products, then customers, then past orders; check variants, SKUs, stock and images. Plan gift cards, balances and refunds separately. Check whether customer passwords carry over; if not, tell customers before the switch.
4. **Real carts:** test payment, shipping and tax with real orders on mobile and desktop, including a discount code, a failed payment, notifications and a refund.
5. **Measurement:** check that view, add-to-cart, checkout and purchase events fire once and a purchase isn't counted twice.
6. **Email and DNS:** move automated flows (abandoned cart, welcome, order notifications) and keep the MX, SPF and DKIM records when DNS changes.
7. **First days:** watch 404s, Search Console, organic traffic, conversion, payment errors and ad measurement. Don't delete the old system or its backup until the checks pass.

## Guardrails

- Bulk store changes, price changes and publishing need the user's approval. So do redirect, DNS and payment changes during a move.
- Discount and urgency wording that may fall under consumer law needs a lawyer's check before it is published.
- Never print or commit API keys, shared secrets or store tokens.
