# FLOOR.PRECISE

## FLOOR.PRECISE

## Purpose
Rounds number down to nearest multiple with precise semantics.

## Syntax
- Excel: `FLOOR.PRECISE(number, [significance])`
- Google Sheets: `FLOOR.PRECISE(number, [significance])`

## Behavior
- Precision variant of FLOOR without mode effects.

## Examples (expected outputs)
- `FLOOR.PRECISE(12.7, 1) -> 12`

## Error Cases
- Domain errors for zero significance or non-numeric inputs.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_floor_precise`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/floor-precise-function-f769b468-1452-4617-8dc3-02f842a0702e

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `FLOOR.PRECISE(number, [significance])`

- Examples:

  - FLOOR.PRECISE(12.7, 1)

- Notes: Not implemented in IronCalc.

- Error behavior: Domain errors for zero significance or non-numeric inputs.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9116270

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `FLOOR.PRECISE(number, [significance])`

- Examples:

  - FLOOR.PRECISE(12.7, 1)

- Notes: Not implemented in IronCalc.

- Error behavior: Domain errors for zero significance or non-numeric inputs.



## Sources
- Excel: https://support.microsoft.com/en-us/office/floor-precise-function-f769b468-1452-4617-8dc3-02f842a0702e
- Google Sheets: https://support.google.com/docs/answer/9116270
