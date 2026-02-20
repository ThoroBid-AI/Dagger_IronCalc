# ROUNDUP

## ROUNDUP

## Purpose
Rounds number away from zero.

## Syntax
- Excel: `ROUNDUP(number, num_digits)`
- Google Sheets: `ROUNDUP(number, num_digits)`

## Behavior
Rounds magnitude up in magnitude direction.

## Examples (expected outputs)
- `ROUNDUP(1.1,0)` -> `2`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_roundup`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/roundup-function-f8bc9b23-e795-47db-8703-db171d0c42a7

- Summary: Syntax: ROUNDUP(number, num_digits)

- Signatures:

  - `ROUNDUP(number, num_digits)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Formula Description (Result) Result =ROUNDUP(3.2,0) Rounds 3.2 up to zero decimal places. 4 =ROUNDUP(76.9,0) Rounds 76.9 up to zero decimal places. 77 =ROUNDUP(3.14159, 3) Rounds 3.14159 up to three decimal places. 3.142 =ROUNDUP(-3.14159, 1) Rounds -3.14159 up to one decimal place. -3.2 =ROUNDUP(31415.92654, -2) Rounds 31415.92654 up to 2 decimal places to the left of the decimal point. 31500

- Notes: - ROUNDUP behaves like ROUND, except that it always rounds a number up. - If num_digits is greater than 0 (zero), then number is rounded up to the specified number of decimal places. - If num_digits is 0, then number is rounded up to the nearest integer. - If num_digits is less than 0, then number is rounded up to the left of the decimal point.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093443

- Summary: Rounds a number to a certain number of decimal places, always rounding up to the next valid increment. Sample Usage ROUNDUP(99.44,1) ROUNDUP(A2) Syntax ROUNDUP(value,[places]) value

- Signatures:

  - `ROUNDUP(value,[places])`

- Examples:

  - ROUNDUP(99.44,1)

  - ROUNDUP(A2)

  - ROUNDUP(value,[places])

- Notes: - ROUNDUP operates like ROUND except that it always rounds up.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/roundup-function-f8bc9b23-e795-47db-8703-db171d0c42a7
- Google Sheets: https://support.google.com/docs/answer/3093443
