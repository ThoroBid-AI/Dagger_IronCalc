# DATE
## DATE
## Purpose
Returns serial date from year month day values.
## Syntax
- Excel: `DATE(year, month, day)`
- Google Sheets: `DATE(year, month, day)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.
## Examples (expected outputs)
- `DATE(2026, 2, 19) -> serial date`
## Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible date arithmetic.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_date`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/date-function-e36c0c8c-4104-49da-ab83-82328b832349

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `DATE(year, month, day)`

- Examples:

  - DATE(2026, 2, 19)

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3092969

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `DATE(year, month, day)`

- Examples:

  - DATE(2026, 2, 19)

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/date-function-e36c0c8c-4104-49da-ab83-82328b832349
- Google Sheets: https://support.google.com/docs/answer/3092969
