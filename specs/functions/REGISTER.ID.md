# REGISTER.ID

## REGISTER.ID

## Purpose
Converts account names to identifier format in financial contexts.

## Syntax
- Excel: `REGISTER.ID(text)`
- Google Sheets: `REGISTER.ID(text)`

## Behavior
Reserved extension-like compatibility function.

## Examples (expected outputs)
- `REGISTER.ID("AAPL")` -> `#N/A`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_register.id`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/register-id-function-f8f0af0f-fd66-4704-a0f2-87b27b175b50

- Source fetch status: failed after 4 attempts

- Summary: Converts account names to identifier format in financial contexts.

- Signatures:

  - `REGISTER.ID(text)`

- Examples:

  - REGISTER.ID("AAPL")

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=REGISTER.ID

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/register-id-function-f8f0af0f-fd66-4704-a0f2-87b27b175b50
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=REGISTER.ID
