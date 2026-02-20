# DDB

## DDB

## Purpose
Returns double declining balance depreciation for period.

## Syntax
- Excel: `DDB(cost, salvage, life, period, [factor])`
- Google Sheets: `DDB(cost, salvage, life, period, [factor])`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `DDB(10000,1000,5,1) -> 2000`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_ddb`
- File: `base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/ddb-function-519a7a37-8772-4c96-85c0-ed2c209717a5

- Source fetch status: failed after 4 attempts

- Summary: Returns double declining balance depreciation for period.

- Signatures:

  - `DDB(cost, salvage, life, period, [factor])`

- Examples:

  - DDB(10000,1000,5,1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093163

- Source fetch status: failed after 4 attempts

- Summary: Returns double declining balance depreciation for period.

- Signatures:

  - `DDB(cost, salvage, life, period, [factor])`

- Examples:

  - DDB(10000,1000,5,1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/ddb-function-519a7a37-8772-4c96-85c0-ed2c209717a5
- Google Sheets: https://support.google.com/docs/answer/3093163
