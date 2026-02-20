# ISPMT

## ISPMT

## Purpose
Returns interest paid during a payment period on an interest-only loan.

## Syntax
- Excel: `ISPMT(rate, per, nper, pv, fv, [type])`
- Google Sheets: `ISPMT(rate, per, nper, pv, [fv], [type])`

## Behavior
- Calculates principal-only reduction component per period with deterministic ordering.

## Examples (expected outputs)
- `ISPMT(0.08/12, 1, 12, -1000) -> -6.22`

## Error Cases
- Invalid terms produce domain errors.

## Notes

## Code Location
- Implemented in IronCalc.
- Handler: `fn_ispmt`
- File: `base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/ispmt-function-fa58adb6-9d39-4ce0-8f43-75399cea56cc

- Source fetch status: failed after 4 attempts

- Summary: Returns interest paid during a payment period on an interest-only loan.

- Signatures:

  - `ISPMT(rate, per, nper, pv, fv, [type])`

- Examples:

  - ISPMT(0.08/12, 1, 12, -1000)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid terms produce domain errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9116481

- Source fetch status: failed after 4 attempts

- Summary: Returns interest paid during a payment period on an interest-only loan.

- Signatures:

  - `ISPMT(rate, per, nper, pv, [fv], [type])`

- Examples:

  - ISPMT(0.08/12, 1, 12, -1000)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid terms produce domain errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/ispmt-function-fa58adb6-9d39-4ce0-8f43-75399cea56cc
- Google Sheets: https://support.google.com/docs/answer/9116481
