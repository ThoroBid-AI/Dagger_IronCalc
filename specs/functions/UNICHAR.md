# UNICHAR
## UNICHAR
## Purpose
Computes UNICHAR semantics for spreadsheet formulas.
## Syntax
- Excel: `UNICHAR(...)`
- Google Sheets: `UNICHAR(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_unichar`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)
- Source URL: https://support.microsoft.com/en-us/office/unichar-function-ffeb64f5-f131-44c6-b332-5cd72f0659b8

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `UNICHAR(...)`

- Examples:
  - `=UNICHAR(1, 2)`,
  - `=UNICHAR(A1, B1)`,
  - `=UNICHAR(10, 20, 30)`,
- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)
- Source URL: https://support.google.com/docs/answer/9369024

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `UNICHAR(...)`

- Examples:
  - `=UNICHAR(1, 2)`,
  - `=UNICHAR(A1, B1)`,
  - `=UNICHAR(10, 20, 30)`,
- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/unichar-function-ffeb64f5-f131-44c6-b332-5cd72f0659b8
- Google Sheets: https://support.google.com/docs/answer/9369024
