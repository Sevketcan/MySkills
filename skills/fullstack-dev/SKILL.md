---
name: fullstack-dev
description: Set up or consult Sevketcan's opt-in full-stack project profile. Use when installing his project conventions or a project explicitly refers to this profile; do not impose it merely because an app uses Next.js or NestJS.
---

# Opt-in full-stack profile

Read project instructions first. They own stack, layout, API, deployment and appearance choices.

When the user requests the personal profile for a selected project, use the bundled [project instructions](assets/project-profile/AGENTS.md) and [Claude companion](assets/project-profile/CLAUDE.md).

Run scripts/apply_project_profile.py with the project path to preview; --apply installs the files. The helper refuses to overwrite unrelated instructions; merge those deliberately when the user requests a project-specific adaptation.

For detailed personal examples, read only the matching reference:

| Need | Reference |
| --- | --- |
| Profile defaults, layout and deployment examples | [Conventions](references/project-conventions.md) |
| Prisma data patterns | [Database](references/database.md) |
| Hosting, deploy, a new project on the platform | [Platform](references/infra.md) |
| Feature boundaries | [Modularity](references/modularity.md) |
| Visual preferences | [Design system](references/design-system.md) |
| Query state, rate limiting, logs | [React Query](references/react-query.md), [rate limiting](references/rate-limiting.md), [logging](references/logging.md) |

Examples are optional defaults for opted-in projects. Existing app decisions and current user scope prevail; do not add layers or migrate an app to satisfy these examples.
