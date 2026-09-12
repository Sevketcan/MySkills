---
name: "fullstack-dev"
description: "Sevketcan's personal full-stack development conventions, architecture patterns, and boilerplate generator. Use this skill whenever the user: starts a new project, asks where to put a file, asks how to structure an API, a module, a component, a database relation, or a form, asks about auth, RBAC, WebSocket setup, Prisma schema design, Vercel/EC2 deployment, or CI/CD. Also trigger for modular decomposition, reusable components/modules, domain separation, folder structure planning, scalable data architecture, updating the production server, handling .env files, multiple projects sharing one EC2 box, PM2/port naming collisions, memory/OOM/swap sizing, form validation, or \"how should I...\", \"where should I...\", \"should I separate this...\", \"is this reusable?\" questions in a full-stack context. Defines THE canonical stack, folder conventions, deployment discipline, and modularity discipline — always consult before any scaffolding, file structure, architecture, deployment, or reusability decision."
---

# Full-Stack Developer Skill

Sevketcan's canonical patterns for every new project. Always follow these conventions exactly — do not improvise alternatives unless explicitly asked.

---

## Stack (Non-Negotiable)

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js, App Router only — min v14 |
| Backend | NestJS — min v10 |
| Language | TypeScript everywhere |
| Database | PostgreSQL (min v14) + Prisma |
| UI | shadcn/ui + Tailwind CSS |
| Forms | react-hook-form + zod |
| Auth | JWT + AWS Cognito (RBAC) |
| API | REST + WebSocket |
| Frontend hosting | Vercel |
| Backend hosting | AWS EC2 + RDS (Postgres) + S3 — often one EC2 box shared across several projects, see Shared EC2 Host below |
| Serverless | AWS Lambda — isolated tasks only, not core backend |
| Backend server | Nginx + PM2, on EC2 |
| CI/CD | GitHub Actions — the only path to production, see Deployment Discipline below |

Versions above are floors, not pins — a newer stable release is always fine. Only go below the floor for a specific, stated reason.

---

## Project Structure

Every project has exactly **two top-level folders**: `frontend/` and `backend/`. 

**No cross-app `shared/` folder at the project root.** There is no shared package between frontend and backend — types that exist on both sides are duplicated manually. Each app is fully independent.

Within each app, internal reusability is encouraged:
- `frontend/src/components/shared/` — reusable UI components across features
- `backend/src/common/` — reusable guards, interceptors, decorators across modules

```
project-root/
├── frontend/          # Next.js App Router
└── backend/           # NestJS
```

### Frontend Structure

```
frontend/
├── src/
│   ├── app/                    # Next.js App Router pages
│   │   ├── (auth)/             # Route groups
│   │   ├── (dashboard)/
│   │   └── layout.tsx
│   ├── components/
│   │   ├── ui/                 # shadcn/ui primitives (auto-generated)
│   │   └── [feature]/          # Feature-specific components
│   ├── lib/
│   │   ├── api/                # Axios instances + REST hooks
│   │   ├── socket/             # WebSocket client setup
│   │   ├── validations/        # zod schemas, one file per feature/form
│   │   └── utils.ts
│   ├── hooks/                  # Custom React hooks
│   ├── store/                  # Zustand stores (if global state needed)
│   ├── types/                  # TypeScript interfaces/types
│   └── constants/
├── public/
├── .env.local
├── next.config.ts
├── tailwind.config.ts
└── package.json
```

### Backend Structure

```
backend/
├── src/
│   ├── main.ts
│   ├── app.module.ts
│   ├── config/                 # ConfigModule setup, env validation
│   ├── common/
│   │   ├── decorators/         # Custom decorators (@CurrentUser, @Roles)
│   │   ├── guards/             # AuthGuard, RolesGuard
│   │   ├── interceptors/       # ResponseInterceptor, LoggingInterceptor
│   │   ├── filters/            # GlobalExceptionFilter
│   │   ├── pipes/              # ValidationPipe
│   │   └── dto/                # Shared DTOs (pagination, response wrappers)
│   ├── prisma/                 # PrismaService + PrismaModule
│   ├── auth/                   # JWT + Cognito auth module
│   ├── users/
│   └── [feature]/              # Each feature is a NestJS module
│       ├── [feature].module.ts
│       ├── [feature].controller.ts
│       ├── [feature].service.ts
│       ├── [feature].gateway.ts  # WebSocket gateway (if needed)
│       ├── dto/
│       │   ├── create-[feature].dto.ts
│       │   └── update-[feature].dto.ts
│       └── entities/
│           └── [feature].entity.ts
├── prisma/
│   └── schema.prisma
├── .env
└── package.json
```

