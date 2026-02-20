# FACT

## FACT

## Purpose
Returns the factorial of an integer argument.

## Syntax
- Excel: `FACT(number)`
- Google Sheets: `FACT(number)`

## Behavior
- Returns 1 for 0, returns #NUM! for negative values, and rounds down non-integers to integer input domain.

## Examples (expected outputs)
- `FACT(5) -> 120`
- `FACT(0) -> 1`

## Error Cases
- Errors on negative or fractional inputs outside allowed domain per host behavior.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_fact`
- File: `base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/fact-function-ca8588c2-15f2-41c0-8e8c-c11bd471a4f3

- Source fetch status: failed after 4 attempts

- Summary: Implemented in IronCalc.

- Signatures:

  - `FACT(number)`

- Examples:

  - FACT(5)

  - FACT(0)

- Notes: Implemented in IronCalc.

- Error behavior: Errors on negative or fractional inputs outside allowed domain per host behavior.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093412

- Source fetch status: failed after 4 attempts

- Summary: Implemented in IronCalc.

- Signatures:

  - `FACT(number)`

- Examples:

  - FACT(5)

  - FACT(0)

- Notes: Implemented in IronCalc.

- Error behavior: Errors on negative or fractional inputs outside allowed domain per host behavior.



## Sources
- Excel: https://support.microsoft.com/en-us/office/fact-function-ca8588c2-15f2-41c0-8e8c-c11bd471a4f3
- Google Sheets: https://support.google.com/docs/answer/3093412
