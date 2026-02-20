# BETA.INVN

## BETA.INVN

## Purpose
Alias-style inverse beta distribution function for legacy naming.

## Syntax
- Excel: `BETA.INVN(probability, alpha, beta, A, B)`
- Google Sheets: `BETA.INV(probability, alpha, beta, A, B)`

## Behavior
- Same intent as `BETA.INV` with older naming variant.

## Examples (expected outputs)
- `BETA.INVN(0.5, 2, 2, 0, 1)` -> same domain as BETA.INV

## Error Cases
- Same validation rules as `BETA.INV`.

## Notes
Not implemented in IronCalc. Planned compatibility alias implementation.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Pseudocode
- Validate input arity and types per function spec.
- Reuse existing date/math helpers for conversion and rounding.
- Implement deterministic error branch for invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/beta-inv-function-e84cb8aa-8df0-4cf6-9892-83a341d252eb

- Source fetch status: failed after 4 attempts

- Summary: Alias-style inverse beta distribution function for legacy naming.

- Signatures:

  - `BETA.INVN(probability, alpha, beta, A, B)`

- Examples:

  - BETA.INVN(0.5, 2, 2, 0, 1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Same validation rules as `BETA.INV`.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=BETA.INVN

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/beta-inv-function-e84cb8aa-8df0-4cf6-9892-83a341d252eb
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=BETA.INVN
