# VLOOKUP
## VLOOKUP
## Purpose
Computes VLOOKUP behavior for spreadsheet formulas.
## Syntax
- Excel: `VLOOKUP(...)`
- Google Sheets: `VLOOKUP(...)`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- `...`
## Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.
## Notes
- Deterministic and reproducible behavior required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_vlookup`
- File: `base/src/functions/lookup_and_reference.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1

- Summary: Learn how to use function VLOOKUP in Excel to find data in a table or range by row. Our step-by-step guide makes vlookup in excel easy and efficient.

- Signatures:

  - `VLOOKUP (lookup_value, table_array, col_index_num, [range_lookup])`

  - `VLOOKUP(What you want to look up, where you want to look for it, the column number in the range containing the value to return, return an Approximate or Exact match – indicated as 1/TRUE, or 0/FALSE)`

  - `VLOOKUP(A2,A10:C20,2,TRUE)`

  - `VLOOKUP("Fontana",B2:E7,2,FALSE)`

- Examples:

  - VLOOKUP (lookup_value, table_array, col_index_num, [range_lookup])

  - VLOOKUP(What you want to look up, where you want to look for it, the column number in the range containing the value to return, return an Approximate or Exact match – indicated as 1/TRUE, or 0/FALSE)

  - VLOOKUP(A2,A10:C20,2,TRUE)

  - VLOOKUP("Fontana",B2:E7,2,FALSE)

  - VLOOKUP(A2,'Client Details'!A:F,3,FALSE)

- Notes: lookup_value (required): The value you want to look up. The value you want to look up must be in the first column of the range of cells you specify in the table_array argument. For example, if table-array spans cells B2:D7, then your lookup_value must be in column B. Lookup_value can be a value or a reference to a cell. | table_array (required): The range of cells in which the VLOOKUP will search for the lookup_value and the return value. You can use a named range or a table, and you can use names in the argument instead of cell references. The first column in the cell range must contain the lookup_value. The cell range also needs to include…

- Error behavior: #N/A in cell | If range_lookup is TRUE, then if the value in the lookup_value is smaller than the smallest value in the first column of the table_array, you'll get the #N/A error value. | If range_lookup is FALSE, the #N/A error value indicates that the exact number isn't found. | For more information on resolving #N/A errors in VLOOKUP, see How to correct a #N/A error in the VLOOKUP function. | #REF! in cell | If col_index_num is greater than the number of columns in table-array, you'll get the #REF! error value. | For more information on resolving #REF! errors in VLOOKUP, see How to correct a #REF! error. | #VALUE! in cell



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093318

- Summary: &nbsp; If you have known information on your spreadsheet, you can use VLOOKUP to search for related information by row. For example, if you want to buy an orange, you can use VLOOKUP to search for th

- Signatures:

  - `VLOOKUP(search_key, range,index, is_sorted)`

- Examples:

  - VLOOKUP("Apple",table_name!fruit,table_name!price)

  - VLOOKUP(search_key, range,index, is_sorted)

  - VLOOKUP(search_key, range, index, [is_sorted])

  - VLOOKUP(G9, B4:D8, 3, FALSE)

  - VLOOKUP("Apple", B4:D8, 3, TRUE)

  - VLOOKUP()

  - VLOOKUP("Orange", B4:D8, 3, FALSE)

  - VLOOKUP("Apple", B4:D8, 3, FALSE)

  - VLOOKUP(G3, B4:D8, 2, FALSE)

  - VLOOKUP(G6, A4:D8, 2, FALSE)

- Notes: The first matched value from the selected range. Technical details: Example: =VLOOKUP(G9, B4:D8, 3, FALSE) =VLOOKUP("Apple", B4:D8, 3, TRUE) Inputs Description search_key This is the value you search in the first column of the range. If you expect a non-error value, the search key must be in the first column of the range. Cell reference is also supported. To do a simple check: If your search_key is located at B3, then your range should start with column B. range This is the range where: - The function searches for the specified search key in its first column. - VLOOKUP returns the value from the column specified by index. You can also use a n…

- Error behavior: You may want to replace an error value returned by VLOOKUP when your search key doesn’t exist. In this case, if you don’t want #N/A, you can use IFNA() functions to replace #N/A. Learn more about IFNA(). Try it out Originally, VLOOKUP returns #N/A because the search key “Pencil” does not exist in the “Fruit” column. IFNA() replaces #N/A error with the second input specified in the function. In our case, it’s “NOT FOUND.” =IFNA(VLOOKUP(G3, B4:D8, 3, FALSE),"NOT FOUND") Return value = “NOT FOUND” Tip: If you want to replace other errors such as #REF!, learn more about IFERROR().



## Sources
- Excel: https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1
- Google Sheets: https://support.google.com/docs/answer/3093318
