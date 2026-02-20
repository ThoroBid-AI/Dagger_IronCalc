# T.DIST.RT
## T.DIST.RT
## Purpose
Computes T.DIST.RT semantics for spreadsheet formulas.
## Syntax
- Excel: `T.DIST.RT(...)`
- Google Sheets: `T.DIST.RT(...)`
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
- Proposed handler: `fn_t.dist.rt`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/t-dist-rt-function-20a30020-86f9-4b35-af1f-7ef6ae683eda

- Source fetch status: failed after 4 attempts

- Summary: Computes T.DIST.RT semantics for spreadsheet formulas.

- Signatures:

  - `T.DIST.RT(...)`

- Examples: `=T.DIST.RT(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9369017

- Source fetch status: failed after 4 attempts

- Summary: Computes T.DIST.RT semantics for spreadsheet formulas.

- Signatures:

  - `T.DIST.RT(...)`

- Examples: `=T.DIST.RT(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/t-dist-rt-function-20a30020-86f9-4b35-af1f-7ef6ae683eda
- Google Sheets: https://support.google.com/docs/answer/9369017
