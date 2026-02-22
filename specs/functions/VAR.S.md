# VAR.S
## VAR.S
## Purpose
Returns sample variance.
## Syntax
- Excel: `VAR.S(number1,...)`
- Google Sheets: `VAR.S(number1,...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- VAR.S({1,2,3}) -> 1
## Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.
## Notes
- Deterministic and reproducible behavior required.
## Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_var.s`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/var-s-function-913633de-136b-449d-813e-65a00b2b990b

- Source fetch status: failed after 4 attempts

- Summary: Returns sample variance.

- Signatures:

  - `VAR.S(number1,...)`

- Examples:

  - VAR.S({1,2,3})

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094063

- Source fetch status: failed after 4 attempts

- Summary: Returns sample variance.

- Signatures:

  - `VAR.S(number1,...)`

- Examples:

  - VAR.S({1,2,3})

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/var-s-function-913633de-136b-449d-813e-65a00b2b990b
- Google Sheets: https://support.google.com/docs/answer/3094063
