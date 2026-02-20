# DEVSQ

## DEVSQ

## Purpose
Returns the sum of squares of deviations from the mean.

## Syntax
- Excel: `DEVSQ(number1, [number2], ...)`
- Google Sheets: `DEVSQ(number1, [number2], ...)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `DEVSQ(2,4,4,4,5,5,7,9) -> 32`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Implemented in IronCalc.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_devsq`
- File: `base/src/functions/statistical/devsq.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/devsq-function-8b739616-8376-4df5-8bd0-cfe0a6caf444

- Source fetch status: failed after 4 attempts

- Summary: DEVSQ(2,4,4,4,5,5,7,9)

- Signatures:

  - `DEVSQ(number1, [number2], ...)`

- Examples:

  - DEVSQ(2,4,4,4,5,5,7,9)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093625

- Source fetch status: failed after 4 attempts

- Summary: DEVSQ(2,4,4,4,5,5,7,9)

- Signatures:

  - `DEVSQ(number1, [number2], ...)`

- Examples:

  - DEVSQ(2,4,4,4,5,5,7,9)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/devsq-function-8b739616-8376-4df5-8bd0-cfe0a6caf444
- Google Sheets: https://support.google.com/docs/answer/3093625
