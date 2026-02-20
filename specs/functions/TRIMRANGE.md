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

- Summary: The TRIMRANGE function excludes all empty rows and/or columns from the outer edges of a range or array.​​​​​​​​​​​​​​

- Signatures:

  - `TRIMRANGE(range,[trim_rows],[trim_cols])`

- Examples:

  - TRIMRANGE(range,[trim_rows],[trim_cols])

  - TRIMRANGE(A1:E10,3,3)

  - TRIMRANGE(A1:E10,2,2)

  - TRIMRANGE(A1:E10,1,1)

- Notes: range Required: The range (or array) to be trimmed | trim_rows: Determines which rows should be trimmed 0 - None 1 - Trims leading blank rows 2 - Trims trailing blank rows 3 - Trims both leading and trailing blank rows (default) | trim_columns: Determines which columns should be trimmed 0 - None 1 - Trims leading blank columns 2 - Trims trailing blank columns 3 - Trims both leading and trailing blank columns (default) | Trim All (.:.): A1.:.E10 | TRIMRANGE(A1:E10,3,3) | Trim leading and trailing blanks

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
