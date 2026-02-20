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
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Handler: `fn_countunique` (to be added)

## Documentation (Microsoft)



- Source URL: not applicable (no Excel counterpart in this backlog)
- Source fetch status: not applicable (no Excel counterpart in this backlog)
- Summary: Counts unique values in supplied arguments.

- Signatures:

  - `COUNTUNIQUE(value1, [value2], ...)`

- Examples:

  - COUNTUNIQUE(1,1,2,3)

- Notes: Source details were not fully captured in this snapshot.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093405

- Source fetch status: not captured in this snapshot

- Summary: Counts unique values in supplied arguments.

- Signatures:

  - `COUNTUNIQUE(value1, [value2], ...)`

- Examples:

  - COUNTUNIQUE(1,1,2,3)

- Notes: Source details were not fully captured in this snapshot.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Sources
- Excel: not applicable (Sheets-only function in this backlog)
- Google Sheets: https://support.google.com/docs/answer/3093405
