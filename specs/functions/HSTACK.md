# HSTACK

## HSTACK

## Purpose
Horizontally stacks arrays/values into a single array.

## Syntax
- Excel: `HSTACK(value1, [value2], ...)`
- Google Sheets: `HSTACK(value1, [value2], ...)`

## Behavior
- Concatenates arguments by column, normalizing scalar values into rows as needed.

## Examples (expected outputs)
- `HSTACK({1,2},{3,4}) -> {1,2,3,4}`

## Error Cases
Mismatched array dimensions or invalid arguments return an error.

## Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_hstack`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_hstack`
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/hstack-function-98c4ab76-10fe-4b4f-8d5f-af1c125fe8c2

- Source fetch status: failed after 4 attempts

- Summary: Horizontally stacks arrays/values into a single array.

- Signatures:

  - `HSTACK(value1, [value2], ...)`

- Examples:

  - HSTACK({1,2},{3,4})

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/13190756

- Source fetch status: failed after 4 attempts

- Summary: Horizontally stacks arrays/values into a single array.

- Signatures:

  - `HSTACK(value1, [value2], ...)`

- Examples:

  - HSTACK({1,2},{3,4})

- Notes: Not implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/hstack-function-98c4ab76-10fe-4b4f-8d5f-af1c125fe8c2
- Google Sheets: https://support.google.com/docs/answer/13190756
