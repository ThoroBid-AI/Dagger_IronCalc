# TREND
## TREND
## Purpose
Computes TREND semantics for spreadsheet formulas.
## Syntax
- Excel: `TREND(...)`
- Google Sheets: `TREND(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_trend`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)
- Source URL: https://support.microsoft.com/en-us/office/trend-function-e2f135f0-8827-4096-9873-9a7cf7b51ef1

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `TREND(...)`

- Examples:
  - `=TREND(1, 2)`,
  - `=TREND(A1, B1)`,
  - `=TREND(10, 20, 30)`,
- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)
- Source URL: https://support.google.com/docs/answer/3094263

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `TREND(...)`

- Examples:
  - `=TREND(1, 2)`,
  - `=TREND(A1, B1)`,
  - `=TREND(10, 20, 30)`,
- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/trend-function-e2f135f0-8827-4096-9873-9a7cf7b51ef1
- Google Sheets: https://support.google.com/docs/answer/3094263
