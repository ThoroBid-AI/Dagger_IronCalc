# TTEST
## TTEST
## Purpose
Computes TTEST semantics for spreadsheet formulas.
## Syntax
- Excel: `TTEST(...)`
- Google Sheets: `TTEST(...)`
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
- Handler: `fn_t_test`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/t_dist.rs`
## Documentation (Microsoft)
- Source URL: https://support.microsoft.com/en-us/office/ttest-function-1696ffc1-4811-40fd-9d13-a0eaad83c7ae

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `TTEST(...)`

- Examples:
  - `=TTEST(1, 2)`,
  - `=TTEST(A1, B1)`,
  - `=TTEST(10, 20, 30)`,
- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)
- Source URL: https://support.google.com/docs/answer/6055837

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable.

- Signatures:

  - `TTEST(...)`

- Examples:
  - `=TTEST(1, 2)`,
  - `=TTEST(A1, B1)`,
  - `=TTEST(10, 20, 30)`,
- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/ttest-function-1696ffc1-4811-40fd-9d13-a0eaad83c7ae
- Google Sheets: https://support.google.com/docs/answer/6055837
