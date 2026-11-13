# Pre-submission check

Use before a first submission, before resubmitting after a rejection, or when the app enters a risky category.

**Output:** every item as pass / fail / unknown, its evidence (file path, screen or App Store Connect field), and a suggested fix for each item that fails.

Lines marked **Implementation note** are not from the sources; they show how to apply the rule in a Flutter + RevenueCat + Firebase project.

## A. Account and data (5.1.1(v))

- [ ] Does the server hold data tied to the user? An anonymous uid counts. If so, Settings offers "Delete account" in a single flow (K1).
- [ ] Deletion completes inside the app; sending an email or filling in a form does not count (K1).
- [ ] With Sign in with Apple, deletion revokes the Apple token on Apple's servers (K2).
  - **Implementation note (Firebase Auth):** sign in again with Apple to get an `authorizationCode` → `FirebaseAuth.instance.revokeTokenWithAuthorizationCode(code)` (present in firebase_auth 6.7.0) → delete the Firebase user and the server data. Without Firebase, the backend calls Apple's revoke endpoint.
  - **Implementation note (RevenueCat):** after deletion, call `Purchases.logOut()` to drop the local identity. The subscription belongs to the user on Apple's or Google's side; the user cancels it.
- [ ] App Store Connect → App Review Information → Notes: the deletion steps ("Settings → Delete account → Confirm") and a link to a short screen recording (K3).

## B. Store text and price

- [ ] The description ends with Privacy Policy, EULA (Terms of Use), Terms and Support links, plus how auto-renewal works and how to cancel (K4).
- [ ] Features that need the subscription are marked as such in the description; listing them without saying so draws a 2.3.2 rejection (K4).
- [ ] On the first submission the weekly plan is below $9.99 (K5). This is not a written Apple rule; raise the price or add packages after approval.
- Price comparison: see the reference anchors in [paywall-pricing.md](paywall-pricing.md) (K20); they are a comparison, not a target.
- [ ] Screenshots come from real screens: little text, one message per screen (K12).

## C. Paywall honesty (3.1.2, 5.6)

- [ ] The billed amount is the most prominent figure on the paywall. If an annual plan shows a weekly or monthly equivalent, that figure is smaller than the billed amount (K6).
- [ ] With a trial, the paywall states the trial length, the amount charged when it ends, and that the plan renews automatically (3.1.2(c)) (K4).
- [ ] Countdowns, "limited offer" text or discount badges appear only when there is a real discount (K6).
- [ ] **Implementation note (Flutter):** prices are not hard-coded. `StoreProduct.priceString` and the period come from RevenueCat, so the paywall text cannot drift from the store price.
- [ ] Every paywall variant the server can show (offerings, experiments) is at least as clear about price and terms as the one the reviewer sees (K31, K6).
- [ ] The system rating prompt is never offered in exchange for a reward or an unlock (K52). Timing: [paywall-pricing.md](paywall-pricing.md), onboarding step 4.

## D. Category and originality risk

- [ ] Check which apps in the niche were removed in the last 30 days (for example screensdesign.com/removed) (K7).
- [ ] The icon and name don't imitate a known app; the name, subtitle and keywords carry no other company's brand or product name (5.2.1); the account has no near-copies of one app (K8, K27).
- [ ] The binary and assets (icon, images, sounds) don't look derived from another app's template (K8).
- [ ] Crowded category (for example astrology or fortune-telling, dating, AI photo): before the first submission, prepare the difference evidence: a numbered list of what sets the app apart, mapped to the screens the reviewer will see, and a one-page technical summary (K34, K7). Details: [rejection.md](rejection.md), step 4.
- [ ] AI image or video generation: non-consensual nudity and "undressing" output is blocked in the model or the provider's safety setting, not only hidden in a menu, and users have a "report" path from the result (1.2) (K32). Describe both in the reviewer notes.
- [ ] Health, fitness or finance: the source of every displayed value (ranges, scores, doses) and the expert or institution behind it are visible inside the app (1.4.1) (K9).

