# AREAS

## AREAS

## Purpose
Returns the number of areas (used in sheet layout context) for a range.

## Syntax
- Excel: `AREAS(reference)`
- Google Sheets: `AREAS(reference)`

## Behavior
- Given a multi-area reference, returns the count of areas.
- Single references return 1.

## Examples (expected outputs)
- `AREAS("A1:C3,A5:B7")` -> `2`

## Error Cases
- Invalid reference format returns an argument error.

## Notes
Not implemented in IronCalc. Targeted for area-aware reference validation and API parity.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Pseudocode
- Validate input arity and types per function spec.
- Reuse existing date/math helpers for conversion and rounding.
- Implement deterministic error branch for invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/areas-function-8392ba32-7a41-43b3-96b0-3695d2ec6152

- Source fetch status: failed after 4 attempts

- Summary: Returns the number of areas (used in sheet layout context) for a range.

- Signatures:

  - `AREAS(reference)`

- Examples:

  - AREAS("A1:C3,A5:B7")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid reference format returns an argument error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=AREAS

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/areas-function-8392ba32-7a41-43b3-96b0-3695d2ec6152
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=AREAS
