# MINA

## MINA

## Purpose
Returns minimum including text/logicals.

## Syntax
- Excel: `MINA(value1, [value2], ...)`
- Google Sheets: `MINA(value1, [value2], ...)`

## Behavior
- Considers special numeric coercion for text/logical values.

## Examples (expected outputs)
- `MINA(1,TRUE,"2") -> 0`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_mina`
- File: `base/src/functions/statistical/count_and_average.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/mina-function-245a6f46-7ca5-4dc7-ab49-805341bc31d3

- Source fetch status: failed after 4 attempts

- Summary: Implemented in IronCalc.

- Signatures:

  - `MINA(value1, [value2], ...)`

- Examples:

  - MINA(1,TRUE,"2")

- Notes: Implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094018

- Source fetch status: failed after 4 attempts

- Summary: Implemented in IronCalc.

- Signatures:

  - `MINA(value1, [value2], ...)`

- Examples:

  - MINA(1,TRUE,"2")

- Notes: Implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/mina-function-245a6f46-7ca5-4dc7-ab49-805341bc31d3
- Google Sheets: https://support.google.com/docs/answer/3094018
