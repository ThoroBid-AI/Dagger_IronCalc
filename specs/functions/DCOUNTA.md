# DCOUNTA

## DCOUNTA

## Purpose
Counts non-empty values in database field meeting criteria.

## Syntax
- Excel: `DCOUNTA(database, field, criteria)`
- Google Sheets: `DCOUNTA(database, field, criteria)`

## Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

## Examples (expected outputs)
- `DCOUNTA(database, "Qty", criteria) -> 5`

## Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

## Notes
Implemented in IronCalc.

## Code Location
- Handler: `fn_dcounta`
- File: `base/src/functions/database.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/dcounta-function-00232a6d-5a66-4a01-a25b-c1653fda1244

- Source fetch status: failed after 4 attempts

- Summary: Counts non-empty values in database field meeting criteria.

- Signatures:

  - `DCOUNTA(database, field, criteria)`

- Examples:

  - DCOUNTA(database, "Qty", criteria)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094147

- Source fetch status: failed after 4 attempts

- Summary: Counts non-empty values in database field meeting criteria.

- Signatures:

  - `DCOUNTA(database, field, criteria)`

- Examples:

  - DCOUNTA(database, "Qty", criteria)

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or malformed arguments return a calculation error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/dcounta-function-00232a6d-5a66-4a01-a25b-c1653fda1244
- Google Sheets: https://support.google.com/docs/answer/3094147
