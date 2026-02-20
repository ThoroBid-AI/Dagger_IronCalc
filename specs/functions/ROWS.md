# ROWS

## ROWS

## Purpose
Returns count of rows in range.

## Syntax
- Excel: `ROWS(array)`
- Google Sheets: `ROWS(array)`

## Behavior
Counts rows in array or range.

## Examples (expected outputs)
- `ROWS({{1,2},{3,4}})` -> `2`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_rows`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/rows-function-b592593e-3fc2-47f2-bec1-bda493811597

- Source fetch status: failed after 4 attempts

- Summary: Returns count of rows in range.

- Signatures:

  - `ROWS(array)`

- Examples:

  - ROWS({{1,2},{3,4}})

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093382

- Source fetch status: failed after 4 attempts

- Summary: Returns count of rows in range.

- Signatures:

  - `ROWS(array)`

- Examples:

  - ROWS({{1,2},{3,4}})

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/rows-function-b592593e-3fc2-47f2-bec1-bda493811597
- Google Sheets: https://support.google.com/docs/answer/3093382
