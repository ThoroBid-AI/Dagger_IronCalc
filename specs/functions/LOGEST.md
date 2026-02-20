# LOGEST

## LOGEST

## Purpose
Returns coefficients/statistics for log-linear fit.

## Syntax
- Excel: `LOGEST(known_ys, known_xs, [const], [stats])`
- Google Sheets: `LOGEST(known_ys, known_xs, [const], [stats])`

## Behavior
- Fits exponential trend in linearized form.

## Examples (expected outputs)
- `LOGEST({1,10,100},{1,2,3}) -> {10,0}`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/statistical/regression.rs`
- Proposed handler: `fn_logest`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/logest-function-f27462d8-3657-4030-866b-a272c1d18b4b

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `LOGEST(known_ys, known_xs, [const], [stats])`

- Examples:

  - LOGEST({1,10,100},{1,2,3})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094251

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `LOGEST(known_ys, known_xs, [const], [stats])`

- Examples:

  - LOGEST({1,10,100},{1,2,3})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/logest-function-f27462d8-3657-4030-866b-a272c1d18b4b
- Google Sheets: https://support.google.com/docs/answer/3094251