---

## Conventions

### API Design (REST)

- All routes prefixed: `/api/v1/`
- Controllers use `@ApiTags`, `@ApiBearerAuth` (Swagger)
- Response wrapper: always `{ data, message, statusCode }`
- Errors: always throw NestJS `HttpException` or built-in exceptions
- DTOs: always use `class-validator` decorators

```typescript
// Standard response shape
{
  statusCode: 200,
  message: "Success",
  data: T
}
```

### WebSocket

- Use `@WebSocketGateway` per feature module, not a single global gateway
- Namespace pattern: `@WebSocketGateway({ namespace: '/feature' })`
- Auth: validate JWT on `handleConnection()` — reject unauthenticated sockets immediately
- Frontend: single `socket.ts` in `lib/socket/` — export named socket instances per namespace
- Events: snake_case names (`user_joined`, `message_sent`)

```typescript
// backend: src/chat/chat.gateway.ts
@WebSocketGateway({ namespace: '/chat', cors: { origin: process.env.FRONTEND_URL } })
export class ChatGateway implements OnGatewayConnection {
  handleConnection(client: Socket) {
    const token = client.handshake.auth.token;
    // validate JWT — disconnect if invalid
  }
}
```

### Auth & RBAC

- JWT issued by NestJS auth module after Cognito verification
- `@Roles('admin', 'user')` decorator + `RolesGuard` applied globally
- JWT payload: `{ sub: userId, email, roles: string[] }`
- Guards order: `AuthGuard` → `RolesGuard`
- All protected routes use `@UseGuards(AuthGuard, RolesGuard)`

### Database & Prisma

See `references/database.md` for full patterns.

**Quick rules:**
- Always define `createdAt`, `updatedAt` on every model
- Use `cuid()` for IDs (not `uuid`)
- Junction tables always named `[ModelA][ModelB]` (e.g., `UserProject`)
- Soft deletes: add `deletedAt DateTime?` — never hard delete user data
- Relations: always define both sides explicitly in schema

### Environment Variables

**`.env` and `.env.local` are committed to git — do not add them to `.gitignore`.** This is a deliberate project convention, not an oversight: env files travel with the code through the deploy pipeline (see Deployment Discipline below) instead of being managed by hand on a server, and it holds even for projects that predate the convention (if an older project's history shows `.env` being untracked, bring it back in line rather than treating that old commit as precedent). Sevketcan has weighed the tradeoff (secrets living in git history) and accepts that risk. Don't "fix" this by adding `.env`/`.env.local` back to `.gitignore` unless explicitly asked to change the convention — and don't keep ad-hoc manual `.env` backup folders on the server (e.g. `project-env-backups/`) either, since git history already is the backup once `.env` is tracked.

```bash
# backend/.env
DATABASE_URL=
JWT_SECRET=
JWT_EXPIRES_IN=7d
AWS_REGION=
AWS_COGNITO_USER_POOL_ID=
AWS_COGNITO_CLIENT_ID=
FRONTEND_URL=

# frontend/.env.local
NEXT_PUBLIC_API_URL=
NEXT_PUBLIC_WS_URL=
```

No env validation library unless the project is large — keep it simple.

### Deployment Discipline (EC2 — Non-Negotiable)

**Never edit files directly on EC2.** No SSH-in-and-`nano`, no manually restarting the app with code that differs from `main`, no hand-patching a config "just to fix it quickly." The only path to production is:

**local → commit → push to `main` → GitHub Actions → EC2**

This isn't just process for its own sake: since `.env` is committed to the repo, the deploy pipeline's `git pull` already brings the correct env alongside the code every time. A manual edit on the server drifts silently from git and gets clobbered on the next deploy anyway — it's not a shortcut, it's a landmine for the next deploy.

**The folder structure on EC2 should always be an exact mirror of the git repo — `git status` on the server should come back clean.** Any file that isn't tracked (log dumps, ad-hoc backup folders, one-off scripts left over from debugging, a stray file created by a typo'd redirect) is evidence something was done by hand instead of through git. Either commit it, delete it, or gitignore it explicitly the moment it's noticed — don't let it accumulate.

