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
- [ ] On the first submission the weekly plan is below $9.99 (K5). This is one developer's experience, not a written Apple rule; raise the price or add packages after approval.
- Price comparison: see the reference anchors in [paywall-pricing.md](paywall-pricing.md) (K20); they are a comparison, not a target.
- [ ] Screenshots come from real screens: little text, one message per screen (K12).

## C. Paywall honesty (3.1.2, 5.6)

- [ ] The billed amount is the most prominent figure on the paywall. If an annual plan shows a "weekly equivalent", that figure is smaller than the billed amount (K6).
- [ ] Countdowns, "limited offer" text or discount badges appear only when there is a real discount (K6).
- [ ] **Implementation note (Flutter):** prices are not hard-coded. `StoreProduct.priceString` and the period come from RevenueCat, so the paywall text cannot drift from the store price.
- [ ] Consider not asking for a rating during onboarding. This is an opinion from one reply in the sources, not a numbered rule and not in kurallar.md.

## D. Category and originality risk

- [ ] Check which apps in the niche were removed in the last 30 days (for example screensdesign.com/removed) (K7).
- [ ] The icon and name don't imitate a known app, and the account has no near-copies of one app (K8, K27).
- [ ] If the app generates content with AI: moderation, a "report" path, and both explained in the reviewer notes. The basis is one developer's guess at a removal reason ("unmoderated generated content"), not verified (K7).
- [ ] Health dose or medical calculation, or finance: an expert or institution is visible, with a "this is not advice" disclaimer (K9).

## E. Screen fit (iPhone Duo)

Steps and implementation notes: [foldable-screens.md](foldable-screens.md).

- [ ] Tested closed, open and rotated (K13).
- [ ] Navigation is not a custom-drawn bar, or it adapts to the width (K14).
- [ ] Paywall: content at most ~600pt and the purchase button ~400pt, centred; on the closed screen the price and button are visible without scrolling; the close button sits in the safe area and is accessible (K15).

## F. Right before submitting

- [ ] Risky category or an earlier rejection: consider booking an App Review appointment first (K10). Steps: [rejection.md](rejection.md).
- [ ] Metadata and the build go through the CLI, with a preview first (K29).
  - **Implementation note:** `flutter build ipa` → `asc publish appstore --app <id> --ipa build/ios/ipa/<name>.ipa --version <x.y.z> --submit --confirm`, after `asc metadata apply --dry-run`. Android: `flutter build appbundle` → `gpc releases upload <aab> --track internal`.
- [ ] If the agent has simulator or device tools (K28), it walks the app like a reviewer: first launch → onboarding → paywall → restore purchases → delete account.
