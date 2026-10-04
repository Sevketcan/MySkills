---
name: tilemap-ruletile-createempty
description: "Create a blank Unity RuleTile, HexagonalRuleTile or IsometricRuleTile when no sprites are supplied. For existing sprite inputs use tilemap-ruletile-createfromsegment."
---

# Tilemap RuleTile Create Empty

## Workflow

### Step 1: Verify No Sprite Inputs
**WAIT** - Confirm that no Sprites or Spritesheets were specified by the user. This skill is only for empty RuleTiles. If there are Sprites or Spritesheets specified by the user, use the tilemap-ruletile-createfromsegment skill instead.

### Step 2: Determine RuleTile Type
Identify which RuleTile type to create based on user request:
- **RuleTile**: Standard rectangular grid
- **HexagonalRuleTile**: Hexagonal grid layout
- **IsometricRuleTile**: Isometric grid layout

### Step 3: Create Empty TilingRules
For each TilingRule, ensure the Sprite array has one `null` entry.

## Branching Logic (RuleTile Types)

### Path A: RuleTile
- Use template from `resources/ruletile.md`.

### Path B: HexagonalRuleTile
- Use template from `resources/hexagonalruletile.md`.

### Path C: IsometricRuleTile
- Create empty rules with appropriate neighbor positions for isometric layout.

## Important Notes

- **TilingRuleOutput.Neighbor.This**: Use to identify RuleTiles that are the same (matching neighbors).
- **TilingRuleOutput.Neighbor.NotThis**: Do NOT use unless explicitly specified by the user to ignore a Tile at a certain position.
