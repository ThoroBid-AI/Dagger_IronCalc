# IMLN

## IMLN

## Purpose
Returns natural logarithm of a complex number.

## Syntax
- Excel: `IMLN(inumber)`
- Google Sheets: `IMLN(inumber)`

## Behavior
- Uses principal complex logarithm with deterministic branch behavior.

## Examples (expected outputs)
- `IMLN("1") -> 0`

## Error Cases
Non-complex/invalid input returns error.

## Notes
- Implemented in IronCalc.
- Handler: `fn_imln`
- File: `base/src/functions/engineering/complex.rs`

## Code Location
- Implemented in IronCalc.
- Handler: `fn_imln`
- File: `base/src/functions/engineering/complex.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/imln-function-32b98bcf-8b81-437c-a636-6fb3aad509d8

- Source fetch status: failed after 4 attempts

- Summary: Returns natural logarithm of a complex number.

- Signatures:

  - `IMLN(inumber)`

- Examples:

  - IMLN("1")

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9000651

- Source fetch status: failed after 4 attempts

- Summary: Returns natural logarithm of a complex number.

- Signatures:

  - `IMLN(inumber)`

- Examples:

  - IMLN("1")

- Notes: Implemented in IronCalc.

- Error behavior: See source for provider-specific behavior details.



## Sources
- Excel: https://support.microsoft.com/en-us/office/imln-function-32b98bcf-8b81-437c-a636-6fb3aad509d8
- Google Sheets: https://support.google.com/docs/answer/9000651
