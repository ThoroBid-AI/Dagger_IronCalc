# INTERCEPT

## INTERCEPT

## Purpose
Returns the y-axis intercept from linear regression of known points.

## Syntax
- Excel: `INTERCEPT(known_y’s, known_x’s)`
- Google Sheets: `INTERCEPT(known_ys, known_xs)`

## Behavior
- Computes slope and intercept from regression formula deterministically.

## Examples (expected outputs)
- `INTERCEPT({1,2,3},{1,2,3}) -> 0`

## Error Cases
- Mismatched arrays or insufficient data returns error.

## Notes

## Code Location
- Implemented in IronCalc.
- Handler: `fn_intercept`
- File: `base/src/functions/statistical/correl.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/intercept-function-2a9b74e2-9d47-4772-b663-3bca70bf63ef

- Source fetch status: failed after 4 attempts

- Summary: Returns the y-axis intercept from linear regression of known points.

- Signatures:

  - `INTERCEPT(known_y’s, known_x’s)`

- Examples:

  - INTERCEPT({1,2,3},{1,2,3})

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Mismatched arrays or insufficient data returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093632

- Source fetch status: failed after 4 attempts

- Summary: Returns the y-axis intercept from linear regression of known points.

- Signatures:

  - `INTERCEPT(known_ys, known_xs)`

- Examples:

  - INTERCEPT({1,2,3},{1,2,3})

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Mismatched arrays or insufficient data returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/intercept-function-2a9b74e2-9d47-4772-b663-3bca70bf63ef
- Google Sheets: https://support.google.com/docs/answer/3093632
