---
name: video-icerik-uretimi
description: "Plan and produce product and channel videos: validate niches and series, write short-form scripts and hooks, break down outlier videos and long-running ads, run faceless TTS pipelines, edit talking footage from word-timed transcripts, build code-driven launch clips and App Store previews, keep AI characters consistent, and package titles, thumbnails and cuts."
---

# Video Content Production

The model gives speed; the system gives quality. In every job, work in this order: gather the facts and real assets, take the structure of a reference that works (never its content), write a brief or script and get it approved, produce a small piece and review it frame by frame with local fixes, measure the render before calling it done, then measure the packaging and make variants.

## Before starting

- Read the project's own documents first (for example README, `LAUNCH.md`, `BRAND.md`, a growth plan). Project decisions about audience, voice, brand and channels override the generic steps here.
- **Goal:** product promotion (success means installs, sign-ups or sales) or channel revenue (views, RPM)? Most decisions change with the answer.
- **Platform and format:** 9:16 (Reels, Shorts, TikTok), 16:9 (YouTube, X), 1:1 (an X or LinkedIn launch post). For designed motion, consider each format its own composition rather than a crop of another; crop camera footage on the face, not the centre (VA10).
- **Real assets:** product screenshots, real outputs (for example a real before/after), logo, fonts, colours, existing audio. If something is missing, ask for it; never invent it (VA2).
- **Tools and budget:** check what is available, for example ffmpeg/ffprobe, Node (for Remotion), access to a generative model (for example through Higgsfield MCP), a TTS engine. No tool is required; work with what the project has.
- Before any paid generation (model credits, API calls), state the estimated cost and get approval.

## Choose the mode

Use only the mode the request needs:

1. **Niche, topics and series:** a channel is being started; validate the niche, find topics, turn a format into a series on a calendar. Read [niche-and-series.md](references/niche-and-series.md).
2. **Script and hook:** a 30-60 second short-form script, opening lines and curiosity loops. Read [script-and-hook.md](references/script-and-hook.md).
3. **Reference and outlier analysis:** break outlier videos or long-running ads down into a reusable structure. Read [reference-analysis.md](references/reference-analysis.md).
4. **Faceless pipeline:** explainers, documentaries or Shorts from open images, TTS, subtitles and scripted editing. Read [faceless-pipeline.md](references/faceless-pipeline.md).
5. **Launch clip and App Store preview:** a product demo in code-driven motion with a brief, a frame-numbered timeline and approval gates. Read [launch-clip.md](references/launch-clip.md).
6. **AI image and video:** choose between generative video, code motion and 3D; lock recurring characters; layer multi-shot prompts. Read [ai-generation.md](references/ai-generation.md).
7. **Packaging and distribution:** titles, thumbnails, YouTube descriptions, CTAs and separate cuts per format. Read [packaging.md](references/packaging.md).
8. **Ads and UGC variants:** rebuild a winning ad structure with your own product and produce variants. Read [ads-and-ugc.md](references/ads-and-ugc.md).
9. **Talking footage edit:** cut raw clips of someone speaking from a word-timed transcript into a captioned short or edit. Read [talking-edit.md](references/talking-edit.md).

When the request is broad:
- For a new channel, start with mode 1.
- Otherwise follow the order above: reference (3) → script (2) or brief (5) → production (4, 5, 6 or 9) → packaging (7).

## Principles

- Hook in the first 2-3 seconds: make clear who could lose what. Don't open with "Hi, in this video…" (YT1).
- Open a curiosity gap and delay the answer into the video: one question, a bold claim or a before/after image (YT2).
- Take the structure of what already works (outlier videos, the longest-running ads), never its subject, text, face, voice or logo (YT5, VA3, YT20).
- The first draft is a starting point. A human checks hooks and factual claims before anything is published (YT6).
- Pull topics from demand signals; once a format works, turn it into a series and keep going (YT8, YT9).
- Split production into single-purpose steps that can be re-run one at a time (YT10).
- When a character recurs, lock its identity before generating scenes (VA12).
- Pick titles and thumbnails by score or test, not by taste (YT15).

## Guardrails

- **No invented results:** never make up earnings, views or outcomes. Don't present "$X a month" claims from sources as rules.
- **No invented product facts:** never invent real product screens, metrics or logos. When an asset is missing, stop and ask. List the claims that need checking, and say so in the video when it uses mock screens, sample data or an AI presenter (VA2).
- **Copying and consent:** don't reproduce someone else's video, face, voice or text; take only the structure. A real person's likeness or voice needs their explicit consent; clone only the user's own voice or one whose owner agreed (VA19).
- **Cost:** show the estimated cost and get approval before any paid generation (model credits, API calls).
- **Publishing:** no upload, publishing or DM automation without the user's approval. Uploads are private by default.
- **Licences:** filter images and sound effects by licence when searching (CC0 or public domain for commercial work, no NC/ND) and keep a source and attribution list; a "free" stock library is not a commercial licence (VA18). Before building on a motion engine, tool or open model, check its licence in the repo, for example Remotion's company-size limit or AGPL when served as a service (VA14, VA21).
- **Labels and hooks:** don't suggest publishing ad-like UGC without a label, or building hooks on shock content.
- **Bulk AI output:** when generating in bulk, remind the user of the platforms' policies on inauthentic and repetitive content; for a channel aiming at YouTube monetisation, read the current YPP text before launch (YT31). Never invent first-hand experiences to make AI content look human.
- **Secrets:** never print or commit API keys.

## Boundaries

- Paid app acquisition (for example TikTok Spark Ads, budgets, MMP, ROAS thresholds), store listing, screenshots and ASO: `mobil-yayin-buyume`. Producing the App Store preview video stays here (mode 5).
- Overall channel plan, launch-day distribution and press: `girisim-pazarlama`. Competitor analysis of e-commerce ads lives there; extracting the structure and rebuilding it lives here (modes 3 and 8).
- Search visibility outside video (web pages, AI answers): `seo-ai-arama`. YouTube titles and descriptions stay here (mode 7).
- Game trailers and devlogs arrive from `indie-oyun-yayin`. This skill has no trailer-specific rules; use the general script and edit steps.

## Completion

End each session with:

- what was produced, with file paths (brief, script, stills, renders);
- measured values, estimates and creative suggestions, labelled separately;
- missing assets and claims still waiting for a human check;
- costs spent or estimated, and the steps waiting for approval (paid generation, upload, DM automation);
- the next variant or test to run.

The (YTn) and (VAn) markers point to [kurallar.md](references/kurallar.md) (Turkish), which lists each rule's sources and evidence level. It is compiled from the owner's research notes in Twitter Notes (taslak v0.6).
