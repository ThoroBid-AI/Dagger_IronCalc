# BETA.INV

## BETA.INV

## Purpose
Returns the inverse of `BETA.DIST` for a given probability.

## Syntax
- Excel: `BETA.INV(probability, alpha, beta, [A], [B])`
- Google Sheets: `BETA.INV(probability, alpha, beta, [A], [B])`

## Behavior
- Inverts cumulative beta distribution.
- Works only on valid cumulative probability in [0,1].

## Examples (expected outputs)
- `BETA.INV(0.5, 2, 2, 0, 1)` -> median-like quantile

## Error Cases
- Probability outside [0,1] or invalid parameters returns an error.

## Notes
Not implemented in IronCalc. Planned distribution inversion support.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Pseudocode
- Validate input arity and types per function spec.
- Reuse existing date/math helpers for conversion and rounding.
- Implement deterministic error branch for invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/betainv-function-8b914ade-b902-43c1-ac9c-c05c54f10d6c

- Source fetch status: failed after 4 attempts

- Summary: Returns the inverse of `BETA.DIST` for a given probability.

- Signatures:

  - `BETA.INV(probability, alpha, beta, [A], [B])`

- Examples:

  - BETA.INV(0.5, 2, 2, 0, 1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Probability outside [0,1] or invalid parameters returns an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9061377

- Source fetch status: failed after 4 attempts

- Summary: Returns the inverse of `BETA.DIST` for a given probability.

- Signatures:

  - `BETA.INV(probability, alpha, beta, [A], [B])`

- Examples:

  - BETA.INV(0.5, 2, 2, 0, 1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Probability outside [0,1] or invalid parameters returns an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/betainv-function-8b914ade-b902-43c1-ac9c-c05c54f10d6c
- Google Sheets: https://support.google.com/docs/answer/9061377