The only things done directly on the EC2 box are read-only: checking `pm2 logs`, `pm2 status`, tailing Nginx logs. Anything that changes behavior — code, config, env — goes through a commit.

Frontend deploys separately and automatically to Vercel on push to `main`; no manual edits in the Vercel dashboard either, for the same reason.

### Shared EC2 Host (Multi-Project Box)

It's normal for more than one project's backend to live on the same EC2 instance. When that's the case:

- **PM2 process name is `<project>-api`, never the generic `api`.** Two projects both naming their process `api` collide the moment you try to `pm2 restart api` and target the wrong one.
- **Nginx site config filename matches the exact domain it serves** (e.g. `api.projectname.com`), so `ls /etc/nginx/sites-enabled/` is self-explanatory and lines up with what Certbot expects. Don't name it after the project instead of the domain.
- **One port per project**, noted somewhere obvious (a comment at the top of each `ecosystem.config.js` is enough) — don't let two services silently fight over the same port.
- **Default PM2 mode is `fork`, not `cluster` / `instances: 'max'`.** Cluster mode multiplies memory footprint per CPU core; on a small shared box running multiple apps, that's how you get OOM-killed. Check `free -h` before ever reaching for cluster mode, and expect fork mode to be the right answer on anything under ~4GB RAM.

### Build & Deploy Correctness

`npm ci --omit=dev` followed by `npm run build` is a trap — the build step needs the TypeScript compiler and other devDependencies that `--omit=dev` just stripped out. Two fixes, prefer the second:
1. Build before pruning dev deps (`npm ci` → `npm run build` → then a separate prune), or
2. Better, especially on a memory-constrained box: don't build on EC2 at all. Run `npm run build` in the GitHub Actions runner (plenty of RAM there), then ship only `dist/`, `package.json`, `package-lock.json`, and `prisma/` to EC2. The box then just runs `npm ci --omit=dev` (fast, no compiler needed) and `pm2 reload ecosystem.config.js` — `reload`, not `restart`, for zero-downtime.

After every deploy, glance at `pm2 list`. A restart count (`↺`) that keeps climbing between deploys — not just incrementing once per deploy — means something is crashing or getting OOM-killed, not that PM2 is "just doing its job." Chase it down via `pm2 logs --err` rather than letting it ride.

### Server Sizing

If an EC2 box is running production traffic with under ~2GB RAM and no swap configured, add a swapfile. It's cheap insurance against a build, a traffic spike, or a slow memory leak OOM-killing a live process outright instead of just degrading gracefully.

### Frontend API Layer

```typescript
// lib/api/client.ts — single Axios instance
import axios from 'axios';

export const apiClient = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL,
});

apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});
```

- One Axios instance, one file
- Feature-specific API functions in `lib/api/[feature].ts`
- No React Query by default — use `useState` + `useEffect` unless the project specifically needs caching

### Forms (react-hook-form + zod)

Every form — not just "complex" ones — goes through `react-hook-form` with a `zod` schema via `zodResolver`. No hand-rolled `useState` per field, no submitting an uncontrolled form and validating after the fact. This isn't extra ceremony for a two-field form: the moment a field is added later, you already have validation, error display, and submit-state handling for free instead of retrofitting it.

**Schema location:** one zod schema per form, in `lib/validations/[feature].ts` — not one giant file with every schema in the project, and not inlined in the component. Export both the schema and its inferred type:

```typescript
// lib/validations/project.ts
import { z } from 'zod';

export const createProjectSchema = z.object({
  name: z.string().min(2, 'En az 2 karakter').max(80),
  budget: z.coerce.number().positive(),
});

export type CreateProjectValues = z.infer<typeof createProjectSchema>;
```

**Component:** always use shadcn's `Form` primitives (`Form`, `FormField`, `FormItem`, `FormLabel`, `FormControl`, `FormMessage`) from `components/ui/form` — never hand-write error text under an input, that's what `FormMessage` is for. Submit-button disabled state comes from `form.formState.isSubmitting`, not a separately tracked loading flag.

