# LINEST

## LINEST

## Purpose
Returns regression statistics for x/y data.

## Syntax
- Excel: `LINEST(known_ys, known_xs, [const], [stats])`
- Google Sheets: `LINEST(known_ys, known_xs, [const], [stats])`

## Behavior
- Linear regression fit with optional statistics output.

## Examples (expected outputs)
- `LINEST({1,2,3},{1,2,3}) -> {1,0}`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/statistical/regression.rs`
- Proposed handler: `fn_linest`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/linest-function-84d7d0d9-6e50-4101-977a-fa7abf772b6d

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `LINEST(known_ys, known_xs, [const], [stats])`

- Examples:

  - LINEST({1,2,3},{1,2,3})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094249

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `LINEST(known_ys, known_xs, [const], [stats])`

- Examples:

  - LINEST({1,2,3},{1,2,3})

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/linest-function-84d7d0d9-6e50-4101-977a-fa7abf772b6d
- Google Sheets: https://support.google.com/docs/answer/3094249
