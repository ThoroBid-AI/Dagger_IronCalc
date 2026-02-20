# MAXA

## MAXA

## Purpose
Returns maximum supporting text/logicals.

## Syntax
- Excel: `MAXA(value1, [value2], ...)`
- Google Sheets: `MAXA(value1, [value2], ...)`

## Behavior
- Includes text/logical conversion rules.

## Examples (expected outputs)
- `MAXA(1,TRUE,"2") -> 2`

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_maxa`
- File: `base/src/functions/statistical/count_and_average.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/maxa-function-814bda1e-3840-4bff-9365-2f59ac2ee62d

- Source fetch status: failed after 4 attempts

- Summary: Returns maximum supporting text/logicals.

- Signatures:

  - `MAXA(value1, [value2], ...)`

- Examples:

  - MAXA(1,TRUE,"2")

- Notes: Implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094016

- Source fetch status: failed after 4 attempts

- Summary: Returns maximum supporting text/logicals.

- Signatures:

  - `MAXA(value1, [value2], ...)`

- Examples:

  - MAXA(1,TRUE,"2")

- Notes: Implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/maxa-function-814bda1e-3840-4bff-9365-2f59ac2ee62d
- Google Sheets: https://support.google.com/docs/answer/3094016
