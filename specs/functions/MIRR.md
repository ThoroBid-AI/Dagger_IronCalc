# MIRR

## MIRR

## Purpose
Modified internal rate of return.

## Syntax
- Excel: `MIRR(values, finance_rate, reinvest_rate)`
- Google Sheets: `MIRR(values, finance_rate, reinvest_rate)`

## Behavior
- IRR variant using separate rates.

## Examples (expected outputs)
- `MIRR({-100,100,100},0.1,0.12) -> 0.1097`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_mirr`
- File: `base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/mirr-function-b020f038-7492-4fb4-93c1-35c345b53524

- Source fetch status: failed after 4 attempts

- Summary: Implemented in IronCalc.

- Signatures:

  - `MIRR(values, finance_rate, reinvest_rate)`

- Examples:

  - MIRR({-100,100,100},0.1,0.12)

- Notes: Implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093180

- Source fetch status: failed after 4 attempts

- Summary: Implemented in IronCalc.

- Signatures:

  - `MIRR(values, finance_rate, reinvest_rate)`

- Examples:

  - MIRR({-100,100,100},0.1,0.12)

- Notes: Implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/mirr-function-b020f038-7492-4fb4-93c1-35c345b53524
- Google Sheets: https://support.google.com/docs/answer/3093180
