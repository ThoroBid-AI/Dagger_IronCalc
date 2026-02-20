# EXPAND

## EXPAND

## Purpose
Expands input to a larger array with fill values.

## Syntax
- Excel: `EXPAND(array, rows, [columns], [pad_with])`
- Google Sheets: `EXPAND(array, rows, [columns], [pad_with])`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `EXPAND({1,2}, 2, 3, 0) -> {{1,2,0},{1,2,0}}`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Function behavior and implementation details to be added as part of batch implementation.

## Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Pseudocode:
  1. `expand matrix shape and preserve input dimension semantics`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/expand-function-7433fba5-4ad1-41da-a904-d5d95808bc38

- Source fetch status: failed after 4 attempts

- Summary: EXPAND({1,2}, 2, 3, 0)

- Signatures:

  - `EXPAND(array, rows, [columns], [pad_with])`

- Examples:

  - EXPAND({1,2}, 2, 3, 0)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=EXPAND

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/expand-function-7433fba5-4ad1-41da-a904-d5d95808bc38
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=EXPAND
