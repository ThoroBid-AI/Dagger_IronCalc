# SKEW
## SKEW
## Purpose
Returns the skewness of a data set, assuming sample skewness.
## Syntax
- Excel: `SKEW(number1, [number2], ...)`
- Google Sheets: `SKEW(number1, [number2], ...)`
## Behavior
Calculates sample skewness by flattening arguments and applying numeric coercion before evaluation.
## Examples (expected outputs)
- `=SKEW({1,2,3,4,5})` -> `0`
- `=SKEW({2,2,2})` -> `0`
## Error Cases
- Requires at least 3 numeric entries after coercion.
- Zero variance output conditions produce `#DIV/0!`/`#NUM!` depending on engine rules.
## Notes
Use for distribution-shape analysis where sample interpretation is required.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_skew`
- File: `base/src/functions/statistical/count_and_average.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/skew-function-6f6f2f8f-5c57-4dca-bd8d-0f8b5f3c6f4f

- Source fetch status: failed after 4 attempts

- Summary: Returns the skewness of a data set, assuming sample skewness.

- Signatures:

  - `SKEW(number1, [number2], ...)`

- Examples:

  - SKEW({1,2,3,4,5})

  - SKEW({2,2,2})

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Requires at least 3 numeric entries after coercion.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094104

- Source fetch status: failed after 4 attempts

- Summary: Returns the skewness of a data set, assuming sample skewness.

- Signatures:

  - `SKEW(number1, [number2], ...)`

- Examples:

  - SKEW({1,2,3,4,5})

  - SKEW({2,2,2})

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Requires at least 3 numeric entries after coercion.



## Sources
- Excel: https://support.microsoft.com/en-us/office/skew-function-6f6f2f8f-5c57-4dca-bd8d-0f8b5f3c6f4f
- Google Sheets: https://support.google.com/docs/answer/3094104
