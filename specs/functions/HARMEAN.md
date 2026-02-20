# HARMEAN

## HARMEAN

## Purpose
Returns harmonic mean of values.

## Syntax
- Excel: `HARMEAN(number1, [number2], ...)`
- Google Sheets: `HARMEAN(number1, [number2], ...)`

## Behavior
- Requires positive data and computes reciprocal-mean formula deterministically.

## Examples (expected outputs)
- `HARMEAN(1, 2, 4) -> 1.7142857`

## Error Cases
- Zero or negative values produce domain error.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_harmean`
- File: `base/src/functions/statistical/count_and_average.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/harmean-function-5efd9184-fab5-42f9-b1d3-57883a1d3bc6

- Source fetch status: failed after 4 attempts

- Summary: Returns harmonic mean of values.

- Signatures:

  - `HARMEAN(number1, [number2], ...)`

- Examples:

  - HARMEAN(1, 2, 4)

- Notes: Implemented in IronCalc.

- Error behavior: Zero or negative values produce domain error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094003

- Source fetch status: failed after 4 attempts

- Summary: Returns harmonic mean of values.

- Signatures:

  - `HARMEAN(number1, [number2], ...)`

- Examples:

  - HARMEAN(1, 2, 4)

- Notes: Implemented in IronCalc.

- Error behavior: Zero or negative values produce domain error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/harmean-function-5efd9184-fab5-42f9-b1d3-57883a1d3bc6
- Google Sheets: https://support.google.com/docs/answer/3094003
