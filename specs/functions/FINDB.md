# FINDB

## FINDB

## Purpose
Byte-level text search equivalent to FIND.

## Syntax
- Excel: `FINDB(find_text, within_text, [start_num])`
- Google Sheets: `FINDB(find_text, within_text, [start_num])`

## Behavior
- Uses byte-aware indexing and otherwise mirrors FIND domain behavior.

## Examples (expected outputs)
- `FINDB("b", "abc") -> 2`

## Error Cases
- Returns value/domain errors when search text is missing or index is invalid.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_findb`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `FINDB(find_text, within_text, [start_num])`

- Examples:

  - FINDB("b", "abc")

- Notes: Not implemented in IronCalc.

- Error behavior: Returns value/domain errors when search text is missing or index is invalid.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3296009

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `FINDB(find_text, within_text, [start_num])`

- Examples:

  - FINDB("b", "abc")

- Notes: Not implemented in IronCalc.

- Error behavior: Returns value/domain errors when search text is missing or index is invalid.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3296009
