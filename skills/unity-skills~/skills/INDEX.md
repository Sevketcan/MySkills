## Triggers
- Browsing the module catalog
- Finding which module handles a task
- Checking mode requirements
- 浏览模块目录、查找某事由哪个模块处理、确认模式要求

# Unity Skills - Module Index

Module docs. Start with [../SKILL.md](../SKILL.md) for mode switching and schema-first rules.

> **Multi-instance**: For version-specific projects, call `unity_skills.set_unity_version(...)` first.
> **Schema-first**: Use `GET /skills/schema` or `unity_skills.get_skill_schema()` for exact signatures. Load module docs for workflow guidance and guardrails.

## Modules

> **Mode legend** (v1.9.0+, caller-facing — describes what the caller can do, not the C# attribute):
> - `SA` — module skills mostly run directly in **all three modes** (Approval / Auto / Bypass) without a grant.
> - `FA` — module skills mostly require **user grant** under Approval (single-shot one-step execution); under Auto / Bypass they run directly with audit only.
> - `Mixed` — module is split between SA and FA; check per-skill `mode` before calling (`GET /skills?full=1`, or the scoped `GET /skills/schema?category=<Category>` — bare `GET /skills` is the brief directory and carries no `mode`).
> - Suffix `*` — module contains auto-forbidden skills (Delete / Play Mode / Domain Reload / high-risk). These return `MODE_FORBIDDEN` under Approval and Auto; only **Bypass** runs them, **or** the user can permanently allow them via the Allowlist. Never attempt grant for them.
>
> Labels are guidance only; the per-skill `mode` field (`GET /skills?full=1` / `GET /skills/schema?category=<Category>`) is authoritative.

| Module | Mode | Description | Batch Support |
|--------|:----:|-------------|---------------|
| [gameobject](./gameobject/GUIDE.md) | FA* | Object create/move/parent | Yes |
| [component](./component/GUIDE.md) | Mixed* | Component add/remove/configure | Yes |
| [material](./material/GUIDE.md) | FA | Material property edits | Yes |
| [light](./light/GUIDE.md) | FA | Light create/configure | Yes |
| [prefab](./prefab/GUIDE.md) | FA | Prefab create/apply/spawn | Yes |
| [asset](./asset/GUIDE.md) | SA* | Asset refresh/find/info | Yes |
| [batch](./batch/GUIDE.md) | SA | Batch and async jobs | Built-in |
| [ui](./ui/GUIDE.md) | FA | UGUI Canvas/UI creation | Yes |
| [uitoolkit](./uitoolkit/GUIDE.md) | Mixed* | UXML/USS/UIDocument | No |
| [script](./script/GUIDE.md) | SA* | Script create/read/update | Yes |
| [scene](./scene/GUIDE.md) | SA* | Scene load/save/query | No |
| [editor](./editor/GUIDE.md) | SA* | Play/select/undo/redo/change journal | No |
| [animator](./animator/GUIDE.md) | FA | Animator controllers | No |
| [shader](./shader/GUIDE.md) | Mixed* | Shader create/list | No |
| [shadergraph](./shadergraph/GUIDE.md) | Mixed* | Shader Graph create/inspect/blackboard edit/constrained node editing | No |
| [graphics](./graphics/GUIDE.md) | Mixed | GraphicsSettings / QualitySettings / SRP assets | No |
| [volume](./volume/GUIDE.md) | Mixed* | Volume / VolumeProfile / VolumeComponent | No |
| [postprocess](./postprocess/GUIDE.md) | FA* | Modern URP/HDRP post-processing | No |
| [urp](./urp/GUIDE.md) | Mixed* | URP asset / renderer / renderer features | No |
| [decal](./decal/GUIDE.md) | Mixed* | URP Decal Projector workflow | Yes |
| [console](./console/GUIDE.md) | SA | Log capture/filter | No |
| [validation](./validation/GUIDE.md) | SA* | Broken reference checks | No |
| [importer](./importer/GUIDE.md) | Mixed | Texture/audio/model import | Yes |
| [cinemachine](./cinemachine/GUIDE.md) | FA* | VCam operations | No |
| [probuilder](./probuilder/GUIDE.md) | FA* | ProBuilder mesh edits | No |
| [xr](./xr/GUIDE.md) | FA | XRI setup | No |
| [terrain](./terrain/GUIDE.md) | FA | Terrain create/paint | No |
| [physics](./physics/GUIDE.md) | Mixed | Raycast/overlap/gravity | No |
| [navmesh](./navmesh/GUIDE.md) | Mixed* | NavMesh bake/query | No |
| [timeline](./timeline/GUIDE.md) | FA* | Timeline tracks/clips | No |
| [workflow](./workflow/GUIDE.md) | SA* | Task snapshots/undo, batch orchestration | No |
| [cleaner](./cleaner/GUIDE.md) | SA* | Unused/duplicate assets | No |
| [smart](./smart/GUIDE.md) | FA* | Query/layout/auto-bind | No |
| [perception](./perception/GUIDE.md) | SA | Scene/project analysis | No |
| [camera](./camera/GUIDE.md) | FA | Scene View camera | No |
| [event](./event/GUIDE.md) | Mixed* | UnityEvent wiring | No |
| [package](./package/GUIDE.md) | Mixed* | UPM install/query | No |
| [project](./project/GUIDE.md) | SA* | Project info/settings | No |
| [profiler](./profiler/GUIDE.md) | SA | Perf statistics | No |
| [optimization](./optimization/GUIDE.md) | Mixed | Asset optimization | No |
| [sample](./sample/GUIDE.md) | Mixed* | Demo/test skills | No |
| [debug](./debug/GUIDE.md) | SA* | Compile/system diagnostics | No |
| [test](./test/GUIDE.md) | Mixed* | Unity Test Runner | No |
| [bookmark](./bookmark/GUIDE.md) | SA | Scene View bookmarks | No |
| [history](./history/GUIDE.md) | SA | Undo/redo history | No |
| [scriptableobject](./scriptableobject/GUIDE.md) | Mixed* | ScriptableObject assets | No |
| [netcode](./netcode/GUIDE.md) | Mixed* | Netcode for GameObjects setup, prefabs, lifecycle, host/server/client | Yes |
| [addressables](./addressables/GUIDE.md) | Mixed* | Addressables authoring: group CRUD, asset entry assignment, profile switching, content build (com.unity.addressables, reflection-based) | No |
| [yooasset](./yooasset/GUIDE.md) | Mixed* | YooAsset hot-update: build bundles, Collector CRUD, BuildReport asset/dependency analysis, PlayMode runtime validation, Reporter/Debugger/AssetArtScanner tools | Yes |
| [dotween](./dotween/GUIDE.md) | Mixed* | DOTween Pro DOTweenAnimation editor-time configuration (add/batch/stagger/tune) | Yes |
| [primetween](./primetween/GUIDE.md) | Mixed* | PrimeTween Free inspection, factory discovery, and runtime tween/sequence script generation | No |
| [behavior](./behavior/GUIDE.md) | Mixed | Unity Behavior graph assets, agents, blackboard variables (com.unity.behavior, reflection-based) | Yes |
| [hybridclr](./hybridclr/GUIDE.md) | Mixed* | HybridCLR hot-update settings, codegen, DLL compile/copy pipeline (com.code-philosophy.hybridclr, reflection-based) | Yes |
| [qframework](./qframework/GUIDE.md) | Mixed* | QFramework editor automation: architecture-layer codegen, ViewController/UIKit panel codegen, ResKit AssetBundle mark/build, architecture scan, API doc query (no UPM package, reflection-based) | Yes |

## Advisory Design Modules

Documentation only — these modules define no REST skills.

| Module | Description |
|--------|-------------|
| [project-scout](./project-scout/GUIDE.md) | Inspect existing project |
| [architecture](./architecture/GUIDE.md) | Plan system boundaries |
| [adr](./adr/GUIDE.md) | Record tradeoffs |
| [performance](./performance/GUIDE.md) | Review hot paths |
| [asmdef](./asmdef/GUIDE.md) | Plan asmdef deps |
| [blueprints](./blueprints/GUIDE.md) | Small-game blueprints |
| [script-roles](./script-roles/GUIDE.md) | Assign class roles |
| [scene-contracts](./scene-contracts/GUIDE.md) | Define scene wiring |
| [testability](./testability/GUIDE.md) | Extract testable logic |
| [patterns](./patterns/GUIDE.md) | Choose patterns |
| [async](./async/GUIDE.md) | Choose async model |
| [inspector](./inspector/GUIDE.md) | Design authoring UX |
| [scriptdesign](./scriptdesign/GUIDE.md) | Review script structure |
| [netcode-design](./netcode-design/GUIDE.md) | Netcode source-anchored rules (lifecycle/ownership/RPC/variables/spawn/scene/transport/pitfalls) |
| [yooasset-design](./yooasset-design/GUIDE.md) | YooAsset v2.3.18 source-anchored rules (init/default-package shortcuts/playmode/handles/loading/update/filesystem/build/pitfalls) |
| [addressables-design](./addressables-design/GUIDE.md) | Addressables dual-version (1.22.3 Unity 2022 / 2.9.1 Unity 6) source-anchored rules (init/handles/loading/scene/update/download/assetref/pitfalls) with migration table |
| [unitask-design](./unitask-design/GUIDE.md) | UniTask 2.5.10 source-anchored rules (basics/playerloop/cancellation/composition/conversion/asyncenumerable/triggers/pitfalls) |
| [dotween-design](./dotween-design/GUIDE.md) | DOTween 1.3.015 source-anchored rules (basics/tween/sequence/shortcuts/ease/lifetime/integration/pitfalls) |
| [primetween-design](./primetween-design/GUIDE.md) | PrimeTween 1.4.6 source-anchored rules (factories/handles/sequences/cycles/callbacks/lifetime/integration) |
| [shadergraph-design](./shadergraph-design/GUIDE.md) | ShaderGraph dual-version source-anchored rules (versions/node subset/recipes/pitfalls/review) |
| [pico-design](./pico-design/GUIDE.md) | PICO Unity Integration SDK v3.4.0 doc-anchored rules (setup/rendering/interaction/MR/SecureMR/platform/API signatures/version diffs 2.x-3.4/pitfalls) |
| [qframework-design](./qframework-design/GUIDE.md) | QFramework v1.0.257 source-anchored rules (layers/CQRS/BindableProperty/event tools/CodeGenKit+UIKit/ResKit/ActionKit+SingletonKit/data kits/pitfalls) |
| [yaml-editing](./yaml-editing/GUIDE.md) | Safe hand-edit rules for serialized YAML (.unity/.prefab/.asset/.meta/ProjectSettings) when REST cannot reach — reference/fileID repair, .meta/GUID safety, ProjectSettings patch, merge conflict |
| [unity-skills-cli-bridge](./unity-skills-cli-bridge/GUIDE.md) | Experimental Unity CLI bridge for a UnitySkills-bound project (opt-in via `Library/UnitySkills/cli_config.json`) — cold start with the Editor closed, headless test/run/build, exit codes, JSON/NDJSON contract, hard DO-NOT list. For general CLI operations use the official `unity-cli` skill. |
| [manual-gameobject](./manual-gameobject/GUIDE.md) | Manually create GameObjects, organize the Hierarchy, and adjust Transforms using Unity Editor UI |
| [manual-component](./manual-component/GUIDE.md) | Manually add, configure, reorder, and copy components on GameObjects using Unity Editor UI |
| [manual-material](./manual-material/GUIDE.md) | Manually create and edit Materials and assign them to objects using Unity Editor UI |
| [manual-scene](./manual-scene/GUIDE.md) | Manually navigate, save, and manage scenes using Unity Editor UI |

## Batch-First Rule

When a task touches `2+` objects in Auto / Bypass mode (or after a successful grant under Approval), prefer `*_batch` skills over repeated single-item calls.

## Skill Naming Convention

Skills follow `<module>_<action>` or `<module>_<action>_batch`.
Use schema to verify the exact prefix list.
Special: `scene_analyze`, `hierarchy_describe`, `project_stack_detect` → `perception`; `job_*` → `batch`.
If a skill name does not match a valid prefix or a schema result, do not invent it.
