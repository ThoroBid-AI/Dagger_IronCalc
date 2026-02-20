# SWITCH
## SWITCH
## Purpose
Computes SWITCH semantics for spreadsheet formulas.
## Syntax
- Excel: `SWITCH(...)`
- Google Sheets: `SWITCH(...)`
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
- Handler: `fn_switch`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/logical.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/switch-function-47ab33c0-28ce-4530-8a45-d532ec4aa25e

- Summary: The SWITCH function evaluates one value (called the expression) against a list of values, and returns the result corresponding to the first matching value. If there is no match, an optional default value may be returned. If there are no matching values, and no default argument is supplied, the SWITCH function returns the #N/A! error.

- Signatures:

  - `SWITCH(expression, value1, result1, [default or value2, result2],…[default or value3, result3])`

  - `SWITCH(Value to switch, Value to match1...[2-126], Value to return if there's a match1...[2-126], Value to return if there's no match)`

  - `SWITCH(WEEKDAY(A2)`

  - `SWITCH(A3,1,"Sunday",2,"Monday",3,"Tuesday")`

- Examples: You can copy the example data in the following table and paste it in cell A1 of a new Excel worksheet to see the SWITCH function in action. If the formulas don't show results, you can select them, then press F2 > Enter. If you need to, you can adjust the column widths to see all the data. Example Value Formula Result 2 =SWITCH(WEEKDAY(A2),1,"Sunday",2,"Monday",3,"Tuesday","No match") Because A2=2, and Monday is the result argument corresponding to the value 2, SWITCH returns Monday 99 =SWITCH(A3,1,"Sunday",2,"Monday",3,"Tuesday") Because there's no match and no else argument, SWITCH returns #N/A 99 =SWITCH(A4,1,"Sunday",2,"Monday",3,"Tuesday"…

- Notes: expression (required): Expression is the value (such as a number, date or some text) that will be compared against value1…value126. | value1…value126: ValueN is a value that will be compared against expression. | result1…result126: ResultN is the value to be returned when the corresponding valueN argument matches expression. ResultN and must be supplied for each corresponding valueN argument. | default (optional): Default is the value to return in case no matches are found in the valueN expressions. The Default argument is identified by having no corresponding resultN expression (see examples). Default must be the final argument in the functi…

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7013690

- Summary: Tests an expression against a list of cases and returns the corresponding value of the first matching case, with an optional default value if nothing else is met. Sample Usage SWITCH(A1:A10, 0,

- Signatures:

  - `SWITCH(expression, case1, value1, [case2, value2, ...], [default])`

- Examples: A B C 1 Data Result Formula 2 1 Yes =SWITCH(A2:A7,0,"No",1,"Yes","Other") 3 1 Yes 4 2 Other 5 0 No 6 3 Other 7 2 Other

- Notes: 1: Data | Result | Formula | 2: 1 | Yes | =SWITCH(A2:A7,0,"No",1,"Yes","Other") | 3: 1 | Yes | 4: 2 | Other

- Error behavior: Invalid argument count, types, and impossible domains return a spreadsheet error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/switch-function-47ab33c0-28ce-4530-8a45-d532ec4aa25e
- Google Sheets: https://support.google.com/docs/answer/7013690
