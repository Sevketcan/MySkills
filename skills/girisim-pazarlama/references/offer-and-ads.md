# Offer and ads check

Use this before recommending ads or more traffic, when traffic arrives but money doesn't, and for ad copy, running and testing ads, paying creators and showing comparison data.

## 1. Offer (G10)

Ask for a one-sentence answer to each question:

- Why us?
- Why now?
- How are we different from the competitor?

If an answer is missing, don't recommend ads. Work on the offer first. If the product compares other sources (prices, ratings, discounts), section 8 can be the difference.

## 2. Leaking bucket (G10)

1. Measure the rate from visitor to target action (signup, trial, purchase, click to the store) per page type.
2. Fix the weakest step before adding traffic.
3. If traffic comes from social ads or bio links, consider testing signup from inside the apps where the link opens: their in-app browsers can block Google sign-in. If it fails, detect the in-app browser and show a screen that leads to the external browser, with a way to continue by email (G29).

## 3. Ad copy (G26)

1. Collect competitors' 1-2 star reviews (marketplaces, app stores, Google) and list the complaints in the buyers' own words.
2. Pick the buyer's single biggest doubt.
3. Make the first line show that the product removes that doubt. Back it with proof, not adjectives: a test report, the origin, a price history.
4. Run the copy past the ICP agent before it ships ([icp-agent.md](icp-agent.md)).

## 4. If ads are running (G11, G28, G33)

1. **Break-even ROAS (G11).** Before judging ROAS, consider computing break-even ROAS as roughly 1 / gross margin before ad spend, and the ad cost per order as a share of the order value. A low-basket product can lose money at a ROAS that is profitable for a high-basket one. Take the margin from the user; don't assume it.
2. **Protect the winner (G28).** Don't copy a working ad to narrow its targeting, and don't change it in its first days. Keep it running and raise its budget gradually; agree the pace with the user.
3. **Test creative every week (G33).**
   - Don't rely on one format: test static ads alongside video. Statics are quick to make and read at a glance.
   - Don't rely on one creative: add new angles every week as new ads, next to the winner rather than in place of it.
   - Let the numbers pick the winner, then go back to step 2.
   - App install and subscription campaigns: `mobil-yayin-buyume`. Producing video variants: `video-icerik-uretimi`.
4. **New or existing customers (G11).** Consider testing whether ads bring new customers rather than existing ones:
   - exclude existing customers in one ad set and compare;
   - report the cost per new customer separately, and measure repeat sales on their own;
   - some platforms reportedly offer a campaign setting that aims ads at new or existing customers; confirm it exists in the account before relying on it.

## 5. Search ads (G27)

Consider bidding on product + feature terms instead of category words, and adding informational patterns (benefits, recipe, how to, is it harmful) as negative keywords. On Reddit a "how do I" post that describes a problem is intent ([intent-posts.md](intent-posts.md)); in a search ad, "how to" usually means someone learning the topic.

## 6. Creators and clippers (G24, G25)

1. **Check the audience first.** Before paying a creator, or copying a format that looks viral, check where the followers are against the target market (G25).
2. **Pay for results:** only verified views, a cap per clip, and signups counted per clip or creator with their own link or code. Pay more to those who convert (G25).
3. **Run it as a portfolio** of many creators and clips rather than one bet (G24). Consider judging the programme as a whole: one breakout can pay for many misses.
4. Report it as in section 7. Producing the clips: `video-icerik-uretimi`.

## 7. Content and UGC reports (G12)

For high-volume content or UGC, consider reporting the floor (the lowest day) instead of the peak.

## 8. Comparison products (G32)

When the product shows prices, ratings or discounts from other sources:

1. Don't show a source's inflated rating or discount as is.
2. Correct it against your own data: rescale ratings within each source's own range, and compute discounts from your own price history.
3. Show the raw and the corrected value side by side, and explain the method in one sentence.
4. A corrected discount is still a discount claim. Where the law sets the reference price, check it with a lawyer ([ecommerce.md](ecommerce.md), section 7).

## Guardrails

- Opening an ad budget, paying creators or clippers and changing prices need the user's approval.
- Never invent conversion or revenue numbers; mark missing data as missing. An ad platform's conversion value is its own attribution, not revenue.
