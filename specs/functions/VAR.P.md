# VAR.P
## VAR.P
## Purpose
Returns population variance.
## Syntax
- Excel: `VAR.P(number1,...)`
- Google Sheets: `VAR.P(number1,...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- VAR.P({1,2,3}) -> 2/3
## Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.
## Notes
- Deterministic and reproducible behavior required.
## Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_var.p`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/varp-function-26a541c4-ecee-464d-a731-bd4c575b1a6b

- Source fetch status: failed after 4 attempts

- Summary: Returns population variance.

- Signatures:

  - `VAR.P(number1,...)`

- Examples: `=VAR.P(1, 2)` -> `0`

  - VAR.P({1,2,3})

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094113

- Source fetch status: failed after 4 attempts

- Summary: Returns population variance.

- Signatures:

  - `VAR.P(number1,...)`

- Examples: `=VAR.P(1, 2)` -> `0`

  - VAR.P({1,2,3})

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/varp-function-26a541c4-ecee-464d-a731-bd4c575b1a6b
- Google Sheets: https://support.google.com/docs/answer/3094113
