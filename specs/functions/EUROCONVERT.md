# EUROCONVERT

## EUROCONVERT

## Purpose
Converts a numeric value between historical currencies.

## Syntax
- Excel: `EUROCONVERT(number, source_currency, target_currency)`
- Google Sheets: `EUROCONVERT(number, source_currency, target_currency)`

## Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

## Examples (expected outputs)
- `EUROCONVERT(100, "EUR", "USD") -> 110`

## Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

## Notes
Function behavior and implementation details to be added as part of batch implementation.

## Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/financial.rs`
- Pseudocode:
  1. `convert units via static conversion table and optional full_conversion flag`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/euroconvert-function-79c8fd67-c665-450c-bb6c-15fc92f8345c

- Source fetch status: failed after 4 attempts

- Summary: Converts a numeric value between historical currencies.

- Signatures:

  - `EUROCONVERT(number, source_currency, target_currency)`

- Examples:

  - EUROCONVERT(100, "EUR", "USD")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count returns an evaluation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=EUROCONVERT

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/euroconvert-function-79c8fd67-c665-450c-bb6c-15fc92f8345c
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=EUROCONVERT
