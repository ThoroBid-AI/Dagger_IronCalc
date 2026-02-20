# ROUND

## ROUND

## Purpose
Rounds number to fixed decimal places.

## Syntax
- Excel: `ROUND(number, num_digits)`
- Google Sheets: `ROUND(number, num_digits)`

## Behavior
Rounds halfway cases away from zero.

## Examples (expected outputs)
- `ROUND(1.6,0)` -> `2`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_round`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/round-function-c018c5d8-40fb-4053-90b1-b3e7f61a213c

- Summary: Syntax: ROUND(number, num_digits)

- Signatures:

  - `ROUND(number, num_digits)`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Formula Description Result =ROUND(2.15, 1) Rounds 2.15 to one decimal place 2.2 =ROUND(2.149, 1) Rounds 2.149 to one decimal place 2.1 =ROUND(-1.475, 2) Rounds -1.475 to two decimal places -1.48 =ROUND(21.5, -1) Rounds 21.5 to one decimal place to the left of the decimal point 20 =ROUND(626.3,-3) Rounds 626.3 to the nearest multiple of 1000 1000 =ROUND(1.98,-1) Rounds 1.98 to the nearest multiple of 10 0 =…

- Notes: - If num_digits is greater than 0 (zero), then number is rounded to the specified number of decimal places. - If num_digits is 0, the number is rounded to the nearest integer. - If num_digits is less than 0, the number is rounded to the left of the decimal point. - To always round up (away from zero), use the ROUNDUP function. - To always round down (toward zero), use the ROUNDDOWN function. - To round a number to a specific multiple (for example, to round to the nearest 0.5), use the MROUND function.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093440

- Summary: The ROUND function rounds a number to a certain number of decimal places according to standard rules. Examples Make a copy

- Signatures:

  - `ROUND(value, [places])`

- Examples:

  - ROUND(1.6,0)

- Notes: - Standard rules indicate that when rounding to a particular place, the next most significant digit (the digit to the right) is considered. If this digit is greater than or equal to 5, the digit is rounded up, otherwise it is rounded down. This occurs irrespective of sign; that is, 'up' and 'down' are in terms of magnitude.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/round-function-c018c5d8-40fb-4053-90b1-b3e7f61a213c
- Google Sheets: https://support.google.com/docs/answer/3093440
