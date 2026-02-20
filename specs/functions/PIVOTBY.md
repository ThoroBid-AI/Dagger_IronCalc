# PIVOTBY

## PIVOTBY

## Purpose
Applies reduction to data and returns reshaped output.

## Syntax
- Excel: `PIVOTBY(data, pivot_column, pivot_value, data_column, function)`
- Google Sheets: `PIVOTBY(data, pivot_column, pivot_value, data_column, function)`

## Behavior
Groups and reduces input data into a pivot table structure.

## Examples (expected outputs)
- `PIVOTBY(A1:C4,"Type","Value",SUM)` -> `table`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/table.rs`
- Proposed handler: `fn_pivotby`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/pivotby-function-de86516a-90ad-4ced-8522-3a25fac389cf

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `PIVOTBY(data, pivot_column, pivot_value, data_column, function)`

- Examples:

  - PIVOTBY(A1:C4,"Type","Value",SUM)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=PIVOTBY

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/pivotby-function-de86516a-90ad-4ced-8522-3a25fac389cf
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=PIVOTBY
