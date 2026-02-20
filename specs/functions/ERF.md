# ERF

## ERF

## Purpose
Returns the Gauss error function.

## Syntax
- Excel: `ERF(lower_bound, [upper_bound])`
- Google Sheets: `ERF(lower_bound, [upper_bound])`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `ERF(1) -> 0.8427`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Implemented in IronCalc.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_erf`
- File: `base/src/functions/engineering/bessel.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/erf-function-c53c7e7b-5482-4b6c-883e-56df3c9af349

- Source fetch status: failed after 4 attempts

- Summary: Returns the Gauss error function.

- Signatures:

  - `ERF(lower_bound, [upper_bound])`

- Examples:

  - ERF(1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9116267

- Source fetch status: failed after 4 attempts

- Summary: Returns the Gauss error function.

- Signatures:

  - `ERF(lower_bound, [upper_bound])`

- Examples:

  - ERF(1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/erf-function-c53c7e7b-5482-4b6c-883e-56df3c9af349
- Google Sheets: https://support.google.com/docs/answer/9116267
