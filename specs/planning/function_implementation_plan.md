# Function Implementation Plan

## Scope
- Target oracles: Excel 365 (current) and Google Sheets.
- Locale: en-US.
- Coverage includes all functions in `specs/matrices/function_matrix_normalized.csv`.

## Complexity Buckets
**Easy**
- Deterministic, single‑value outputs.
- Minimal cross‑function dependencies.
- Examples: basic math, text transforms, simple stats.

**Medium**
- Requires helper utilities, coercion rules, or non‑trivial edge cases.
- Examples: lookup variations, date/time with calendars, array‑aware functions.

**Hard**
- Dynamic arrays, iterative calculations, or complex statistical/financial behavior.
- Functions with cross‑engine behavioral differences.

## Dependencies & Shared Helpers (Build First)
1. **Type coercion & error rules**
   - Numeric/text/boolean coercion.
   - Error propagation and precedence.
2. **Array/spill mechanics**
   - Shape validation, broadcasting rules.
3. **Date/time engine**
   - Serial date conversion, leap‑year handling, time zones (if applicable).
4. **Statistical distributions**
   - Shared PDF/CDF helpers and numerical stability.
5. **Lookup helpers**
   - Match modes, binary search, sort order utilities.

## Batch Plan (Estimated Effort)
**Batch 1: Easy functions (40)**
- Focus: simple math/text/logical wrappers.
- Dependencies: type coercion, error rules.
- Estimate: 1–2 days.
- Testing: unit tests + basic conformance fixtures.

**Batch 2: Easy/Medium mix (40)**
- Focus: count/average variants, simple rounding/formatting.
- Dependencies: array handling.
- Estimate: 2–3 days.
- Testing: unit tests + edge‑case fixtures.

**Batch 3: Medium functions (40)**
- Focus: lookup and reference (INDEX/MATCH class), date/time basics.
- Dependencies: lookup helpers, date/time engine.
- Estimate: 3–5 days.
- Testing: conformance fixtures with oracle outputs.

**Batch 4: Medium/Hard (40)**
- Focus: dynamic arrays (FILTER/SORT/UNIQUE class), array‑aware math.
- Dependencies: spill mechanics, array broadcasting.
- Estimate: 4–6 days.
- Testing: array fixtures, spill size validation.

**Batch 5: Hard (40)**
- Focus: advanced statistical distributions, financial functions.
- Dependencies: distribution helpers, numeric stability.
- Estimate: 5–8 days.
- Testing: numeric tolerance tests, oracle fixtures.

**Batch 6+: Remaining hard/engine‑specific**
- Focus: Excel‑only, Sheets‑only, external/web functions.
- Dependencies: engine‑specific behavior, network stubs (if any).
- Estimate: 6–10 days per 40‑function batch.
- Testing: engine‑specific fixtures and compatibility validation.

## Testing Strategy Per Batch
- **Unit tests** for core logic and error rules.
- **Conformance fixtures** with recorded oracle outputs (Excel 365 + Sheets).
- **Regression tests** covering previously implemented functions.
- **Determinism checks** for JSON output and calculation order.

## Milestones
1. Deliver Batches 1–2 with full tests and coverage report.
2. Deliver Batches 3–4 with array/lookup parity.
3. Deliver Batches 5+ with high‑risk statistical/financial functions.

## Deliverables
- `specs/function_implementation_plan.md`
- Batch coverage reports (per batch)
- Test fixtures and conformance suite updates
