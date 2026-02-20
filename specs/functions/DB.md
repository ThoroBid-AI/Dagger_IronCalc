# DB

## DB

## Purpose
Returns fixed declining balance depreciation for period.

## Syntax
- Excel: `DB(cost, salvage, life, period, [month])`
- Google Sheets: `DB(cost, salvage, life, period, [month])`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.
- - Uses declining balance and periodic schedule assumptions.

## Examples (expected outputs)
- `DB(10000,1000,5,1) -> 1860`

## Error Cases
- Invalid `life` or `period` returns error.
- Cost values must be non-negative.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_db`
- File: `base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/db-function-354e7d28-5f93-4ff1-8a52-eb4ee549d9d7

- Source fetch status: failed after 4 attempts

- Summary: Returns fixed declining balance depreciation for period.

- Signatures:

  - `DB(cost, salvage, life, period, [month])`

- Examples:

  - DB(10000,1000,5,1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid `life` or `period` returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093162

- Source fetch status: failed after 4 attempts

- Summary: Returns fixed declining balance depreciation for period.

- Signatures:

  - `DB(cost, salvage, life, period, [month])`

- Examples:

  - DB(10000,1000,5,1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid `life` or `period` returns error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/db-function-354e7d28-5f93-4ff1-8a52-eb4ee549d9d7
- Google Sheets: https://support.google.com/docs/answer/3093162
