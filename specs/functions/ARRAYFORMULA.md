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
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Handler: `fn_arrayformula` (to be added)

## Pseudocode
- Validate input arity and types per function spec.
- Reuse existing date/math helpers for conversion and rounding.
- Implement deterministic error branch for invalid inputs.

## Documentation (Microsoft)



- Source URL: not applicable (no Excel counterpart in this backlog)
- Source fetch status: not applicable (no Excel counterpart in this backlog)
- Summary: Allows a formula to return an array result that spills across adjacent cells.

- Signatures: No signatures available for this function.

- Examples:

  - ARRAYFORMULA(A1:A3*2)

- Notes: Source details were not fully captured in this snapshot.

- Error behavior: Misaligned input/output sizes can produce overflow/spill errors in sheet implementations.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093275

- Source fetch status: not captured in this snapshot

- Summary: Allows a formula to return an array result that spills across adjacent cells.

- Signatures:

  - `=ARRAYFORMULA(formula)`

- Examples:

  - ARRAYFORMULA(A1:A3*2)

- Notes: Source details were not fully captured in this snapshot.

- Error behavior: Misaligned input/output sizes can produce overflow/spill errors in sheet implementations.



## Sources
- Excel: not applicable (Sheets-only function in this backlog)
- Google Sheets: https://support.google.com/docs/answer/3093275
