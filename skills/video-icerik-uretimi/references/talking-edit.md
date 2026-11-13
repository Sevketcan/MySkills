# Talking footage edit: raw clips to a captioned cut

Use this when there is camera footage of someone speaking (talking head, interview, a phone-recorded explanation, a tutorial, a vlog) to cut into a short or a longer edit. The agent doesn't watch the whole video; it cuts from a word-timed transcript (VA16). Tools are examples (for example `browser-use/video-use`, `kajisho5/ffmpeg-skill`, a DaVinci Resolve skill set); use what the project has.

## Before recording

If the footage isn't shot yet and the user records themselves, one checklist to try (YT29):

- Spend the budget on sound first: a wireless lavalier whose receiver plugs into the phone, not an ordinary Bluetooth mic (those use the call profile and drop the audio to 8-16 kHz).
- Clip it on the chest about a hand-span below the mouth, outside clothing.
- Pick a room that doesn't echo (rug, curtains, a full bookshelf). In a quiet room, turn the mic's noise cancellation off.
- Don't count on AI audio repair to rescue a bad take; it can produce syllables that were never said.
- One soft light (an LED panel with a softbox, about 45° to the face, slightly above eye level); ceiling light off.
- Record 10 seconds and listen on headphones before the real take. This also catches an app that is still using the phone's own mic.

## Steps

1. **Inventory.** Probe every file (duration, fps, resolution, audio streams) and make a contact sheet. Name missing capabilities (for example no transcription engine, no subtitle support in ffmpeg). Work on copies; never overwrite the originals.
2. **Transcribe with word timestamps (VA16).** One transcript per take, at word level. Don't transcribe the same take twice. Removing filler words needs measured word timings; without a transcription engine that step can't run. If several people speak, consider separating them by voice (speaker diarisation or voice matching) before choosing lines.
3. **Cut plan first, render after approval (VA8, VA9, VA16).**
   - Decide from the transcript. One brief that works, for example: drop false starts, repeated takes and filler words, keep the best take of each line, trim long pauses but keep the speaker's rhythm, open on the strongest line.
   - Look at frames only where the transcript can't decide (an unclear pause, a cut check) or to learn what a clip shows; a grid with a frame every few seconds is enough.
   - Save a numbered cut list (source file, in and out times, position in the final video) and show it before rendering. Later fixes become one line ("undo cut 4", "end on the price sentence").
4. **Cut cleanly (VA16).** Never cut mid-word. Put a short audio crossfade (around 30 ms) on every cut and normalise loudness.
5. **Format (VA10).** Crop horizontal footage to 9:16 framed on the face or on the screen being shown, not from the centre. If the tool can't find the face, give it the crop coordinates. Consider separate 9:16 and 16:9 cuts from the same take (YT19).
6. **Captions (VA17).** Tie captions to the word timestamps (word by word or karaoke). Consider writing the style out (case, highlight colour, words per caption, font); "in my style" gives the tool nothing to work with, and its defaults are generic.
7. **Measure and review the render (VA15).**
   - Re-measure duration, loudness, streams, the platform's specs and every cut boundary. Don't accept "done" without the numbers.
   - Have a separate critic (a subagent with a clean context that hasn't seen the work) review the render with a fixed round limit (for example 3) and a narrow checklist, for example flashes, clipped words, hidden captions and audio drifting off the lips. Don't deliver while a known defect is open.
   - The agent can't hear: ask the user to listen to the final cut once on headphones.
8. **Deliver.** The final file with the cut list, the captions file and the measurements. Upload as private by default and only with the user's approval.

## Long raw footage into a vlog

For a day of scattered clips (vlog, event, founder diary), the same steps can run fully locally:

1. Copy the clips into one folder and transcribe them locally with word timestamps (for example Whisper through `mlx-whisper` on Apple Silicon).
2. Make a frame grid per clip so the agent can see what each one shows (VA16).
3. Write the edit as a JSON cut list (clip, in, out) chosen from the transcripts and grids, and show it before rendering. Keep the scripts and the cut list so the next edit starts from the same base (VA9).
4. Keep it plain: a vlog rarely needs motion graphics, and a heavy template makes it look generic (VA20). Consider captions only where they help, for example the first minute.
5. For a cover image, consider picking from frames with a detected face (for example OpenCV with a face detector).

## Notes

- If the speaker reads from a script regularly, see the note on teaching a per-channel script template from recordings in [script-and-hook.md](script-and-hook.md) (YT23).
- Transcription services can need an API key and cost money; check a tool's "no key" or "offline" claim in its README before relying on it (VA14).
- Edit only footage the user owns or has the rights to; a real person's face and voice need their consent.
