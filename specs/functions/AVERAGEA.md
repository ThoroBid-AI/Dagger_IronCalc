# AVERAGEA

## AVERAGEA

## Purpose
Returns average of arguments, counting TRUE as 1 and FALSE as 0, and including text-numeric per host rules.

## Syntax
- Excel: `AVERAGEA(value1, [value2], ...)`
- Google Sheets: `AVERAGEA(value1, [value2], ...)`

## Behavior
- Includes logical and text values according to host conversion policy.
- Numeric text may be included or excluded based on context.

## Examples (expected outputs)
- `AVERAGEA(1, TRUE, FALSE)` -> `1`

## Error Cases
- If no valid operands remain, returns an error.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_averagea`
- File: `base/src/functions/statistical/count_and_average.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/averagea-function-f5f84098-d453-4f4c-bbba-3d2c66356091

- Source fetch status: failed after 4 attempts

- Summary: Returns average of arguments, counting TRUE as 1 and FALSE as 0, and including text-numeric per host rules.

- Signatures:

  - `AVERAGEA(value1, [value2], ...)`

- Examples:

  - AVERAGEA(1, TRUE, FALSE)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: If no valid operands remain, returns an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093617

- Source fetch status: failed after 4 attempts

- Summary: Returns average of arguments, counting TRUE as 1 and FALSE as 0, and including text-numeric per host rules.

- Signatures:

  - `AVERAGEA(value1, [value2], ...)`

- Examples:

  - AVERAGEA(1, TRUE, FALSE)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: If no valid operands remain, returns an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/averagea-function-f5f84098-d453-4f4c-bbba-3d2c66356091
- Google Sheets: https://support.google.com/docs/answer/3093617
