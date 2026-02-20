# NORM.INV

## NORM.INV

## Purpose
Returns inverse of normal CDF.

## Syntax
- Excel: `NORM.INV(probability, mean, standard_dev)`
- Google Sheets: `NORM.INV(probability, mean, standard_dev)`

## Behavior
Returns x such that `NORM.DIST(x, mean, stdev, TRUE)=probability`.

## Examples (expected outputs)
- `NORM.INV(0.5, 0, 1)` -> `0`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/statistical/normal.rs`
- Proposed handler: `fn_norm.inv`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/norm-inv-function-54b30935-fee7-493c-bedb-2278a9db7e13

- Source fetch status: failed after 4 attempts

- Summary: Returns inverse of normal CDF.

- Signatures:

  - `NORM.INV(probability, mean, standard_dev)`

- Examples:

  - NORM.INV(0.5, 0, 1)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094022

- Source fetch status: failed after 4 attempts

- Summary: Returns inverse of normal CDF.

- Signatures:

  - `NORM.INV(probability, mean, standard_dev)`

- Examples:

  - NORM.INV(0.5, 0, 1)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/norm-inv-function-54b30935-fee7-493c-bedb-2278a9db7e13
- Google Sheets: https://support.google.com/docs/answer/3094022
