# FLATTEN

## FLATTEN

## Purpose
Flattens nested arrays into a single-column array.

## Syntax
- Excel: `FLATTEN(value1, [value2], ...)`
- Google Sheets: `FLATTEN(value1, [value2], ...)`

## Behavior
- Recursively traverses array-like inputs and concatenates in stable row-major order.

## Examples (expected outputs)
- `FLATTEN({{1,2},{3,4}}) -> {1;2;3;4}`

## Error Cases
- Invalid nested values and circular references are rejected.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_flatten`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Flattens nested arrays into a single-column array.

- Signatures:

  - `FLATTEN(value1, [value2], ...)`

- Examples:

  - FLATTEN({{1,2},{3,4}})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid nested values and circular references are rejected.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/10307761

- Source fetch status: failed after 4 attempts

- Summary: Flattens nested arrays into a single-column array.

- Signatures:

  - `FLATTEN(value1, [value2], ...)`

- Examples:

  - FLATTEN({{1,2},{3,4}})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid nested values and circular references are rejected.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/10307761
