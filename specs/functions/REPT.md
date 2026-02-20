# REPT

## REPT

## Purpose
Repeats text a number of times.

## Syntax
- Excel: `REPT(text, number_times)`
- Google Sheets: `REPT(text, number_times)`

## Behavior
Concatenates repeated text segments.

## Examples (expected outputs)
- `REPT("A",3)` -> `AAA`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_rept`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/rept-function-04c4d778-e712-43b4-9c15-d656582bb061

- Summary: The REPT function repeats text a given number of times. Use REPT to fill a cell with a number of instances of a text string.

- Signatures:

  - `REPT(text, number_times)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Formula Description Result =REPT("*-", 3) Displays an asterisk and a dash (*-) 3 times. *-*-*- =REPT("-",10) Displays a dash (-) 10 times. ----------

- Notes: - If number_times is 0 (zero), REPT returns "" (empty text). - If number_times is not an integer, it is truncated. - The result of the REPT function cannot be longer than 32,767 characters, or REPT returns #VALUE!.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094134

- Summary: Repeats text a number of times.

- Signatures:

  - `REPT(text_to_repeat, number_of_repetitions)`

- Examples:

  - REPT("ha",4)

  - REPT(A2,3)

  - REPT(text_to_repeat, number_of_repetitions)

- Notes: - REPT does not insert spaces between repetitions of text_to_repeat. If spaces are desired, a space must be appended to the end of the value of text_to_repeat. The resulting return value from REPT will have at least one trailing space, which may be removed with TRIM.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/rept-function-04c4d778-e712-43b4-9c15-d656582bb061
- Google Sheets: https://support.google.com/docs/answer/3094134
