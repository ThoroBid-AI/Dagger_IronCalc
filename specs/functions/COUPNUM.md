# COUPNUM

## COUPNUM

## Purpose
Returns number of coupon payments between dates.

## Syntax
- Excel: `COUPNUM(settlement, maturity, frequency, [basis])`
- Google Sheets: `COUPNUM(settlement, maturity, frequency, [basis])`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `COUPNUM(45234, 45600, 2, 0) -> 4`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/coupnum-function-a90af57b-de53-4969-9c99-dd6139db2522

- Source fetch status: failed after 4 attempts

- Summary: Returns number of coupon payments between dates.

- Signatures:

  - `COUPNUM(settlement, maturity, frequency, [basis])`

- Examples:

  - COUPNUM(45234, 45600, 2, 0)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093208

- Source fetch status: failed after 4 attempts

- Summary: Returns number of coupon payments between dates.

- Signatures:

  - `COUPNUM(settlement, maturity, frequency, [basis])`

- Examples:

  - COUPNUM(45234, 45600, 2, 0)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/coupnum-function-a90af57b-de53-4969-9c99-dd6139db2522
- Google Sheets: https://support.google.com/docs/answer/3093208
