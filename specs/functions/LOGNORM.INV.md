# LOGNORM.INV

## LOGNORM.INV

## Purpose
Returns inverse lognormal value.

## Syntax
- Excel: `LOGNORM.INV(probability, mean, standard_dev)`
- Google Sheets: `LOGNORM.INV(probability, mean, standard_dev)`

## Behavior
- Inverts lognormal CDF for target probability.

## Examples (expected outputs)
- `LOGNORM.INV(0.5,0,1) -> 1.6487

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/statistical/log_normal.rs`
- Proposed handler: `fn_lognorm_inv`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/lognorm-inv-function-fe79751a-f1f2-4af8-a0a1-e151b2d4f600

- Source fetch status: failed after 4 attempts

- Summary: Returns inverse lognormal value.

- Signatures:

  - `LOGNORM.INV(probability, mean, standard_dev)`

- Examples:

  - LOGNORM.INV(0.5,0,1)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094010

- Source fetch status: failed after 4 attempts

- Summary: Returns inverse lognormal value.

- Signatures:

  - `LOGNORM.INV(probability, mean, standard_dev)`

- Examples:

  - LOGNORM.INV(0.5,0,1)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/lognorm-inv-function-fe79751a-f1f2-4af8-a0a1-e151b2d4f600
- Google Sheets: https://support.google.com/docs/answer/3094010
