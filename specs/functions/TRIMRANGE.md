# TRIMRANGE
## TRIMRANGE
## Purpose
Computes TRIMRANGE semantics for spreadsheet formulas.
## Syntax
- Excel: `TRIMRANGE(...)`
- Google Sheets: `TRIMRANGE(...)`
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
- Proposed handler: `fn_trimrange`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)
- Source URL: https://support.microsoft.com/en-us/office/trimrange-function-d7812248-3bc5-4c6b-901c-1afa9564f999

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `TRIMRANGE(...)`

- Examples:
  - `=TRIMRANGE(1, 2)`,
  - `=TRIMRANGE(A1, B1)`,
  - `=TRIMRANGE(10, 20, 30)`,
- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)
- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=TRIMRANGE

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/trimrange-function-d7812248-3bc5-4c6b-901c-1afa9564f999
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=TRIMRANGE
