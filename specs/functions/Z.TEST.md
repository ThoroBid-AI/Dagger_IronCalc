# Z.TEST
## Z.TEST
## Purpose
Returns z-test p-value.
## Syntax
- Excel: `Z.TEST(array, x, [sigma])`
- Google Sheets: `Z.TEST(array, x, [sigma])`
## Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.
## Examples (expected outputs)
- Z.TEST({1,2,3},2) -> 0.5
## Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.
## Notes
- Deterministic and reproducible behavior required.
## Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_z.test`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.
## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/ztest-function-8f33be8a-6bd6-4ecc-8e3a-d9a4420c4a6a

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and reproducible behavior required.

- Signatures:

  - `Z.TEST(array, x, [sigma])`

- Examples:

  - Z.TEST({1,2,3},2)

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094067

- Source fetch status: failed after 4 attempts

- Summary: Deterministic and reproducible behavior required.

- Signatures:

  - `Z.TEST(array, x, [sigma])`

- Examples:

  - Z.TEST({1,2,3},2)

- Notes: Deterministic and reproducible behavior required.

- Error behavior: Invalid argument count/types and impossible domain values return spreadsheet errors.



## Sources
- Excel: https://support.microsoft.com/en-us/office/ztest-function-8f33be8a-6bd6-4ecc-8e3a-d9a4420c4a6a
- Google Sheets: https://support.google.com/docs/answer/3094067