## E. Hidden features and the release binary (2.5.19, 5.6)

- [ ] Every feature that can be switched remotely (feature flags, remote config, server-sent modes or templates) is visible in the reviewed build and described in the reviewer notes. Nothing new or hidden is turned on by a flag after approval (2.5.19) (K31).
- [ ] A feature that drew a rejection is fixed inside the build, not switched off on the server (K31).
- [ ] Scan the binary in the release archive, not the source, with `strings` and `nm` before uploading (K30). Look for switches that unlock paid features (test or debug keys), remote-config or eval patterns, and dynamic calls (`NSClassFromString`, `performSelector`) leaked by an unused SDK. Remove an unused SDK that leaks them.
  ```
  strings YourApp.app/YourApp | grep -iE "(remote_config|eval|bypass|is_enabled)"
  nm -u YourApp.app/YourApp | grep -E "NSClassFromString|performSelector"
  ```
  A match is not a rejection: `eval` appears inside ordinary words and many legitimate SDKs use `NSClassFromString`. Check what each match is.
  - **Implementation note (Flutter):** the Dart code is in `Runner.app/Frameworks/App.framework/App` and the native code in `Runner.app/Runner`; scan both and add the project's own debug names (developer menus, simulated purchases) to the pattern. Text from localisation files is compiled into every build, so the real test is that the debug UI doesn't appear in the TestFlight build.

## F. Screen fit (iPhone Duo)

Steps and implementation notes: [foldable-screens.md](foldable-screens.md).

- [ ] Tested closed, open and rotated (K13).
- [ ] Navigation is not a custom-drawn bar, or it adapts to the width (K14).
- [ ] Paywall: content at most ~600pt and the purchase button ~400pt, centred; on the closed screen the price and button are visible without scrolling; the close button sits in the safe area and is accessible (K15).

## G. Right before submitting

- [ ] Scan the source code and the App Store Connect metadata (description, keywords, age rating, reviewer notes, demo account) with an agent skill that checks them against the guidelines, for example `dabodamjan/app-store-rejection-checker` (K47). Each finding gives a guideline number, the evidence in the repo, a fix and a confidence level.
  - Verify low-confidence findings by hand, then add every finding to this pass / fail list.
  - It is a static check: crashes, restore purchases and server-sent content are not covered. It doesn't replace the binary scan (section E) or walking the app (last item).
  - Check first how much of the project's language it reads (for example Dart). Installing a third-party skill is the user's call.
- [ ] Read the review archive before every submission ([rejection.md](rejection.md), step 7): no guideline that drew an earlier rejection may come back a second time (K35, K36).
- [ ] New subscriptions: consider adding a TestFlight screenshot that shows every plan loading to the reviewer notes; new products may fail to load during review (2.1(b)) (K33).
- [ ] Risky category or an earlier rejection: consider booking an App Review appointment first (K10). Steps: [rejection.md](rejection.md).
- [ ] Metadata and the build go through the CLI or the store API, with a preview first. The `.p8` key and the Play service-account JSON never enter the repo (K29).
  - **Implementation note:** `flutter build ipa` → `asc publish appstore --app <id> --ipa build/ios/ipa/<name>.ipa --version <x.y.z> --submit --confirm`, after `asc metadata apply --dry-run`. Android: `flutter build appbundle` → `gpc releases upload <aab> --track internal`.
  - **Google Play (consider):** create the app in Play Console by hand first; the API cannot create a new app, but later releases, the first one included, can go through it. Give the automation service account release, store-listing and review permissions for that app only, not Admin, and upload to the internal track first (K46). For a new personal developer account, check Google's current testing requirements before planning the production date.
- [ ] If the agent has simulator or device tools (for example Apple's Xcode plugin for Claude Code, XcodeBuildMCP or ios-simulator-mcp) (K28), it walks the app like a reviewer: first launch → onboarding → paywall → restore purchases → delete account.
