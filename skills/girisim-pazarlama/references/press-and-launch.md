# Press emails, launch day, launch video and directories

## 1. Press email (G13)

One approach to try: bring journalists a story from the product's own data, not a launch announcement.

1. **Pick one surprising finding** from the product's own data. If the data isn't published on a page yet, consider a statistics page first (`seo-ai-arama`): journalists and AI assistants link to where they find the number.
2. **Personalise the first line.** For each journalist, find their latest article and open with it.
3. **Draft** in the journalist's language, from this structure:

   ```
   Subject: [Trend] is changing [industry], with data
   Hi [Name],
   I read [your latest article]; the [specific point] angle was great.
   Our data shows [one surprising finding]. For example: [one-line real user story].
   If useful, I can share the full data or set up a call with the founder.
   ```

4. **Keep it under 100 words, with no ask.** The user sends it.

## 2. Launch day (G6)

One approach that worked for an open-source product sold to developers. Adapt it to the product:

- List the communities the user belongs to and draft a short, personal announcement for each.
- If there are several launches (open-source release, Product Hunt, changelog), consider putting them on the same day, with the README and the announcements linking to each other.
- Instead of a polished demo, consider one memorable video and a single post around it; brief it as in section 3. Production: `video-icerik-uretimi`.
- After the launch, keep a regular changelog with real news only (G4).

## 3. Launch video brief (G35)

This skill writes the brief: what the video shows, where it goes and what it asks for. Production lives in `video-icerik-uretimi`. Treat each point as a hypothesis to test:

1. **One promise, shown working.** Pick the single job the product promises and show the real product doing it. Consider a plain screen recording as the first version; it can look more genuine than a polished film. If the user wants both, compare them.
2. **The audience's words.** No jargon; describe the new idea the way the target users talk about the problem.
3. **Look at the first seconds of others.** Before recording, consider watching the first 5 seconds of well-watched and poorly watched launches in the same category, and noting what the first frame shows. Judge "well-watched" against each account's usual reach.
4. **Where and what for.** Share it where the audience already is (G6). If the product isn't open yet, give the video a single call to action: the waitlist.
5. **Spark, not channel.** A launch video can fill a waitlist; plan the channel that carries growth afterwards ([channel-plan.md](channel-plan.md)).

## 4. Directory and awesome-list submissions (G34)

Launch directories and awesome-lists can give a new product cheap backlinks and help it get indexed. Don't plan them as a revenue channel; set the expectation with the user before spending time on them.

1. **Check the list is alive.** A status code is not enough: parked or for-sale domains still return 200. Check the page title or body, and drop dead entries.
2. **One product manifest.** Keep name, short and long description, category, links and logo in one file, and fill every submission from it.
3. **Prepare, then get approval.** Draft each entry or awesome-list pull request from the manifest and show the user the full list. Submitting is publishing: by default the user submits the forms and opens the pull requests. Submit an open form or open a pull request yourself only when the user explicitly says so for that item.
4. **The user handles sign-ins and bot checks.** Forms behind a login and forms with a CAPTCHA are submitted by the user. Hidden bot-trap fields mean the site doesn't want automated submissions; leave those forms to the user too.
5. **Stop at payment.** If a "free" listing asks for payment along the way, stop and ask; paid fast tracks need the user's approval.
6. **Follow each list's rules.** For awesome-lists, read the contribution guide and keep to one well-formed pull request per list.
7. **Measure what went live.** Track listings that actually appeared and pull requests that were merged (a submission is not a link), new referring domains in Search Console, and signups and payments. Check after four weeks, as in [channel-plan.md](channel-plan.md).

For an MCP server or API, start with the official registry: [agent-distribution.md](agent-distribution.md).

## Guardrails

- The user sends every email and posts every announcement.
- Directory and awesome-list submissions follow section 4: approval first; the user handles sign-ins and CAPTCHAs. Never solve a CAPTCHA or get around a bot check.
- Don't paste the same text into many places (G15).
