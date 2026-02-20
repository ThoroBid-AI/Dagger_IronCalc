# SPLIT
## SPLIT
## Purpose
Computes SPLIT semantics for spreadsheet formulas.
## Syntax
- Excel: `SPLIT(...)`
- Google Sheets: `SPLIT(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_split`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/

- Summary: Get support, help, and learning resources for Microsoft 365. Organize your life, expand your creativity, and protect what’s important with Microsoft 365.

- Signatures:

  - `Not implemented for this provider per matrix metadata.`

- Examples:

  - split('; ')

- Notes: Deterministic and version-stable behavior is required.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



- Compatibility note: Function is not listed as supported for this provider in the shared matrix.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094136

- Summary: Divides text around a specified character or string, and puts each fragment into a separate cell in the row. Examples Make a copy

- Signatures:

  - `SPLIT(text, delimiter, [split_by_each], [remove_empty_text])`

- Examples:

  - SPLIT(text, delimiter, [split_by_each], [remove_empty_text])

- Notes: - Note that the character or characters to split the string around will not be contained in the result themselves.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/
- Google Sheets: https://support.google.com/docs/answer/3094136
