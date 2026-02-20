# ROW

## ROW

## Purpose
Returns row number of reference.

## Syntax
- Excel: `ROW([reference])`
- Google Sheets: `ROW([reference])`

## Behavior
Default returns current row when reference omitted.

## Examples (expected outputs)
- `ROW(A5)` -> `5`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_row`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/row-function-3a63b74a-c4d0-4093-b49a-e76eb49a6d8d

- Source fetch status: failed after 4 attempts

- Summary: Returns row number of reference.

- Signatures:

  - `ROW([reference])`

- Examples:

  - ROW(A5)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093316

- Source fetch status: failed after 4 attempts

- Summary: Returns row number of reference.

- Signatures:

  - `ROW([reference])`

- Examples:

  - ROW(A5)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/row-function-3a63b74a-c4d0-4093-b49a-e76eb49a6d8d
- Google Sheets: https://support.google.com/docs/answer/3093316
