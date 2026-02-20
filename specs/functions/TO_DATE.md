# TO_DATE
## TO_DATE
## Purpose
Computes TO_DATE semantics for spreadsheet formulas.
## Syntax
- Excel: `TO_DATE(...)`
- Google Sheets: `TO_DATE(...)`
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
- Proposed handler: `fn_to_date`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Computes TO_DATE semantics for spreadsheet formulas.

- Signatures:

  - `TO_DATE(...)`

- Examples: `=TO_DATE(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094239

- Source fetch status: failed after 4 attempts

- Summary: Computes TO_DATE semantics for spreadsheet formulas.

- Signatures:

  - `TO_DATE(...)`

- Examples: `=TO_DATE(1)` -> `0`

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3094239
