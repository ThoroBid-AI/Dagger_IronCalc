# ISBETWEEN

## ISBETWEEN

## Purpose
Returns TRUE if value is between two bounds.

## Syntax
- Excel: `ISBETWEEN(value, lower, upper)`
- Google Sheets: `ISBETWEEN(value, lower, upper)`

## Behavior
- Compares with inclusive or deterministic comparison rules against numeric/text inputs.

## Examples (expected outputs)
- `ISBETWEEN(5, 1, 10) -> TRUE`

## Error Cases
- Invalid argument count returns arity error.

## Notes

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_isbetween`
- Proposed file: `base/src/functions/information.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Returns TRUE if value is between two bounds.

- Signatures:

  - `ISBETWEEN(value, lower, upper)`

- Examples:

  - ISBETWEEN(5, 1, 10)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns arity error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/10538337

- Source fetch status: failed after 4 attempts

- Summary: Returns TRUE if value is between two bounds.

- Signatures:

  - `ISBETWEEN(value, lower, upper)`

- Examples:

  - ISBETWEEN(5, 1, 10)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns arity error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/10538337
