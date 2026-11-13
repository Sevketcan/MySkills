# AI image and video generation

## Steps

1. **Pick the tool by the shot (VA11).**
   - Photoreal people, lip sync, character acting and organic motion → a generative video model (for example Kling, Seedance, Veo) or 3D.
   - Product, UI, typography, data and editing → code-driven motion (for example HyperFrames, Remotion, HTML, Canvas, SVG, three.js; see [launch-clip.md](launch-clip.md)). Which engine per scene: see "Choosing a code-motion engine" below.
   - Simple line or stick-figure animation, for example for an explainer → code as well, instead of stock or generated images (YT25):
     - describe the drawing style once and reuse it across the series;
     - have the agent write a program (or a Remotion composition) that draws each frame from the frame number, so frame-by-frame capture is exact (VA5);
     - turn the frames into video, for example browser capture with Playwright and then ffmpeg, or a Remotion render;
     - consider approving a short low-resolution moving preview before the full render; motion that looks right in a still can break when it moves.
   - Stylised 3D scenes and characters → Blender (for example through Blender MCP).
2. **If a character recurs, lock its identity first (VA12).** Generate a character sheet from a reference image, or at least a close-up plus front, side and back views:
   - the main view (front, 3/4, side, back; with a height scale) takes the largest area;
   - next to it: silhouette, 8 expressions, micro-expressions, head angles, poses, one close-up, clothing and hand details;
   - flat background, no style drift.

   Give this sheet as the reference for every later generation, and write what each reference image locks (for example "image 1 fixes the face and hair, image 2 the outfit and proportions").
3. **Layer multi-shot video prompts (VA4, VA23):**
   1. style and genre
   2. characters (look and attitude)
   3. location and light
   4. shot order (medium, close-up, over-the-shoulder, wide, final), each shot with its time range, shot size, camera move and content
   5. dialogue
   6. twist and close
   7. sound effects
   8. camera movement, duration and quality

   - One main action per shot; don't cram a whole sequence into one shot (VA4).
   - Say what may change and what stays fixed: face, outfit, number of people, location and large props stay; pose, expression, small objects and light may change. Add continuity limits: the camera doesn't jump the axis, objects don't appear from nowhere or vanish, motion doesn't skip or repeat. When editing an existing image, ask it to change only what is named (VA23).
   - Consider writing motion as an ordered chain (who moves first, who reacts, where it ends) and a colour card with one HEX value per element to stop colour drifting between shots (VA23).
4. **Cost (VA8).** Show the estimated cost before rendering and get approval. Set a budget cap per job; for batch generation, propose a daily cap and start with a dry run.

## Choosing a code-motion engine (VA20, VA21)

One engine and a stock style pack for every scene give the generic "made with code" look. Split the video into scenes and pick the engine by what each scene shows (VA20). One starting mapping, to adjust to taste:

| Scene shows | Engine (example) |
|---|---|
| Text, numbers, counters, info cards, UI | HTML + GSAP (for example HyperFrames) or Remotion |
| Real 3D: orbiting camera, light, shadow | three.js; Blender for modelled scenes |
| Formulas, graphs, diagrams | Manim |
| Particles, explosions, glow | PixiJS |
| Self-drawing lines and sketches | Paper.js |
| Characters walking, shapes morphing | plain Canvas |
| Photoreal people, lip sync, acting | a generative video model or 3D, not code (VA11) |

Render each scene on its own and join them; browser scenes are captured frame by frame with seeded randomness (VA5).

Ready-made tools build on these engines (for example motionforge, cinecode, kalem, ReelMimic, OpenMontage); check in each README and in the code what a tool actually does and needs before relying on it (VA14).

**Licences (VA21).** Check them before building on an engine or tool, not at delivery, and verify in the LICENSE file because terms change. As of November 2026:
- HyperFrames: Apache 2.0; some Pro features are paid.
- Remotion: free for individuals, companies of up to 3 employees and non-profits; larger companies need a company licence.
- OpenMontage: AGPLv3; if you modify it and offer it as a service, you have to share the source.
- Open video models: the weights' licence can differ from the code's (VA14).
- Map data from OpenStreetMap needs attribution.

## Recurring AI presenter (to test)

When the same AI presenter appears in many videos, consider generating the presenter once rather than per video (VA22):

1. Generate one consistent master take from a locked reference (step 2): face and mouth clear, and after every gesture the presenter returns to the same neutral pose, so any clip can follow any other.
2. Cut it at natural pauses into a clip library tagged by gesture, expression and shot size (plain delivery, emphasis, transition, close).
3. For each new video: script → voice → lock the timeline to the approved voice → pick a clip per sentence.
4. Apply lip sync only where the face is visible and speaking. Crop and change speed before lip sync; scale and place windows after it, or the mouth drifts off the audio.
5. Keep the background and place the presenter as a window or card instead of cutting them out; cut-out edges around hair and shoulders tend to ghost.

The video says that the presenter is AI-generated. Use a fully generated character, or a face and voice whose owner agreed.

## Notes

- A real person's face or voice needs their explicit consent. Don't recreate someone else's video, face or voice. Talking avatars and voice clones only from the user's own face and voice, or with the owner's permission.
- Open models: the model's licence is separate from the code's, and "free" models can need large GPUs. Check both in the repo before planning around one (VA14).
- When generating in bulk, remind the user of the platforms' policies on inauthentic and repetitive content.
