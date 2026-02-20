# SIN
## SIN
## Purpose
Returns the sine of an angle measured in radians.
## Syntax
- Excel: `SIN(number)`
- Google Sheets: `SIN(number)`
## Behavior
SIN uses radians for input and standard floating-point math, with deterministic IEEE-754 result ordering and formatting.
## Examples (expected outputs)
- `=SIN(0)` -> `0`
- `=SIN(PI()/2)` -> `1`
- `=SIN(PI())` -> `0`
## Error Cases
- `SIN("abc")` -> `#VALUE!`
- Missing/extra arguments -> `#VALUE!`
## Notes
Core trigonometric function for geometry and modeling formulas.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_sin`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`
## Documentation (Microsoft)

- Source URL: https://support.microsoft.com/en-us/office/sin-function-cf0e3432-8b9e-483c-bc55-a76651c95602

- Summary: Returns the sine of an angle measured in radians.

- Signatures:

  - `SIN(number)`

- Examples: `=SIN(0)` -> `0`; `=SIN(PI()/2)` -> `1`

- Notes: Core trigonometric function for geometry and modeling formulas.

- Error behavior: #VALUE! when input cannot be parsed as a number.


## Documentation (Google Sheets)

- Source URL: https://support.google.com/docs/answer/3093447

- Summary: Returns the sine of an angle measured in radians.

- Signatures:

  - `SIN(angle)`

- Examples: `=SIN(0)` -> `0`; `=SIN(PI()/2)` -> `1`

- Notes: Core trigonometric function for geometry and modeling formulas.

- Error behavior: #VALUE! when input cannot be parsed as a number.


## Sources
- Excel: https://support.microsoft.com/en-us/office/sin-function-cf0e3432-8b9e-483c-bc55-a76651c95602
- Google Sheets: https://support.google.com/docs/answer/3093447
