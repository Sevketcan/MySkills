# Modular Decomposition & Reusability Playbook

## Principle

Design systems where every piece has one home, one responsibility, and zero duplication. Build for growth from day one — not after the mess accumulates.

**Architecture pattern: Modular Monolith with Microservice-Ready Boundaries**

One NestJS app, one deployment. But every domain module is isolated enough that it could be extracted into a separate service later with surgical precision — no spaghetti to untangle.

---

## Backend: NestJS Module Architecture

### Domain-Driven Module Boundaries

Each module owns its domain completely:
- Its own controller (HTTP interface)
- Its own service (business logic)
- Its own DTOs (input/output contracts)
- Its own Prisma queries (data access)

**Never reach into another module's service directly.** If you need data from another domain → either import that module, or use events.

```typescript
// WRONG — ProjectService directly instantiating UserService
@Injectable()
export class ProjectService {
  constructor(private userService: UserService) {} // tight coupling
}

// RIGHT — import the module and use its public service
// projects.module.ts
@Module({
  imports: [UsersModule],   // UsersModule exports UsersService
  providers: [ProjectsService],
})
export class ProjectsModule {}
```

### Backend Extraction Thresholds

Just as frontend components get split when they grow too large, backend services have their own extraction triggers:

| Signal | Action |
|--------|--------|
| Service file exceeds ~200 lines | Split into use-case-specific services within the same module |
| Same Prisma query pattern repeated 3+ times | Extract to a repository class inside the owning module |
| Service handles both orchestration AND persistence | Separate: orchestration stays in service, DB access moves to repository |
| More than one distinct responsibility in a service | Split into two services — one responsibility per service |

```typescript
// BEFORE — ProjectsService doing too much
@Injectable()
export class ProjectsService {
  async create() { /* orchestration + db */ }
  async findAll() { /* complex query repeated elsewhere */ }
  async findWithMembers() { /* same complex query, different shape */ }
  async addMember() { /* orchestration + db + event emit */ }
  async generateReport() { /* completely different concern */ }
}

// AFTER — responsibilities separated
// projects.repository.ts  → all Prisma queries
// projects.service.ts     → orchestration, events, business rules
// projects-report.service.ts → report generation (separate concern)
```

### `@Global()` Usage Rule

`@Global()` is for **infrastructure-level modules only** — modules that provide technical capabilities, not business logic.

```
✅ @Global() allowed          ❌ @Global() never
PrismaModule                  BrandsModule
ConfigModule                  ProjectsModule
LoggerModule                  UsersModule
MailModule                    NotificationsModule (unless truly infra)
FilesModule
AuditModule
```

Domain modules are always imported explicitly — if a domain module feels like it needs `@Global()`, it's a sign the boundary is wrong, not that it should be global.

Any module used by 2+ other modules becomes a standalone reusable module:

```
src/
├── files/
│   ├── files.module.ts      # @Global() if used everywhere
│   ├── files.service.ts     # S3 upload, presigned URL logic
│   └── dto/
├── mail/
│   ├── mail.module.ts
│   ├── mail.service.ts      # Resend/SES wrapper
│   └── templates/           # Email templates
├── notifications/
│   ├── notifications.module.ts
│   ├── notifications.service.ts
│   └── notifications.gateway.ts
└── audit/
    ├── audit.module.ts
    └── audit.service.ts     # Write audit logs — used by everything
```

Mark truly universal **infrastructure-level** modules as `@Global()` — never domain modules:

```typescript
// ✅ Infrastructure — @Global() appropriate
@Global() @Module({ providers: [FilesService], exports: [FilesService] })
export class FilesModule {}

// ❌ Domain module — never @Global(), always import explicitly
@Module({ providers: [BrandsService], exports: [BrandsService] })
export class BrandsModule {}
```

`@Global()` is for: `PrismaModule`, `ConfigModule`, `MailModule`, `FilesModule`, `AuditModule`.
Never for: any module that represents a business domain.

### Inter-Module Communication Rules

**Synchronous operations → direct service injection**
```typescript
// ProjectsService needs to verify a user — import UsersModule, inject UsersService
@Module({ imports: [UsersModule], providers: [ProjectsService] })
export class ProjectsModule {}

@Injectable()
export class ProjectsService {
  constructor(private usersService: UsersService) {}

  async addMember(projectId: string, userId: string) {
    const user = await this.usersService.findById(userId); // direct call — correct
    if (!user) throw new NotFoundException('User not found');
    // ...
  }
}
```

