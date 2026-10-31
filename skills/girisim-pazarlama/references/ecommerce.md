# E-commerce and marketplace seller tooling

Use this for a seller's own tools on a store or marketplace platform, bulk listing work, marketplace AI policy, competitor ad creative and orders from AI search.

## 1. Own seller tool (E1, E3)

1. Build the seller's own tool on the platform's API or CLI with AI, instead of renting a monthly tool for the job (for example Etsy Open API v3, Shopify CLI or AI Toolkit) (E1).
2. When a model writes the API code, include an instruction such as: "Don't invent endpoints or fields; use the current official documentation." (E3)
3. Request only the permissions the job needs (E3).

## 2. Approval gate for bulk changes (E2)

Prepare → show the change as a list → the user checks it → apply only after the user says "apply". Nothing is written to the store before that.

## 3. Listing scoring (E4)

Consider scoring each listing out of 100 against the user's own rules document, with the broken fields and the top 5 fixes.

## 4. Marketplace AI policy (E6)

If any design, text or image is AI-generated, have the user open the marketplace's current policy and check against it. Points reported for one marketplace, to confirm in the official text:

- disclose AI use;
- the seller's own role is visible;
- at least one real photo;
- no bot-driven, one-click bulk listing.

Rely on the official text, not on a social post about it.

## 5. Competitor ad creative (E7)

1. Consider tagging competitors' running ads by hook, format, offer, CTA and awareness stage.
2. When adapting, never copy an ad verbatim, and tell the user about the brand and copyright risk.
3. Producing variants with the user's product: `video-icerik-uretimi`.

## 6. Orders from AI search (E10)

Consider measuring ChatGPT and Perplexity visits as a separate channel and comparing their conversion with Google. Setup steps: `seo-ai-arama`.

## Guardrails

- Bulk store changes, price changes and publishing need the user's approval.
- Never print or commit API keys or store tokens.
