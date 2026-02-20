# T.TEST
## T.TEST
## Purpose
Computes T.TEST semantics for spreadsheet formulas.
## Syntax
- Excel: `T.TEST(...)`
- Google Sheets: `T.TEST(...)`
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
- Proposed handler: `fn_t.test`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/ttest-function-1696ffc1-4811-40fd-9d13-a0eaad83c7ae

- Source fetch status: failed after 4 attempts

- Summary: Computes T.TEST semantics for spreadsheet formulas.

- Signatures:

  - `T.TEST(...)`

- Examples: `=T.TEST(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/6055837

- Source fetch status: failed after 4 attempts

- Summary: Computes T.TEST semantics for spreadsheet formulas.

- Signatures:

  - `T.TEST(...)`

- Examples: `=T.TEST(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/ttest-function-1696ffc1-4811-40fd-9d13-a0eaad83c7ae
- Google Sheets: https://support.google.com/docs/answer/6055837