**Cross-domain side effects → event-based**
```typescript
// projects.service.ts — emits, doesn't know who listens
this.eventEmitter.emit('project.created', { projectId, userId });

// notifications.service.ts — listens, fully decoupled
@OnEvent('project.created')
async handleProjectCreated(payload: ProjectCreatedEvent) {
  await this.sendNotification(payload.userId, 'Your project is ready');
}

// mail.service.ts — also listens to the same event, independently
@OnEvent('project.created')
async sendWelcomeMail(payload: ProjectCreatedEvent) {
  await this.send({ to: payload.email, template: 'project-welcome' });
}
```

**Circular dependency → always resolve with events, never `forwardRef()`**
```typescript
// If A depends on B and B depends on A:
// WRONG: forwardRef(() => BModule) — masks the problem
// RIGHT: extract the shared concern to a third module C, or use events
```

### Data Ownership Rule

**Each module owns its Prisma models exclusively.**

| Rule | Detail |
|------|--------|
| Only the owner writes | Only `ProjectsService` writes to the `Project` table |
| Others use the service layer | `UsersService` calls `ProjectsService.findById()` — never `prisma.project` directly |
| No cross-module Prisma queries | If you find yourself reaching for `prisma.user` inside `ProjectsService`, stop — inject `UsersService` instead |
| Read-only exceptions | Allowed only in reporting/analytics modules with explicit justification |

```typescript
// WRONG — BrandsService crossing into Projects data
@Injectable()
export class BrandsService {
  async getBrandWithProjects(brandId: string) {
    return this.prisma.brand.findUnique({
      include: { projects: true },  // ❌ Projects data owned by ProjectsModule
    });
  }
}

// RIGHT — BrandsService stays in its lane, asks ProjectsService
@Injectable()
export class BrandsService {
  constructor(private projectsService: ProjectsService) {}

  async getBrandWithProjects(brandId: string) {
    const brand = await this.prisma.brand.findUnique({ where: { id: brandId } });
    const projects = await this.projectsService.findByBrand(brandId); // ✅
    return { ...brand, projects };
  }
}
```

### Repository Pattern (when queries get complex)

When a module's service has 5+ Prisma queries, extract to a repository class:

```typescript
// projects/projects.repository.ts
@Injectable()
export class ProjectsRepository {
  constructor(private prisma: PrismaService) {}

  findByBrand(brandId: string, pagination: PaginationDto) {
    return this.prisma.project.findMany({
      where: { brandId, deletedAt: null },
      include: { users: true },
      skip: (pagination.page - 1) * pagination.limit,
      take: pagination.limit,
    });
  }

  findWithMembers(id: string) {
    return this.prisma.project.findUnique({
      where: { id },
      include: { users: { include: { user: true } } },
    });
  }
}

// projects.module.ts — add to providers
providers: [ProjectsService, ProjectsRepository]
```

---

## Frontend: Component Architecture

### Three-Tier Hierarchy (strict)

**Tier 1 — `components/ui/`**
- shadcn/ui generated components + your custom primitives
- Zero business logic, zero API calls, zero global state
- Props only — pure display

**Tier 2 — `components/shared/`**
- Composite components reusable across features
- May know about data shapes (types) but not about specific feature domains
- Minimal logic — formatting, display state, generic interactions only
- **Purity rule:** Does NOT contain feature-specific API calls, role/permission checks, or domain business rules. If a component needs any of these → it stays in `[feature]/`, even if used in multiple places. Duplicate rather than pollute `shared/`.

```typescript
// ❌ Does NOT belong in shared/ — has role check + feature API call
export function ProjectActionsMenu({ projectId }: { projectId: string }) {
  const { role } = useAuth();
  const deleteFn = () => projectApi.delete(projectId);
  return role === 'admin' ? <Menu onDelete={deleteFn} /> : null;
}

// ✅ Belongs in shared/ — generic, no domain coupling
export function ActionsMenu({ items }: { items: MenuItem[] }) {
  return <DropdownMenu items={items} />;
}
```

**Tier 3 — `components/[feature]/`**
- Feature-specific, intentionally not reusable by design
- Business logic lives here: API calls, feature state, domain rules

### Logic Placement Rules

```
components/ui/         → zero logic. props in, JSX out.
components/shared/     → minimal reusable display logic only
components/[feature]/  → feature business logic, API calls, local state
hooks/                 → any logic used in 2+ components — extract immediately
```

**Extraction trigger:** If a component exceeds ~150 lines OR has 3+ `useState` calls → extract logic to a custom hook. Component stays presentational, hook owns the logic.

```typescript
// BEFORE — component doing too much
export function ProjectList() {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(false);
  const [page, setPage] = useState(1);
  const [total, setTotal] = useState(0);
  // + fetch logic, error handling, pagination logic...
}

// AFTER — clean separation
// hooks/project/useProjects.ts owns all the logic
export function useProjects() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(false);
  const pagination = usePagination();
  // fetch logic here
  return { projects, loading, ...pagination };
}

// component stays thin
export function ProjectList() {
  const { projects, loading, page, setPage } = useProjects();
  return <DataTable data={projects} ... />;
}
```

