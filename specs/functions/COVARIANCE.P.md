# COVARIANCE.P

## COVARIANCE.P

## Purpose
Returns population covariance.

## Syntax
- Excel: `COVARIANCE.P(array1, array2)`
- Google Sheets: `COVARIANCE.P(array1, array2)`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `COVARIANCE.P({1,2,3},{2,4,6}) -> 1`

## Error Cases
- Non-numeric values are ignored where required or return error based on host mode.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_covariance_p`
- File: `base/src/functions/statistical/covariance.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/covariance-p-function-6f0e1e6d-956d-4e4b-9943-cfef0bf9edfc

- Source fetch status: failed after 4 attempts

- Summary: Returns population covariance.

- Signatures:

  - `COVARIANCE.P(array1, array2)`

- Examples:

  - COVARIANCE.P({1,2,3},{2,4,6})

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-numeric values are ignored where required or return error based on host mode.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093993

- Source fetch status: failed after 4 attempts

- Summary: Returns population covariance.

- Signatures:

  - `COVARIANCE.P(array1, array2)`

- Examples:

  - COVARIANCE.P({1,2,3},{2,4,6})

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-numeric values are ignored where required or return error based on host mode.



## Sources
- Excel: https://support.microsoft.com/en-us/office/covariance-p-function-6f0e1e6d-956d-4e4b-9943-cfef0bf9edfc
- Google Sheets: https://support.google.com/docs/answer/3093993
