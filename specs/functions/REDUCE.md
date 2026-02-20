# REDUCE

## REDUCE

## Purpose
Accumulates values from an array with a lambda-like reducer.

## Syntax
- Excel: `REDUCE(initial_value, array, reducer, [initial_value2], ...)`
- Google Sheets: `REDUCE(initial_value, array, reducer, ...)`

## Behavior
Runs reducer left-to-right across array values.

## Examples (expected outputs)
- `REDUCE(0,{1,2,3},LAMBDA(a,b,a+b))` -> `6`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_reduce`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/reduce-function-42e39910-b345-45f3-84b8-0642b568b7cb

- Summary: Reduces an array to an accumulated value by applying a LAMBDA function to each value and returning the total value in the accumulator

- Signatures:

  - `REDUCE([initial_value], array, lambda(accumulator, value, body)`

- Examples: Example 1: Sum the squared values Enter the sample data into cells A1:C2, and then copy the formula into cell D4: =REDUCE(, A1:C2, LAMBDA(a,b,a+b^2)) Example 2: Create a customized "PRODUCTIF" function to multiply only values greater than 50 Create a table named "Table3" with one column named "nums" starting at cell E1. Copy the following formula into cell G2: =REDUCE(1,Table3[nums],LAMBDA(a,b,IF(b>50,a*b,a))) Example 3: Count only even values Create a table named "Table4" with one column named "Nums" starting at cell D1. Copy the following formula into cell F2: =REDUCE(0,Table4[Nums],LAMBDA(a,n,IF(ISEVEN(n),1+a, a)))

- Notes: Use the initial_value argument to set the starting value for the accumulator parameter. In Example 2, where you multiply the accumulator, set the value to 1 to avoid multiplying by 0.

- Error behavior: Providing an invalid LAMBDA function or an incorrect number of parameters returns a #VALUE! error called "Incorrect Parameters".



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/12568597

- Summary: This function reduces an array to an accumulated result by application of a LAMBDA function to each value. Sample Usage REDUCE(5, A1:A3, LAMBDA(accumulator, current_value, accumulator+current_value)

- Signatures:

  - `REDUCE(initial_value, array_or_range, LAMBDA)`

- Examples:

  - REDUCE(5, A1:A3, LAMBDA(accumulator, current_value, accumulator+current_value)

  - REDUCE(2, A1:A3, LAMBDA(accumulator, current_value, accumulator*current_value)

  - REDUCE(initial_value, array_or_range, LAMBDA)

  - REDUCE(5, A1:A3, LAMBDA(accumulator, current_value, accumulator*current_value)

  - REDUCE(0, A1:A4, LAMBDA(accumulator, price, if(price>=20, accumulator + price, accumulator)

  - REDUCE(C2,B1:B4,PRICE_INCREASE)

  - REDUCE({B2}, B2:E4, ADD_IF_NOT_PRESENT)

  - REDUCE(5, C1:C4, LAMBDA(current_value, current_value+1)

  - REDUCE(5, C1:C4, 3)

  - REDUCE(5, C1:C4, LAMBDA(C1, v, C1+v)

- Notes: - The passed LAMBDA should accept exactly 2 name arguments, otherwise an #N/A error is returned. These arguments correspond to accumulator and current_value, in order. These are explained as: - name1: Resolves to the current value in the accumulator. - name2: Resolves to the current_value in the input array. - The accumulator is initialized by initial_value and updated in each step to the intermediate value obtained in the previous step. - The current_value in the input array are found row by row, while the LAMBDA is being applied. - A named function can be passed for the LAMBDA parameter and behaves like a LAMBDA in this case. Learn more abo…

- Error behavior: The passed LAMBDA doesn't have exactly 2 name arguments If the LAMBDA function doesn’t have 2 name arguments, this error occurs: “Wrong number of arguments to LAMBDA. Expected 3 arguments, but got 2 arguments.” Example: =REDUCE(5, C1:C4, LAMBDA(current_value, current_value+1)) In this example, LAMBDA was given only 1 name argument when it needed 2. The last parameter of REDUCE wasn’t a LAMBDA If the last parameter of REDUCE function wasn’t a LAMBDA function, this error occurs: “Argument must be a LAMBDA.” Example: =REDUCE(5, C1:C4, 3) In this example the last function is 3, instead of a LAMBDA function. The LAMBDA passed to REDUCE was incorre…



## Sources
- Excel: https://support.microsoft.com/en-us/office/reduce-function-42e39910-b345-45f3-84b8-0642b568b7cb
- Google Sheets: https://support.google.com/docs/answer/12568597
