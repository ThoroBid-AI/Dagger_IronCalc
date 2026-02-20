# SINH
## SINH
## Purpose
Returns the hyperbolic sine of a real number.
## Syntax
- Excel: `SINH(number)`
- Google Sheets: `SINH(number)`
## Behavior
Input is evaluated as a real number and the output uses stable mathematical hyperbolic sine computation.
## Examples (expected outputs)
- `=SINH(0)` -> `0`
- `=SINH(1)` -> `1.1752011936438`
## Error Cases
- `SINH("abc")` -> `#VALUE!`
- Wrong argument count -> `#VALUE!`
## Notes
Used in engineering and growth modeling contexts.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_sinh`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)

- Source URL: https://support.microsoft.com/en-us/office/sinh-function-1e4e8b9f-2b65-43fc-ab8a-0a37f4081fa7

- Summary: Returns the hyperbolic sine of a real number.

- Signatures:

  - `SINH(number)`

- Examples: `=SINH(0)` -> `0`; `=SINH(1)` -> `1.1752011936438`

- Notes: Used in engineering and growth modeling contexts.

- Error behavior: #VALUE! when non-numeric values are supplied.


## Documentation (Google Sheets)

- Source URL: https://support.google.com/docs/answer/3093517

- Summary: Returns the hyperbolic sine of a real number.

- Signatures:

  - `SINH(value)`

- Examples: `=SINH(0)` -> `0`; `=SINH(1)` -> `1.1752011936438`

- Notes: Used in engineering and growth modeling contexts.

- Error behavior: #VALUE! when non-numeric values are supplied.


## Sources
- Excel: https://support.microsoft.com/en-us/office/sinh-function-1e4e8b9f-2b65-43fc-ab8a-0a37f4081fa7
- Google Sheets: https://support.google.com/docs/answer/3093517
