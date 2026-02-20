# LT

## LT

## Purpose
Returns TRUE if value1 < value2.

## Syntax
- Excel: `LT(value1, value2)`
- Google Sheets: `LT(value1, value2)`

## Behavior
- Compares two values with host semantics.

## Examples (expected outputs)
- `LT(2,5) -> TRUE`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/logical.rs`
- Proposed handler: `fn_lt`
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

  - `LT(value1, value2)`

- Examples:

  - LT(2,5)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093596

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `LT(value1, value2)`

- Examples:

  - LT(2,5)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093596
