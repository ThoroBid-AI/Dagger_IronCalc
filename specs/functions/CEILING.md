# CEILING

## CEILING

## Purpose
Rounds a number up to nearest multiple of significance.

## Syntax
- Excel: `CEILING(number, significance)`
- Google Sheets: `CEILING(number, significance)`

## Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

## Examples (expected outputs)
- `CEILING(2.3,1)` -> `3`

## Error Cases
- Returns `#VALUE!` when significance is zero or invalid.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_ceiling`
- File: `base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/ceiling-function-0a5cd7c8-0720-4f0a-bd2c-c943e510899f

- Source fetch status: failed after 4 attempts

- Summary: Rounds a number up to nearest multiple of significance.

- Signatures:

  - `CEILING(number, significance)`

- Examples:

  - CEILING(2.3,1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Returns `#VALUE!` when significance is zero or invalid.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093471

- Source fetch status: failed after 4 attempts

- Summary: Rounds a number up to nearest multiple of significance.

- Signatures:

  - `CEILING(number, significance)`

- Examples:

  - CEILING(2.3,1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Returns `#VALUE!` when significance is zero or invalid.



## Sources
- Excel: https://support.microsoft.com/en-us/office/ceiling-function-0a5cd7c8-0720-4f0a-bd2c-c943e510899f
- Google Sheets: https://support.google.com/docs/answer/3093471
