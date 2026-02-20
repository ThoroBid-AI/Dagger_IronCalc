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
- File: `base/src/functions/mathematical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sinh-function-1e4e8b9f-2b65-43fc-ab8a-0a37f4081fa7

- Source fetch status: failed after 4 attempts

- Summary: Returns the hyperbolic sine of a real number.

- Signatures:

  - `SINH(number)`

- Examples:

  - SINH(0)

  - SINH(1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: `SINH("abc")` -> `#VALUE!`



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093517

- Source fetch status: failed after 4 attempts

- Summary: Returns the hyperbolic sine of a real number.

- Signatures:

  - `SINH(number)`

- Examples:

  - SINH(0)

  - SINH(1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: `SINH("abc")` -> `#VALUE!`



## Sources
- Excel: https://support.microsoft.com/en-us/office/sinh-function-1e4e8b9f-2b65-43fc-ab8a-0a37f4081fa7
- Google Sheets: https://support.google.com/docs/answer/3093517
