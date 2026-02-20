# SEARCHB
## SEARCHB
## Purpose
Find byte-wise substring position within text.
## Syntax
- Excel: `SEARCHB(find_text, within_text, [start_num])`
- Google Sheets: `SEARCHB(find_text, within_text, [start_num])`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `SEARCHB("b","abc") -> 2`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_searchb`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Source fetch status: failed after 4 attempts

- Summary: Find byte-wise substring position within text.

- Signatures:

  - `SEARCHB(find_text, within_text, [start_num])`

- Examples:

  - SEARCHB("b","abc")

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3295923

- Source fetch status: failed after 4 attempts

- Summary: Find byte-wise substring position within text.

- Signatures:

  - `SEARCHB(find_text, within_text, [start_num])`

- Examples:

  - SEARCHB("b","abc")

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3295923