```typescript
// components/[feature]/ProjectForm.tsx
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { Form, FormField, FormItem, FormLabel, FormControl, FormMessage } from '@/components/ui/form';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { createProjectSchema, CreateProjectValues } from '@/lib/validations/project';

export function ProjectForm({ onSubmit }: { onSubmit: (values: CreateProjectValues) => Promise<void> }) {
  const form = useForm<CreateProjectValues>({
    resolver: zodResolver(createProjectSchema),
    defaultValues: { name: '', budget: 0 },
  });

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
        <FormField
          control={form.control}
          name="name"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Name</FormLabel>
              <FormControl><Input {...field} /></FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <Button type="submit" disabled={form.formState.isSubmitting}>Save</Button>
      </form>
    </Form>
  );
}
```

**Placement:** a form component almost always has feature-specific API calls and business rules baked in, so it belongs in `components/[feature]/` under the three-tier hierarchy — it does not qualify for `components/shared/` even if the same shape of form appears in two features (see the `shared/` purity rule below).

**Frontend/backend duplication is expected here too:** the zod schema on the frontend and the `class-validator` DTO on the backend describe the same shape but are two separate definitions, consistent with this project's "no shared types folder" convention. When a field changes, update both by hand — there's no codegen step tying them together.

---

## Boilerplate Generation

When asked to scaffold a new project or a new feature module, always generate:

**New project:**
1. `frontend/` — Next.js with the structure above, shadcn/ui initialized, Axios client, socket setup
2. `backend/` — NestJS with PrismaModule, AuthModule, common guards/interceptors wired in `AppModule`

**New feature module:**
1. `[feature].module.ts`
2. `[feature].controller.ts` (REST)
3. `[feature].service.ts`
4. `[feature].gateway.ts` (WebSocket, if needed)
5. `dto/create-[feature].dto.ts`, `dto/update-[feature].dto.ts`
6. Prisma model snippet
7. If the feature has a create/edit form: `lib/validations/[feature].ts` (zod schema) + the form component in `components/[feature]/`

Always produce complete, runnable TypeScript — no pseudocode, no `// TODO: implement`.

---

## Modular Decomposition & Reusability Discipline

This is a core principle, not optional. Every architecture decision must pass this filter first.

See `references/modularity.md` for the full playbook. Quick rules below:

### Architecture: Modular Monolith with Microservice-Ready Boundaries

The backend is a **modular monolith** — one NestJS application, one deployment unit, but with hard domain boundaries that could be split into true microservices later with minimal refactoring.

- ✅ Modular monolith — correct term, correct approach for this stage
- ✅ Microservice-ready — boundaries are clean enough to extract anytime
- ❌ Microservices — we do NOT run separate processes/deployments per domain

### The Core Question
Before writing any file, ask: **"Will this exist in exactly one place, or could it be needed elsewhere?"**
- If it could be needed elsewhere → write it future-proof from day one, extract on second use
- If it's truly feature-specific → keep it local, don't over-engineer

### Domain Separation (Backend)
Split `backend/src/` by **business domain**, not by technical type:

```
src/
├── auth/           # Authentication, token management
├── users/          # User profile, settings
├── brands/         # Brand entity + brand-scoped logic
├── projects/       # Project entity + project operations
├── notifications/  # Reusable across all domains
├── files/          # S3 upload abstraction — reusable
├── mail/           # Email sending — reusable
└── common/         # Guards, interceptors, decorators — always reusable
```

**Rule:** If a module is imported by 2+ other modules → dedicated reusable module. Never duplicate service logic.

### Inter-Module Communication Rules

| Scenario | Pattern |
|----------|---------|
| Synchronous data fetch | Direct service injection — import the module, inject the service |
| Cross-domain side effect (e.g. send email on user created) | Event-based — `EventEmitter2`, never direct call |
| Circular dependency detected | Break with events, never `forwardRef()` as default solution |
| Universal utility (files, mail, audit) | `@Global()` module — infrastructure-level only, never domain modules |

```typescript
// Sync: ProjectsService needs to verify a user exists
constructor(private usersService: UsersService) {}  // direct injection, fine

// Async side effect: notify on project creation — use events
this.eventEmitter.emit('project.created', { projectId, userId });
// NotificationsService listens via @OnEvent('project.created')
```

### Data Ownership Rule

Each module owns its data exclusively:
- **Only the owning module's service writes to its tables**
- Other modules must call that module's service — never query its tables directly
- No cross-module Prisma queries — if `ProjectsService` needs user data, it calls `UsersService.findById()`, it does not query `prisma.user` itself

