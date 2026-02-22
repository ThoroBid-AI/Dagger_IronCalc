# PRODUCT

## PRODUCT

## Purpose
Multiplies all numeric arguments.

## Syntax
- Excel: `PRODUCT(number1, [number2], ...)`
- Google Sheets: `PRODUCT(number1, [number2], ...)`

## Behavior
Returns product of all numbers after coercion.

## Examples (expected outputs)
- `PRODUCT(2,3,4)` -> `24`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_product`
- File: `base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/product-function-8e6b5b24-90ee-4650-aeec-80982a0512ce

- Source fetch status: failed after 4 attempts

- Summary: Multiplies all numeric arguments.

- Signatures:

  - `PRODUCT(number1, [number2], ...)`

- Examples:

  - PRODUCT(2,3,4)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093502

- Source fetch status: failed after 4 attempts

- Summary: Multiplies all numeric arguments.

- Signatures:

  - `PRODUCT(number1, [number2], ...)`

- Examples:

  - PRODUCT(2,3,4)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/product-function-8e6b5b24-90ee-4650-aeec-80982a0512ce
- Google Sheets: https://support.google.com/docs/answer/3093502
