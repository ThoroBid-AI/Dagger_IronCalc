# RANDBETWEEN

## RANDBETWEEN

## Purpose
Returns random integer within a range.

## Syntax
- Excel: `RANDBETWEEN(bottom, top)`
- Google Sheets: `RANDBETWEEN(bottom, top)`

## Behavior
Volatile integer generation with inclusive bounds.

## Examples (expected outputs)
- `RANDBETWEEN(1,10)` -> `5`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Implemented in IronCalc.
- Handler: `fn_randbetween`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/randbetween-function-4cc7f0d1-87dc-4eb7-987f-a469ab381685

- Source fetch status: failed after 4 attempts

- Summary: Returns random integer within a range.

- Signatures:

  - `RANDBETWEEN(bottom, top)`

- Examples:

  - RANDBETWEEN(1,10)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093507

- Source fetch status: failed after 4 attempts

- Summary: Returns random integer within a range.

- Signatures:

  - `RANDBETWEEN(bottom, top)`

- Examples:

  - RANDBETWEEN(1,10)

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/randbetween-function-4cc7f0d1-87dc-4eb7-987f-a469ab381685
- Google Sheets: https://support.google.com/docs/answer/3093507
