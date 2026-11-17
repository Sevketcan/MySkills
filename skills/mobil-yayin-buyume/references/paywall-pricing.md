# Paywall, onboarding and retention

Lines marked **Implementation note** are not from the sources; they show how to apply the rule with RevenueCat.

## Onboarding and first session

1. **Placement:** start with the paywall at the end of onboarding, and keep the later paywalls inside the app too (K16). The sources also describe the opposite flow for products that show a result in the first minute: no onboarding, first value before the home screen and the paywall (K40). Test both flows; don't settle it by rule.
   - Account creation comes after the purchase or the first piece of work, or at the end of onboarding just before the paywall; both appear in the sources (K40). Deferring the account doesn't remove the account-deletion requirement ([pre-submission.md](pre-submission.md), section A).
2. **Onboarding content:** if the flow has one, personalise it with a short survey or questions, show the problem and social proof, and use the loading screen to show value or ask a question (K17).
   - Consider a confirmation screen after the questions ("here is what we understood, here is how we'll help") and a paywall headline tied to the goal the user just picked (K17).
   - On the paywall, consider placing social proof (awards, rating) right next to the price (K17; one case, not measured).
3. **Measure onboarding screen by screen (K51):**
   - Log every screen view and every step forward as an event.
   - Build a separate funnel for the core action (the first result, the first reading, the first transaction).
   - Give every screen you add or remove its own A/B test; that needs enough traffic.
   - The sources read this funnel two ways: fix the largest drop between screens first, or ignore the completion rate and judge by D1 (and D5) retention and day-one subscription across everyone who started onboarding. A longer flow can lose more people and still earn more. Report all three metrics in each test; don't settle it by rule.
4. **Rating prompt (K52):** show the system rating prompt right after a success, once the user has had the first value. Not at the start of onboarding, not after an error, and never in exchange for a reward or an unlock.

## Paywall and offer

1. **Plan set:** start with two plans in most cases, one of them preselected, and move a rarely used plan behind "all plans" (K21). Vendor data shows this is common, not that it performs better; use it as a starting assumption. Which plan to preselect (annual, or a discounted weekly) differs between sources; test it per category.
2. **Trial:** the sources disagree on trial length; test it instead of assuming.
   - One starting point sets the trial by plan: 3 days on weekly plans, 7 days on monthly and annual plans (K19).
   - Other data favours longer trials: test a 3-day trial against a longer one (K38).
   - With a short trial, day one decides; most cancellations happen on the first day, so the first session has to prove the product (K38).
   - Judge every trial test on refunds too (next step, "Hard paywall and refunds").
3. **Hard paywall and refunds:** if you test a hard paywall (no close button) against a soft paywall or freemium, judge it on trials plus direct purchases, revenue per install and refund rate, not on trial count alone (K39). Apple counts excessive refunds against the developer (5.6.4); watch the refund rate in App Store Connect and RevenueCat after each paywall change.
   - **Refund requests (consider):** answer Apple's request for consumption information automatically with usage data (Consumption API). RevenueCat can send it, or the backend can call it (K50).
4. **Price:** typical prices in a vendor report are about $6.99 weekly, $9.99 monthly and $39.99 annual (K20). They are a reference, not a target; choose the price from your own market and test. For the first submission, see the weekly-price check in [pre-submission.md](pre-submission.md), section B (K5).
5. **Test order:** consider testing the offer first (trial length, plan set, localisation), then visuals and copy (K18). Change one variable per test.
6. **Personalisation opportunity:** consider a different offer per acquisition source, for example TikTok traffic versus organic (K23).
7. **Seasonal offers (consider):** a time-limited offer to existing free users around Black Friday and in January; in vendor data a Christmas-only campaign made little difference (K42). The countdown runs only while the offer is real and comes down when it ends (K6). A lifetime plan can eat into annual subscriptions.
8. **Android billing (consider):** turn on Google Play billing retry and the grace period; involuntary billing failures are a large share of Play cancellations (K41).
9. **AI credits (consider):** if the app sells generative-AI credits as consumables, Apple allows credits that expire at least 12 months after purchase, by application (K48). Check Apple's current page first. The conditions the sources list:
   - expiring credits are a new in-app purchase; an existing product can't be converted;
   - the app must already be live and selling consumables to apply, and credits for anything other than generative AI can't expire;
   - the paywall shows the term and what the credits are for, and the app shows the current balance;
   - subscription credits are spent first, then the credits closest to expiry;
   - users with a remaining balance get a reminder 30 and 7 days before expiry; plan how to reach anonymous accounts.
10. **AI inference cost (consider)** (K61): for a small text-based AI feature on iOS, Apple Foundation Models on Private Cloud Compute have no cloud API cost if the developer is in the App Store Small Business Program, has fewer than 2 million first-time downloads on every app, and holds the PCC entitlement. Check Apple's current page first.
    - Daily usage limits apply and expanded access will cost a fee later; build a fallback to a paid model for the limit and for devices or regions without Apple Intelligence.
    - If an app passes 2 million first-time downloads, the developer must migrate within 6 months. Keep the model behind one interface.
    - **Implementation note (Flutter):** Foundation Models is a Swift framework; call it through a platform channel.
11. **Implementation note (RevenueCat):**
    - Each variant is its own offering. The app fills the paywall from `Purchases.getOfferings()` → `offerings.current`; plans and prices are not hard-coded.
    - Run the test in RevenueCat Experiments. Read the estimated 12-month LTV in the results, then roll out the winner.
    - Every variant served after approval is at least as clear about price and terms as the paywall the reviewer saw (K31, K6). Whether a paywall tool that changes the flow without a new build falls under 2.5.19 is an open question; keep every remote change within the flow the reviewer saw.
    - The trial is defined in the store as the product's introductory offer; a different trial length needs a separate product or offer in the store.

## Cancellation and win-back

1. **Cancellation message (consider):** set up Apple's Retention Messaging in App Store Connect; it needs no code (K49).
   - Start with a message without an offer: what the user loses, an answer to the cancel reason, or what is coming next.
   - Keep prices and discounts out of the message text; Apple shows an offer separately.
   - Add a discount only when price stands out in reviews and cancel reasons, and judge it by revenue per subscriber, not by the save rate. Users still in a trial can't receive the offer.
2. **Win-back offers:** the sources point in different directions: an offer to everyone who cancels, no win-back offers at all because of account risk, or a reward tied to an action. Don't settle it by rule. Start with the offerless message above; give a discount only as a real time-limited offer (K6) and measure it by revenue.
   - Consider tying the comeback reward to an action instead of a discount (for example a streak restored after three lessons), tested against a paid restore; measure activity a week later (K53).
3. **When done,** re-run section C (paywall honesty) of [pre-submission.md](pre-submission.md).
