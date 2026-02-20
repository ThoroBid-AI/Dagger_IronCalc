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
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Summary: Get support, help, and learning resources for Microsoft 365. Organize your life, expand your creativity, and protect what’s important with Microsoft 365.

- Signatures:

  - `Not implemented for this provider per matrix metadata.`

- Examples:

  - SEARCH("b","abc")

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



- Compatibility note: Function is not listed as supported for this provider in the shared matrix.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094154

- Summary: Find substring position within text.

- Signatures:

  - `SEARCH(search_for, text_to_search, [starting_at])`

- Examples:

  - SEARCH("n",A2)

  - SEARCH("wood","How much wood can a woodchuck chuck",14)

  - SEARCH(search_for, text_to_search, [starting_at])

  - search(nja)

  - search(b.ma,1)

  - search(this.qa,a)

  - search(YN(a.o)

  - search(l)

  - search(5)

  - search(2)

- Notes: - SEARCH is not case-sensitive, meaning that uppercase and lowercase letters do not matter. For example, "abc" will match "ABC". To compare text where case matters, use the FIND function. - Ensure that search_for and text_to_search are not supplied in reverse order, or the #VALUE! error will likely be returned. The arguments are supplied in a different order than other text functions such as SPLIT and SUBSTITUTE. - It's recommended to use a function such as IFERROR to check for cases when there aren't matches to the search.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3094154
