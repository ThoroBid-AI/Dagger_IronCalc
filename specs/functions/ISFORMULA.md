# ISFORMULA

## ISFORMULA

## Purpose
Checks whether referenced cell contains a formula.

## Syntax
- Excel: `ISFORMULA(reference)`
- Google Sheets: `ISFORMULA(reference)`

## Behavior
- For static evaluator, determines formula-flag metadata for the reference.

## Examples (expected outputs)
- `ISFORMULA(A1) -> TRUE`

## Error Cases
- Invalid reference returns #REF! style error.

## Notes

## Code Location
- Implemented in IronCalc.
- Handler: `fn_isformula`
- File: `base/src/functions/information.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/isformula-function-e4d1355f-7121-4ef2-801e-3839bfd6b1e5

- Source fetch status: failed after 4 attempts

- Summary: Checks whether referenced cell contains a formula.

- Signatures:

  - `ISFORMULA(reference)`

- Examples:

  - ISFORMULA(A1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid reference returns #REF! style error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/6270316

- Source fetch status: failed after 4 attempts

- Summary: Checks whether referenced cell contains a formula.

- Signatures:

  - `ISFORMULA(reference)`

- Examples:

  - ISFORMULA(A1)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid reference returns #REF! style error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/isformula-function-e4d1355f-7121-4ef2-801e-3839bfd6b1e5
- Google Sheets: https://support.google.com/docs/answer/6270316
