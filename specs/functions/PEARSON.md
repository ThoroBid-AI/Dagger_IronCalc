# PEARSON

## PEARSON

## Purpose
Returns Pearson product-moment correlation coefficient.

## Syntax
- Excel: `PEARSON(array1, array2)`
- Google Sheets: `PEARSON(array1, array2)`

## Behavior
Calculates linear correlation between paired data ranges.

## Examples (expected outputs)
- `PEARSON({1,2,3},{2,4,6})` -> `1`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_pearson`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/pearson.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/pearson-function-0c3e30fc-e5af-49c4-808a-3ef66e034c18

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `PEARSON(array1, array2)`

- Examples:

  - PEARSON({1,2,3},{2,4,6})

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094092

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `PEARSON(array1, array2)`

- Examples:

  - PEARSON({1,2,3},{2,4,6})

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/pearson-function-0c3e30fc-e5af-49c4-808a-3ef66e034c18
- Google Sheets: https://support.google.com/docs/answer/3094092
