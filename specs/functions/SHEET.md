# SHEET
## SHEET
## Purpose
Return worksheet index or name context.
## Syntax
- Excel: `SHEET([reference])`
- Google Sheets: `SHEET([reference])`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `SHEET() -> 1`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_sheet`
- File: `base/src/functions/information.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sheet-function-44718b6f-8b87-47a1-a9d6-b701c06cff24

- Source fetch status: failed after 4 attempts

- Summary: Return worksheet index or name context.

- Signatures:

  - `SHEET([reference])`

- Examples:

  - SHEET()

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=SHEET

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sheet-function-44718b6f-8b87-47a1-a9d6-b701c06cff24
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=SHEET
