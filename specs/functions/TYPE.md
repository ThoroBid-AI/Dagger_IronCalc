# TYPE
## TYPE
## Purpose
Computes TYPE semantics for spreadsheet formulas.
## Syntax
- Excel: `TYPE(...)`
- Google Sheets: `TYPE(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_type`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs`
## Documentation (Microsoft)
- Source URL: https://support.microsoft.com/en-us/office/type-function-45b4e688-4bc3-48b3-a105-ffa892995899

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `TYPE(...)`

- Examples:
  - `=TYPE(1, 2)`,
  - `=TYPE(A1, B1)`,
  - `=TYPE(10, 20, 30)`,
- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)
- Source URL: https://support.google.com/docs/answer/3267375

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `TYPE(...)`

- Examples:
  - `=TYPE(1, 2)`,
  - `=TYPE(A1, B1)`,
  - `=TYPE(10, 20, 30)`,
- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/type-function-45b4e688-4bc3-48b3-a105-ffa892995899
- Google Sheets: https://support.google.com/docs/answer/3267375
