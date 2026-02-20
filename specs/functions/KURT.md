# KURT

## KURT

## Purpose
Returns the kurtosis of a data set.

## Syntax
- Excel: `KURT(number1, [number2], ...)`
- Google Sheets: `KURT(number1, [number2], ...)`

## Behavior
- Computes fourth central moment standardized by variance^2.

## Examples (expected outputs)
- `KURT(1,2,3,4) -> -1.36`

## Error Cases
- Insufficient samples return error.

## Notes

## Code Location
- Implemented in IronCalc.
- Handler: `fn_kurt`
- File: `base/src/functions/statistical/count_and_average.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/kurt-function-bc3a265c-5da4-4dcb-b7fd-c237789095ab

- Source fetch status: failed after 4 attempts

- Summary: KURT(1,2,3,4)

- Signatures:

  - `KURT(number1, [number2], ...)`

- Examples:

  - KURT(1,2,3,4)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Insufficient samples return error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093634

- Source fetch status: failed after 4 attempts

- Summary: KURT(1,2,3,4)

- Signatures:

  - `KURT(number1, [number2], ...)`

- Examples:

  - KURT(1,2,3,4)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Insufficient samples return error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/kurt-function-bc3a265c-5da4-4dcb-b7fd-c237789095ab
- Google Sheets: https://support.google.com/docs/answer/3093634
