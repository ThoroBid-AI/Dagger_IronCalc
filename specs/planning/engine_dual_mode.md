# Dual‑Engine Strategy (Excel + Sheets)

## Goal
Provide Excel‑compatible and Google Sheets‑compatible evaluation paths under a unified engine.

## Engine Selection
- **Phase 1**: workbook‑level engine selection (Excel or Sheets).
- **Phase 2**: optional cell‑level engine override.
- Engine selection must be explicit in the evaluation context.

## Function Resolution
- If a function exists in both engines with identical semantics, use shared implementation.
- If semantics differ, route to engine‑specific implementation:
  - `excel::<function>` and `sheets::<function>` variants.
- Missing functions return engine‑specific errors.

## Formula Translation
- Maintain a translation map for function aliases and syntax differences.
- Translation is deterministic and reversible when possible.
- When translation is ambiguous, surface a diagnostic error with guidance.

## Compatibility Rules
- Use per‑engine coercion rules and error types.
- Numeric formatting and rounding must follow engine rules.
- Locale handling is engine‑specific but defaults to `en-US`.

## Testing
- All functions must have oracle fixtures for **both** engines where applicable.
- Cross‑engine comparisons should be explicit and documented.

## Long‑Term Goals
- Mixed engine cells with explicit engine tags.
- UI selection to choose default engine and override per cell.
