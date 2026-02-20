# CUBEVALUE

## CUBEVALUE

## Purpose
Returns value from a cube expression.

## Syntax
- Excel: `CUBEVALUE(connection, member1, member2, ...)`
- Google Sheets: no direct equivalent

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `CUBEVALUE("conn","[Measure]","[Member]") -> 10`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/cubevalue-function-8733da24-26d1-4e34-9b3a-84a8f00dcbe0

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CUBEVALUE(connection, member1, member2, ...)`

- Examples:

  - CUBEVALUE("conn","[Measure]","[Member]")

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=CUBEVALUE

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/cubevalue-function-8733da24-26d1-4e34-9b3a-84a8f00dcbe0
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=CUBEVALUE
