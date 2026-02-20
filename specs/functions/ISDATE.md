# ISDATE

## ISDATE

## Purpose
Returns TRUE if value is a valid date.

## Syntax
- Excel: `ISDATE(value)`
- Google Sheets: `ISDATE(value)`

## Behavior
- Recognizes serial dates and parseable date tokens under deterministic locale rules.

## Examples (expected outputs)
- `ISDATE("2026-02-19") -> TRUE`

## Error Cases
- Non-date values return FALSE, not an error.

## Notes

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_isdate`
- Proposed file: `base/src/functions/date_and_time.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Returns TRUE if value is a valid date.

- Signatures:

  - `ISDATE(value)`

- Examples:

  - ISDATE("2026-02-19")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-date values return FALSE, not an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9061381

- Source fetch status: failed after 4 attempts

- Summary: Returns TRUE if value is a valid date.

- Signatures:

  - `ISDATE(value)`

- Examples:

  - ISDATE("2026-02-19")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-date values return FALSE, not an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/9061381
