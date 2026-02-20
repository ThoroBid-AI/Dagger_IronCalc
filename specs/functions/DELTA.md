# DELTA

## DELTA

## Purpose
Returns 1 when two values equal else 0.

## Syntax
- Excel: `DELTA(number1, [number2])`
- Google Sheets: `DELTA(number1, [number2])`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `DELTA(10,10) -> 1`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_delta`
- File: `base/src/functions/engineering/misc.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/delta-function-2f763672-c959-4e07-ac33-fe03220ba432

- Source fetch status: failed after 4 attempts

- Summary: DELTA(10,10)

- Signatures:

  - `DELTA(number1, [number2])`

- Examples:

  - DELTA(10,10)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3401147

- Source fetch status: failed after 4 attempts

- Summary: DELTA(10,10)

- Signatures:

  - `DELTA(number1, [number2])`

- Examples:

  - DELTA(10,10)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/delta-function-2f763672-c959-4e07-ac33-fe03220ba432
- Google Sheets: https://support.google.com/docs/answer/3401147
