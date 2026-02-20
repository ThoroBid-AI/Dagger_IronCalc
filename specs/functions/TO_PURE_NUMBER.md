# TO_PURE_NUMBER
## TO_PURE_NUMBER
## Purpose
Computes TO_PURE_NUMBER semantics for spreadsheet formulas.
## Syntax
- Excel: `TO_PURE_NUMBER(...)`
- Google Sheets: `TO_PURE_NUMBER(...)`
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
- Proposed handler: `fn_to_pure_number`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)
- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `TO_PURE_NUMBER(...)`

- Examples: No examples available for this function.

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)
- Source URL: https://support.google.com/docs/answer/3094243

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `TO_PURE_NUMBER(...)`

- Examples:
  - `=TO_PURE_NUMBER(1, 2)`,
  - `=TO_PURE_NUMBER(A1, B1)`,
  - `=TO_PURE_NUMBER(10, 20, 30)`,
- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3094243
