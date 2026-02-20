# GEOMEAN

## GEOMEAN

## Purpose
Returns geometric mean of numeric values.

## Syntax
- Excel: `GEOMEAN(number1, [number2], ...)`
- Google Sheets: `GEOMEAN(number1, [number2], ...)`

## Behavior
- Uses only positive values where required by geometric mean definition.

## Examples (expected outputs)
- `GEOMEAN(1, 2, 4) -> 2`

## Error Cases
- Non-positive inputs cause domain error in strict mode.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_geomean`
- File: `base/src/functions/statistical/geomean.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/geomean-function-db1ac48d-25a5-40a0-ab83-0b38980e40d5

- Source fetch status: failed after 4 attempts

- Summary: Returns geometric mean of numeric values.

- Signatures:

  - `GEOMEAN(number1, [number2], ...)`

- Examples:

  - GEOMEAN(1, 2, 4)

- Notes: Implemented in IronCalc.

- Error behavior: Non-positive inputs cause domain error in strict mode.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094001

- Source fetch status: failed after 4 attempts

- Summary: Returns geometric mean of numeric values.

- Signatures:

  - `GEOMEAN(number1, [number2], ...)`

- Examples:

  - GEOMEAN(1, 2, 4)

- Notes: Implemented in IronCalc.

- Error behavior: Non-positive inputs cause domain error in strict mode.



## Sources
- Excel: https://support.microsoft.com/en-us/office/geomean-function-db1ac48d-25a5-40a0-ab83-0b38980e40d5
- Google Sheets: https://support.google.com/docs/answer/3094001
