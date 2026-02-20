# INDEX
## INDEX
## Purpose
Returns value at row/column in array.
## Syntax
- Excel: `INDEX(array, row_num, [column_num])`
- Google Sheets: `INDEX(array, row_num, [column_num])`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.
## Examples (expected outputs)
- `INDEX({1,2;3,4},2,1) -> 3`
## Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible date arithmetic.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_index`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/index-function-a5dcf0dd-996d-40a4-a822-b56b061328bd

- Source fetch status: failed after 4 attempts

- Summary: Returns value at row/column in array.

- Signatures:

  - `INDEX(array, row_num, [column_num])`

- Examples:

  - INDEX({1,2;3,4},2,1)

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3098242

- Source fetch status: failed after 4 attempts

- Summary: Returns value at row/column in array.

- Signatures:

  - `INDEX(array, row_num, [column_num])`

- Examples:

  - INDEX({1,2;3,4},2,1)

- Notes: Deterministic and reproducible date arithmetic.

- Error behavior: Invalid dates or impossible ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/index-function-a5dcf0dd-996d-40a4-a822-b56b061328bd
- Google Sheets: https://support.google.com/docs/answer/3098242
