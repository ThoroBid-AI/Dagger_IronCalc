# CUBEMEMBERPROPERTY

## CUBEMEMBERPROPERTY

## Purpose
Returns cube member metadata property.

## Syntax
- Excel: `CUBEMEMBERPROPERTY(cube_name, member_expression, property_name)`
- Google Sheets: no direct equivalent

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `CUBEMEMBERPROPERTY("conn","[Member]","CAPTION") -> text`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/cubememberproperty-function-001e57d6-b35a-49e5-abcd-05ff599e8951

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CUBEMEMBERPROPERTY(cube_name, member_expression, property_name)`

- Examples:

  - CUBEMEMBERPROPERTY("conn","[Member]","CAPTION")

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=CUBEMEMBERPROPERTY

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/cubememberproperty-function-001e57d6-b35a-49e5-abcd-05ff599e8951
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=CUBEMEMBERPROPERTY
