# AI image and video generation

## Steps

1. **Pick the tool by the shot (K25).**
   - Photoreal people and organic motion → a generative video model (for example Kling, Seedance, Veo).
   - UI, typography, data, product screens → code-driven motion ([launch-clip.md](launch-clip.md)).
   - Stylised 3D scenes and characters → Blender (for example through Blender MCP).
2. **If a character recurs, lock its identity first (K26).** Generate a character sheet from a reference image:
   - the main view (front, 3/4, side, back; with a height scale) takes the largest area;
   - next to it: silhouette, 8 expressions, micro-expressions, head angles, poses, one close-up, clothing and hand details;
   - flat background, no style drift.

   Give this sheet as the reference for every later generation.
3. **Layer multi-shot video prompts (K18):**
   1. style and genre
   2. characters (look and attitude)
   3. location and light
   4. shot order (medium, close-up, over-the-shoulder, wide, final)
   5. dialogue
   6. twist and close
   7. sound effects
   8. camera movement, duration and quality
4. **Cost.** Show the estimated cost before rendering and get approval. For batch generation, propose a daily cap.

## Notes

- A real person's face or voice needs their explicit consent. Don't recreate someone else's video, face or voice.
- When generating in bulk, remind the user of the platforms' policies on inauthentic and repetitive content.
