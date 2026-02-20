# LOGNORM.DIST

## LOGNORM.DIST

## Purpose
Returns the lognormal distribution value.

## Syntax
- Excel: `LOGNORM.DIST(x, mean, standard_dev, cumulative)`
- Google Sheets: `LOGNORM.DIST(x, mean, standard_dev, cumulative)`

## Behavior
- PDF/CDF based on cumulative flag.

## Examples (expected outputs)
- `LOGNORM.DIST(10,0,1,TRUE) -> 0.8413

## Error Cases
- Invalid argument count or input values return errors per host semantics.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/statistical/log_normal.rs`
- Proposed handler: `fn_lognorm_dist`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/lognormdist-function-f8d194cb-9ee3-4034-8c75-1bdb3884100b

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `LOGNORM.DIST(x, mean, standard_dev, cumulative)`

- Examples:

  - LOGNORM.DIST(10,0,1,TRUE)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3094011

- Source fetch status: failed after 4 attempts

- Summary: Not implemented in IronCalc.

- Signatures:

  - `LOGNORM.DIST(x, mean, standard_dev, cumulative)`

- Examples:

  - LOGNORM.DIST(10,0,1,TRUE)

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid argument count or input values return errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/lognormdist-function-f8d194cb-9ee3-4034-8c75-1bdb3884100b
- Google Sheets: https://support.google.com/docs/answer/3094011
