# ROUNDDOWN

## ROUNDDOWN

## Purpose
Rounds number toward zero.

## Syntax
- Excel: `ROUNDDOWN(number, num_digits)`
- Google Sheets: `ROUNDDOWN(number, num_digits)`

## Behavior
For negative and positive, moves magnitude down.

## Examples (expected outputs)
- `ROUNDDOWN(1.9,0)` -> `1`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_rounddown`
- File: `base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/rounddown-function-2ec94c73-241f-4b01-8c6f-17e6d7968f53

- Source fetch status: failed after 4 attempts

- Summary: Rounds number toward zero.

- Signatures:

  - `ROUNDDOWN(number, num_digits)`

- Examples:

  - ROUNDDOWN(1.9,0)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093442

- Source fetch status: failed after 4 attempts

- Summary: Rounds number toward zero.

- Signatures:

  - `ROUNDDOWN(number, num_digits)`

- Examples:

  - ROUNDDOWN(1.9,0)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/rounddown-function-2ec94c73-241f-4b01-8c6f-17e6d7968f53
- Google Sheets: https://support.google.com/docs/answer/3093442
