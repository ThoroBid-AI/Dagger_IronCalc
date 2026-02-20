# MEDIAN

## MEDIAN

## Purpose
Returns median value.

## Syntax
- Excel: `MEDIAN(number1, [number2], ...)`
- Google Sheets: `MEDIAN(number1, [number2], ...)`

## Behavior
- Middle value in sorted list (or average of two).

## Examples (expected outputs)
- `MEDIAN({1,3,3,6,7,8,9}) -> 6`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_median`
- File: `base/src/functions/statistical/count_and_average.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/median-function-d0916313-4753-414c-8537-ce85bdd967d2

- Source fetch status: failed after 4 attempts

- Summary: Implemented in IronCalc.

- Signatures:

  - `MEDIAN(number1, [number2], ...)`

- Examples:

  - MEDIAN({1,3,3,6,7,8,9})

- Notes: Implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094025

- Source fetch status: failed after 4 attempts

- Summary: Implemented in IronCalc.

- Signatures:

  - `MEDIAN(number1, [number2], ...)`

- Examples:

  - MEDIAN({1,3,3,6,7,8,9})

- Notes: Implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/median-function-d0916313-4753-414c-8537-ce85bdd967d2
- Google Sheets: https://support.google.com/docs/answer/3094025
