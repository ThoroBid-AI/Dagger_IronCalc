# ROMAN

## ROMAN

## Purpose
Converts number to Roman numeral.

## Syntax
- Excel: `ROMAN(number, [form])`
- Google Sheets: `ROMAN(number, [form])`

## Behavior
Converts Arabic number to Roman numeric string with optional compact form.

## Examples (expected outputs)
- `ROMAN(1987)` -> `MCMLXXXVII`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_roman`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/roman-function-d6b0b99e-de46-4704-a518-b45a0f8b56f5

- Summary: Converts an arabic numeral to roman, as text.

- Signatures:

  - `ROMAN(number, [form])`

  - `ROMAN(499,0)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Formula Description (Result) Result =ROMAN(499,0) Classic roman numeral style for 499 (CDXCIX) CDXCIX =ROMAN(499,1) More concise version for 499 (LDVLIV) LDVLIV =ROMAN(499,2) More concise version for 499 (XDIX) XDIX =ROMAN(499,3) More concise version for 499 (VDIV) VDIV =ROMAN(499,4) Simplified version for 499 (ID) ID

- Notes: - If number is negative, the #VALUE! error value is returned. - If number is greater than 3999, the #VALUE! error value is returned.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094153

- Summary: Formats a number in Roman numerals. Sample Usage ROMAN(499,0) ROMAN(A2) Syntax ROMAN(number, [rule_relaxation]) number - The number to format, between 1 and 3999, inclusive.

- Signatures:

  - `ROMAN(number, [rule_relaxation])`

  - `ROMAN(499,0)`

  - `ROMAN(499,1)`

  - `ROMAN(499,2)`

- Examples:

  - ROMAN(499,0)

  - ROMAN(A2)

  - ROMAN(number, [rule_relaxation])

  - ROMAN(499,1)

  - ROMAN(499,2)

  - ROMAN(499,3)

  - ROMAN(499,4)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/roman-function-d6b0b99e-de46-4704-a518-b45a0f8b56f5
- Google Sheets: https://support.google.com/docs/answer/3094153
