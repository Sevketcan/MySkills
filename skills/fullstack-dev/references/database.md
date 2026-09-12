# Database & Prisma Reference

## Schema Conventions

```prisma
// Every model follows this base pattern
model User {
  id        String    @id @default(cuid())
  createdAt DateTime  @default(now())
  updatedAt DateTime  @updatedAt
  deletedAt DateTime? // soft delete

  email String @unique
  name  String
  roles Role[] @default([USER])

  // relations always defined on both sides
  projects UserProject[]
}

enum Role {
  USER
  ADMIN
  MANAGER
}
```

## Relation Patterns

### One-to-Many
```prisma
model Brand {
  id       String    @id @default(cuid())
  name     String
  projects Project[]
}

model Project {
  id      String @id @default(cuid())
  brandId String
  brand   Brand  @relation(fields: [brandId], references: [id])
}
```

### Many-to-Many (always explicit junction table)
```prisma
// Never use implicit @@relation — always explicit junction
model User {
  id       String        @id @default(cuid())
  projects UserProject[]
}

model Project {
  id    String        @id @default(cuid())
  users UserProject[]
}

model UserProject {
  userId    String
  projectId String
  role      ProjectRole @default(MEMBER)
  joinedAt  DateTime    @default(now())

  user    User    @relation(fields: [userId], references: [id])
  project Project @relation(fields: [projectId], references: [id])

  @@id([userId, projectId])
  @@index([projectId])
}
```

### Multi-tenant Structure
```prisma
// Tenant isolation via brandId on every entity
model Project {
  id        String   @id @default(cuid())
  brandId   String   // tenant key
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt

  brand Brand @relation(fields: [brandId], references: [id])

  @@index([brandId]) // always index tenant key
}
```

## Query Optimization

### N+1 Problem — Always Use `include` or `select`
```typescript
// BAD — causes N+1
const projects = await prisma.project.findMany();
for (const p of projects) {
  const users = await prisma.userProject.findMany({ where: { projectId: p.id } });
}

// GOOD — single query
const projects = await prisma.project.findMany({
  include: {
    users: {
      include: { user: { select: { id: true, name: true, email: true } } }
    }
  }
});
```

### Pagination (always cursor or offset — be consistent per endpoint)
```typescript
// Offset pagination (simpler, use for admin panels)
async findAll(page: number, limit: number) {
  const [data, total] = await prisma.$transaction([
    prisma.project.findMany({
      skip: (page - 1) * limit,
      take: limit,
      orderBy: { createdAt: 'desc' },
    }),
    prisma.project.count(),
  ]);
  return { data, total, page, limit, totalPages: Math.ceil(total / limit) };
}

// Cursor pagination (use for infinite scroll / feeds)
async findAll(cursor?: string, limit = 20) {
  const items = await prisma.project.findMany({
    take: limit + 1,
    ...(cursor && { cursor: { id: cursor }, skip: 1 }),
    orderBy: { createdAt: 'desc' },
  });
  const hasMore = items.length > limit;
  return { data: items.slice(0, limit), nextCursor: hasMore ? items[limit - 1].id : null };
}
```

### Indexing Rules
- Always index foreign keys (Prisma doesn't auto-index them)
- Index any field used in `WHERE` clauses frequently
- Composite index for multi-column filters: `@@index([brandId, status])`
- Never index booleans alone — low cardinality

```prisma
model Project {
  id      String        @id @default(cuid())
  brandId String
  status  ProjectStatus
  
  @@index([brandId])
  @@index([brandId, status]) // composite for filtered queries
}
```

### Transactions
```typescript
// Use $transaction for multi-step writes
async createProjectWithOwner(dto: CreateProjectDto, userId: string) {
  return prisma.$transaction(async (tx) => {
    const project = await tx.project.create({ data: { ...dto } });
    await tx.userProject.create({
      data: { userId, projectId: project.id, role: 'OWNER' }
    });
    return project;
  });
}
```

## Data Flow: DB → Backend → Frontend

```
Prisma Entity → Service (business logic) → DTO (strip sensitive fields) → Controller → Response
```

**Never return raw Prisma objects from controllers.** Always map to a response DTO:

```typescript
// entities/project.entity.ts — what Prisma returns (internal)
// dto/project-response.dto.ts — what the API returns (public)

class ProjectResponseDto {
  id: string;
  name: string;
  brand: { id: string; name: string };
  memberCount: number;
  // NO: passwordHash, deletedAt, internal flags
}
```

## PrismaService Pattern
```typescript
// prisma/prisma.service.ts
@Injectable()
export class PrismaService extends PrismaClient implements OnModuleInit {
  async onModuleInit() {
    await this.$connect();
  }
}

// prisma/prisma.module.ts
@Global()
@Module({
  providers: [PrismaService],
  exports: [PrismaService],
})
export class PrismaModule {}
```
