# Faceless pipeline: explainer, documentary, Shorts

Every step is its own script and can be re-run on its own (K10). The tools named below are examples; use what the project already has.

## Steps

1. **`topic.json`:** the scenes and the search keywords for each scene.
2. **Images (K14).** Take them from an open archive or generate them.
   - NASA's image API, for example, needs no key and its images are public domain.
   - On Wikimedia Commons, one pipeline found that 1-2 word queries and about 1.8 seconds between requests worked.
   - Drop results that look like diagrams or charts.
3. **Voice (K12).** A free TTS such as Edge TTS is enough for explainers and documentaries.
   - Pin a version that works (`edge-tts` or `msedge-tts`).
   - One audio file per paragraph. On an error, retry 3 times, then skip.
4. **Subtitles (K11).** The text is already in hand.
   - Measure each paragraph's duration with ffprobe and spread its lines in proportion to character count;
   - or align at word level with Whisper.
   - For bilingual subtitles, both languages must have the same number of paragraphs.
5. **Edit, for example with ffmpeg (K13).**
   - One slow-zoom clip per image → groups of 8 joined with a short crossfade → final.
   - Burn in the subtitles and mix the audio.
   - Consider merging large jobs in stages like this rather than in one pass.
   - When layering audio with `amix`, try `normalize=0`; otherwise the music can disappear.
6. **Publish.** Upload as private by default and only with the user's approval. A human checks the hook and the factual claims first (K6).

## Ready-made alternatives

Open-source examples:
- `rushindrasinha/youtube-shorts-pipeline`: from a topic to a finished Short.
- `hypit-ai/hypit`: turns a viral video's structure into an editable workflow.

## Notes

- When producing in bulk, remind the user of the platforms' policies on inauthentic and repetitive content.
- Generated images and paid TTS or model calls cost money: show the estimate and get approval first.
