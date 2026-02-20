# DEC2OCT

## DEC2OCT

## Purpose
Converts decimal to octal text.

## Syntax
- Excel: `DEC2OCT(number, [places])`
- Google Sheets: `DEC2OCT(number, [places])`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `DEC2OCT(8,2) -> 10`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_dec2oct`
- File: `base/src/functions/engineering/number_basis.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/dec2oct-function-c9d835ca-20b7-40c4-8a9e-d3be351ce00f

- Source fetch status: failed after 4 attempts

- Summary: DEC2OCT(8,2)

- Signatures:

  - `DEC2OCT(number, [places])`

- Examples:

  - DEC2OCT(8,2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093138

- Source fetch status: failed after 4 attempts

- Summary: DEC2OCT(8,2)

- Signatures:

  - `DEC2OCT(number, [places])`

- Examples:

  - DEC2OCT(8,2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/dec2oct-function-c9d835ca-20b7-40c4-8a9e-d3be351ce00f
- Google Sheets: https://support.google.com/docs/answer/3093138
