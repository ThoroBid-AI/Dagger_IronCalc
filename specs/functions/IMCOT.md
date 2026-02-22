# IMCOT

## IMCOT

## Purpose
Returns cotangent of a complex number.

## Syntax
- Excel: `IMCOT(inumber)`
- Google Sheets: `IMCOT(inumber)`

## Behavior
- Returns complex cotangent using 1/tan with branch handling for zero/near-zero denominators.

## Examples (expected outputs)
- `IMCOT("1") -> 0.6420926159`

## Error Cases
Zero denominator or invalid input returns error.

## Notes
- Implemented in IronCalc.
- Handler: `fn_imcot`
- File: `base/src/functions/engineering/complex.rs`

## Code Location
- Implemented in IronCalc.
- Handler: `fn_imcot`
- File: `base/src/functions/engineering/complex.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/imcot-function-dc6a3607-d26a-4d06-8b41-8931da36442c

- Source fetch status: failed after 4 attempts

- Summary: Returns cotangent of a complex number.

- Signatures:

  - `IMCOT(inumber)`

- Examples:

  - IMCOT("1")

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9366254

- Source fetch status: failed after 4 attempts

- Summary: Returns cotangent of a complex number.

- Signatures:

  - `IMCOT(inumber)`

- Examples:

  - IMCOT("1")

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/imcot-function-dc6a3607-d26a-4d06-8b41-8931da36442c
- Google Sheets: https://support.google.com/docs/answer/9366254
