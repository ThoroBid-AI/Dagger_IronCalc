# BITRSHIFT

## BITRSHIFT

## Purpose
Shifts bits right by a specified amount.

## Syntax
- Excel: `BITRSHIFT(number, shift_amount)`
- Google Sheets: `BITRSHIFT(number, shift)`

## Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

## Examples (expected outputs)
- `BITRSHIFT(20,2)` -> `5`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_bitrshift`
- File: `base/src/functions/engineering/bit_operations.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/bitrshift-function-274d6996-f42c-4743-abdb-4ff95351222c

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `BITRSHIFT(number, shift_amount)`

- Examples:

  - BITRSHIFT(20,2)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9084100

- Source fetch status: failed after 4 attempts

- Summary: Source temporarily unavailable; retained local documentation details where available.

- Signatures:

  - `BITRSHIFT(number, shift)`

- Examples:

  - BITRSHIFT(20,2)

- Notes: See source link when network access is restored.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/bitrshift-function-274d6996-f42c-4743-abdb-4ff95351222c
- Google Sheets: https://support.google.com/docs/answer/9084100
