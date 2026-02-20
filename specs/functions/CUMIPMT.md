# CUMIPMT

## CUMIPMT

## Purpose
Returns cumulative interest paid between periods.

## Syntax
- Excel: `CUMIPMT(rate, nper, pv, start_period, end_period, type)`
- Google Sheets: `CUMIPMT(rate, nper, pv, start_period, end_period, type)`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `CUMIPMT(0.05, 12, 10000, 1, 3, 0) -> -1234`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_cumipmt`
- File: `base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/cumipmt-function-61067bb0-9016-427d-b95b-1a752af0e606

- Source fetch status: failed after 4 attempts

- Summary: Returns cumulative interest paid between periods.

- Signatures:

  - `CUMIPMT(rate, nper, pv, start_period, end_period, type)`

- Examples:

  - CUMIPMT(0.05, 12, 10000, 1, 3, 0)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093211

- Source fetch status: failed after 4 attempts

- Summary: Returns cumulative interest paid between periods.

- Signatures:

  - `CUMIPMT(rate, nper, pv, start_period, end_period, type)`

- Examples:

  - CUMIPMT(0.05, 12, 10000, 1, 3, 0)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/cumipmt-function-61067bb0-9016-427d-b95b-1a752af0e606
- Google Sheets: https://support.google.com/docs/answer/3093211
