---
name: unity-mcp-orchestrator
description: "Operate Unity through MCP tools and resources: instance selection, compilation lifecycle, target discovery, edit hashes and result verification."
---

# Unity MCP integration

Use the connected tool schema and current Editor state as the authority. Read only resources and references needed to resolve an uncertain target or operation.

- Select the intended Unity instance when several are connected. Discover target IDs/components before writing; names and template payloads may be ambiguous.
- `create_script` and `script_apply_edits` already import and request compilation. Wait for compilation to finish and inspect console errors before attaching components; avoid a redundant refresh.
- Batch independent operations within the server's current limit. Dependent operations need sequential execution or fail-fast handling.
- For hash-based edits, refetch the source/hash after a stale-hash failure rather than forcing the edit.
- During compilation/domain reload, wait for a ready state before retrying; a timeout does not prove the previous write failed.
- Verify affected behavior or returned Editor state. Capture a screenshot for a visual change; code-only operations do not require a screenshot ritual.

| Need | Reference |
| --- | --- |
| Tool payload examples | [Tools](references/tools-reference.md) |
| Available resources | [Resource examples](references/operator-examples.md) |
| Scene and script workflows | [Workflows](references/workflows.md) |
| ProBuilder operations | [ProBuilder tools](references/tools-reference.md#probuilder-tools) |
| Additional connector examples | [Operator examples](references/operator-examples.md) |

Examples must be adapted to the installed packages, Unity version and live tool schema. Do not load the full reference set for a single edit.
