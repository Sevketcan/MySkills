# Distribution and acquisition

Lines marked **Implementation note** are not from the sources; they show how to apply the rule with RevenueCat.

## Distribution plan

1. **Plan distribution with the product (K24):** organic store traffic alone rarely carries a new app. Pick the channel early: paid acquisition, or a content channel built before launch (your own short-video or slideshow accounts, an expert who already has an audience). Whether paid ads are required is open: some apps grew on their own content, though one of them still turned to ads to scale.
2. **Don't depend on one store (K57):** build a second revenue leg next to iOS: Google Play, the web, or both. One terminated account then doesn't take all the revenue, and payouts arrive on different dates. Consider testing Android before assuming it won't pay.
   - **Android budget (consider):** fund Android while its CPI stays below the revenue-parity threshold: Android CPI < iOS CPI × (Android revenue per install ÷ iOS revenue per install). Take revenue per install from your own first 60 days, net of commission and refunds, and update the threshold when price, paywall or countries change (K56).

## Web funnel and monetisation

A web funnel or web checkout lowers the store commission, but the cases behind it run heavy paid traffic (K22).

1. **When:** only if paid traffic already exists or will be set up. The case behind the web funnel had hundreds of active ads (K22).
2. **Tooling:** if the project uses RevenueCat, start with Funnels + Web Billing; it is said to fit EU revenue reporting (K22).
3. **In-app links to web payment:** the rules vary by region and are not in these sources. Don't put an external payment link in the app without checking Apple's current guidelines.
4. **Implementation note (RevenueCat):** for an entitlement bought on the web to show up in the app, the RevenueCat app user id must equal the backend user id; link an anonymous user to an account first.

## Organic content

1. **A showable feature (K58):** the product needs a visual feature that a short video makes clear in about a second; streaks, community or an AI chat don't stop the scroll. An agent can scan the code for features that can be shown.
2. **Don't invent a format (K58):** find accounts in the niche that post daily and draw strong views over the last 30 days, and study their structure. Put forward the feature that fits that format naturally, and add your own angle instead of copying the template. Production: `video-icerik-uretimi`.
3. **Organic first, then paid (K25):** find the format organically first. Put budget behind the organic videos that already hold (Spark Ads on TikTok) instead of making new ads for them. Organic views alone don't predict ad success.
4. **Bio link (consider):** a link that opens the App Store app instead of a plain App Store link, with a visible "Open in App Store" button on the page in case the social app blocks the redirect (K45).

## Paid acquisition

1. **Channel:** which ad network works depends on the niche; the sources report the TikTok system below working in one niche and failing in another, where Meta worked instead. Test both with a small budget before committing (K25).
2. **Measurement:** consider setting up an MMP before running ads and connecting it to RevenueCat (K25).
   - Judge campaigns on cost per paying user, not cost per trial (K43). Cost per payer = cost per trial ÷ trial-to-paid rate; show the trial-to-paid rate, cost per purchase and D7/D30 revenue next to cost per trial.
   - Don't scale up or switch off a campaign before its trial cohort matures: the trial has ended and the first renewal has passed (K43).
   - Move the optimisation event toward payment (for example Subscribe instead of Start Trial) once volume allows. Below the volume an ad set needs to leave the learning phase (reported as about 50 events a week on Meta; check Meta's current guidance), stay on a shallower event: the trial or a key action (K43).
   - Choose countries by cost per payer, not cost per install (K43).
3. **Predicted value (K55):** when payment volume is too low to optimise on, send a predicted value before the user pays: a conversion value at trial start for Google tROAS, or value optimisation on Meta.
   - Build the prediction from past cohorts: how onboarding answers and day-one behaviour relate to later payment. A new app doesn't have that data yet.
   - Compare it with real revenue every week; a biased prediction scales the campaign toward the wrong audience.
4. **Creative concepts (K54):** keep targeting broad on Meta and TikTok, merge campaigns, get the variety from creative and add new concepts regularly.
   - Consider counting concepts, not ads. One working definition: a new concept changes at least two of persona, motivation, hook, format, visual world and presenter; near-copies are removed before uploading.
   - One view scales a winning video into many variations; another warns that near-copies compete for the same people. Test how many variations of a winner to run.
5. **Meta on iOS (consider)** (K44): before launching, compare the installs in the attribution tool with Meta's dashboard. With the iOS 14+ campaign switch on, move ad sets to AEM. Check the audience estimate before every launch; turning the switch off can silently narrow targeting to old iOS versions. Choose audiences and placements on your own cost-per-payer data. Setting names change; check Meta's current interface.
6. **Paid (TikTok case):** the sequence from one US case (K25). The figures are that case's parameters, not rules, and the source doesn't say over which window ROAS was measured. Recompute the budget and thresholds with the user's unit economics.
   1. Use every video as a Spark Ad, not only the viral ones.
   2. One broad campaign, one country.
   3. In the case: started at $100 a day and raised it 15-20% a week.
   4. In the case: creatives with ROAS below 1.5x were switched off.
   5. Produce new creatives every week; creative fatigue kills paid ads. Production: `video-icerik-uretimi`.

## Idea stage

1. **Multiply a proven pattern (K27):** small, focused apps are one portfolio path: the same feature applied to new objects, or apps for unserved keyword pockets in the same category. Similar apps on the same account carry 4.3 risk (K8).
2. **Mine competitor reviews (consider)** (K59): have an agent cluster competitors' 1-2 star reviews into the five most common complaints, in the users' own words.
   - Prefer a market whose complaints are about the product (bugs, missing features). Don't count price complaints as an opening; those users will write the same review about your app.
   - Top-grossing apps usually have high ratings, so read the reviews instead of filtering by rating.
   - Many complaints don't prove people will pay for a new app; test that separately.
