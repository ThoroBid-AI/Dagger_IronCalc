# T.DIST
## T.DIST
## Purpose
Computes T.DIST semantics for spreadsheet formulas.
## Syntax
- Excel: `T.DIST(...)`
- Google Sheets: `T.DIST(...)`
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
- Proposed handler: `fn_t.dist`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/tdist-function-630a7695-4021-4853-9468-4a1f9dcdd192

- Source fetch status: failed after 4 attempts

- Summary: Computes T.DIST semantics for spreadsheet formulas.

- Signatures:

  - `T.DIST(...)`

- Examples: `=T.DIST(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3295914

- Source fetch status: failed after 4 attempts

- Summary: Computes T.DIST semantics for spreadsheet formulas.

- Signatures:

  - `T.DIST(...)`

- Examples: `=T.DIST(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/tdist-function-630a7695-4021-4853-9468-4a1f9dcdd192
- Google Sheets: https://support.google.com/docs/answer/3295914
