# FORMULATEXT

## FORMULATEXT

## Purpose
Returns the formula text of a referenced cell.

## Syntax
- Excel: `FORMULATEXT(reference)`
- Google Sheets: `FORMULATEXT(reference)`

## Behavior
- Returns formula string if target cell contains formula, otherwise errors or blank as host semantics.

## Examples (expected outputs)
- `FORMULATEXT(A1) -> "=SUM(A1:A3)"`

## Error Cases
- Non-formula references and inaccessible cells return error.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_formulatext`
- File: `base/src/functions/lookup_and_reference.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/formulatext-function-0a786771-54fd-4ae2-96ee-09cda35439c8

- Source fetch status: failed after 4 attempts

- Summary: Returns the formula text of a referenced cell.

- Signatures:

  - `FORMULATEXT(reference)`

- Examples:

  - FORMULATEXT(A1)

- Notes: Implemented in IronCalc.

- Error behavior: Non-formula references and inaccessible cells return error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9365792

- Source fetch status: failed after 4 attempts

- Summary: Returns the formula text of a referenced cell.

- Signatures:

  - `FORMULATEXT(reference)`

- Examples:

  - FORMULATEXT(A1)

- Notes: Implemented in IronCalc.

- Error behavior: Non-formula references and inaccessible cells return error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/formulatext-function-0a786771-54fd-4ae2-96ee-09cda35439c8
- Google Sheets: https://support.google.com/docs/answer/9365792
