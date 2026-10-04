---
name: blender
description: "Look up version-sensitive Blender Manual and bpy API facts in the bundled topic indexes. Use for uncertain operators, animation, nodes, rendering, libraries or addon APIs."
metadata:
  covers:
    - actions-fcurves
    - addons-panels
    - cameras-lights
    - linked-libraries
    - material-nodes
    - python-api
---

# Blender Documentation Reference

Faithful, task-routed reference for the Blender Manual and the Blender Python API, rendered from the
full documentation corpus into one focused file per subject. Original prose; identifiers are
preserved verbatim. This package routes to six area guides — open the one that matches and use
its `references/INDEX.md`.

## Scope

Use the indexes to resolve uncertain or version-sensitive Blender facts. Familiar operations do not require reading this corpus. Read one matching subject rather than every area guide; verify conflicts against the installed version's live API or official documentation.

## Routes

| Area | Use for | Open |
| --- | --- | --- |
| Blender Linked Libraries and Append/Link | linking and appending data, library overrides, and reusing assets across .blend files. | `linked-libraries/GUIDE.md` |
| Blender Material Nodes and Images | materials, shader and geometry nodes, textures, images, and UV data. | `material-nodes/GUIDE.md` |
| Blender Cameras, Lights, and Rendering | cameras, lights, the render engines, and rendering behavior. | `cameras-lights/GUIDE.md` |
| Blender Actions, F-Curves, and Animation | actions, F-curves, keyframes, drivers, the NLA, and animation behavior. | `actions-fcurves/GUIDE.md` |
| Blender Add-ons, Panels, and Properties | add-ons, UI panels, properties, and operator-driven UI integration. | `addons-panels/GUIDE.md` |
| Blender Python API Essentials | bpy scripting, operators, add-on and extension authoring, the command line, and application templates. | `python-api/GUIDE.md` |

## Workflow

1. Identify the area above and open that guide's `GUIDE.md` (or its `references/INDEX.md`).
2. Pick the one reference file that matches; read only what you need.
3. Treat every operator name, `bpy` path, enum value, shortcut, and number as an exact reference fact.

## Gotchas

Recurring failure modes and what to do instead live in the sibling [GOTCHA.md](GOTCHA.md).

## References

Each guide carries its own `references/INDEX.md`, `references/topics.json`, and per-subject
`references/*.md`. Start from the area's `INDEX.md`.

## Official documentation

Includes original content written for this skill. The official documentation is at https://docs.blender.org/manual/en/latest/ — consult it to verify anything uncertain, conflicting, or version-specific.
