# Function Implementation Plan (Rust)

## Scope
- Target oracles: Excel 365 (current) and Google Sheets.
- Locale: en-US.
- Coverage includes all functions in `specs/matrices/function_matrix_normalized.csv`.
- Documentation is authoritative and validated by `scripts/validate_function_docs.py`.
- Current gap list is tracked in `specs/reports/function_unsupported_nimpl.csv`.

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
- External data dependencies or side effects (e.g., network functions).

## Implementation Workflow (Per Function)
- Review the function doc in `specs/functions/<FN>.md` and extract canonical behavior.
- Add unit tests that mirror the doc examples and error cases.
- Add conformance fixtures when Excel/Sheets behavior differs.
- Implement in Rust in the correct module under `base/src/functions/`.
- Update `specs/pipelines/function_fallbacks.csv`:
  - Set `action=implemented` and add `handler` + `file_path`.
  - Remove any fallback tests specific to the old placeholder behavior.
- Regenerate fallbacks/tests with `scripts/generate_batch_fallbacks.py --batch all`.
- Run tests:
  - `cargo test -p ironcalc_base batch_fallback -- --nocapture`
  - Targeted unit tests for the function module.
- Verify validator still passes:
  - `python scripts/validate_function_docs.py`

## Dependencies & Shared Helpers (Build First)
- Type coercion & error rules
- Array/spill mechanics
- Date/time engine
- Statistical distributions
- Lookup helpers
- Formatting utilities (numeric, date, currency)

## Phased Rust Implementation Plan
**Phase 0: Baseline readiness**
- Lock down current behavior with tests for existing implementations.
- Confirm `function_unsupported_nimpl.csv` matches current source state.
- Ensure fallback coverage remains stable while implementations land.

**Phase 1: Deterministic core functions**
- Target: math, text, basic logic, simple stats.
- Goal: fastest parity wins with low edge‑case risk.
- Output: implemented Rust functions + conformance fixtures.

**Phase 2: Array and dynamic‑array functions**
- Target: array transforms, SORT/UNIQUE‑class, TAKE/DROP, MAP/REDUCE.
- Requires: array shape rules, broadcasting, spill handling.
- Output: array‑aware behavior aligned with docs.

**Phase 3: Date/time and lookup**
- Target: DATE/TIME families, lookup variants, reference helpers.
- Requires: consistent date serial conversions and locale rules.

**Phase 4: Statistical & financial**
- Target: distributions, regressions, financial instruments.
- Requires: numeric stability, tolerance‑based tests.

**Phase 5: External/side‑effect functions**
- Target: GOOGLEFINANCE, IMPORTXML, WEBSERVICE, etc.
- Policy: isolate behind feature flags or service boundaries.
- Provide deterministic mocks for tests.

## Batch Execution Strategy
- Use `specs/planning/function_batches.csv` as the execution order.
- For each batch:
  - Convert `unsupported_nimpl` entries to real implementations.
  - Keep fallbacks only as temporary safety nets.
  - Deliver tests + conformance fixtures alongside code.

## Testing Strategy
- Unit tests: validate examples, edge cases, error propagation.
- Conformance tests: Excel/Sheets oracles with deterministic fixtures.
- Regression tests: ensure prior functions remain unchanged.
- Determinism checks: outputs stable across platforms.

## Definition of Done (Per Function)
- Rust implementation in correct module.
- Unit tests added and passing.
- Conformance tests added if behavior differs by provider.
- `function_fallbacks.csv` updated to `implemented`.
- Documentation already validated by `validate_function_docs.py`.

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
- Updated `specs/pipelines/function_fallbacks.csv` per function
