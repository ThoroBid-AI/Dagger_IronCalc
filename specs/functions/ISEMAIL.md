# ISEMAIL

## ISEMAIL

## Purpose
Validates whether text is an email-like address.

## Syntax
- Excel: `ISEMAIL(value)`
- Google Sheets: `ISEMAIL(value)`

## Behavior
- Uses syntax-based validation without external network checks.

## Examples (expected outputs)
- `ISEMAIL("a@b.com") -> TRUE`

## Error Cases
- Non-text values return FALSE.

## Notes

## Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_isemail`
- Proposed file: `base/src/functions/text.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: ISEMAIL("a@b.com")

- Signatures:

  - `ISEMAIL(value)`

- Examples:

  - ISEMAIL("a@b.com")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-text values return FALSE.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3256503

- Source fetch status: failed after 4 attempts

- Summary: ISEMAIL("a@b.com")

- Signatures:

  - `ISEMAIL(value)`

- Examples:

  - ISEMAIL("a@b.com")

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Non-text values return FALSE.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3256503