### Component Reusability (Frontend)

Three-tier component hierarchy — never mix tiers:

```
components/
├── ui/             # Tier 1: shadcn primitives + your extensions (zero business logic)
├── shared/         # Tier 2: composite components, domain-agnostic, zero feature coupling
│   ├── DataTable/
│   ├── PageHeader/
│   ├── ConfirmModal/
│   └── FileUploader/
└── [feature]/      # Tier 3: feature-specific, intentionally not reusable
    ├── brand/
    ├── project/
    └── user/
```

**`components/shared/` purity rule:** A component does NOT belong in `shared/` if it contains any of:
- Feature-specific API calls
- Role or permission checks
- Business rules tied to a specific domain

If it has any of these → it stays in `components/[feature]/` regardless of how many places use it. Duplicate if necessary. `shared/` must stay domain-agnostic.

### Logic Placement (Frontend)

| Layer | What goes here |
|-------|----------------|
| `components/ui/` | Zero logic — props in, JSX out |
| `components/shared/` | Minimal reusable logic only (formatting, display state) |
| `components/[feature]/` | Feature business logic, API calls, local state |
| `hooks/` | Any logic used in 2+ components — extract immediately |

**Rule:** If a component file exceeds ~150 lines or has 3+ `useState` calls → extract logic to a custom hook.

### Layouts (Frontend)
App Router `layout.tsx` hierarchy handles structural layouts:

```
src/app/
├── (auth)/layout.tsx         # Auth layout (centered, no sidebar)
├── (dashboard)/layout.tsx    # Dashboard layout (sidebar + topbar)
└── layout.tsx                # Root (providers, fonts)
```

Never inline layout structure inside page components.

### Reusability Decision Table

| Situation | Action |
|-----------|--------|
| Used in 1 place, domain-specific | Keep local — write future-proof but don't extract yet |
| Used in 2+ places, no business logic | Extract to `components/shared/` |
| Used in 2+ places, has feature-specific logic | Stay in `components/[feature]/` — duplicate if needed |
| Used in 2+ places, generic logic only | Extract to `components/shared/` |
| Backend service used by 2+ modules | Standalone NestJS module, export the service |
| Utility function in 2+ files | `lib/utils/` or `common/utils/` |
| Repeated Prisma query pattern | Repository class inside the owning module |

---

## Frontend Design System

All UI must follow the design system rules. See `references/design-system.md` for the full spec.

**Non-negotiable summary:**

| Property | Rule |
|----------|------|
| Border radius | `rounded-none` or `rounded-sm` only |
| Shadows | `shadow-none` — use `border border-gray-200` instead |
| Backgrounds | `bg-white`, `bg-gray-50`, `bg-gray-100` — no gradients |
| Colors | One accent color per project, standard status colors only |
| Spacing | Tailwind 4px scale only — no arbitrary values |
| Animations | `transition-colors duration-150` max — no bounces, no scale |
| Dark mode | Project-specific — not default |

**Anti-patterns (hard stop):** `rounded-xl`, `shadow-lg`, gradient backgrounds, multiple accent colors, inconsistent padding, mixed visual styles on the same page.

Read `references/design-system.md` whenever generating any UI code — it contains the full Tailwind token constraints, component rules, and a pre-ship checklist.

---

## Reference Files

- `references/database.md` — Prisma patterns, ERD conventions, query optimization, N+1 fixes
- `references/infra.md` — AWS + Vercel setup, Nginx config, PM2 ecosystem, GitHub Actions CI/CD (frontend → Vercel, backend → EC2). Note: its sample GitHub Actions workflow builds on EC2 directly — superseded by Build & Deploy Correctness above; prefer building in the CI runner and shipping only build output.
- `references/modularity.md` — Full modular decomposition playbook, inter-module dependency rules, data consistency patterns
- `references/design-system.md` — Frontend design rules, Tailwind token constraints, component rules, anti-patterns, dark mode spec
- `references/react-query.md` — When to use React Query vs useState+useEffect, query key conventions, setup
- `references/rate-limiting.md` — `@nestjs/throttler` global setup, per-endpoint overrides, WebSocket handling
- `references/logging.md` — Logger usage, what to log/not log, GlobalExceptionFilter, LoggingInterceptor, PM2 log management

Read the relevant reference file when the task involves schema design, deployment, architecture decisions, UI generation, or any of the above topics.

