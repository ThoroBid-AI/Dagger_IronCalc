# PROB

## PROB

## Purpose
Returns cumulative probability from a list, given bounds.

## Syntax
- Excel: `PROB(x_range, prob_range, [lower_limit], [upper_limit])`
- Google Sheets: `PROB(x_range, prob_range, [lower_limit], [upper_limit])`

## Behavior
Integrates discrete probabilities within optional limits.

## Examples (expected outputs)
- `PROB({0,1,2},{0.2,0.5,0.3},0,1)` -> `0.7`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_prob`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/prob-function-9ac30561-c81c-4259-8253-34f0a238fc49

- Source fetch status: failed after 4 attempts

- Summary: Returns cumulative probability from a list, given bounds.

- Signatures:

  - `PROB(x_range, prob_range, [lower_limit], [upper_limit])`

- Examples:

  - PROB({0,1,2},{0.2,0.5,0.3},0,1)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094039

- Source fetch status: failed after 4 attempts

- Summary: Returns cumulative probability from a list, given bounds.

- Signatures:

  - `PROB(x_range, prob_range, [lower_limit], [upper_limit])`

- Examples:

  - PROB({0,1,2},{0.2,0.5,0.3},0,1)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/prob-function-9ac30561-c81c-4259-8253-34f0a238fc49
- Google Sheets: https://support.google.com/docs/answer/3094039
