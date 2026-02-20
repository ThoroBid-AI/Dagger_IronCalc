# RANK.EQ

## RANK.EQ

## Purpose
Returns standard ranked order with ties equal.

## Syntax
- Excel: `RANK.EQ(number, ref, [order])`
- Google Sheets: `RANK.EQ(number, ref, [order])`

## Behavior
Equivalent to classic Excel/Sheets rank where tied values share same rank.

## Examples (expected outputs)
- `RANK.EQ(3,{1,3,3,4})` -> `3`

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/statistical/statistics.rs`
- Proposed handler: `fn_rank.eq`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/rank-eq-function-284858ce-8ef6-450e-b662-26245be04a40

- Source fetch status: failed after 4 attempts

- Summary: Returns standard ranked order with ties equal.

- Signatures:

  - `RANK.EQ(number, ref, [order])`

- Examples:

  - RANK.EQ(3,{1,3,3,4})

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3267310

- Source fetch status: failed after 4 attempts

- Summary: Returns standard ranked order with ties equal.

- Signatures:

  - `RANK.EQ(number, ref, [order])`

- Examples:

  - RANK.EQ(3,{1,3,3,4})

- Notes: Deterministic and ordered input handling required.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/rank-eq-function-284858ce-8ef6-450e-b662-26245be04a40
- Google Sheets: https://support.google.com/docs/answer/3267310
