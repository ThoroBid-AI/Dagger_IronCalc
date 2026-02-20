# COUPDAYS

## COUPDAYS

## Purpose
Returns number of days from settlement to maturity based on frequency and basis.

## Syntax
- Excel: `COUPDAYS(settlement, maturity, frequency, [basis])`
- Google Sheets: `COUPDAYS(settlement, maturity, frequency, [basis])`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.
- - Counts coupon period duration with basis-dependent day-count rules.

## Examples (expected outputs)
- `COUPDAYS(45234, 45600, 2, 0) -> integer`

## Error Cases
- Settlement after maturity returns error.
- Invalid `basis` returns error.

## Notes
Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/coupdays-function-cc64380b-315b-4e7b-950c-b30b0a76f671

- Source fetch status: failed after 4 attempts

- Summary: Returns number of days from settlement to maturity based on frequency and basis.

- Signatures:

  - `COUPDAYS(settlement, maturity, frequency, [basis])`

- Examples:

  - COUPDAYS(45234, 45600, 2, 0)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Settlement after maturity returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093204

- Source fetch status: failed after 4 attempts

- Summary: Returns number of days from settlement to maturity based on frequency and basis.

- Signatures:

  - `COUPDAYS(settlement, maturity, frequency, [basis])`

- Examples:

  - COUPDAYS(45234, 45600, 2, 0)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Settlement after maturity returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/coupdays-function-cc64380b-315b-4e7b-950c-b30b0a76f671
- Google Sheets: https://support.google.com/docs/answer/3093204
