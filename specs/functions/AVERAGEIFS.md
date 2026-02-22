# AVERAGEIFS

## AVERAGEIFS

## Purpose
Returns the average of values that meet multiple criteria.

## Syntax
- Excel: `AVERAGEIFS(average_range, criteria_range1, criteria1, ...)`
- Google Sheets: `AVERAGEIFS(average_range, criteria_range1, criterion1, ...)`

## Behavior
- Supports multiple criteria pairs.
- All criteria conditions are combined with AND.

## Examples (expected outputs)
- `AVERAGEIFS(C1:C4,A1:A4,">10",B1:B4,"A*")`

## Error Cases
- Range length mismatch or malformed criteria returns an error.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_averageifs`
- File: `base/src/functions/statistical/if_ifs.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/averageifs-function-48910c45-1fc0-4389-a028-f7c5c3001690

- Source fetch status: failed after 4 attempts

- Summary: Returns the average of values that meet multiple criteria.

- Signatures:

  - `AVERAGEIFS(average_range, criteria_range1, criteria1, ...)`

- Examples:

  - AVERAGEIFS(C1:C4,A1:A4,">10",B1:B4,"A*")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Range length mismatch or malformed criteria returns an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3256534

- Source fetch status: failed after 4 attempts

- Summary: Returns the average of values that meet multiple criteria.

- Signatures:

  - `AVERAGEIFS(average_range, criteria_range1, criterion1, ...)`

- Examples:

  - AVERAGEIFS(C1:C4,A1:A4,">10",B1:B4,"A*")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Range length mismatch or malformed criteria returns an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/averageifs-function-48910c45-1fc0-4389-a028-f7c5c3001690
- Google Sheets: https://support.google.com/docs/answer/3256534
