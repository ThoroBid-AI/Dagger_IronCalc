# ARRAYFORMULA

## ARRAYFORMULA

## Purpose
Allows a formula to return an array result that spills across adjacent cells.

## Syntax
- Excel: no direct equivalent; Excel uses dynamic arrays
- Google Sheets: `=ARRAYFORMULA(formula)`

## Behavior
- In Sheets, forces array evaluation over ranges when entering formula in a single cell.
- Requires result expansion behavior for spill arrays.

## Examples (expected outputs)
- `=ARRAYFORMULA(A1:A3*2)` -> doubles each value in `A1:A3`

## Error Cases
- Misaligned input/output sizes can produce overflow/spill errors in sheet implementations.

## Notes
Not implemented in IronCalc. Sheets-specific behavior; map to dynamic array engine semantics.

## Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Pseudocode
- Validate input arity and types per function spec.
- Reuse existing date/math helpers for conversion and rounding.
- Implement deterministic error branch for invalid inputs.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Allows a formula to return an array result that spills across adjacent cells.

- Signatures: No signatures available for this function.

- Examples:

  - ARRAYFORMULA(A1:A3*2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Misaligned input/output sizes can produce overflow/spill errors in sheet implementations.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093275

- Source fetch status: failed after 4 attempts

- Summary: Allows a formula to return an array result that spills across adjacent cells.

- Signatures:

  - `=ARRAYFORMULA(formula)`

- Examples:

  - ARRAYFORMULA(A1:A3*2)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Misaligned input/output sizes can produce overflow/spill errors in sheet implementations.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093275
