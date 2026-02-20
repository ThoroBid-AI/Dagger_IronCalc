# COUPDAYBS

## COUPDAYBS

## Purpose
Returns coupon days from settlement to next interest period start.

## Syntax
- Excel: `COUPDAYBS(settlement, maturity, frequency, [basis])`
- Google Sheets: `COUPDAYBS(settlement, maturity, frequency, [basis])`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.
- - Counts coupon interval length in fractional days as documented by host.

## Examples (expected outputs)
- `COUPDAYBS(45234, 45600, 2, 0) -> integer`

## Error Cases
- Settlement after maturity returns error.
- Invalid `frequency` returns error.

## Notes
Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/coupdaybs-function-eb9a8dfb-2fb2-4c61-8e5d-690b320cf872

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `COUPDAYBS(settlement, maturity, frequency, [basis])`

- Examples:

  - COUPDAYBS(45234, 45600, 2, 0)

- Notes: See source link when network access is restored.

- Error behavior: Settlement after maturity returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093154

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `COUPDAYBS(settlement, maturity, frequency, [basis])`

- Examples:

  - COUPDAYBS(45234, 45600, 2, 0)

- Notes: See source link when network access is restored.

- Error behavior: Settlement after maturity returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/coupdaybs-function-eb9a8dfb-2fb2-4c61-8e5d-690b320cf872
- Google Sheets: https://support.google.com/docs/answer/3093154
