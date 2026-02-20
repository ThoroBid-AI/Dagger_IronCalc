# WEIBULL.DIST
## WEIBULL.DIST
## Purpose
Returns Weibull distribution values.
## Syntax
- Excel: `WEIBULL.DIST(x, alpha, beta, cumulative)`
- Google Sheets: `WEIBULL.DIST(x, alpha, beta, cumulative)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- WEIBULL.DIST(2,1,1,TRUE) -> 0.8647
## Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.
## Notes
- Deterministic and reproducible behavior required.
## Code Location
- Proposed file: `base/src/functions/statistical/distribution.rs`
- Proposed handler: `fn_weibull.dist`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/weibull-dist-function-4e783c39-9325-49be-bbc9-a83ef82b45db

- Source fetch status: failed after 4 attempts

- Summary: Returns Weibull distribution values.

- Signatures:

  - `WEIBULL.DIST(x, alpha, beta, cumulative)`

- Examples:

  - WEIBULL.DIST(2,1,1,TRUE)

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094116

- Source fetch status: failed after 4 attempts

- Summary: Returns Weibull distribution values.

- Signatures:

  - `WEIBULL.DIST(x, alpha, beta, cumulative)`

- Examples:

  - WEIBULL.DIST(2,1,1,TRUE)

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/weibull-dist-function-4e783c39-9325-49be-bbc9-a83ef82b45db
- Google Sheets: https://support.google.com/docs/answer/3094116
