# RANK.EQ

## RANK.EQ

## Purpose
Returns standard ranked order with ties equal.

## Syntax
- Excel: `RANK.EQ(number, ref, [order])`
- Google Sheets: `RANK.EQ(number, ref, [order])`

## Behavior
Equivalent to classic Excel/Sheets rank where tied values share same rank.

## Examples (expected outputs)
- `RANK.EQ(3,{1,3,3,4})` -> `3`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/statistical/statistics.rs`
- Proposed handler: `fn_rank.eq`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/rank-eq-function-284858ce-8ef6-450e-b662-26245be04a40

- Summary: Returns the rank of a number in a list of numbers. Its size is relative to other values in the list; if more than one value has the same rank, the top rank of that set of values is returned. If you were to sort the list, the rank of the number would be its position.

- Signatures:

  - `RANK.EQ(number,ref,[order])`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data 7 3.5 3.5 1 2 Formula Description Result =RANK.EQ(A2,A2:A6,1) Rank of 7 in the list contained in the range A2:A6. Because the Order argument (1) is a non-zero value, the list is sorted lowest to highest. 5 =RANK.EQ(A6,A2:A6) Rank of 2 in the same list. Because the Order argument is omitted, the list is sorted, by default, highest to lowest. 4 =RANK.EQ(A3,A2:A6,1) Rank of 3.5 in the same list. 3

- Notes: - If Order is 0 (zero) or omitted, Excel ranks Number as if Ref were a list sorted in descending order. - If Order is any nonzero value, Excel ranks Number as if Ref were a list sorted in ascending order. - RANK.EQ gives duplicate numbers the same rank. However, the presence of duplicate numbers affects the ranks of subsequent numbers. For example, in a list of integers sorted in ascending order, if the number 10 appears twice and has a rank of 5, then 11 would have a rank of 7 (no number would have a rank of 6). - For some purposes one might want to use a definition of rank that takes ties into account. In the previous example, you would wan…

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3267310

- Summary: Returns the rank of a specified value in a dataset. If there is more than one entry of the same value in the dataset, the top rank of the entries will be returned. Sample Usage RANK.EQ(A10, A1:A100,

- Signatures:

  - `RANK.EQ(value, data, [is_ascending])`

- Examples:

  - RANK.EQ(A10, A1:A100, TRUE)

  - RANK.EQ(B32, B8:B47, FALSE)

  - RANK.EQ(A10, A1:A100)

  - RANK.EQ(value, data, [is_ascending])

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/rank-eq-function-284858ce-8ef6-450e-b662-26245be04a40
- Google Sheets: https://support.google.com/docs/answer/3267310
