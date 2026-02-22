# AVERAGE.WEIGHTED

## AVERAGE.WEIGHTED

## Purpose
Returns weighted average of values with corresponding weights.

## Syntax
- Excel: `AVERAGE.WEIGHTED(avg_range, weight_range, [additional_pairs...], [ignore_text])`
- Google Sheets: not native; emulate with `SUMPRODUCT/ SUM` patterns

## Behavior
- Each value is multiplied by weight and divided by sum(weights).
- Optional extra ranges and include-logic can alter matching behavior.

## Examples (expected outputs)
- `AVERAGE.WEIGHTED({10,20,30},{1,2,3})` -> `23.3333333333`

## Error Cases
- Zero or negative total weight in supported modes may return divide-by-zero style error.

## Notes
Not implemented in IronCalc. Planned as dedicated weighted average function.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Pseudocode
- Validate input arity and types per function spec.
- Reuse existing date/math helpers for conversion and rounding.
- Implement deterministic error branch for invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Returns weighted average of values with corresponding weights.

- Signatures:

  - `AVERAGE.WEIGHTED(avg_range, weight_range, [additional_pairs...], [ignore_text])`

- Examples:

  - AVERAGE.WEIGHTED({10,20,30},{1,2,3})

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Zero or negative total weight in supported modes may return divide-by-zero style error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9084098

- Source fetch status: failed after 4 attempts

- Summary: Returns weighted average of values with corresponding weights.

- Signatures: No signatures available for this function.

- Examples:

  - AVERAGE.WEIGHTED({10,20,30},{1,2,3})

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Zero or negative total weight in supported modes may return divide-by-zero style error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/9084098
