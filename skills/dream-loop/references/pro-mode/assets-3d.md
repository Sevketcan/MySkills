## How to get 3D Assets

Choose the asset source that fits the requested visual target, constraints and existing assets. These are options, not a mandatory sequence.

### 1. Can you download an external asset?

If the user has allowed it, you can download free assets from the internet. If unspecified, assume this isn't allowed.

If unallowed or you can't find the model you need, move on to 2.

### 2. Use an image-to-3D model

When external generation is in scope, the bundled Fal helper is an available integration. A configured key alone does not determine the asset source.

For Fal requests, read [Fal integration](../fal.md) and use the bundled batch helper. Use Fal’s HTTP API or SDK through the shell. Only report Fal as unavailable after an actual request fails and reasonable recovery fails, or credentials/access are absent.

User restrictions on external assets or services also apply to generated assets. Do not reinterpret a restriction as permission for a different provider.

Start with the two verified endpoint/input recipes in [Fal integration](../fal.md), using its offline check and batch commands. The default model roles are:
- A strong model (like tripo3d/h3.1/image-to-3d or newer equivalent); check current provider pricing before a submission. Use this for large assets or key, important ones like characters, buildings, scenery, greenery.
- A smaller model (like fal-ai/trellis or newer equivalent); check current provider pricing before a submission. Use this for things like small environmental/decorative objects, etc.

Use these for any major assets. For things like rocks, tiles, etc., you'll need some judgment. If it is detailed, image-to-3D is a good fit. If not, subsequent steps may be better. Depending on the target image you'll need to make a call.

To produce the input images for the assets, use your image gen tool. Pass the target image into it and ask it to extract a clean image of just the target asset over a solid or transparent background, then use that as the input for the image-to-3D model. This ensures it's perfectly aligned to the target image, not reimagined.

If image-to-3D is blocked, disallowed, or overkill, move on to 3.

### 3. Model it in Blender

Blender is the next option if installed locally. You can use its Python scripting interface.

You'll need to texture and add additional detail (e.g. normal maps) via image generation.

If Blender is unavailable or overkill, move on to 4.

### 4. Procedural assets

Build the asset in code and use image generation for texturing, normals, etc.

Don't do this to save time or reduce complexity. Do it only because it is either the only remaining option, or because it truly is the option that produces the best-looking result that's most closely aligned to the target image.

### Note on textures for 3D assets (in all of the above cases)

If you have an image generation tool, use it for textures, normal maps, skyboxes, etc, to enhance the visuals. This looks better and is faster than procedurally generated textures or normals. Do not replace missing generated textures with procedural noise or flat-color substitutes. Textures and normals make things look realistic and impressive, do not skip them.
