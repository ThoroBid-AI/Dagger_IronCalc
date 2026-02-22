# DROP

## DROP

## Purpose
Returns a range/array with rows and/or columns removed.

## Syntax
- Excel: `DROP(array, rows, [columns])`
- Google Sheets: `DROP(array, rows, [columns])`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `DROP({1,2,3,4}, 1, 1) -> {2,3}`

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
  1. `slice array after removing requested rows/cols and fill truncation rules`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/drop-function-1cb4e151-9e17-4838-abe5-9ba48d8c6a34

- Source fetch status: failed after 4 attempts

- Summary: Returns a range/array with rows and/or columns removed.

- Signatures:

  - `DROP(array, rows, [columns])`

- Examples:

  - DROP({1,2,3,4}, 1, 1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=DROP

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/drop-function-1cb4e151-9e17-4838-abe5-9ba48d8c6a34
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=DROP
