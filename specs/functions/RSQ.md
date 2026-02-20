# RSQ

## RSQ

## Purpose
Returns square of Pearson correlation coefficient.

## Syntax
- Excel: `RSQ(known_y, known_x)`
- Google Sheets: `RSQ(known_y, known_x)`

## Behavior
Equivalent to `PEARSON(y,x)^2`.

## Examples (expected outputs)
- `RSQ({1,2,3},{2,4,6})` -> `1`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_rsq`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/pearson.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/rsq-function-d7161715-250d-4a01-b80d-a8364f2be08f

- Summary: This article describes the formula syntax and usage of the RSQ function, which returns the square of the Pearson product moment correlation coefficient through data points in known_y's and known_x's.

- Signatures:

  - `RSQ(known_y's,known_x's)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Known y Known x 2 6 3 5 9 11 1 7 8 5 7 4 5 4 Formula Description R esult =RSQ(A3:A9, B3:B9) Square of the Pearson product moment correlation coefficient through data points in A3:A9 and B3:B9. 0.05795

- Notes: - Arguments can either be numbers or names, arrays, or references that contain numbers. - Logical values and text representations of numbers that you type directly into the list of arguments are counted. - If an array or reference argument contains text, logical values, or empty cells, those values are ignored; however, cells with the value zero are included. - Arguments that are error values or text that cannot be translated into numbers cause errors. - If known_y's and known_x's are empty or have a different number of data points, RSQ returns the #N/A error value. - If known_y's and known_x's contain only 1 data point, RSQ returns the #DIV/…

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094099

- Summary: Calculates the square of r, the Pearson product-moment correlation coefficient of a dataset. Sample Usage RSQ(A2:A100,B2:B100) Syntax RSQ(data_y, data_x) data_y - The range representing t

- Signatures:

  - `RSQ(data_y, data_x)`

- Examples:

  - RSQ(A2:A100,B2:B100)

  - RSQ(data_y, data_x)

- Notes: - Any text encountered in the value arguments will be ignored.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/rsq-function-d7161715-250d-4a01-b80d-a8364f2be08f
- Google Sheets: https://support.google.com/docs/answer/3094099
