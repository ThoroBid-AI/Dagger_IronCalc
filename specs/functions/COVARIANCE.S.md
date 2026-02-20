# COVARIANCE.S

## COVARIANCE.S

## Purpose
Returns sample covariance.

## Syntax
- Excel: `COVARIANCE.S(array1, array2)`
- Google Sheets: `COVARIANCE.S(array1, array2)`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `COVARIANCE.S({1,2,3},{2,4,6}) -> 1`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_covariance_s`
- File: `base/src/functions/statistical/covariance.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/covariance-s-function-0a539b74-7371-42aa-a18f-1f5320314977

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `COVARIANCE.S(array1, array2)`

- Examples:

  - COVARIANCE.S({1,2,3},{2,4,6})

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9365675

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `COVARIANCE.S(array1, array2)`

- Examples:

  - COVARIANCE.S({1,2,3},{2,4,6})

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/covariance-s-function-0a539b74-7371-42aa-a18f-1f5320314977
- Google Sheets: https://support.google.com/docs/answer/9365675
