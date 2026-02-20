# LTE

## LTE

## Purpose
Returns TRUE if value1 <= value2.

## Syntax
- Excel: `LTE(value1, value2)`
- Google Sheets: `LTE(value1, value2)`

## Behavior
- Less-or-equal comparison.

## Examples (expected outputs)
- `LTE(2,2) -> TRUE`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/logical.rs`
- Proposed handler: `fn_lte`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Returns TRUE if value1 <= value2.

- Signatures:

  - `LTE(value1, value2)`

- Examples:

  - LTE(2,2)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093976

- Source fetch status: failed after 4 attempts

- Summary: Returns TRUE if value1 <= value2.

- Signatures:

  - `LTE(value1, value2)`

- Examples:

  - LTE(2,2)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093976
