# Web funnel and acquisition

Lines marked **Implementation note** are not from the sources; they show how to apply the rule with RevenueCat.

## Web funnel and monetisation

A web funnel or web checkout lowers the store commission, but the cases behind it run heavy paid traffic (K22).

1. **When:** only if paid traffic already exists or will be set up. The case behind the web funnel had hundreds of active ads (K22, K24).
2. **Tooling:** if the project uses RevenueCat, start with Funnels + Web Billing; it is said to fit EU revenue reporting (K22).
3. **In-app links to web payment:** the rules vary by region and are not in these sources. Don't put an external payment link in the app without checking Apple's current guidelines.
4. **Implementation note (RevenueCat):** for an entitlement bought on the web to show up in the app, the RevenueCat app user id must equal the backend user id; link an anonymous user to an account first.

## Acquisition

1. **Budget:** plan paid acquisition from the start (K24).
2. **Organic:** consider finding the video format with an organic TikTok account first, as in the source case. Organic views don't predict ad success (K25).
3. **Measurement:** consider setting up an MMP before running ads and connecting it to RevenueCat (K25).
4. **Paid:** the sequence from one US case (K25). The figures are that case's parameters, not rules, and the source doesn't say over which window ROAS was measured. Recompute the budget and thresholds with the user's unit economics.
   1. Use every video as a Spark Ad, not only the viral ones.
   2. One broad campaign, one country.
   3. In the case: started at $100 a day and raised it 15-20% a week.
   4. In the case: creatives with ROAS below 1.5x were switched off.
   5. Produce new creatives every week; creative fatigue kills paid ads. Production: `video-icerik-uretimi`.
5. **At the idea stage:** porting a proven pattern to a new vertical is one portfolio path (K27), but similar apps on the same account carry 4.3 risk (K8).
