# GT

## GT

## Purpose
Returns TRUE when first argument is greater than the second.

## Syntax
- Excel: `GT(value1, value2)`
- Google Sheets: `GT(value1, value2)`

## Behavior
- Strict comparison with coercion semantics consistent with logical operators.

## Examples (expected outputs)
- `GT(5, 3) -> TRUE`

## Error Cases
- Uncomparable types may return error.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/logical.rs`
- Proposed handler: `fn_gt`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Returns TRUE when first argument is greater than the second.

- Signatures:

  - `GT(value1, value2)`

- Examples:

  - GT(5, 3)

- Notes: Not implemented in IronCalc.

- Error behavior: Uncomparable types may return error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3098240

- Source fetch status: failed after 4 attempts

- Summary: Returns TRUE when first argument is greater than the second.

- Signatures:

  - `GT(value1, value2)`

- Examples:

  - GT(5, 3)

- Notes: Not implemented in IronCalc.

- Error behavior: Uncomparable types may return error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3098240
