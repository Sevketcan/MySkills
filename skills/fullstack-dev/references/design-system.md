# Frontend Design System Rules

Clean, minimal, structured. Every UI decision must pass this filter.

---

## Core Philosophy

The interface must feel: **clean, structured, modern, professional, easy to scan, easy to maintain.**

- Light theme is the primary design target
- Dark mode is project-specific — not required by default
- No decorative UI, no visual noise, no heavy effects
- Whitespace and typography hierarchy are the primary design tools

---

## Tailwind Token Constraints

These are the allowed and forbidden values. Treat this as a hard ruleset.

### Border Radius

```
✅ Allowed        ❌ Never use
rounded-none      rounded-lg
rounded-sm        rounded-xl
                  rounded-2xl
                  rounded-full (except avatars/icon badges)
```

### Shadows

```
✅ Allowed           ❌ Never use
shadow-none          shadow-md
shadow-xs (rarely)   shadow-lg
border (preferred)   shadow-xl
                     drop-shadow
                     glow effects
```

Use `border border-gray-200` to separate surfaces — not shadows.

### Backgrounds

```
✅ Allowed           ❌ Never use
bg-white             bg-gradient-to-*
bg-gray-50           bg-[colorful]
bg-gray-100          overly tinted backgrounds
bg-zinc-50
```

Dark mode equivalents: `dark:bg-gray-900`, `dark:bg-gray-950`

### Borders

```
✅ Allowed              ❌ Never use
border-gray-200         border-2 (unless intentional)
border-gray-300         colored borders for decoration
divide-gray-200
```

### Spacing

Always use Tailwind's 4px base scale. Never use arbitrary values unless unavoidable.

```
✅ p-4, p-6, p-8, gap-4, gap-6
❌ p-[13px], mt-[7px]
```

Pick one spacing rhythm per layout and stick to it. Never mix dense and spacious sections on the same page.

### Typography

```
✅ Use weight + size for hierarchy
   text-sm / text-base / text-lg / text-xl / text-2xl
   font-medium / font-semibold / font-bold
   text-gray-900 (headings)
   text-gray-600 (secondary)
   text-gray-400 (muted/placeholder)

❌ Never use
   More than 4 font sizes on one screen
   Decorative or display fonts unless explicitly scoped
   Color for emphasis (use weight instead)
```

### Colors

```
✅ One primary accent color per project
   Standard status colors: green (success), red (error), yellow (warning), blue (info)
   Neutral grays for surfaces and borders

❌ Multiple strong accent colors in the same view
   Color overload in primary UI
   Overly saturated backgrounds
```

---

## Component Rules

### Buttons

```
Variants: default (filled), outline, ghost, destructive
Radius: rounded-sm only
No shadow on buttons
Hover: subtle background shift — no scale transforms
```

### Inputs & Forms

```
Border: border border-gray-300, focus:border-gray-500 (or primary)
Radius: rounded-sm
No shadow on inputs
Label always above — never floating label
Error state: red border + error text below, no icons cluttering the field
```

### Cards & Containers

```
Separation method: border border-gray-200, NOT shadow
Background: bg-white or bg-gray-50
Padding: p-4 or p-6 — consistent within a view
Radius: rounded-sm or rounded-none
```

### Tables

```
Row separator: divide-y divide-gray-200
Header: text-xs font-semibold text-gray-500 uppercase tracking-wide
No zebra stripe by default (use only if dataset is very dense)
Row hover: bg-gray-50 — subtle
```

### Badges & Status Indicators

```
Radius: rounded-sm (never rounded-full unless it's a dot indicator)
Size: text-xs, px-2 py-0.5
Keep color set to 4: green / red / yellow / gray
```

---

## Interaction & Animation

```
✅ Allowed
   transition-colors duration-150
   opacity change on hover
   Subtle translate-y on dropdown open

❌ Never use
   Bounce, spring, or elastic animations
   Scale transforms on hover (scale-105 etc.)
   Flashy enter/exit animations
   Blur effects as decoration
```

---

## Layout Principles

- Every page must breathe — use `max-w-*` containers, never edge-to-edge content
- Sidebar layouts: fixed width sidebar, fluid content area
- Consistent section padding: `px-6 py-8` or `px-8 py-10` — pick one per layout and don't deviate
- Never compress two separate concerns into one section

---

## Visual Anti-Patterns

These are hard stops. If you're about to do any of these — stop and rethink.

| Anti-Pattern | Why It's Wrong |
|---|---|
| `rounded-xl` / `rounded-2xl` on cards | Looks soft and toy-like, breaks professional feel |
| `shadow-lg` on containers | Creates visual weight without hierarchy purpose |
| Gradient backgrounds | Decorative noise, hard to maintain across states |
| Multiple accent colors in one view | Destroys visual hierarchy |
| Inconsistent padding across same-level components | Looks unpolished, breaks grid rhythm |
| Decorative cards with no clear content hierarchy | "Pretty box" problem — style over substance |
| Mixing flat and heavy-shadow components | Incoherent system feel |
| Uppercase text overuse | Noisy, reduces readability |
| Too many font sizes on one screen | No clear hierarchy, feels crowded |
| Colored section backgrounds for decoration | Use whitespace and borders instead |

---

## Dark Mode (when required)

Only apply when the project explicitly requires it. When you do:

```
Surface scale:
  bg-gray-950  (app background)
  bg-gray-900  (card / panel)
  bg-gray-800  (elevated surface)

Borders:
  border-gray-700 / border-gray-800

Text:
  text-gray-100 (primary)
  text-gray-400 (secondary)
  text-gray-500 (muted)
```

Use `dark:` variants consistently — never conditionally apply dark styles only to some components.

---

## Design Checklist (before shipping any UI)

- [ ] No `rounded-lg` or larger anywhere
- [ ] No `shadow-md` or larger anywhere
- [ ] Surfaces separated by borders, not shadows
- [ ] Max 4 font sizes on the page
- [ ] Spacing is consistent within each section
- [ ] Only one accent color used
- [ ] Hover states are subtle
- [ ] No gradients used decoratively
- [ ] Page content breathes — not compressed
- [ ] New components look like they belong to the same system
