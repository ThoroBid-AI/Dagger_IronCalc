# ARRAY_CONSTRAIN

## ARRAY_CONSTRAIN

## Purpose
Limits array output to a specified row/column size.

## Syntax
- Excel: no direct function (use dynamic array helpers)
- Google Sheets: `ARRAY_CONSTRAIN(array, rows, columns)`

## Behavior
- Returns top-left `rows x columns` slice of an array.
- Excess values are discarded.

## Examples (expected outputs)
- `ARRAY_CONSTRAIN({1,2;3,4;5,6},2,1)` -> `{1;3}`

## Error Cases
- Non-positive row/column limits result in an error.

## Notes
Not implemented in IronCalc. Planned as array shaping operator.

## Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Handler: `fn_array_constrain` (to be added)

## Pseudocode
- Validate input arity and types per function spec.
- Reuse existing date/math helpers for conversion and rounding.
- Implement deterministic error branch for invalid inputs.

## Documentation (Microsoft)



- Source URL: not applicable (no Excel counterpart in this backlog)
- Source fetch status: not applicable (no Excel counterpart in this backlog)
- Summary: Limits array output to a specified row/column size.

- Signatures: No signatures available for this function.

- Examples:

  - ARRAY_CONSTRAIN({1,2;3,4;5,6},2,1)

- Notes: Source details were not fully captured in this snapshot.

- Error behavior: Non-positive row/column limits result in an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3267036

- Source fetch status: not captured in this snapshot

- Summary: Limits array output to a specified row/column size.

- Signatures:

  - `ARRAY_CONSTRAIN(array, rows, columns)`

- Examples:

  - ARRAY_CONSTRAIN({1,2;3,4;5,6},2,1)

- Notes: Source details were not fully captured in this snapshot.

- Error behavior: Non-positive row/column limits result in an error.



## Sources
- Excel: not applicable (Sheets-only function in this backlog)
- Google Sheets: https://support.google.com/docs/answer/3267036
