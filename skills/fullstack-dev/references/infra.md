# Platform: hosting and deploy

Sevketcan's projects run on one shared server, **platform-1** (Hetzner, Germany), behind Cloudflare. The infra repository is the source of truth: `Sevketcan/infra` (locally `~/Development/infra`).

**To put a project on the platform, follow `infra/docs/NEW-PROJECT.md` step by step.** It has the current commands, file templates, workflow and the next free project number. Do not rebuild the steps from this summary; read the guide, and `infra/docs/DECISIONS.md` for the reasons.

## Shape

- Request path: Cloudflare (DNS, TLS, WAF) → Cloudflare Tunnel → nginx on 127.0.0.1:80 → the app on 127.0.0.1. The server has no inbound ports; SSH goes through Cloudflare Access (`ssh platform`).
- Every project has a permanent two-digit number NN: API port `30NN`, web `40NN`, extra process `50NN`, Redis DB `NN`. The project name (lowercase letters and digits) names its Unix user, its Postgres database and `/srv/<project>`. PM2 apps are `<project>-api`, `<project>-web`.
- Hostnames: API on `api.<domain>`, site on `www.<domain>` and/or the apex.
- PostgreSQL 18 (PostGIS on request) and Redis run on the same server, localhost only. `max_connections` (100) is shared by every project; keep Prisma pools small.
- Media: Cloudflare R2, served from `media.<domain>`. Browsers upload with a presigned **PUT** that signs the content type and size (R2 has no presigned POST). Use an R2 token scoped to the project's bucket, and a bucket CORS rule that allows only the site's origins.
- Sign-in: Firebase Authentication through the backend (REST, no browser SDK), or the project's own accounts when it already holds the password hashes. The backend issues the app's JWT either way.
- Email: MailBaby SMTP from the project's own domain, DKIM-signed by the app.
- Monitoring: Grafana Cloud (server, Postgres, Redis, uptime checks) and healthchecks.io (nightly backup). Alerts go to email and Telegram.
- Backups: a nightly `pg_dump` of every database, encrypted with `age`, kept in R2. Each deploy also dumps the database before it migrates.

## Repository side

Details and templates are in NEW-PROJECT.md:

- `platform/platform.json`, `platform/ecosystem.config.cjs` and `platform/build.sh`.
- Health endpoints that return the release: the API's health route and the web's `/healthz`. The deploy waits for both.
- Secrets: `<app>/.env.production`, encrypted with dotenvx and committed. `.env.keys` is never committed; it lives on the Mac (`~/.config/platform/dotenvx/<project>/`), on the server and in the offline backup. Public `NEXT_PUBLIC_*` values sit unencrypted in `.env`.
- `.github/workflows/deploy.yml` runs CI, then calls the shared `Sevketcan/infra/.github/workflows/deploy.yml@main`.

## Deploy

Push to `main` → CI → GitHub Actions builds the artifact → it is shipped through Cloudflare Access → `platform-release` on the server:

1. decrypts the env;
2. dumps the database and runs pending migrations;
3. switches `current` and reloads PM2;
4. waits for the health endpoints, and rolls back if they fail.

Write migrations additively; they are not rolled back. Never change files on the server; reading logs and status there is fine.

## Limits to design around

- Cloudflare drops a request after about 100 s. Move longer work to the background: start it, store its status, and announce the end on a socket with polling as a fallback. Travela's itinerary generation is the example.
- Each API runs as one PM2 process (fork mode). An in-process background job dies on deploy, so mark it interrupted when its status is read, or use a queue.
- The whole server has 8 GB of RAM for all projects. Real-time UDP game servers do not belong here, because Cloudflare and the Tunnel carry no UDP.
