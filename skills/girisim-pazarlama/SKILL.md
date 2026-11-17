---
name: girisim-pazarlama
description: "Plan acquisition for a small product or startup: choose and order channels, find buying-intent posts, build a customer-language ICP agent, check the offer, ad copy, running ads and creator payouts, draft data-led press emails and launch plans, position AI services, build e-commerce seller tooling with approval gates, and open the product to AI agents through an MCP server listed in the registry and directories."
---

# Startup Marketing

Offer and leaks first, then one channel, then the next. Learn the product, its revenue model and its stage. Check the offer and the step where money leaks. Pick the one channel that fits the stage and measure it; when it works, add the next channel on top without dropping the first. Decide on real measurements, not on figures from other people's case studies.

## Before starting

- Read the project's own growth, revenue and decision documents first, read-only (for example `docs/BUYUME.md`, `docs/DECISIONS.md`): the growth plan, the revenue model (subscription, affiliate or commission, ads) and the analytics source. Project decisions override the generic rules here.
- Establish the stage: number of customers or users (or MRR), and which channel brings them today. If it is unknown, ask; don't guess.
- Agree who sends what. Emails, DMs, Reddit replies, press emails, ad budgets and publishing are the user's job; you prepare drafts.

## Choose the mode

Use only the mode the request needs:

1. **Channel plan**: which acquisition channel to work on now, in what order, and how to tell that it works. Read [channel-plan.md](references/channel-plan.md).
2. **Buying-intent posts**: find posts on Reddit, forums and comment sections where people ask for what the product does, and draft replies. Read [intent-posts.md](references/intent-posts.md).
3. **Customer language and ICP agent**: collect customers' own words and build an agent that reviews copy, ads and offers as that customer. Read [icp-agent.md](references/icp-agent.md).
4. **Offer and ads check**: why us, why now, the leaking step of the funnel, ad copy, running, testing and measuring ads, paying creators and clippers, correcting comparison data. Read [offer-and-ads.md](references/offer-and-ads.md).
5. **Press and launch**: a data-led email to journalists, a launch-day plan, a launch video brief, or directory and awesome-list submissions. Read [press-and-launch.md](references/press-and-launch.md).
6. **AI service positioning**: scope and sell an AI service or agent product. Read [ai-service.md](references/ai-service.md).
7. **E-commerce seller tooling**: own tools on a platform API, API access and test modes, bulk listing edits, listing scoring, marketplace AI policy, competitor ad breakdown, discount and urgency claims, moving to a new platform. Read [ecommerce.md](references/ecommerce.md).
8. **Turkish tax question**: the 20/B exemption, Bağ-Kur and VAT on foreign subscriptions, as information only. Read [turkey-tax.md](references/turkey-tax.md).
9. **Agent distribution**: open the product to AI agents through an API or MCP server, publish it to the MCP registry and list it in directories. Read [agent-distribution.md](references/agent-distribution.md).

When the request is broad ("how do I get customers?"), run mode 4 first, then mode 1.

## Principles

- Offer before budget: don't scale with ads or traffic until the offer answers why us, why now and how it differs, and the leaking step is fixed (G10).
- Channels stack: add the next channel on top of the one that works; don't drop it (G1).
- Consider working one channel at a time: push it until it works, then add the next (G2).
- Paid ads come last, once unit economics hold (G3).
- Find buyers by intent signal, not by lists. One well-aimed reply beats many generic ones (G7, G9).
- Work in the customer's own words (G8).
- Revenue figures from case studies are examples, never targets or forecasts.

## Guardrails

- **Drafts only:** never send messages, replies, DMs, emails or posts on the user's behalf.
- **No spam:** don't recommend auto-reply bots, mass cold messaging, pasting the same text in many places or copying the same post across accounts (G15). Follow each community's rules.
- **No invention:** never make up revenue, conversion, follower or reach numbers, and don't present figures from sources as rules.
- **Approval:** opening an ad budget, paying creators, changing prices, bulk store changes and publishing (including to MCP registries, directories and awesome-lists) need the user's approval.
- **Ad accounts:** if an agent tool can write to an ad account, build campaigns, ad sets and ads paused. Going live, pausing and every budget or targeting change need the user's approval. The user sets write permissions and spending caps in the platform's own account rules (G37).
- **Third-party forms and bot checks:** on directories and other third-party sites, the user signs in and submits any form behind a login or a CAPTCHA. Never solve a CAPTCHA or get around a bot check.
- **Discounts, ratings, urgency:** don't show a source's inflated rating or discount as is, and don't write urgency ("last item", "last hours") that isn't true (G32, E12). Reference-price rules and fines for discounts vary by country; have a lawyer verify the current rule before discount claims go out.
- **Vendor claims:** a vendor describing its own tool is marketing, not independent evidence. Say so when you rely on one.
- **Tax and law:** no personal tax or legal advice. Relay what the sources say and the open questions, and refer the user to a certified accountant (mali müşavir) or, for consumer-law questions, a lawyer.
- **Secrets:** never print or commit API keys or store tokens.

## Boundaries

This skill decides channel, offer and distribution. Executing a chosen channel lives elsewhere:

- SEO and AI search (ranking in Google, earning links with a statistics page, being cited in AI answers, tracking AI-search traffic): `seo-ai-arama`.
- Mobile apps (store rejection, paywall, ASO, TikTok and paid app acquisition): `mobil-yayin-buyume`.
- Video production (launch video, ad and UGC variants, clips, Reels and Shorts): `video-icerik-uretimi`. Breaking down competitor ads and paying and measuring creators stay here; rebuilding the format and producing the clips happen there.
- Games (Steam, Next Fest): `indie-oyun-yayin`.
- This skill has no rules for email marketing flows, pricing strategy or Turkish marketplace (Trendyol, Hepsiburada) seller rules.

## Completion

End each session with:

- the product's stage and the channel being worked on, with its 4-week success criterion;
- drafts prepared for the user to send, each with its target (post, journalist, community);
- changes made, listed separately from proposals;
- decisions waiting for the user (budget, prices, bulk changes, publishing) and questions for an expert.

The (Gn) and (En) markers point to [kurallar.md](references/kurallar.md) (Turkish), which lists each rule's sources and evidence level. It is compiled from the owner's research notes in Twitter Notes (taslak v0.6).
