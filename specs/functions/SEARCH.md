# SEARCH
## SEARCH
## Purpose
Find substring position within text.
## Syntax
- Excel: `SEARCH(find_text, within_text, [start_num])`
- Google Sheets: `SEARCH(find_text, within_text, [start_num])`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `SEARCH("b","abc") -> 2`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_search`
- File: `base/src/functions/text.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Find substring position within text.

- Signatures:

  - `SEARCH(find_text, within_text, [start_num])`

- Examples:

  - SEARCH("b","abc")

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094154

- Source fetch status: failed after 4 attempts

- Summary: Find substring position within text.

- Signatures:

  - `SEARCH(find_text, within_text, [start_num])`

- Examples:

  - SEARCH("b","abc")

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3094154
