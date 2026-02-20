# SKEW.P
## SKEW.P
## Purpose
Computes the population skewness of a data set.
## Syntax
- Excel: `SKEW.P(number1, [number2], ...)`
- Google Sheets: `SKEW.P(number1, [number2], ...)`
## Behavior
Calculates population skewness for an entire data set after flattening ranges and applying numeric coercion semantics.
## Examples (expected outputs)
- `=SKEW.P({1,2,3,4,5})` -> `0`
- `=SKEW.P({1,1,1,1})` -> `0`
## Error Cases
- Requires at least 3 numeric entries after coercion.
- Zero variance output conditions produce `#DIV/0!`/`#NUM!` depending on engine rules.
## Notes
Use for distribution-shape analysis in population mode.
## Code Location
- Implemented in IronCalc.
- Handler: `fn_skew_p`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs`
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/skew-p-function-76530a5c-99b9-48a1-8392-26632d542fcb

- Source fetch status: failed after 4 attempts

- Summary: Computes the population skewness of a data set.

- Signatures:

  - `SKEW.P(number1, [number2], ...)`

- Examples:

  - SKEW.P({1,2,3,4,5})

  - SKEW.P({1,1,1,1})

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Requires at least 3 numeric entries after coercion.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/9368569

- Source fetch status: failed after 4 attempts

- Summary: Computes the population skewness of a data set.

- Signatures:

  - `SKEW.P(number1, [number2], ...)`

- Examples:

  - SKEW.P({1,2,3,4,5})

  - SKEW.P({1,1,1,1})

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Requires at least 3 numeric entries after coercion.



## Sources
- Excel: https://support.microsoft.com/en-us/office/skew-p-function-76530a5c-99b9-48a1-8392-26632d542fcb
- Google Sheets: https://support.google.com/docs/answer/9368569
