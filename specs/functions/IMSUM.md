# IMSUM

## IMSUM

## Purpose
Returns the sum of multiple complex numbers.

## Syntax
- Excel: `IMSUM(inumber1, [inumber2], ...)`
- Google Sheets: `IMSUM(inumber1, [inumber2], ...)`

## Behavior
- Adds all inputs using deterministic complex arithmetic.

## Examples (expected outputs)
- `IMSUM("1+i","2+3i") -> 3+4i`

## Error Cases
- Empty input list or malformed values return errors.

## Notes

## Code Location
- Implemented in IronCalc.
- Handler: `fn_imsum`
- File: `base/src/functions/engineering/complex.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/imsum-function-81542999-5f1c-4da6-9ffe-f1d7aaa9457f

- Source fetch status: failed after 4 attempts

- Summary: IMSUM("1+i","2+3i")

- Signatures:

  - `IMSUM(inumber1, [inumber2], ...)`

- Examples:

  - IMSUM("1+i","2+3i")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Empty input list or malformed values return errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7408295

- Source fetch status: failed after 4 attempts

- Summary: IMSUM("1+i","2+3i")

- Signatures:

  - `IMSUM(inumber1, [inumber2], ...)`

- Examples:

  - IMSUM("1+i","2+3i")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Empty input list or malformed values return errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/imsum-function-81542999-5f1c-4da6-9ffe-f1d7aaa9457f
- Google Sheets: https://support.google.com/docs/answer/7408295
