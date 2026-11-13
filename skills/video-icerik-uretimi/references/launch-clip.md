# Launch clip and App Store preview (code-driven motion)

Use this for a product demo, launch video or App Store preview built from real screens. Take product facts from the project's own documents (for example README, `LAUNCH.md`, `BRAND.md`).

## 1. Brief (VA1, VA2)

Write a director's brief, not a vibe prompt: a one-sentence idea (or event), audience, duration, formats, real assets and the clichés to avoid. Ask only for what's missing (duration, format, look, voice), then restate the brief in one sentence and wait for a yes. Consider keeping product facts in their own section, apart from film decisions. `brief.md` contains:

- **Goal:** which feature, for whom, the opening text (8 words at most), the closing CTA.
- **Delivery:** resolution, fps, total frames. Consider a separate composition for each aspect ratio rather than cropping one from another (VA10).
- **Assets:** real screens, logo, fonts, audio. If anything is missing, stop and ask.
- **Claims:** every statement in the script that needs checking, listed for the user. If mock screens, sample data or an AI presenter appear, the video says so (VA2).
- **Layout:** colours, safe margins, title and card boxes.
- **Timeline:** entry, hold, action, result and close, with frame numbers.
- **Review stages.**

## 2. Shot list: each shot as an event (VA4, VA5)

Each shot has a start state, an end state and a purpose, plus its duration, shot size, camera move and on-screen text. One action per shot: start state → the cursor moves to the action → press → result → a hold long enough to read the result. Don't cram several actions into one shot; as a rough guide, about 9 shots for 30 seconds. Consider keeping on-screen text to a few words per shot so it reads on a phone.

Write timing in seconds first, then convert it to frames (at 30 fps, 0.6 s = 18 frames).

Pace follows the job: a fast kinetic cut suits a teaser; a feature demo needs each text on screen long enough to be read aloud.

## 3. Engine and renderer (VA5, VA11, VA20, VA21)

- Pick the engine by what each scene shows instead of one engine for everything, and check its licence before building on it: see "Choosing a code-motion engine" in [ai-generation.md](ai-generation.md).
- A small one-off job: Canvas or SVG. A series that will repeat: a code-motion framework, for example HyperFrames or Remotion.
- Derive every value from the frame number (in Remotion, `useCurrentFrame()`). Seed any randomness. Every frame must be renderable on its own.
- Browser scenes are captured frame by frame, not recorded in real time; `requestAnimationFrame` loops, CSS transitions and wall-clock timers are not seekable. A real-time screen recording can do for a quick test; render the delivery frame by frame.
- Realistic close-up faces are weak in code-drawn film: stylise them or use a silhouette, and leave photoreal people to generative video (VA11).

## 4. Narration and word timing (VA13, VA19)

- If the clip has a voiceover, generate it with word timestamps and anchor each scene and cut to a word. When a new or real recording arrives, re-anchor to its actual words; because every scene is a function of time, nothing needs re-animating.
- Once the voice is approved, lock the timeline to it. If one line is misread, consider re-recording only that segment and patching it into the voice track (VA13).
- When the user narrates, one split that works: the user records the personal part (the first line, the face) themselves, and a clone of their own voice carries the body over code-drawn scenes. Re-time to the real take when it exists. Clone only the user's own voice, with their consent.

## 5. Sound (VA7, VA18)

- Put each effect on the frame of its event: a click on the press, a whoosh on the frame the logo appears. Let the scene's event list (for example `events.json`: which event lands on which frame) drive the sound.
- If the piece is cut to music, measure the beats first and place cuts on the beat grid.
- For commercial work, use only CC0 or public-domain sound effects. Write the licence filter into the search request, and save each file's source page and licence in a list next to the assets; mark any unclear licence. A "free" stock library is not automatically cleared for commercial use.

## 6. Gates (VA6, VA8)

Wait for the user's approval at each gate. The agent does not make irreversible brand decisions. Paid steps (generated music, voice, model calls) need a budget cap and the user's approval before money is spent: before each paid call, say what will be generated and the estimated cost. Read API keys only from environment variables.

1. Assets and references approved.
2. Style guide and shot list.
3. Three stills: opening, product result, close (for example `npx remotion still <Comp> out/x.png --frame=N`). Check them at phone size: readable text, safe area, real assets, a hook in the first 2 seconds. Motion that looks right in a still can break when it moves; consider adding a short low-resolution moving preview at this gate (YT25).
4. Rough cut and contact sheet; partial renders for transitions (for example `--frames=90-149`).
5. Fixes for the three biggest defects.
6. Final check (VA15): re-measure resolution, fps, duration, loudness, streams and the platform's specs (for example with `ffprobe`), and check every cut boundary. Have a separate critic (a subagent with a clean context that hasn't seen the work, or a blind review) look at the render, with a fixed round limit. Don't deliver while a known defect is open. Ask the user to watch it at normal speed and listen once on headphones; the agent can't hear.

## 7. Revision loop (VA6)

Each fix names:

- the frame number or timecode, and the scene and layer it falls in;
- the observed problem, ideally with the spot marked on the frame (a circle or box gives the agent exact pixel coordinates instead of "top right");
- one change, and what stays fixed.

Fix the scene's source and re-render only the affected frames or scene, never the whole video. Consider anchoring each note to its scene rather than to the global second, so notes don't drift when an earlier scene changes length. A review editor that lets the user watch, mark a frame and send the note to the agent (for example Kurgu) can speed this up; check in its README which projects it can import (VA14).

Order: missing information and unreadable text first, then timing, visual detail last.

## 8. Keep decisions in files (VA9)

`brief.md`, `style-guide.md`, `shotlist.md`, a source file (the words and facts the clip may use) and a look file (its visual style), `assets/` with the licence list, `reviews/`, `out/`. The next video should start by changing only the brief and the assets.

## Setup example: Remotion

```
npx create-video --yes --blank <project>
npx remotion skills add
npm run dev
```

Check Remotion's licence before commercial use: as of November 2026 it is free for individuals, companies of up to 3 employees and non-profits, and larger companies need a company licence. Verify in its LICENSE file (VA21).
