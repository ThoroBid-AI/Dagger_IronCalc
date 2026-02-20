# MARGINOFERROR

## MARGINOFERROR

## Purpose
Returns margin of error for estimate.

## Syntax
- Excel: `MARGINOFERROR(range, confidence, [stddev], [population])`
- Google Sheets: `MARGINOFERROR(range, confidence, [stddev], [population])`

## Behavior
- Uses mean and dispersion to compute interval margin.

## Examples (expected outputs)
- `MARGINOFERROR({1,2,3},0.95) -> 0.58`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/statistical/standardize.rs`
- Proposed handler: `fn_marginoferror`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `MARGINOFERROR(range, confidence, [stddev], [population])`

- Examples:

  - MARGINOFERROR({1,2,3},0.95)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/12487850

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `MARGINOFERROR(range, confidence, [stddev], [population])`

- Examples:

  - MARGINOFERROR({1,2,3},0.95)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/12487850
