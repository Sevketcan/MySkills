# Reference and outlier analysis

Use this to turn videos or ads that already work into a structure template. [script-and-hook.md](script-and-hook.md), [launch-clip.md](launch-clip.md) and [ads-and-ugc.md](ads-and-ugc.md) build on its output.

## Steps

1. **Choose the sources (K5, K33).** Either:
   - outlier videos in the niche from the last 3 months (views far above the channel's own average);
   - or the ads that have stayed live longest in Meta Ad Library.
2. **Extract the transcript and frames.** For a local file, for example:

   ```
   ffmpeg -i ref.mp4 -vf "fps=2,scale=960:-2" frames/ref-%04d.jpg
   ```

   If a video-watching skill is available (for example claude-video `/watch`), use it instead.
3. **Pull measurable decisions from each reference (K17).** For each one, write down:
   - the hook type in the first 30 seconds;
   - the order of beats;
   - duration;
   - cutting rhythm;
   - the CTA.

   Label measured values, estimates and creative suggestions separately.
4. **Output: a structure template.** Subject, text, faces, voice and logos are not copied (K17).

## Notes

- The template is the input for the script (K5) and for ad variants (K33). The new video gets its own subject, wording and assets.
- Rebuilding someone else's ad one-to-one is not this mode's job; see the guardrails in [SKILL.md](../SKILL.md).
