# CUBESET

## CUBESET

## Purpose
Returns a cube set object.

## Syntax
- Excel: `CUBESET(connection, set_expression, [caption], [sort_order])`
- Google Sheets: no direct equivalent

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `CUBESET("conn","{set expr}") -> set`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/cubeset-function-5b2146bd-62d6-4d04-9d8f-670e993ee1d9

- Source fetch status: failed after 4 attempts

- Summary: Returns a cube set object.

- Signatures:

  - `CUBESET(connection, set_expression, [caption], [sort_order])`

- Examples:

  - CUBESET("conn","{set expr}")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=CUBESET

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/cubeset-function-5b2146bd-62d6-4d04-9d8f-670e993ee1d9
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=CUBESET
