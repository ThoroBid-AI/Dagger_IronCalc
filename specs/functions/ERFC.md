# ERFC

## ERFC

## Purpose
Returns the complementary error function.

## Syntax
- Excel: `ERFC(lower_bound)`
- Google Sheets: `ERFC(lower_bound)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `ERFC(1) -> 0.1573`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Implemented in IronCalc.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_erfc`
- File: `base/src/functions/engineering/bessel.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/erfc-function-736e0318-70ba-4e8b-8d08-461fe68b71b3

- Source fetch status: failed after 4 attempts

- Summary: Returns the complementary error function.

- Signatures:

  - `ERFC(lower_bound)`

- Examples:

  - ERFC(1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093407

- Source fetch status: failed after 4 attempts

- Summary: Returns the complementary error function.

- Signatures:

  - `ERFC(lower_bound)`

- Examples:

  - ERFC(1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/erfc-function-736e0318-70ba-4e8b-8d08-461fe68b71b3
- Google Sheets: https://support.google.com/docs/answer/3093407
