# GROUPBY

## GROUPBY

## Purpose
Groups rows by key(s) and applies aggregation.

## Syntax
- Excel: `GROUPBY(array, by_array, col_by_array, function)`
- Google Sheets: `GROUPBY(array, by_array, col_by_array, function)`

## Behavior
- Groups input by stable key ordering and computes requested aggregate per group.

## Examples (expected outputs)
- `GROUPBY({1,2,1}, {"a","b","a"}, , SUM) -> {{"a",2},{"b",2}}`

## Error Cases
- Mismatched sizes or invalid function token returns error.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/statistical/groupby.rs`
- Proposed handler: `fn_groupby`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/groupby-function-5e08ae8c-6800-4b72-b623-c41773611505

- Source fetch status: failed after 4 attempts

- Summary: Groups rows by key(s) and applies aggregation.

- Signatures:

  - `GROUPBY(array, by_array, col_by_array, function)`

- Examples:

  - GROUPBY({1,2,1}, {"a","b","a"}, , SUM)

- Notes: Not implemented in IronCalc.

- Error behavior: Mismatched sizes or invalid function token returns error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=GROUPBY

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/groupby-function-5e08ae8c-6800-4b72-b623-c41773611505
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=GROUPBY
