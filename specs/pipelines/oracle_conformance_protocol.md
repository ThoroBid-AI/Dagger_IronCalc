# Oracle & Conformance Protocol

## Scope
- Oracles: Excel 365 (current) and Google Sheets.
- Locale: en-US for canonical fixtures.
- Goal: deterministic, reproducible, versioned reference outputs.

## Oracle Capture Rules
- Record **Excel version/build** for each fixture.
- Record **Sheets version/date** for each fixture.
- Capture **inputs**, **formula**, and **expected outputs**.
- Store artifacts in versioned fixtures with stable ordering.

## Deterministic Output Rules
- JSON output must use stable key ordering.
- Arrays must preserve row/column order.
- Numeric representation must define precision, rounding, and formatting rules.

## Tolerance Policy
- Default tolerances (unless specified otherwise):
  - Absolute tolerance: `1e-12`
  - Relative tolerance: `1e-9`
- Use absolute tolerance near zero; use relative tolerance for larger magnitudes.
- Document any function‑specific tolerances (e.g., statistical distributions).

## Fixture Format (Proposed)
- `fixtures/<function>/<case_id>.json`
- Fields:
  - `engine`: `excel` | `sheets`
  - `version`: string (Excel build / Sheets date)
  - `locale`: `en-US`
  - `inputs`: arrays/ranges literal
  - `formula`: string
  - `expected`: value or array
  - `notes`: optional

## Validation Workflow
1. Generate fixtures from oracle.
2. Run conformance tests against IronCalc.
3. Fail on mismatch.
4. If behavior changes, update:
   - fixture
   - spec
   - tests

## Reporting
- Per‑batch conformance report.
- Coverage and mismatch summary per function.
