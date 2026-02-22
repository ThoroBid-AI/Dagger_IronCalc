# GETPIVOTDATA

## GETPIVOTDATA

## Purpose
Extracts data from a pivot table structure by field/item pairs.

## Syntax
- Excel: `GETPIVOTDATA(data_field, pivot_table, [field, item, ...])`
- Google Sheets: `GETPIVOTDATA(data_field, pivot_table, [field, item, ...])`

## Behavior
- Locates pivot field combinations deterministically and returns aggregate value.

## Examples (expected outputs)
- `GETPIVOTDATA("Sum", A1:F10, "Month", "Jan") -> 125`

## Error Cases
- Invalid pivot reference or missing field returns reference error.

## Notes
- Not implemented in IronCalc.

## Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_getpivotdata`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/getpivotdata-function-8c083b99-a922-4ca0-af5e-3af55960761f

- Source fetch status: failed after 4 attempts

- Summary: Extracts data from a pivot table structure by field/item pairs.

- Signatures:

  - `GETPIVOTDATA(data_field, pivot_table, [field, item, ...])`

- Examples:

  - GETPIVOTDATA("Sum", A1:F10, "Month", "Jan")

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid pivot reference or missing field returns reference error.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/6167538

- Source fetch status: failed after 4 attempts

- Summary: Extracts data from a pivot table structure by field/item pairs.

- Signatures:

  - `GETPIVOTDATA(data_field, pivot_table, [field, item, ...])`

- Examples:

  - GETPIVOTDATA("Sum", A1:F10, "Month", "Jan")

- Notes: Not implemented in IronCalc.

- Error behavior: Invalid pivot reference or missing field returns reference error.



## Sources
- Excel: https://support.microsoft.com/en-us/office/getpivotdata-function-8c083b99-a922-4ca0-af5e-3af55960761f
- Google Sheets: https://support.google.com/docs/answer/6167538
