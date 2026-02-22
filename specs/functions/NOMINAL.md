# NOMINAL

## NOMINAL

## Purpose
Converts effective annual rate to nominal interest rate.

## Syntax
- Excel: `NOMINAL(effect_rate, periods)`
- Google Sheets: `NOMINAL(effect_rate, periods)`

## Behavior
Calculates nominal rate by scaling effective rate for compounding periods.

## Examples (expected outputs)
- `NOMINAL(0.08, 12)` -> `0.0766`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_nominal`
- File: `base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/nominal-function-7f1ae29b-6b92-435e-b950-ad8b190ddd2b

- Source fetch status: failed after 4 attempts

- Summary: Converts effective annual rate to nominal interest rate.

- Signatures:

  - `NOMINAL(effect_rate, periods)`

- Examples:

  - NOMINAL(0.08, 12)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093234

- Source fetch status: failed after 4 attempts

- Summary: Converts effective annual rate to nominal interest rate.

- Signatures:

  - `NOMINAL(effect_rate, periods)`

- Examples:

  - NOMINAL(0.08, 12)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/nominal-function-7f1ae29b-6b92-435e-b950-ad8b190ddd2b
- Google Sheets: https://support.google.com/docs/answer/3093234
