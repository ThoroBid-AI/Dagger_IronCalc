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

- Summary: Get support, help, and learning resources for Microsoft 365. Organize your life, expand your creativity, and protect what’s important with Microsoft 365.

- Signatures:

  - `Not implemented for this provider per matrix metadata.`

- Examples:

  - SEARCHB("b","abc")

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



- Compatibility note: Function is not listed as supported for this provider in the shared matrix.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3295923

- Summary: Find byte-wise substring position within text.

- Signatures:

  - `SEARCHB(search_for, text_to_search, [starting_at])`

- Examples:

  - SEARCHB("新", "农历新年", 2)

  - SEARCHB(search_for, text_to_search, [starting_at])

- Notes: - If search_for is not found, the #VALUE! error value is returned. - Ensure that search_for and text_to_search are not supplied in reverse order, or the #VALUE! error will likely be returned. The arguments are supplied in a different order than other text functions such as SPLIT and SUBSTITUTE. - It's recommended to use a function such as IFERROR to check for cases when there aren't matches to the search. - You can use the wildcard characters: question mark (?) and asterisk (*), in search_for. A question mark matches any single character; an asterisk matches any sequence of characters. If you want to find an actual question mark or asterisk,…

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3295923
