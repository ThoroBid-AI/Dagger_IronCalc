# ROUNDDOWN

## ROUNDDOWN

## Purpose
Rounds number toward zero.

## Syntax
- Excel: `ROUNDDOWN(number, num_digits)`
- Google Sheets: `ROUNDDOWN(number, num_digits)`

## Behavior
For negative and positive, moves magnitude down.

## Examples (expected outputs)
- `ROUNDDOWN(1.9,0)` -> `1`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_rounddown`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/rounddown-function-2ec94c73-241f-4b01-8c6f-17e6d7968f53

- Summary: Syntax: ROUNDDOWN(number, num_digits)

- Signatures:

  - `ROUNDDOWN(number, num_digits)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Formula Description Result =ROUNDDOWN(3.2, 0) Rounds 3.2 down to zero decimal places. 3 =ROUNDDOWN(76.9,0) Rounds 76.9 down to zero decimal places. 76 =ROUNDDOWN(3.14159, 3) Rounds 3.14159 down to three decimal places. 3.141 =ROUNDDOWN(-3.14159, 1) Rounds -3.14159 down to one decimal place. -3.1 =ROUNDDOWN(31415.92654, -2) Rounds 31415.92654 down to 2 decimal places to the left of the decimal point. 31400

- Notes: - ROUNDDOWN behaves like ROUND, except that it always rounds a number down. - If num_digits is greater than 0 (zero), then number is rounded down to the specified number of decimal places. - If num_digits is 0, then number is rounded down to the nearest integer. - If num_digits is less than 0, then number is rounded down to the left of the decimal point.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093442

- Summary: The ROUNDDOWN function rounds a number to a certain number of decimal places, always rounding down to the next valid increment. Sample Usage ROUNDDOWN(99.44,1) ROUNDDOWN(A2) Syntax ROUNDDOWN(valu

- Signatures:

  - `ROUNDDOWN(value,[places])`

- Examples:

  - ROUNDDOWN(99.44,1)

  - ROUNDDOWN(A2)

  - ROUNDDOWN(value,[places])

- Notes: - ROUNDDOWN operates like ROUND except that it always rounds down.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/rounddown-function-2ec94c73-241f-4b01-8c6f-17e6d7968f53
- Google Sheets: https://support.google.com/docs/answer/3093442
