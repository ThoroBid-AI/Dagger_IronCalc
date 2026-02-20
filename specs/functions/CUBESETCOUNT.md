# CUBESETCOUNT

## CUBESETCOUNT

## Purpose
Returns count of members in cube set.

## Syntax
- Excel: `CUBESETCOUNT(cube_set)`
- Google Sheets: no direct equivalent

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `CUBESETCOUNT({set}) -> 2`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/cubesetcount-function-c4c2a438-c1ff-4061-80fe-982f2d705286

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `CUBESETCOUNT(cube_set)`

- Examples:

  - CUBESETCOUNT({set})

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=CUBESETCOUNT

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/cubesetcount-function-c4c2a438-c1ff-4061-80fe-982f2d705286
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=CUBESETCOUNT
