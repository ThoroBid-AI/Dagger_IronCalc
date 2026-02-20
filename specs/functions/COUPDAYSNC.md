# COUPDAYSNC

## COUPDAYSNC

## Purpose
Returns number of days from settlement to next coupon date.

## Syntax
- Excel: `COUPDAYSNC(settlement, maturity, frequency, [basis])`
- Google Sheets: `COUPDAYSNC(settlement, maturity, frequency, [basis])`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `COUPDAYSNC(45234, 45600, 2, 0) -> integer`

## Error Cases
- Invalid schedule results return error.

## Notes
Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/coupdaysnc-function-5ab3f0b2-029f-4a8b-bb65-47d525eea547

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `COUPDAYSNC(settlement, maturity, frequency, [basis])`

- Examples:

  - COUPDAYSNC(45234, 45600, 2, 0)

- Notes: See source link when network access is restored.

- Error behavior: Invalid schedule results return error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093156

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `COUPDAYSNC(settlement, maturity, frequency, [basis])`

- Examples:

  - COUPDAYSNC(45234, 45600, 2, 0)

- Notes: See source link when network access is restored.

- Error behavior: Invalid schedule results return error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/coupdaysnc-function-5ab3f0b2-029f-4a8b-bb65-47d525eea547
- Google Sheets: https://support.google.com/docs/answer/3093156
