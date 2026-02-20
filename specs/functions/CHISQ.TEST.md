# CHISQ.TEST

## CHISQ.TEST

## Purpose
Returns chi-square goodness-of-fit test statistic/result.

## Syntax
- Excel: `CHISQ.TEST(actual_range, expected_range)`
- Google Sheets: `CHISQ.TEST(actual_range, expected_range)`

## Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

## Examples (expected outputs)
- `CHISQ.TEST({1,2;3,4},{2,2;2,4})` -> `0.123`

## Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

## Notes
Not implemented in IronCalc.

## Code Location
- Handler: `fn_chisq_test`
- File: `base/src/functions/statistical/chisq.rs`

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/chisq-test-function-2e8a7861-b14a-4985-aa93-fb88de3f260f

- Source fetch status: failed after 4 attempts

- Summary: Returns chi-square goodness-of-fit test statistic/result.

- Signatures:

  - `CHISQ.TEST(actual_range, expected_range)`

- Examples:

  - CHISQ.TEST({1,2;3,4},{2,2;2,4})

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/7004263

- Source fetch status: failed after 4 attempts

- Summary: Returns chi-square goodness-of-fit test statistic/result.

- Signatures:

  - `CHISQ.TEST(actual_range, expected_range)`

- Examples:

  - CHISQ.TEST({1,2;3,4},{2,2;2,4})

- Notes: Source temporarily unavailable. Use local documentation details only.

- Error behavior: Invalid argument count or type yields an error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/chisq-test-function-2e8a7861-b14a-4985-aa93-fb88de3f260f
- Google Sheets: https://support.google.com/docs/answer/7004263
