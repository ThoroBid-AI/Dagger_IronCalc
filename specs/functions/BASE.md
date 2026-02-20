# BASE

## BASE

## Purpose
Converts a number to text using a chosen base and minimum digits.

## Syntax
- Excel: `BASE(number, radix, [min_length])`
- Google Sheets: `BASE(number, radix, [min_length])`

## Behavior
- Number is converted to base between 2 and 36.
- Optional minimum length pads with leading zeros to requested width.

## Examples (expected outputs)
- `BASE(10,2,8)` -> `00001010`

## Error Cases
- Radix out of range or invalid number causes error.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_base`
- File: `base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/base-function-2ef61411-aee9-4f29-a811-1c42456c6342

- Source fetch status: failed after 4 attempts

- Summary: Converts a number to text using a chosen base and minimum digits.

- Signatures:

  - `BASE(number, radix, [min_length])`

- Examples:

  - BASE(10,2,8)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Radix out of range or invalid number causes error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9084167

- Source fetch status: failed after 4 attempts

- Summary: Converts a number to text using a chosen base and minimum digits.

- Signatures:

  - `BASE(number, radix, [min_length])`

- Examples:

  - BASE(10,2,8)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Radix out of range or invalid number causes error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/base-function-2ef61411-aee9-4f29-a811-1c42456c6342
- Google Sheets: https://support.google.com/docs/answer/9084167
