# COUPNCD

## COUPNCD

## Purpose
Returns next coupon date after settlement date.

## Syntax
- Excel: `COUPNCD(settlement, maturity, frequency, [basis])`
- Google Sheets: `COUPNCD(settlement, maturity, frequency, [basis])`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `COUPNCD(45234, 45600, 2, 0) -> date`

## Error Cases
- Missing schedule yields error.

## Notes
Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/coupncd-function-fd962fef-506b-4d9d-8590-16df5393691f

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `COUPNCD(settlement, maturity, frequency, [basis])`

- Examples:

  - COUPNCD(45234, 45600, 2, 0)

- Notes: See source link when network access is restored.

- Error behavior: Missing schedule yields error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093157

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `COUPNCD(settlement, maturity, frequency, [basis])`

- Examples:

  - COUPNCD(45234, 45600, 2, 0)

- Notes: See source link when network access is restored.

- Error behavior: Missing schedule yields error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/coupncd-function-fd962fef-506b-4d9d-8590-16df5393691f
- Google Sheets: https://support.google.com/docs/answer/3093157
