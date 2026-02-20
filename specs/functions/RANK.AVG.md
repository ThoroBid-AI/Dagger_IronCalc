# RANK.AVG

## RANK.AVG

## Purpose
Returns average rank for ties.

## Syntax
- Excel: `RANK.AVG(number, ref, [order])`
- Google Sheets: `RANK.AVG(number, ref, [order])`

## Behavior
When ties occur, average rank is returned.

## Examples (expected outputs)
- `RANK.AVG(3,{1,3,3,4})` -> `2.5`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/statistical/statistics.rs`
- Proposed handler: `fn_rank.avg`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/rank-avg-function-bd406a6f-eb38-4d73-aa8e-6d1c3c72e83a

- Summary: The RANK.AVG function returns the rank of a number in a list of numbers: its size relative to other values in the list; if more than one value has the same rank, the average rank is returned.

- Signatures:

  - `RANK.AVG(number,ref,[order])`

- Examples: Copy the example data in the following table and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Day Temp (F) 7/1/2011 89 7/2/2011 88 7/3/2011 92 7/4/2011 101 7/5/2011 94 7/6/2011 97 7/7/2011 95 Formula Description Result =RANK.AVG(94,B2:B8) Finds the rank (the position) of the value 94 in the cell range B2:B8. In this case, 7/5/11, when the temperature reached 94, was the 4th hottest day of the days listed. 4

- Notes: - If Order is 0 (zero) or omitted, Excel ranks number as if ref were a list sorted in descending order. - If Order is any nonzero value, Excel ranks number as if ref were a list sorted in ascending order.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3267309

- Summary: Returns the rank of a specified value in a dataset. If there is more than one entry of the same value in the dataset, the average rank of the entries will be returned. Sample Usage RANK.AVG(A10, A1:A

- Signatures:

  - `RANK.AVG(value, data, [is_ascending])`

- Examples:

  - RANK.AVG(A10, A1:A100, TRUE)

  - RANK.AVG(B32, B8:B47, FALSE)

  - RANK.AVG(A10, A1:A100)

  - RANK.AVG(value, data, [is_ascending])

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/rank-avg-function-bd406a6f-eb38-4d73-aa8e-6d1c3c72e83a
- Google Sheets: https://support.google.com/docs/answer/3267309
