# AVERAGEIF

## AVERAGEIF

## Purpose
Returns the average of values that match a condition.

## Syntax
- Excel: `AVERAGEIF(range, criteria, [average_range])`
- Google Sheets: `AVERAGEIF(range, criterion, [average_range])`

## Behavior
- Applies criteria to each item in `range` and averages corresponding items from `average_range` if provided.

## Examples (expected outputs)
- `AVERAGEIF(A1:A4, ">10", B1:B4)` -> average of B where A>10

## Error Cases
- Criteria parse failures and mismatched ranges return an error.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_averageif`
- File: `base/src/functions/statistical/if_ifs.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/averageif-function-faec8e2e-0dec-4308-af69-f5576d8ac642

- Source fetch status: failed after 4 attempts

- Summary: Returns the average of values that match a condition.

- Signatures:

  - `AVERAGEIF(range, criteria, [average_range])`

- Examples:

  - AVERAGEIF(A1:A4, ">10", B1:B4)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Criteria parse failures and mismatched ranges return an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3256529

- Source fetch status: failed after 4 attempts

- Summary: Returns the average of values that match a condition.

- Signatures:

  - `AVERAGEIF(range, criterion, [average_range])`

- Examples:

  - AVERAGEIF(A1:A4, ">10", B1:B4)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Criteria parse failures and mismatched ranges return an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/averageif-function-faec8e2e-0dec-4308-af69-f5576d8ac642
- Google Sheets: https://support.google.com/docs/answer/3256529
