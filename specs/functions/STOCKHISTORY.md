# STOCKHISTORY
## STOCKHISTORY
## Purpose
Computes STOCKHISTORY semantics for spreadsheet formulas.
## Syntax
- Excel: `STOCKHISTORY(...)`
- Google Sheets: `STOCKHISTORY(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_stockhistory`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/stockhistory-function-1ac8b5b3-5f62-4d94-8ab8-7504ec7239a8

- Source fetch status: failed after 4 attempts

- Summary: Computes STOCKHISTORY semantics for spreadsheet formulas.

- Signatures:

  - `STOCKHISTORY(...)`

- Examples: `=STOCKHISTORY(1)` -> `0`

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=STOCKHISTORY

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: `=STOCKHISTORY(1)` -> `0`

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/stockhistory-function-1ac8b5b3-5f62-4d94-8ab8-7504ec7239a8
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=STOCKHISTORY
