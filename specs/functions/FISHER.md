# FISHER

## FISHER

## Purpose
Returns the hyperbolic arctangent-like Fisher transform.

## Syntax
- Excel: `FISHER(x)`
- Google Sheets: `FISHER(x)`

## Behavior
- Domain is unrestricted real input; deterministic transform with stable numeric path.

## Examples (expected outputs)
- `FISHER(1) -> 0.868591`

## Error Cases
- Non-numeric values return calculation error; overflow handled deterministically.

## Notes
- Implemented in IronCalc.

## Code Location
- Handler: `fn_fisher`
- File: `base/src/functions/statistical/fisher.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/fisher-function-d656523c-5076-4f95-b87b-7741bf236c69

- Source fetch status: failed after 4 attempts

- Summary: Returns the hyperbolic arctangent-like Fisher transform.

- Signatures:

  - `FISHER(x)`

- Examples:

  - FISHER(1)

- Notes: Implemented in IronCalc.

- Error behavior: Non-numeric values return calculation error; overflow handled deterministically.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093626

- Source fetch status: failed after 4 attempts

- Summary: Returns the hyperbolic arctangent-like Fisher transform.

- Signatures:

  - `FISHER(x)`

- Examples:

  - FISHER(1)

- Notes: Implemented in IronCalc.

- Error behavior: Non-numeric values return calculation error; overflow handled deterministically.



## Sources
- Excel: https://support.microsoft.com/en-us/office/fisher-function-d656523c-5076-4f95-b87b-7741bf236c69
- Google Sheets: https://support.google.com/docs/answer/3093626
