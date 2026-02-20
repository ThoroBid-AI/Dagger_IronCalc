# COUPPCD

## COUPPCD

## Purpose
Returns previous coupon date before settlement.

## Syntax
- Excel: `COUPPCD(settlement, maturity, frequency, [basis])`
- Google Sheets: `COUPPCD(settlement, maturity, frequency, [basis])`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `COUPPCD(45234, 45600, 2, 0) -> date`

## Error Cases
- Missing schedule yields error.

## Notes
Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/couppcd-function-2eb50473-6ee9-4052-a206-77a9a385d5b3

- Source fetch status: failed after 4 attempts

- Summary: Returns previous coupon date before settlement.

- Signatures:

  - `COUPPCD(settlement, maturity, frequency, [basis])`

- Examples:

  - COUPPCD(45234, 45600, 2, 0)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Missing schedule yields error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093210

- Source fetch status: failed after 4 attempts

- Summary: Returns previous coupon date before settlement.

- Signatures:

  - `COUPPCD(settlement, maturity, frequency, [basis])`

- Examples:

  - COUPPCD(45234, 45600, 2, 0)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Missing schedule yields error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/couppcd-function-2eb50473-6ee9-4052-a206-77a9a385d5b3
- Google Sheets: https://support.google.com/docs/answer/3093210
