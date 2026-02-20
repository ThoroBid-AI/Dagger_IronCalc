# CUBEMEMBER

## CUBEMEMBER

## Purpose
Returns member from cube hierarchy.

## Syntax
- Excel: `CUBEMEMBER(connection, member_expression, [caption], [unique_name], [property])`
- Google Sheets: no direct equivalent

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `CUBEMEMBER("conn","[Geography].[Country].[USA]") -> member`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/cubemember-function-0f6a15b9-2c18-4819-ae89-e1b5c8b398ad

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CUBEMEMBER(connection, member_expression, [caption], [unique_name], [property])`

- Examples:

  - CUBEMEMBER("conn","[Geography].[Country].[USA]")

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=CUBEMEMBER

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/cubemember-function-0f6a15b9-2c18-4819-ae89-e1b5c8b398ad
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=CUBEMEMBER
