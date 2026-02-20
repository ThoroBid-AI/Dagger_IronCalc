# JOIN

## JOIN

## Purpose
Concatenates strings with a delimiter.

## Syntax
- Excel: `JOIN(delimiter, value1, [value2], ...)`
- Google Sheets: `JOIN(delimiter, value1, [value2], ...)`

## Behavior
- Joins values in order with delimiter, skipping empty values where host-defined.

## Examples (expected outputs)
- `JOIN(",", "a", "b", "c") -> "a,b,c"`

## Error Cases
- Invalid delimiter types return errors.

## Notes

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_join`
- Proposed file: `base/src/functions/text.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: JOIN(",", "a", "b", "c")

- Signatures:

  - `JOIN(delimiter, value1, [value2], ...)`

- Examples:

  - JOIN(",", "a", "b", "c")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid delimiter types return errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094077

- Source fetch status: failed after 4 attempts

- Summary: JOIN(",", "a", "b", "c")

- Signatures:

  - `JOIN(delimiter, value1, [value2], ...)`

- Examples:

  - JOIN(",", "a", "b", "c")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid delimiter types return errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3094077
