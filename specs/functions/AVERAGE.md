# AVERAGE

## AVERAGE

## Purpose
Returns arithmetic mean of numeric values.

## Syntax
- Excel: `AVERAGE(number1, [number2], ...)`
- Google Sheets: `AVERAGE(value1, value2, ...)`

## Behavior
- Averages numeric arguments, ignoring empty cells and non-numeric where defined by host semantics.
- Text numeric coercion may apply when explicit in parser context.

## Examples (expected outputs)
- `AVERAGE(1,2,3)` -> `2`

## Error Cases
- All arguments non-numeric and non-coercible return an error.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_average`
- File: `base/src/functions/statistical/count_and_average.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/average-function-047bac88-d466-426c-a32b-8f33eb960cf6

- Source fetch status: failed after 4 attempts

- Summary: Returns arithmetic mean of numeric values.

- Signatures:

  - `AVERAGE(number1, [number2], ...)`

- Examples:

  - AVERAGE(1,2,3)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: All arguments non-numeric and non-coercible return an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093615

- Source fetch status: failed after 4 attempts

- Summary: Returns arithmetic mean of numeric values.

- Signatures:

  - `AVERAGE(value1, value2, ...)`

- Examples:

  - AVERAGE(1,2,3)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: All arguments non-numeric and non-coercible return an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/average-function-047bac88-d466-426c-a32b-8f33eb960cf6
- Google Sheets: https://support.google.com/docs/answer/3093615
