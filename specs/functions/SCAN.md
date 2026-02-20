# SCAN
## SCAN
## Purpose
Scan/reduce across array values using a reducer.
## Syntax
- Excel: `SCAN(initial_value, array, lambda)`
- Google Sheets: `SCAN(initial_value, array, lambda)`
## Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.
## Examples (expected outputs)
- `SCAN(0,{1,2,3},LAMBDA(a,b,a+b)) -> {0,1,3,6}
## Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.
## Notes
- Deterministic and version-stable behavior is required.
## Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_scan`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/scan-function-d58dfd11-9969-4439-b2dc-e7062724de29

- Summary: Scans an array by applying a LAMBDA function to each value and returns an array that has each intermediate value

- Signatures:

  - `SCAN ([initial_value], array, lambda(accumulator, value, body)`

- Examples: Example 1: Create a list of factorials Enter the sample data into cells A1:C2, and then copy the formula into cell D4: =SCAN(1, A1:C2, LAMBDA(a,b,a*b)) Example 2: Concatenate characters in an array Enter the sample data into cells A1:C2, and then copy the formula into cell D4: =SCAN("",A1:C2,LAMBDA(a,b,a&b))

- Notes: Use the initial_value argument to set the starting value for the accumulator parameter. If you are working with text, set the initial value to "".

- Error behavior: Providing an invalid LAMBDA function or an incorrect number of parameters returns a #VALUE! error called "Incorrect Parameters".



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/12569094

- Summary: This function scans an array and produces intermediate values by application of a LAMBDA function to each value. Returns an array of the intermediate values obtained at each step. Sample Usage SCAN(

- Signatures:

  - `SCAN(initial_value, array_or_range, LAMBDA)`

  - `SCAN(5, A1:A3, LAMBDA(accumulator, current_value, accumulator+current_value)`

- Examples:

  - SCAN(5, A1:A3, LAMBDA(accumulator, current_value, accumulator+current_value)

  - SCAN(2, A1:A3, LAMBDA(accumulator, current_value, accumulator*current_value)

  - SCAN(initial_value, array_or_range, LAMBDA)

  - SCAN(0, A1:A3, LAMBDA(accumulator, current_value, accumulator + current_value/sum(A1:A3)

  - SCAN(0, A1:A6, RUNNING_TOTAL_0)

  - SCAN(5, C1:C4, LAMBDA(current_value, current_value+1)

  - SCAN(5, C1:C4, 3)

  - SCAN(5, C1:C4, LAMBDA(C1, v, C1+v)

  - SCAN(5, C1:C4, LAMBDA(accumulator, value, {accumulator, value})

- Notes: - The passed LAMBDA should accept exactly 2 name arguments, otherwise an #N/A error is returned. These arguments correspond to accumulator and current_value, in order. These are explained as: - name1: Resolves to the value in the accumulator. - name2: Resolves to the current_value in the input array. - The accumulator is initialized by initial_value and updated in each step to the intermediate value obtained in the previous step. - The current_value in the input array are found row by row, while you apply the LAMBDA. - A named function can be passed for the LAMBDA parameter and behaves like a LAMBDA in this case. Learn more about named functi…

- Error behavior: The passed LAMBDA doesn't have exactly 2 name arguments If the LAMBDA function doesn’t have 2 name arguments, this error occurs: “Wrong number of arguments to LAMBDA. Expected 3 arguments, but got 2 arguments." Example: =SCAN(5, C1:C4, LAMBDA(current_value, current_value+1)) In this example, LAMBDA was given only 1 name argument when it needed 2. The last parameter of SCAN wasn’t a LAMBDA If the last parameter of SCAN function wasn’t a LAMBDA function, this error occurs: “Argument must be a LAMBDA.” Example: =SCAN(5, C1:C4, 3) In this example the last function is 3, instead of a LAMBDA function. The LAMBDA passed to SCAN was incorrect If 1 or…



## Sources
- Excel: https://support.microsoft.com/en-us/office/scan-function-d58dfd11-9969-4439-b2dc-e7062724de29
- Google Sheets: https://support.google.com/docs/answer/12569094
