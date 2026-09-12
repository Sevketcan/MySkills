# React Query Usage Criteria

Default is `useState + useEffect`. React Query is only introduced when a specific need justifies it.

---

## Decision Rule

```
Does the data need to be:
  - cached across multiple components?     → React Query
  - refetched on window focus/interval?    → React Query
  - shared between unrelated components?   → React Query
  - fetched once and never updated?        → useState + useEffect
  - local to a single component?           → useState + useEffect
```

If you answer "yes" to any of the first three → use React Query. Otherwise, don't add the dependency.

---

## When to Use React Query

### ✅ Cache shared across components
Multiple components on the same page or across pages need the same data and it should not be re-fetched redundantly.

```typescript
// Without React Query: BrandList and BrandSelector both fetch /brands separately
// With React Query: one cache key, one request, both components stay in sync
const { data: brands } = useQuery({
  queryKey: ['brands'],
  queryFn: () => brandApi.findAll(),
  staleTime: 1000 * 60 * 5, // 5 minutes
});
```

### ✅ Background refetch needed
Data that must stay fresh — dashboards, live counts, notification badges.

```typescript
useQuery({
  queryKey: ['project-stats', projectId],
  queryFn: () => projectApi.getStats(projectId),
  refetchInterval: 30_000,        // poll every 30s
  refetchOnWindowFocus: true,     // refetch when user returns to tab
});
```

### ✅ Dependent / chained queries
Query B depends on the result of Query A.

```typescript
const { data: project } = useQuery({
  queryKey: ['project', projectId],
  queryFn: () => projectApi.findById(projectId),
});

const { data: members } = useQuery({
  queryKey: ['project-members', project?.id],
  queryFn: () => projectApi.getMembers(project!.id),
  enabled: !!project?.id,   // only runs after project is loaded
});
```

### ✅ Mutations with cache invalidation
After a mutation, related query cache should be invalidated automatically.

```typescript
const queryClient = useQueryClient();

const createProject = useMutation({
  mutationFn: (dto: CreateProjectDto) => projectApi.create(dto),
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ['projects'] }); // auto-refetch list
  },
});
```

### ✅ Paginated or infinite lists
When pagination state needs to be tied to cache.

```typescript
useQuery({
  queryKey: ['projects', { page, limit }],
  queryFn: () => projectApi.findAll({ page, limit }),
  placeholderData: keepPreviousData, // no flicker between pages
});
```

---

## When NOT to Use React Query

### ❌ One-time form submissions
```typescript
// Just use useState — no caching needed
const [loading, setLoading] = useState(false);
const handleSubmit = async (dto) => {
  setLoading(true);
  await projectApi.create(dto);
  setLoading(false);
  router.push('/projects');
};
```

### ❌ Data local to a single component that never shared
```typescript
// A modal that loads its own data on open — no other component needs it
const [data, setData] = useState(null);
useEffect(() => { api.get(id).then(setData); }, [id]);
```

### ❌ WebSocket-driven data
Real-time data comes through WebSocket — React Query polling is redundant.
Use socket events to update local state directly. Do not mix React Query with WebSocket streams.

### ❌ Auth state / user session
Use a dedicated auth store (Zustand or Context) — not React Query.

---

## Setup (when adding to a project)

```typescript
// app/providers.tsx
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 1000 * 60,     // 1 minute default stale time
      retry: 1,                  // retry once on failure
      refetchOnWindowFocus: false, // disable by default, enable per-query
    },
  },
});

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <QueryClientProvider client={queryClient}>
      {children}
    </QueryClientProvider>
  );
}
```

---

## Query Key Convention

Keys are arrays. Always structured as `[entity, identifier?, filters?]`:

```typescript
['brands']                                // all brands
['brands', brandId]                       // single brand
['projects', { page, brandId }]          // filtered list
['project-members', projectId]            // sub-resource
```

Never use string-only keys. Never use dynamic objects at the root level.

---

## Summary Table

| Situation | Solution |
|-----------|----------|
| Data shared across 2+ components | React Query |
| Data needs background refresh | React Query |
| Dependent/chained fetches | React Query |
| Mutation + cache invalidation | React Query `useMutation` |
| Paginated list | React Query |
| Single component, one-time fetch | `useState + useEffect` |
| Form submit | `useState` + async handler |
| Real-time / WebSocket data | Socket event → local state |
| Auth / session | Zustand or Context |
