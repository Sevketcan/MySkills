---
name: manage-sprite-atlas
description: "Create or fix Unity SpriteAtlas V2 authoring, packing, variants and runtime delivery. Includes prebuild and Addressables examples; preserve the project delivery pipeline."
---

# SpriteAtlas V2 integration

Inspect the project's atlas format, packing mode, existing scripts and delivery pipeline. For a targeted fix, update the existing path; do not introduce another pipeline or ask for an already-authorized edit again. Clarify delivery only when project context cannot settle a material choice.

- Keep editor authoring (`UnityEditor.U2D.SpriteAtlasAsset` and Editor-only APIs) separate from runtime access (`UnityEngine.U2D.SpriteAtlas`). Confirm compatibility with the installed Unity version.
- Use a prebuild generator when automated atlas generation is requested. Manual asset authoring and existing pipelines remain valid for other tasks.
- Read the shipped example relevant to the operation; names and values are templates, not project requirements.
- For built-in delivery verify inclusion, packing and a runtime sprite lookup. For Addressables/late binding verify both content building and runtime registration/loading; a successful Editor import alone is insufficient.
- Read back changed settings and check the failure the user actually reported. Avoid generating loaders, variants or Addressables code that the task does not need.

| Operation | Read |
| --- | --- |
| Authoring/runtime boundary | [Example](resources/authoringvsruntime.cs), [common errors](references/common-errors.md) |
| Automated prebuild | [Generator](resources/spriteatlasprebuildgenerator.cs), [packing mode](resources/enablespritepacking.cs), [save](resources/savespriteatlasasset.cs) |
| Addressables delivery | [Delivery guide](references/addressables-delivery.md), relevant late-binding examples in `resources/` |
| Manual authoring | [Manual guide](references/manual-authoring.md) |
| API, variants and packing | [API](references/api.md), [custom packing](references/custom-packing.md) |

`resources/` contains further C# examples. [Workflow examples](references/workflow-examples.md) retains the previous complete cookbook for specific integration details; its repeated question formats and default full pipeline are optional, subordinate to this scoped workflow.
