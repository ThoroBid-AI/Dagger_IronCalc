# ROUND

## ROUND

## Purpose
Rounds number to fixed decimal places.

## Syntax
- Excel: `ROUND(number, num_digits)`
- Google Sheets: `ROUND(number, num_digits)`

## Behavior
Rounds halfway cases away from zero.

## Examples (expected outputs)
- `ROUND(1.6,0)` -> `2`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_round`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/round-function-c018c5d8-40fb-4053-90b1-b3e7f61a213c

- Source fetch status: failed after 4 attempts

- Summary: Rounds number to fixed decimal places.

- Signatures:

  - `ROUND(number, num_digits)`

- Examples:

  - ROUND(1.6,0)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093440

- Source fetch status: failed after 4 attempts

- Summary: Rounds number to fixed decimal places.

- Signatures:

  - `ROUND(number, num_digits)`

- Examples:

  - ROUND(1.6,0)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/round-function-c018c5d8-40fb-4053-90b1-b3e7f61a213c
- Google Sheets: https://support.google.com/docs/answer/3093440
