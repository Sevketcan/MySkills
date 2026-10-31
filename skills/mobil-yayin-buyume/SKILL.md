---
name: mobil-yayin-buyume
description: "Prepare iOS and Android apps for store review and grow them after launch: check rejection and removal risks (account deletion, paywall honesty, risky niches) before submission, answer rejections, and plan paywalls and pricing tests, foldable-screen fit, store pages (ASO), web funnels and paid acquisition."
---

# Mobile Release and Growth

Stay in the store first, then grow. The order for every app is: pre-submission check (rejection and removal risk), paywall and offer, store page, acquisition. Then test one change at a time and decide on real data.

## Before starting

- Read the project's own documents first (README, AGENTS.md, plan, growth or store files). Project decisions override the generic rules here.
- Read the project (read only):
  - dependencies: for Flutter, `pubspec.yaml` (`purchases_flutter`, `purchases_ui_flutter`, `firebase_auth`, Sign in with Apple packages);
  - authentication: anonymous or not, whether Sign in with Apple is used, and what the server stores per user;
  - the paywall file, the store text file (for example `docs/store/listing.md`), and whether iPad is targeted (`TARGETED_DEVICE_FAMILY` in `ios/Runner.xcodeproj`).
- Place the app's category: is it in a risky niche? AI photo or video, AI companion, video chat or dating, health dose calculation, finance, or a look-alike of a known app (K7, K8, K9).
- Lines marked **Implementation note** in the references are not from the sources. They show how to apply a rule with Flutter, RevenueCat or Firebase; check them against the installed package versions.

## Choose the mode

Use only the mode the request needs:

1. **Pre-submission check**: before a first submission or an update. Account deletion, store text and price, paywall honesty, category risk, screen fit, final steps. Read [pre-submission.md](references/pre-submission.md).
2. **Rejection response**: a rejection, a repeated rejection or a terminated developer account. Read [rejection.md](references/rejection.md).
3. **Paywall and pricing**: paywall placement, onboarding, plan set, trial, price anchors and offer tests. Read [paywall-pricing.md](references/paywall-pricing.md).
4. **Foldable and large screens**: iPhone Duo closed, open and rotated; adaptive navigation; paywall width. Read [foldable-screens.md](references/foldable-screens.md).
5. **Store page (ASO)**: keywords, Custom Product Pages, screenshots, metadata kept in the repo. Read [store-page.md](references/store-page.md).
6. **Web funnel and acquisition**: web checkout, organic and paid acquisition, measurement before ads. Read [web-funnel-acquisition.md](references/web-funnel-acquisition.md).

When the request is broad, go 1 → 3 → 5 → 6. If the app has not passed review yet, finish mode 1 before any growth work.

## Principles

- Don't start growth work while a rejection or removal risk is still open.
- The billed amount is the most prominent figure on the paywall; urgency and discount badges only with a real discount (K6).
- Put the paywall at the end of onboarding and keep the later in-app paywalls (K16).
- Plan paid acquisition from the start; organic store traffic alone rarely carries a new app (K24).
- Change one variable at a time and judge it on real data.
- Benchmark prices and case figures are references, not targets. Recompute prices, budgets and thresholds with the user's own unit economics.
- Where a reference says "consider" or "start with", the rule is a starting assumption; confirm it with the project's own test.

## Guardrails

- **No invention:** never make up revenue, downloads, review times or conversion rates. Don't present one app's case figures as rules.
- **Approval:** store submission, price changes, publishing a RevenueCat offering, paywall or experiment, opening an ad budget and changing store-account settings need the user's approval.
- **No dark patterns:** don't sell an annual plan at its weekly price, add a fake countdown or hide the billed amount.
- **No copies:** don't imitate another app's icon or name, and don't put near-copies of one app on the same account.
- **External payment links:** don't add an in-app link to web payment without checking Apple's current guidelines; the rules vary by region.
- **Guideline numbers** (5.1.1(v), 3.1.2, 5.6, 4.3, 2.1, 3.2(f)) come from the sources. Check Apple's current text before quoting them.
- **Vendor data:** benchmarks from paywall, subscription or funnel vendors describe their own customers; don't present them as independent evidence.
- **Secrets:** never print or commit `AuthKey.p8`, the Play service-account JSON or a RevenueCat secret key.

## Boundaries

- TikTok or Reels videos, ad creative variants and the App Store preview video: `video-icerik-uretimi`. This skill keeps the budget, MMP, ROAS and offer decisions.
- Search and AI-search visibility of the app's landing or web funnel pages: `seo-ai-arama`.
- General channel plan (Reddit, press, launch day): `girisim-pazarlama`.
- Mobile games: the store checks apply from here; Steam timing, demo and wishlists: `indie-oyun-yayin`.
- Not covered by the sources: Google Play review and policy rules, App Privacy labels and ATT, in-app external payment link rules, the App Store keyword field's technical details. Use Apple's and Google's current documentation.

## Completion

End each session with:

- for a pre-submission check: each item as pass / fail / unknown, with its evidence (file path, screen or App Store Connect field) and a fix for each failing item;
- the next single change to test and the data that will judge it;
- changes made, listed separately from proposals;
- decisions waiting for the user's approval.

The (Kn) markers point to [kurallar.md](references/kurallar.md) (Turkish), which lists each rule's sources and evidence level. It is compiled from the owner's research notes in Twitter Notes (taslak v0.3).
