# Faceless pipeline: explainer, documentary, Shorts

Every step is its own script and can be re-run on its own (YT10). The tools named below are examples; use what the project already has.

## Steps

1. **`topic.json`:** the scenes and the search keywords for each scene. If the script needs approval, get it before any visuals or voice are made (VA8).
   - **Facts (VA2).** List the claims that need checking. For a documentary or history explainer, consider a source and claim table kept apart from the script: what is verified, what is interpretation, where the sources disagree, and what the visuals must not show (invented dialogue, a single exact number or a compass arrow the sources don't support). A wrong map movement repeats the error even after the narration is fixed.
2. **Visuals.** Choose per scene:
   - **Open-archive images (YT14).**
     - NASA's image API, for example, needs no key and its images are public domain.
     - On Wikimedia Commons, one pipeline found that 1-2 word queries and about 1.8 seconds between requests worked.
     - Drop results that look like diagrams or charts.
   - **Generated images:** show the cost estimate and get approval first.
   - **Simple line or stick-figure animation drawn in code** instead of stock images: see step 1 in [ai-generation.md](ai-generation.md) (YT25).
3. **Licences, filtered at search time (VA18).**
   - For commercial use, keep CC0 and public domain; drop NC and ND licences.
   - Put the filter in the search query or the script, not in a later clean-up.
   - Save each file's source page and licence next to it, mark any unclear licence, and generate the attribution list automatically for files that need one.
   - A "free" stock library is not automatically cleared for commercial use; check each source's terms.
4. **Voice (YT12).** A free TTS such as Edge TTS is enough for explainers and documentaries.
   - Pin a version that works (`edge-tts` or `msedge-tts`).
   - One audio file per paragraph. On an error, retry 3 times, then skip.
   - Build the timeline on the real audio's duration, not an estimate; when only the visuals are revised, reuse the approved voice track (VA13).
5. **Subtitles (YT11, VA17).** The text is already in hand.
   - Measure each paragraph's duration with ffprobe and spread its lines in proportion to character count;
   - or align at word level (Whisper, or a TTS that returns word timestamps) and show captions word by word.
   - Consider writing the caption style out (case, highlight colour, words per caption) rather than relying on the tool's generic defaults (VA17).
   - For bilingual subtitles, both languages must have the same number of paragraphs.
6. **Pilot before the long render (VA6, VA8).** For a long video, render a short pilot first (one source uses 30 seconds), get it approved, save the approved style and only then apply it to the full length. Fixing a problem in 30 seconds is cheaper than in 9 minutes. When a scene is wrong later, change only that scene or its timing and re-render it.
7. **Edit, for example with ffmpeg (YT13).**
   - One slow-zoom clip per image → groups of 8 joined with a short crossfade → final.
   - Burn in the subtitles and mix the audio.
   - Consider merging large jobs in stages like this rather than in one pass.
   - When layering audio with `amix`, try `normalize=0`; otherwise the music can disappear.
8. **Measure the render (VA15).** Don't accept "done" without numbers: re-check duration, loudness, audio and video streams and the target platform's specs. Don't mark anything as passed that wasn't actually checked. The agent can't hear the result, so ask the user to listen once on headphones, including pronunciation of names.
9. **Publish.** Upload as private by default and only with the user's approval. A human checks the hook and the factual claims first (YT6).
   - For a Short taken from a long video, consider writing a separate short narration rather than speeding up the long one; an excerpt must make sense to someone who hasn't seen the rest (VA10).

## Ready-made alternatives

Open-source examples:
- `rushindrasinha/youtube-shorts-pipeline`: from a topic to a finished Short.
- `hypit-ai/hypit`: turns a viral video's structure into an editable workflow.
- `wj-sidiss/otopilot`: topic to video with licence filtering, a script approval gate and per-job budget caps.
- `calesthio/OpenMontage`: research to finished video with fixed approval gates, a budget cap and post-render checks. It is AGPLv3; read the licence before building it into a service (VA21).

Check what a repo actually does in its README and code before relying on a claim such as "no API key", "free" or "auto-upload" (VA14).

## Notes

- When producing in bulk, remind the user of the platforms' policies on inauthentic and repetitive content.
- For a channel that aims at YouTube monetisation, read YouTube's current YPP and inauthentic-content text before launch. One creator's checklist to test: reply to comments, add the creator's own opinions to scripts, avoid widely used stock AI voices (or use a clone of the user's own voice), at most one upload a day, no repeated title pattern or description (YT31). Never invent first-hand experiences to make the content look human.
- Generated images and paid TTS or model calls cost money: show the estimate, propose a per-job cap and get approval first. Report costs as separate items: successful generations, failed requests, reused files and actual account charges; leave unknown totals blank rather than estimating them (VA8).
