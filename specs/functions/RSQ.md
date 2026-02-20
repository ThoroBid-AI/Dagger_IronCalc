# RSQ

## RSQ

## Purpose
Returns square of Pearson correlation coefficient.

## Syntax
- Excel: `RSQ(known_y, known_x)`
- Google Sheets: `RSQ(known_y, known_x)`

## Behavior
Equivalent to `PEARSON(y,x)^2`.

## Examples (expected outputs)
- `RSQ({1,2,3},{2,4,6})` -> `1`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_rsq`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/pearson.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/rsq-function-d7161715-250d-4a01-b80d-a8364f2be08f

- Source fetch status: failed after 4 attempts

- Summary: Returns square of Pearson correlation coefficient.

- Signatures:

  - `RSQ(known_y, known_x)`

- Examples:

  - RSQ({1,2,3},{2,4,6})

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094099

- Source fetch status: failed after 4 attempts

- Summary: Returns square of Pearson correlation coefficient.

- Signatures:

  - `RSQ(known_y, known_x)`

- Examples:

  - RSQ({1,2,3},{2,4,6})

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/rsq-function-d7161715-250d-4a01-b80d-a8364f2be08f
- Google Sheets: https://support.google.com/docs/answer/3094099
