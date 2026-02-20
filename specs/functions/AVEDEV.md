# AVEDEV

## AVEDEV

## Purpose
Returns the average of the absolute deviations from the mean.

## Syntax
- Excel: `AVEDEV(number1, [number2], ...)`
- Google Sheets: `AVEDEV(number1, [number2], ...)`

## Behavior
- Ignores non-numeric values based on engine rules.
- Computes absolute difference from arithmetic mean for all included values.

## Examples (expected outputs)
- `AVEDEV(1,2,3,4)` -> `1`

## Error Cases
- Fewer than one valid numeric argument yields error.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_avedev`
- File: `base/src/functions/statistical/count_and_average.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/avedev-function-58fe8d65-2a84-4dc7-8052-f3f87b5c6639

- Source fetch status: failed after 4 attempts

- Summary: Returns the average of the absolute deviations from the mean.

- Signatures:

  - `AVEDEV(number1, [number2], ...)`

- Examples:

  - AVEDEV(1,2,3,4)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Fewer than one valid numeric argument yields error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093613

- Source fetch status: failed after 4 attempts

- Summary: Returns the average of the absolute deviations from the mean.

- Signatures:

  - `AVEDEV(number1, [number2], ...)`

- Examples:

  - AVEDEV(1,2,3,4)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Fewer than one valid numeric argument yields error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/avedev-function-58fe8d65-2a84-4dc7-8052-f3f87b5c6639
- Google Sheets: https://support.google.com/docs/answer/3093613
