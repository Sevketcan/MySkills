---
name: blender-mcp
description: "Operate the Blender MCP connector: execution result formats, headless persistence, context overrides, timeout recovery and verified asset export."
---

# Blender MCP connector

Inspect the affected scene or objects, then verify the requested change with relevant state checks. Use screenshots when appearance matters. Keep edits within the authorized task and preserve unrelated scene data.

## Connector contracts

- Interactive Python calls assign a JSON-serializable dictionary to `result`; CLI calls use `summary`. Import required modules in each call: namespaces do not persist.
- Convert Vector/Euler/Matrix values to lists before returning them.
- For active-scene objects, use bpy.context.scene.objects; bpy.data.objects includes objects from other scenes. A minimal interactive example is: import bpy; result = {"objects": [obj.name for obj in bpy.context.scene.objects]}.
- A render or bake timeout may leave the operation running. Re-inspect before submitting it again.
- Headless CLI changes disappear unless saved to the intended file. Confirm the target path from task context and preserve the open interactive session.
- GUI operators require the correct window/area/region through `bpy.context.temp_override`. Use OBJECT mode for selection or transforms and restore temporary render settings in `finally`.
- Query the live API documentation when an operator or parameter is uncertain; the installed Blender version is authoritative.
- On connection refusal, check whether the addon server is running (normally localhost:9876); avoid a retry loop.

## Optional recipes

[Connector recipes](references/connector-recipes.md) contains context override examples, evaluated mesh statistics, material/export traps, physics scatter, texture baking and the user's Godot/Cogito conventions. Read only the matching section. Cogito dimensions, polygon budgets and its historical Windows path apply only to that project; discover the current destination before export. These examples do not establish a general asset style or a universal verification checklist.

## Deterministic selected-asset export

For a requested GLB export, [export_selected_glb.py](scripts/export_selected_glb.py) exports only the named or selected objects, verifies the output and restores selection/active object. It does not save the source .blend or apply transforms to its objects. Run it in Blender or import export_glb inside a connector call; assign its return value to result (interactive) or summary (CLI). Existing output requires the explicit overwrite argument.

Example for a headless file:

    blender --background SOURCE.blend --python <skill-dir>/scripts/export_selected_glb.py -- --output DESTINATION.glb --objects AssetName

Use the requested destination and actual object names. This helper is not an art-direction or polygon-budget policy.
