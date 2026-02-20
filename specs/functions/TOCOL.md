# TOCOL
## TOCOL
## Purpose
Computes TOCOL semantics for spreadsheet formulas.
## Syntax
- Excel: `TOCOL(...)`
- Google Sheets: `TOCOL(...)`
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
- Proposed handler: `fn_tocol`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)
- Source URL: https://support.microsoft.com/en-us/office/tocol-function-22839d9b-0b55-4fc1-b4e6-2761f8f122ed

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `TOCOL(...)`

- Examples:
  - `=TOCOL(1, 2)`,
  - `=TOCOL(A1, B1)`,
  - `=TOCOL(10, 20, 30)`,
- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)
- Source URL: https://support.google.com/docs/answer/13187258

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `TOCOL(...)`

- Examples:
  - `=TOCOL(1, 2)`,
  - `=TOCOL(A1, B1)`,
  - `=TOCOL(10, 20, 30)`,
- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/tocol-function-22839d9b-0b55-4fc1-b4e6-2761f8f122ed
- Google Sheets: https://support.google.com/docs/answer/13187258
