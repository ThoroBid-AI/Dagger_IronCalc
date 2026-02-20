# CUBERANKEDMEMBER

## CUBERANKEDMEMBER

## Purpose
Returns ranked member from a cube set.

## Syntax
- Excel: `CUBERANKEDMEMBER(connection, set_expression, rank, [order], [tie]...)`
- Google Sheets: no direct equivalent

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.
- - Relies on cube engine metadata and ordering semantics.

## Examples (expected outputs)
- `CUBERANKEDMEMBER("conn","{set}",1) -> member`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/cuberankedmember-function-07efecde-e669-4075-b4bf-6b40df2dc4b3

- Source fetch status: failed after 4 attempts

- Summary: Returns ranked member from a cube set.

- Signatures:

  - `CUBERANKEDMEMBER(connection, set_expression, rank, [order], [tie]...)`

- Examples:

  - CUBERANKEDMEMBER("conn","{set}",1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=CUBERANKEDMEMBER

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/cuberankedmember-function-07efecde-e669-4075-b4bf-6b40df2dc4b3
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=CUBERANKEDMEMBER
