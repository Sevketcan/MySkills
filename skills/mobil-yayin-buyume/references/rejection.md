# Rejection response

1. **Map the guideline** in the rejection message to the check list in [pre-submission.md](pre-submission.md):
   - 5.1.1(v) → section A (account deletion).
   - 2.1 (incomplete app) → the reviewer notes and demo steps (K3). 2.1(b) (the reviewer couldn't buy a plan) → consider replying with a TestFlight screenshot that shows the plans loading (K33).
   - 2.3.2 → the description doesn't say which features need the subscription (K4).
   - 3.1.2 → how the billed amount and the trial terms are presented (K6, K4).
   - 5.6 → fake urgency or a fake discount (K6), or a test or debug switch left in the release build (K30).
   - 5.2.1 → another company's brand in the app name (K8).
   - 1.4.1 → the source of health values isn't visible in the app (K9).
   - 1.2 → generated intimate imagery without a filter or a report path (K32).
   - 2.5.19 or 2.3.1 → a remotely switched or undocumented feature (K31).
   - 4.3 or 4.2.6 → a copy, spam or template appearance (K8); answer as in step 4.
2. **Check whether the same build can pass.** Consider first whether a text change or a reply with evidence resolves it; metadata, missing-product and some 4.3 rejections have passed with the same build (K33). Whatever has to change in the app changes inside the build; never "close" a rejected feature with a server switch (K31).
3. **Ask what exactly was wrong.** If the message only quotes the guideline, ask in writing which feature, screen or output is the problem (K35). Remove the cause at its root in the build, and in the model or provider settings for generated content, not only its visible entry point.
4. **4.3 and 4.2.6: answer with difference evidence, not screenshots** (K34). Write calmly. Use:
   - a short opening that asks which part looked similar;
   - a numbered list of what the app does that similar apps don't, mapped to the screens the reviewer sees;
   - a one-page technical summary (architecture, data model) or an unlisted demo video;
   - if needed, the git history, design files and issue tracker.

   The outcome is not guaranteed. An explanation with an unlisted demo video has passed a 4.3(a) rejection with the app unchanged. The exception is a rejection that arrives within seconds, which may come from automated screening (K8; not confirmed): a video alone is said not to get past it, so also make the build itself more distinct (binary, assets, name).
5. **If the same guideline comes back after two rounds,** stop arguing in Resolution Center and change channel (K10). None of these channels guarantees a different result.
   - **App Review appointment:**
     1. Go to developer.apple.com/events/view/upcoming-events and search for "app review".
     2. Pick an "App Review appointment" on a suitable date. Sessions fill quickly and requests have a deadline.
     3. In the request, give the app's Apple ID, the rejection text, the guideline number and the issue itself, plus the preferred language. An active Developer Program membership is required.
   - **Phone call:** request one through Apple Developer → Contact Us → App Review.
   - **Appeal:** submit it to the App Review Board.
6. **Describe the fix step by step** in the reviewer notes, then resubmit.
7. **Keep a review archive** from the first submission, approvals included (K35). App Store Connect may not show old rejection reasons, so keep your own copy.
   - One folder per submitted version: a screenshot of the rejection message, Apple's attachments, the guideline number, what you changed and why, and the approved build with its date.
   - Read it before every new submission.
   - An approval doesn't prove the issue is closed. The archive won't prevent a termination, but it is the evidence that makes an appeal possible.
8. **Account terminated under 3.2(f)** (K11):
   1. Export the notice and the full rejection and approval history.
   2. Appeal in the order Apple asks for: apology, explanation, prevention plan. Admit only what you actually did; document the rest with the history (the approved build, the change made inside the build).
   3. Don't open a new developer account after the notice; Apple's message says associated accounts can be closed too.
   4. Check App Store Connect regularly; a reinstatement may not be announced by email.
9. **Account-risk hygiene:**
   - Don't let the same guideline draw a second rejection: check the archive before each submission and remove the earlier cause inside the build first (K36, K35). Rejection history, even an old one, can be cited later as a 3.2(f) signal.
   - Consider planning name changes and submission frequency too; rapid resubmissions and frequent renames may read the same way (K36).
   - Consider keeping the Mac, test devices, payment card and network you use for the developer account apart from other developer accounts (K37).
