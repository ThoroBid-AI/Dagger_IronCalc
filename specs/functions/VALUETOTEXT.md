# VALUETOTEXT
## VALUETOTEXT
## Purpose
Computes VALUETOTEXT behavior for spreadsheet formulas.
## Syntax
- Excel: `VALUETOTEXT(...)`
- Google Sheets: `VALUETOTEXT(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.
## Notes
- Deterministic and reproducible behavior required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_valuetotext`
- File: `base/src/functions/text.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/valuetotext-function-5fff61a2-301a-4ab2-9ffa-0a5242a08fea

- Source fetch status: failed after 4 attempts

- Summary: Computes VALUETOTEXT behavior for spreadsheet formulas.

- Signatures:

  - `VALUETOTEXT(...)`

- Examples: No examples available for this function.

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=VALUETOTEXT

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/valuetotext-function-5fff61a2-301a-4ab2-9ffa-0a5242a08fea
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=VALUETOTEXT
