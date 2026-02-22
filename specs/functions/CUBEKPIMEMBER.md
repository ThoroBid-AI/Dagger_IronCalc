# CUBEKPIMEMBER

## CUBEKPIMEMBER

## Purpose
Returns a cube key member for OLAP metadata.

## Syntax
- Excel: `CUBEKPIMEMBER(connection, dimension_expression, hierarchy_unique_name, [property], [caption], [set_expression])`
- Google Sheets: no direct equivalent

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `CUBEKPIMEMBER("conn","dim","name") -> value`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/cubekpimember-function-744608bf-2c62-42cd-b67a-a56109f4b03b

- Source fetch status: failed after 4 attempts

- Summary: Returns a cube key member for OLAP metadata.

- Signatures:

  - `CUBEKPIMEMBER(connection, dimension_expression, hierarchy_unique_name, [property], [caption], [set_expression])`

- Examples:

  - CUBEKPIMEMBER("conn","dim","name")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/table/25273?hl=en&unsupported=CUBEKPIMEMBER

- Summary: Function is not present in the provider's function index for this batch.

- Signatures: Not available for this provider.

- Examples: Not available for this provider.

- Notes: Use provider compatibility layer only when a canonical equivalent exists.



## Sources
- Excel: https://support.microsoft.com/en-us/office/cubekpimember-function-744608bf-2c62-42cd-b67a-a56109f4b03b
- Google Sheets: https://support.google.com/docs/table/25273?hl=en&unsupported=CUBEKPIMEMBER
