# SEQUENCE
## SEQUENCE
## Purpose
Generates sequential numeric array.
## Syntax
- Excel: `SEQUENCE(rows, [columns], [start], [step])`
- Google Sheets: `SEQUENCE(rows, [columns], [start], [step])`
## Behavior
Deterministic behavior is required with explicit evaluation order.
## Examples (expected outputs)
- `SEQUENCE(3,1) -> {1,2,3}`
## Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.
## Notes
- Deterministic and reproducible under seeded execution context.
## Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_sequence`
- Pseudocode: deterministic parsing, coercion, and computation.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/sequence-function-57467a98-57e0-4817-9f14-2eb78519ca90

- Summary: Learn more about the SEQUENCE function, which allows you to generate a list of sequential numbers in an array, such as 1, 2, 3, 4. SEQUENCE is in a class of functions called dynamic arrays.

- Signatures:

  - `SEQUENCE(rows,[columns],[start],[step])`

- Examples: If you need to create a quick sample dataset, here's an example using SEQUENCE with TEXT, DATE, YEAR, and TODAY to create a dynamic list of months for a header row, where the underlying date will always be the current year. Our formula is: =TEXT(DATE(YEAR(TODAY()),SEQUENCE(1,6),1),"mmm"). Here's an example of nesting SEQUENCE with INT and RAND to create a 5 row by 6 column array with a random set of increasing integers. Our formula is: =SEQUENCE(5,6,INT(RAND()*100),INT(RAND()*100)). In addition, you could use =SEQUENCE(5,1,1001,1000) to create the sequential list of GL Code numbers in the examples.

- Notes: rows Required: The number of rows to return | [columns] Optional: The number of columns to return | [start] Optional: The first number in the sequence | [step] Optional: The amount to increment each subsequent value in the array

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9368244

- Summary: The SEQUENCE function&nbsp;returns an array of sequential numbers, such as 1, 2, 3, 4. Parts of a SEQUENCE function SEQUENCE(rows, columns, start, step) Part Descrip

- Signatures:

  - `SEQUENCE(2)`

  - `SEQUENCE(2, 3)`

  - `SEQUENCE(2, 3, 3, 2)`

  - `SEQUENCE(2, 3, 10, -1)`

- Examples:

  - SEQUENCE(rows, columns, start, step)

  - SEQUENCE(2)

  - SEQUENCE(2, 3)

  - SEQUENCE(2, 3, 3, 2)

  - SEQUENCE(2, 3, 10, -1)

- Notes: If columns is omitted, the resulting array will be a vertical list. If a horizontal list is needed, either specify rows as 1 and specify columns or transpose the vertical result. Result for A1=SEQUENCE(2) A B 1 1 2 2 Result for A1= SEQUENCE(2, 3) A B C 1 1 2 3 2 4 5 6 3 Result for A1= SEQUENCE(2, 3, 3, 2) A B C 1 3 5 7 2 9 11 13 3 Result for A1= SEQUENCE(2, 3, 10, -1) A B C 1 10 9 8 2 7 6 5 3 4 3 2

- Error behavior: Invalid argument types or malformed ranges return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/sequence-function-57467a98-57e0-4817-9f14-2eb78519ca90
- Google Sheets: https://support.google.com/docs/answer/9368244