### Future-Proof Writing Rule

When writing a component for the first time in `[feature]/`:
- Write it as if it *might* become shared someday
- Use generic prop names, avoid hardcoding feature-specific strings inside
- Extract any reusable sub-pieces to `ui/` immediately even on first use
- On second use anywhere → promote to `shared/` before proceeding

**Promotion workflow:**
```
First use → [feature]/ComponentName.tsx  (write future-proof)
Second use needed → move to shared/ComponentName/ → update imports → continue
```

### Custom Hooks — Reusability Layer

Extract any logic used in 2+ components into a custom hook:

```
hooks/
├── useDebounce.ts          # Generic
├── usePagination.ts        # Generic
├── useConfirmModal.ts      # Generic
├── useFileUpload.ts        # Generic (calls FilesService)
└── [feature]/
    ├── useBrands.ts        # Feature-specific API hook
    └── useProjectMembers.ts
```

```typescript
// hooks/usePagination.ts — generic, reusable
export function usePagination(defaultLimit = 20) {
  const [page, setPage] = useState(1);
  const [limit] = useState(defaultLimit);
  const reset = () => setPage(1);
  return { page, limit, setPage, reset };
}

// hooks/brand/useBrands.ts — feature-specific
export function useBrands() {
  const [brands, setBrands] = useState<Brand[]>([]);
  const [loading, setLoading] = useState(false);
  const pagination = usePagination();

  useEffect(() => {
    setLoading(true);
    brandApi.findAll(pagination.page).then(setBrands).finally(() => setLoading(false));
  }, [pagination.page]);

  return { brands, loading, ...pagination };
}
```

### API Layer Decomposition

```
lib/api/
├── client.ts               # Axios instance (single)
├── brands.ts               # All brand endpoints
├── projects.ts             # All project endpoints
├── users.ts                # All user endpoints
└── files.ts                # Upload URL, etc.
```

One file per domain. Functions are plain async functions, not classes:

```typescript
// lib/api/projects.ts
export const projectApi = {
  findAll: (brandId: string, page: number) =>
    apiClient.get<PaginatedResponse<Project>>(`/projects`, { params: { brandId, page } }),

  findById: (id: string) =>
    apiClient.get<Project>(`/projects/${id}`),

  create: (dto: CreateProjectDto) =>
    apiClient.post<Project>(`/projects`, dto),
};
```

---

## Data Architecture: Feature-Aligned but Consistent

### Schema Mirrors Domain Boundaries

Every backend domain has its own Prisma models. Cross-domain relations are explicit:

```prisma
// Brand domain
model Brand { ... }

// Project domain — references Brand
model Project {
  brandId String
  brand   Brand  @relation(...)
}

// User domain — junction with Project (cross-domain)
model UserProject {
  userId    String
  projectId String
  role      ProjectRole
}
```

### Cross-Module Data Consistency

When data spans multiple domains (e.g., deleting a Brand should cascade):

- Define `onDelete: Cascade` in Prisma schema at the relation level
- Never handle cascades manually in service code
- For soft deletes: set `deletedAt` on parent, filter children by join

```prisma
model Project {
  brandId String
  brand   Brand  @relation(fields: [brandId], references: [id], onDelete: Cascade)
}
```

### Feature-Aligned Indexing

Add indexes that reflect your actual query patterns per feature:

```prisma
model Project {
  @@index([brandId])               // always — tenant filter
  @@index([brandId, status])       // if you filter by status within brand
  @@index([createdAt])             // if you sort by date frequently
}

model UserProject {
  @@index([projectId])             // find members of a project
  @@index([userId])                // find projects of a user
}
```

---

## Growth Rules Summary

| Rule | Detail |
|------|--------|
| Write future-proof from day one | Even first-use code should be clean enough to promote later |
| 2+ uses → extract immediately | Module, component, function — extract before adding the second use |
| Domain owns its data | No service queries another domain's tables via Prisma directly |
| Events for side effects | Cross-domain triggers use EventEmitter, never direct injection |
| No circular deps | Resolve with events or a third shared module — never `forwardRef()` |
| Logic out of components | 3+ useState or 150+ lines → extract to a custom hook |
| Promote early | Move `[feature]/` components to `shared/` on second use — never copy-paste |
| Index at design time | Add Prisma indexes when writing the schema, not after seeing slow queries |
| `@Global()` for universals | FilesModule, MailModule, AuditModule — import once in AppModule |
