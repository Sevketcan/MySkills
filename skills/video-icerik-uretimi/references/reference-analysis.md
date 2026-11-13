# Reference and outlier analysis

Use this to turn videos or ads that already work into a structure template. [script-and-hook.md](script-and-hook.md), [launch-clip.md](launch-clip.md) and [ads-and-ugc.md](ads-and-ugc.md) build on its output.

## Steps

1. **Choose the sources (YT5, YT20, YT28).** Either:
   - outlier videos in the niche from the last 3 months (views far above the channel's own average);
   - or the ads that have stayed live longest in Meta Ad Library;
   - or a format that has started working in another language's market.
2. **Extract the transcript and the edit skeleton (YT5).**
   - The transcript gives the script structure: beats, lines, where the hook and the CTA sit.
   - The edit skeleton comes from the frames. Take one frame at every scene change rather than at a fixed rate. For a local file, for example:

     ```
     ffmpeg -i ref.mp4 -vf "select='eq(n\,0)+gt(scene\,0.3)',showinfo" -fps_mode vfr frame_%03d.jpg
     ```

     `eq(n\,0)` keeps the opening frame, and `showinfo` logs each frame's `pts_time` (in seconds) so frames can be matched to the transcript. Lower the threshold (for example to 0.2) for fast cuts or crossfades. On an older ffmpeg, replace `-fps_mode vfr` with `-vsync vfr`.
   - Give the frames to a vision-capable model and ask for a table with one row per frame: shot type, on-screen text, and what changed from the previous frame. Put it next to the transcript: which line each cut falls on, whether the on-screen text repeats the voice, how many cuts the opening has.
   - A talking head with few cuts gives few frames; rely on the transcript there. Frames carry no sound or music; judge rhythm from the transcript and the waveform.
   - If a video-watching skill is available (for example claude-video `/watch`), it can replace the frame step.
   - Downloading a video (for example with `yt-dlp`) is subject to the platform's terms. The frames are for analysis only and never go into the new video.
3. **Pull measurable decisions from each reference (VA3).** For each one, write down:
   - the hook type in the first 30 seconds;
   - the order of beats;
   - duration, shot durations and cutting rhythm (BPM, if it is cut to music);
   - transitions;
   - the CTA;
   - for a motion or design reference: palette, typography, motion style and the frame numbers of key moments.

   Give each reference one job (for example "pacing only"). Label measured values, estimates and creative suggestions separately.
4. **Output: a structure template.** Subject, text, footage, faces, voice and logos are not copied (VA3).

## Notes

- The template is the input for the script (YT5) and for ad variants (YT20). The new video gets its own subject, wording and assets.
- Rebuilding someone else's ad one-to-one is not this mode's job; see the guardrails in [SKILL.md](../SKILL.md).
