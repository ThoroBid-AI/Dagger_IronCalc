# SUBSTITUTE
## SUBSTITUTE
## Purpose
Computes SUBSTITUTE semantics for spreadsheet formulas.
## Syntax
- Excel: `SUBSTITUTE(...)`
- Google Sheets: `SUBSTITUTE(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_substitute`
- File: `base/src/functions/text.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/substitute-function-6434944e-a904-4336-a9b0-1e58df3bc332

- Summary: Substitutes new_text for old_text in a text string. Use SUBSTITUTE when you want to replace specific text in a text string; use REPLACE when you want to replace any text that occurs in a specific location in a text string.

- Signatures:

  - `SUBSTITUTE(text, old_text, new_text, [instance_num])`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Sales Data < Quarter 1, 2008 < Quarter 1, 2011 < Formula Description (Result) Result =SUBSTITUTE(A2, "Sales", "Cost") Substitutes Cost for Sales (Cost Data) Cost Data =SUBSTITUTE(A3, "1", "2", 1) Substitutes first instance of "1" with "2" (Quarter 2, 2008) Quarter 2, 2008 =SUBSTITUTE(A4, "1", "2", 3) Substitutes third instance of "1" with "2" (Quarter 1, 2012) Quarter 1, 2012

- Notes: Sales Data: < | Quarter 1, 2008: < | Quarter 1, 2011: < | Formula: Description (Result) | Result

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094215

- Summary: Computes SUBSTITUTE semantics for spreadsheet formulas.

- Signatures:

  - `SUBSTITUTE(text_to_search, search_for, replace_with, [occurrence_number])`

- Examples:

  - SUBSTITUTE("search for it","search for","Google")

  - SUBSTITUTE(A2,"new york","New York")

  - SUBSTITUTE("January 2, 2012",2,3,1)

  - SUBSTITUTE(text_to_search, search_for, replace_with, [occurrence_number])

- Notes: - SUBSTITUTE can be used to replace one or all instances of a string within text_to_search. It cannot be used to replace multiple, but not all instances within a single call. - This function returns text as the output. If a number is desired, try using the VALUE function in conjunction with this function.

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/substitute-function-6434944e-a904-4336-a9b0-1e58df3bc332
- Google Sheets: https://support.google.com/docs/answer/3094215
