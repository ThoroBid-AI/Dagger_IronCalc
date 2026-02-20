# DBCS

## DBCS

## Purpose
Converts single-byte text to double-byte string.

## Syntax
- Excel: `DBCS(text)`
- Google Sheets: `DBCS(text)`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `DBCS("ABC") -> fullwidth-ABC`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-gb/office/dbcs-function-a4025e73-63d2-4958-9423-21a24794c9e5

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `DBCS(text)`

- Examples:

  - DBCS("ABC")

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=DBCS

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-gb/office/dbcs-function-a4025e73-63d2-4958-9423-21a24794c9e5
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=DBCS
