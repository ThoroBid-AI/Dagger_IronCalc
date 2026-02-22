# GTE

## GTE

## Purpose
Returns TRUE when first argument is greater than or equal to second.

## Syntax
- Excel: `GTE(value1, value2)`
- Google Sheets: `GTE(value1, value2)`

## Behavior
- Deterministic comparison with type-coercion rules equivalent to comparison operators.

## Examples (expected outputs)
- `GTE(5, 5) -> TRUE`

## Error Cases
- Uncomparable types may return error.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/logical.rs`
- Proposed handler: `fn_gte`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Returns TRUE when first argument is greater than or equal to second.

- Signatures:

  - `GTE(value1, value2)`

- Examples:

  - GTE(5, 5)

- Notes: Not implemented in IronCalc.

- Error behavior: Uncomparable types may return error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093975

- Source fetch status: failed after 4 attempts

- Summary: Returns TRUE when first argument is greater than or equal to second.

- Signatures:

  - `GTE(value1, value2)`

- Examples:

  - GTE(5, 5)

- Notes: Not implemented in IronCalc.

- Error behavior: Uncomparable types may return error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093975
