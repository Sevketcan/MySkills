# Paywall, offer and pricing

Lines marked **Implementation note** are not from the sources; they show how to apply the rule with RevenueCat.

## Steps

1. **Placement:** put the paywall at the end of onboarding, and keep the later paywalls inside the app too (K16).
2. **Onboarding:** personalise it with a short survey or questions, show the problem and social proof, and use the loading screen to show value or ask a question (K17).
3. **Plan set:** start with two plans in most cases, one of them preselected, and move a rarely used plan behind "all plans" (K21). Vendor data shows this is common, not that it performs better; use it as a starting assumption.
4. **Trial:** in one vendor's data, 3-day trials did better on weekly plans and 7-day trials on monthly and annual plans (K19). Start there as a default and confirm it with your own test.
5. **Price:** typical prices in a vendor report are about $6.99 weekly, $9.99 monthly and $39.99 annual (K20). They are a reference, not a target; choose the price from your own market and test. For the first submission, see the weekly-price check in [pre-submission.md](pre-submission.md), section B (K5).
6. **Test order:** consider testing the offer first (trial length, plan set, localisation), then visuals and copy (K18). Change one variable per test.
7. **Personalisation opportunity:** consider a different offer per acquisition source, for example TikTok traffic versus organic (K23).
8. **Implementation note (RevenueCat):**
   - Each variant is its own offering. The app fills the paywall from `Purchases.getOfferings()` → `offerings.current`; plans and prices are not hard-coded.
   - Run the test in RevenueCat Experiments. Read the estimated 12-month LTV in the results, then roll out the winner.
   - The trial is defined in the store as the product's introductory offer; a different trial length needs a separate product or offer in the store.
9. **When done,** re-run section C (paywall honesty) of [pre-submission.md](pre-submission.md).
