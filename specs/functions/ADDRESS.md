# ADDRESS

## ADDRESS

## Purpose
Converts row and column numbers into a cell reference string.

## Syntax
- Excel: `ADDRESS(row_num, column_num, [abs_num], [a1], [sheet_text])`
- Google Sheets: `ADDRESS(row, column, [abs_num], [A1], [sheet])`

## Behavior
- Row and column must be positive integers.
- Supports absolute/relative styles through `abs_num` and optional A1 flag.
- Optional sheet_text prefixes sheet name.

## Examples (expected outputs)
- `ADDRESS(2, 3)` -> `$C$2`
- `ADDRESS(2, 3, 4)` -> `C2`

## Error Cases
- Out-of-range row/column or invalid style flag returns an error.

## Notes
Not implemented in IronCalc. Required for formula output generation and interoperability.

## Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Handler: `fn_address` (to be added)

## Pseudocode
- Validate input arity and types per function spec.
- Reuse existing date/math helpers for conversion and rounding.
- Implement deterministic error branch for invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/address-function-d0c26c0d-3991-446b-8de4-ab46431d4f89

- Source fetch status: not captured in this snapshot

- Summary: Converts row and column numbers into a cell reference string.

- Signatures:

  - `ADDRESS(row_num, column_num, [abs_num], [a1], [sheet_text])`

- Examples:

  - ADDRESS(2, 3)

  - ADDRESS(2, 3, 4)

- Notes: Source details were not fully captured in this snapshot.

- Error behavior: Out-of-range row/column or invalid style flag returns an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093308

- Source fetch status: not captured in this snapshot

- Summary: Converts row and column numbers into a cell reference string.

- Signatures:

  - `ADDRESS(row, column, [abs_num], [A1], [sheet])`

- Examples:

  - ADDRESS(2, 3)

  - ADDRESS(2, 3, 4)

- Notes: Source details were not fully captured in this snapshot.

- Error behavior: Out-of-range row/column or invalid style flag returns an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/address-function-d0c26c0d-3991-446b-8de4-ab46431d4f89
- Google Sheets: https://support.google.com/docs/answer/3093308
