# NUMBERVALUE

## NUMBERVALUE

## Purpose
Converts localized text into numeric value.

## Syntax
- Excel: `NUMBERVALUE(text, [decimal_separator], [group_separator])`
- Google Sheets: `NUMBERVALUE(text, [decimal_separator], [group_separator])`

## Behavior
Parses numeric text using explicit decimal and thousands separators.

## Examples (expected outputs)
- `NUMBERVALUE("1,234.56", ".", ",")` -> `1234.56`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_numbervalue`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/numbervalue-function-1b05c8cf-2bfa-4437-af70-596c7ea7d879

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `NUMBERVALUE(text, [decimal_separator], [group_separator])`

- Examples:

  - NUMBERVALUE("1,234.56", ".", ",")

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=NUMBERVALUE

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/numbervalue-function-1b05c8cf-2bfa-4437-af70-596c7ea7d879
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=NUMBERVALUE
