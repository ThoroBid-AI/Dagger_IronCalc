# SUBTOTAL
## SUBTOTAL
## Purpose
Computes SUBTOTAL semantics for spreadsheet formulas.
## Syntax
- Excel: `SUBTOTAL(...)`
- Google Sheets: `SUBTOTAL(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_subtotal`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/subtotal.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/subtotal-function-7b027003-f060-4ade-9040-e478765b9939

- Source fetch status: failed after 4 attempts

- Summary: Computes SUBTOTAL semantics for spreadsheet formulas.

- Signatures:

  - `SUBTOTAL(...)`

- Examples: `=SUBTOTAL(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093649

- Source fetch status: failed after 4 attempts

- Summary: Computes SUBTOTAL semantics for spreadsheet formulas.

- Signatures:

  - `SUBTOTAL(...)`

- Examples: `=SUBTOTAL(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/subtotal-function-7b027003-f060-4ade-9040-e478765b9939
- Google Sheets: https://support.google.com/docs/answer/3093649
