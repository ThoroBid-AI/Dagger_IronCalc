# MAP

## MAP

## Purpose
Applies lambda across arrays.

## Syntax
- Excel: `MAP(array1, [array2, ...], lambda)`
- Google Sheets: `MAP(array1, [array2, ...], lambda)`

## Behavior
- Per-element mapping with deterministic argument alignment.

## Examples (expected outputs)
- `MAP({1,2,3}, LAMBDA(x,x*2)) -> {2,4,6}`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_map`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/map-function-48006093-f97c-47c1-bfcc-749263bb1f01

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `MAP(array1, [array2, ...], lambda)`

- Examples:

  - MAP({1,2,3}, LAMBDA(x,x*2)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/12568985

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `MAP(array1, [array2, ...], lambda)`

- Examples:

  - MAP({1,2,3}, LAMBDA(x,x*2)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/map-function-48006093-f97c-47c1-bfcc-749263bb1f01
- Google Sheets: https://support.google.com/docs/answer/12568985
