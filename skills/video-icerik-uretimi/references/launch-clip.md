# Launch clip and App Store preview (code-driven motion)

Use this for a product demo, launch video or App Store preview built from real screens. Treat the workflow as a method to test and adjust on the first video. Take product facts from the project's own documents (for example README, `LAUNCH.md`, `BRAND.md`).

## 1. Brief (K15, K16)

Write a director's brief, not a vibe prompt. Keep product facts separate from film decisions. `brief.md` contains:

- **Goal:** which feature, for whom, the opening text (8 words at most), the closing CTA.
- **Delivery:** resolution, fps, total frames. Consider a separate composition for each aspect ratio rather than cropping one from another (K24).
- **Assets:** real screens, logo, fonts, audio. If anything is missing, stop and ask.
- **Layout:** colours, safe margins, title and card boxes.
- **Timeline:** entry, hold, action, result and close, with frame numbers.
- **Review stages.**

## 2. Write each shot as an event (K18, K19)

start state → the cursor moves to the action → press → result → a hold long enough to read the result.

Write timing in seconds first, then convert it to frames (at 30 fps, 0.6 s = 18 frames).

## 3. Renderer (K19)

- A small one-off job: Canvas or SVG.
- A series that will repeat: a code-motion framework, for example Remotion.
- Derive every value from the frame number (in Remotion, `useCurrentFrame()`). Seed any randomness. Every frame must be renderable on its own.

## 4. Gates (K20, K21, K22)

Wait for the user's approval at each gate. The agent does not make irreversible brand decisions.

1. Assets and references approved.
2. Style guide and shot list.
3. Three stills: opening, product result, close (for example `npx remotion still <Comp> out/x.png --frame=N`).
4. Rough cut and contact sheet; partial renders for transitions (for example `--frames=90-149`).
5. Fixes for the three biggest defects.
6. Audio sync (sound events on the same timeline as the picture), formats, and an `ffprobe` check of resolution, fps and duration. Watch the file at normal speed.

## 5. Fix format (K20)

Each fix names the frame number, the observed problem, one change, and what stays fixed.

Order: missing information and unreadable text first, then timing, visual detail last.

## 6. Keep decisions in files (K23)

`brief.md`, `style-guide.md`, `shotlist.md`, `assets/`, `reviews/`, `out/`. The next video should start by changing only the brief and the assets.

## Setup example: Remotion

```
npx create-video --yes --blank <project>
npx remotion skills add
npm run dev
```

Check Remotion's commercial-use licence before using it for commercial work.
