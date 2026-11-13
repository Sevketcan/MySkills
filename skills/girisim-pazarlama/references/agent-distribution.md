# Agent distribution: open the product to AI agents

Use this when the product does a job an agent could call for someone (look up data, add or change records, search) and the user wants to reach people who work inside ChatGPT, Claude or other agents. Writing the API or MCP server is engineering work in the project; this mode decides what to expose, where to publish it and how to judge it.

## Steps

1. **Check fit.** List the jobs users do in the interface and mark the ones an agent would call for them. If none fits, stop: this channel needs an API or MCP surface first.
2. **Match the interface (G22).** Every job the interface offers should also exist in the API or MCP server: reading, adding, editing, deleting.
3. **Choose the login per tool (G22).**
   - Read-only tools on public data can work without login.
   - Tools that touch a user's own data need OAuth; many directories and agent clients don't accept an API key alone.
   - Keep OAuth scopes narrow. An agent can call a write or delete tool many times in a row.
4. **Test end to end** in at least one agent client: sign-in, read, write, delete.
5. **Publish to the official MCP Registry first (G22).** Many directories copy their listings from it.
   - Consider keeping the registry definition files (for example `server.json` for the official registry, and the files other registries ask for) in one public repository. Some registries reportedly index from such a repository without a form; check each one's current instructions.
6. **Then list it in directories,** the highest-traffic ones first. Check each directory's current submission rules; some sell paid fast tracks. Prepare and submit as in [press-and-launch.md](press-and-launch.md), section 4: one manifest, the user's approval, and the user handles sign-ins and CAPTCHAs.
7. **Measure it like any other channel.** Record visits and connections per directory (a UTM tag, or the client name on the server side) and set a 4-week criterion as in [channel-plan.md](channel-plan.md).

## Guardrails

- Publishing to the registry or a directory, and paying for a fast track, need the user's approval.
- Never print or commit API keys, OAuth client secrets or registry tokens.
- Don't invent usage or traffic numbers for this channel; mark missing data as missing.
