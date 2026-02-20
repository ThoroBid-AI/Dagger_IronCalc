# NORM.S.INV

## NORM.S.INV

## Purpose
Inverse of standard normal CDF.

## Syntax
- Excel: `NORM.S.INV(probability)`
- Google Sheets: `NORM.S.INV(probability)`

## Behavior
Returns z-score for the cumulative standard normal probability.

## Examples (expected outputs)
- `NORM.S.INV(0.5)` -> `0`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/statistical/normal.rs`
- Proposed handler: `fn_norm.s.inv`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/normsinv-function-8d1bce66-8e4d-4f3b-967c-30eed61f019d

- Source fetch status: failed after 4 attempts

- Summary: Inverse of standard normal CDF.

- Signatures:

  - `NORM.S.INV(probability)`

- Examples:

  - NORM.S.INV(0.5)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094091

- Source fetch status: failed after 4 attempts

- Summary: Inverse of standard normal CDF.

- Signatures:

  - `NORM.S.INV(probability)`

- Examples:

  - NORM.S.INV(0.5)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/normsinv-function-8d1bce66-8e4d-4f3b-967c-30eed61f019d
- Google Sheets: https://support.google.com/docs/answer/3094091
