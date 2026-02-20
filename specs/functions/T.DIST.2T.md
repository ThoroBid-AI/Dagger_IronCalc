# T.DIST.2T
## T.DIST.2T
## Purpose
Computes T.DIST.2T semantics for spreadsheet formulas.
## Syntax
- Excel: `T.DIST.2T(...)`
- Google Sheets: `T.DIST.2T(...)`
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
- Proposed handler: `fn_t.dist.2t`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/t-dist-2t-function-198e9340-e360-4230-bd21-f52f22ff5c28

- Source fetch status: failed after 4 attempts

- Summary: Computes T.DIST.2T semantics for spreadsheet formulas.

- Signatures:

  - `T.DIST.2T(...)`

- Examples: `=T.DIST.2T(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9368252

- Source fetch status: failed after 4 attempts

- Summary: Computes T.DIST.2T semantics for spreadsheet formulas.

- Signatures:

  - `T.DIST.2T(...)`

- Examples: `=T.DIST.2T(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/t-dist-2t-function-198e9340-e360-4230-bd21-f52f22ff5c28
- Google Sheets: https://support.google.com/docs/answer/9368252
