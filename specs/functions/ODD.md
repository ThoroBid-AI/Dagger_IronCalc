# ODD

## ODD

## Purpose
Rounds away from zero to nearest odd integer.

## Syntax
- Excel: `ODD(number)`
- Google Sheets: `ODD(number)`

## Behavior
Returns the nearest odd integer with magnitude >= input absolute value.

## Examples (expected outputs)
- `ODD(2.5)` -> `3`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_odd`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/odd-function-deae64eb-e08a-4c88-8b40-6d0b42575c98

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `ODD(number)`

- Examples:

  - ODD(2.5)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093499

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `ODD(number)`

- Examples:

  - ODD(2.5)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/odd-function-deae64eb-e08a-4c88-8b40-6d0b42575c98
- Google Sheets: https://support.google.com/docs/answer/3093499
