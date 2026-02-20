# FLOOR.MATH

## FLOOR.MATH

## Purpose
Rounds a number down to nearest multiple with explicit precision mode.

## Syntax
- Excel: `FLOOR.MATH(number,[significance],[mode],[step])`
- Google Sheets: `FLOOR.MATH(number,[significance],[mode],[step])`

## Behavior
- Supports mode and step overrides for negative rounding behavior with deterministic output.

## Examples (expected outputs)
- `FLOOR.MATH(-3.7,1,1) -> -3`

## Error Cases
- Invalid significance and invalid mode values trigger errors.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_floor_math`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/floor-math-function-c302b599-fbdb-4177-ba19-2c2b1249a2f5

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `FLOOR.MATH(number,[significance],[mode],[step])`

- Examples:

  - FLOOR.MATH(-3.7,1,1)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid significance and invalid mode values trigger errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9061444

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `FLOOR.MATH(number,[significance],[mode],[step])`

- Examples:

  - FLOOR.MATH(-3.7,1,1)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid significance and invalid mode values trigger errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/floor-math-function-c302b599-fbdb-4177-ba19-2c2b1249a2f5
- Google Sheets: https://support.google.com/docs/answer/9061444
