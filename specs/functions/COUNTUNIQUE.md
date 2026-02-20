# COUNTUNIQUE

## COUNTUNIQUE

## Purpose
Counts unique values in supplied arguments.

## Syntax
- Excel: `COUNTUNIQUE(value1, [value2], ...)`
- Google Sheets: `COUNTUNIQUE(value1, [value2], ...)`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.
- - Uniqueness determined by normalized text/value comparison.

## Examples (expected outputs)
- `COUNTUNIQUE(1,1,2,3) -> 3`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Counts unique values in supplied arguments.

- Signatures:

  - `COUNTUNIQUE(value1, [value2], ...)`

- Examples:

  - COUNTUNIQUE(1,1,2,3)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093405

- Source fetch status: failed after 4 attempts

- Summary: Counts unique values in supplied arguments.

- Signatures:

  - `COUNTUNIQUE(value1, [value2], ...)`

- Examples:

  - COUNTUNIQUE(1,1,2,3)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093405
