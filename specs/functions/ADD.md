# ADD

## ADD

## Purpose
Adds numbers (legacy alias to arithmetic addition in formula workflows).

## Syntax
- Excel: `ADD(number1, number2, ...)`
- Google Sheets: `ADD(number1, number2, ...)`

## Behavior
- Normal numeric addition with implicit coercion of numeric strings where supported by parser.
- A variadic form is expected to sum at least two values.

## Examples (expected outputs)
- `ADD(1,2,3)` -> `6`

## Error Cases
- Non-numeric arguments return an error consistent with host behavior.

## Notes
Not implemented in IronCalc. Prefer native `+` and `SUM` operator/function patterns.

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

- Summary: Adds numbers (legacy alias to arithmetic addition in formula workflows).

- Signatures:

  - `ADD(number1, number2, ...)`

- Examples:

  - ADD(1,2,3)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-numeric arguments return an error consistent with host behavior.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093590

- Source fetch status: failed after 4 attempts

- Summary: Adds numbers (legacy alias to arithmetic addition in formula workflows).

- Signatures:

  - `ADD(number1, number2, ...)`

- Examples:

  - ADD(1,2,3)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-numeric arguments return an error consistent with host behavior.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3093590
