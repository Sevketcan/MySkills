# Opt-in personal full-stack project profile

This profile is for a project that has chosen Sevketcan's Next.js/NestJS stack. Current user requirements and deliberate existing project decisions take precedence over its defaults.

- New app layout: independent frontend/ and backend/ directories; reuse within each app.
- TypeScript, Next.js App Router, NestJS, PostgreSQL/Prisma.
- UI preference: shadcn/ui + Tailwind; react-hook-form + zod for forms.
- API default: /api/v1/ and {data, message, statusCode}; feature gateways only when WebSockets are needed.
- Data defaults: cuid IDs, createdAt/updatedAt, explicit relations, soft deletion for user data.
- Hosting: the shared platform server (platform-1) behind Cloudflare, following `Sevketcan/infra` docs/NEW-PROJECT.md (project number NN → ports 30NN/40NN, `<project>-api`/`-web` in PM2 fork mode, media in Cloudflare R2).
- Builds run in GitHub Actions; production changes go only through the project's pipeline and the shared platform deploy. Deployment remains subject to the current task's authorization.
- Secrets: dotenvx-encrypted `.env.production` in git, `.env.keys` never. Keep this project's chosen environment-file policy; this template establishes no new permission to commit credentials.
- Nothing longer than ~100 s inside one request (Cloudflare drops it); move it to the background.
- Read the existing design system before changing appearance; do not impose a generic style.

Only introduce auth providers, WebSockets, state stores or other layers when the feature needs them. Select actual service names, ports and deployment branches from this repository; this profile does not supply them.
