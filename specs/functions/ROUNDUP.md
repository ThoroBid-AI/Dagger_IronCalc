# ROUNDUP

## ROUNDUP

## Purpose
Rounds number away from zero.

## Syntax
- Excel: `ROUNDUP(number, num_digits)`
- Google Sheets: `ROUNDUP(number, num_digits)`

## Behavior
Rounds magnitude up in magnitude direction.

## Examples (expected outputs)
- `ROUNDUP(1.1,0)` -> `2`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_roundup`
- File: `base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/roundup-function-f8bc9b23-e795-47db-8703-db171d0c42a7

- Source fetch status: failed after 4 attempts

- Summary: Rounds number away from zero.

- Signatures:

  - `ROUNDUP(number, num_digits)`

- Examples:

  - ROUNDUP(1.1,0)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093443

- Source fetch status: failed after 4 attempts

- Summary: Rounds number away from zero.

- Signatures:

  - `ROUNDUP(number, num_digits)`

- Examples:

  - ROUNDUP(1.1,0)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/roundup-function-f8bc9b23-e795-47db-8703-db171d0c42a7
- Google Sheets: https://support.google.com/docs/answer/3093443
