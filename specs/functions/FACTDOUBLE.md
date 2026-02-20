# FACTDOUBLE

## FACTDOUBLE

## Purpose
Returns the double factorial of a number.

## Syntax
- Excel: `FACTDOUBLE(number)`
- Google Sheets: `FACTDOUBLE(number)`

## Behavior
- Multiplies numbers with step 2 using 1/2! base cases; deterministic for integer inputs.

## Examples (expected outputs)
- `FACTDOUBLE(7) -> 105`
- `FACTDOUBLE(4) -> 8`

## Error Cases
- Returns domain error for negative inputs and non-numeric values.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_factdouble`
- File: `base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/factdouble-function-e67697ac-d214-48eb-b7b7-cce2589ecac8

- Source fetch status: failed after 4 attempts

- Summary: Implemented in IronCalc.

- Signatures:

  - `FACTDOUBLE(number)`

- Examples:

  - FACTDOUBLE(7)

  - FACTDOUBLE(4)

- Notes: Implemented in IronCalc.

- Error behavior: Returns domain error for negative inputs and non-numeric values.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093414

- Source fetch status: failed after 4 attempts

- Summary: Implemented in IronCalc.

- Signatures:

  - `FACTDOUBLE(number)`

- Examples:

  - FACTDOUBLE(7)

  - FACTDOUBLE(4)

- Notes: Implemented in IronCalc.

- Error behavior: Returns domain error for negative inputs and non-numeric values.



## Sources
- Excel: https://support.microsoft.com/en-us/office/factdouble-function-e67697ac-d214-48eb-b7b7-cce2589ecac8
- Google Sheets: https://support.google.com/docs/answer/3093414
