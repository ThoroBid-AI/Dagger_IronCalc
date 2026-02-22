# GROWTH

## GROWTH

## Purpose
Fits exponential trend and projects values for x inputs.

## Syntax
- Excel: `GROWTH(known_ys, [known_xs], [new_x], [const])`
- Google Sheets: `GROWTH(known_ys, [known_xs], [new_x], [const])`

## Behavior
- Computes log-space regression and returns predicted y values; deterministic fit path.

## Examples (expected outputs)
- `GROWTH({2,4,8}, {1,2,3}, {4}) -> {16}`

## Error Cases
- Non-positive known_ys or invalid args return error.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/statistical/forecast.rs`
- Proposed handler: `fn_growth`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/growth-function-541a91dc-3d5e-437d-b156-21324e68b80d

- Source fetch status: failed after 4 attempts

- Summary: Fits exponential trend and projects values for x inputs.

- Signatures:

  - `GROWTH(known_ys, [known_xs], [new_x], [const])`

- Examples:

  - GROWTH({2,4,8}, {1,2,3}, {4})

- Notes: Not implemented in IronCalc.

- Error behavior: Non-positive known_ys or invalid args return error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094287

- Source fetch status: failed after 4 attempts

- Summary: Fits exponential trend and projects values for x inputs.

- Signatures:

  - `GROWTH(known_ys, [known_xs], [new_x], [const])`

- Examples:

  - GROWTH({2,4,8}, {1,2,3}, {4})

- Notes: Not implemented in IronCalc.

- Error behavior: Non-positive known_ys or invalid args return error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/growth-function-541a91dc-3d5e-437d-b156-21324e68b80d
- Google Sheets: https://support.google.com/docs/answer/3094287
