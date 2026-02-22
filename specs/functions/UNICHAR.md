# UNICHAR
## UNICHAR
## Purpose
Computes UNICHAR semantics for spreadsheet formulas.
## Syntax
- Excel: `UNICHAR(number)`
- Google Sheets: `UNICHAR(number)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- `UNICHAR(66)` -> `B`
## Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.
## Notes
- Deterministic and platform-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_unichar`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/unichar-function-ffeb64f5-f131-44c6-b332-5cd72f0659b8

- Summary: Syntax: UNICHAR(number)

- Signatures:

  - `UNICHAR(number)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Formula Description Result =UNICHAR(66) Returns the character represented by the unicode number 66 (uppercase B). B =UNICHAR(32) Returns the character represented by the unicode number 32 (space character). Space character =UNICHAR(0) The unicode number 0 returns the error value #VALUE! #VALUE! Top of Page

- Notes: - The Unicode character that is returned can be a string of characters, for example in UTF-8 or UTF-16 codes. - If Unicode numbers are partial surrogates and data types that are not valid, UNICHAR returns the #N/A error value. - If numbers are numeric values that fall outside the allowable range, UNICHAR returns the #VALUE! error value. - If number is zero (0), UNICHAR returns the #VALUE! error value.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9369024

- Summary: Returns the Unicode character for a number.&nbsp;This method supports returning characters in both the UTF-8 and UTF-16 character set. Parts of a UNICHAR function UNICHAR(number) Par

- Signatures:

  - `UNICHAR(68)`

  - `UNICHAR(307)`

  - `UNICHAR(number)`

- Examples: Result for =UNICHAR(68) A B 1 D 2 Result for =UNICHAR(307) A B 1 ij 2

- Notes: - If number is 0, the method returns a #VALUE error. - If the number does not have a Unicode character, the method returns a #VALUE error. - It is possible that the method’s output changes overtime as the Unicode character set is refined.

- Error behavior: Invalid argument count or invalid domains return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/unichar-function-ffeb64f5-f131-44c6-b332-5cd72f0659b8
- Google Sheets: https://support.google.com/docs/answer/9369024
