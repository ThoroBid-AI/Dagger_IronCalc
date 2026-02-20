# PDURATION

## PDURATION

## Purpose
Returns Macauley modified duration for a security.

## Syntax
- Excel: `PDURATION(rate, pv, fv, nper)`
- Google Sheets: `PDURATION(rate, pv, fv, nper)`

## Behavior
Computes weighted average time to receive cash flows for a zero-coupon bond approximation.

## Examples (expected outputs)
- `PDURATION(0.08, 95, 100, 10)` -> `6.2`

## Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

## Notes
- Deterministic and platform-stable behavior is required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_pduration`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/pduration-function-44f33460-5be5-4c90-b857-22308892adaf

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `PDURATION(rate, pv, fv, nper)`

- Examples:

  - PDURATION(0.08, 95, 100, 10)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9368165

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and platform-stable behavior is required.

- Signatures:

  - `PDURATION(rate, pv, fv, nper)`

- Examples:

  - PDURATION(0.08, 95, 100, 10)

- Notes: Deterministic and platform-stable behavior is required.

- Error behavior: Invalid argument types, arity, or domain values return standardized spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/pduration-function-44f33460-5be5-4c90-b857-22308892adaf
- Google Sheets: https://support.google.com/docs/answer/9368165
