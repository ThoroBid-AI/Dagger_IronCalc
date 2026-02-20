# Lua Implementation Prompts (All Functions)

## ABS — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_abs
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Return the absolute value of a number.

### Syntax
- Excel: `ABS(number)`
- Google Sheets: `ABS(value)`

### Behavior
- Returns the magnitude of the input without its sign.

### Examples
- `ABS(-2)` -> `2`
- `ABS(2)` -> `2`

### Error Cases
- Non-numeric input returns an error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_abs`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ABS.md


---

## ACCRINT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the accrued interest for a security that pays periodic interest.

### Syntax
- Excel: `ACCRINT(issue, first_interest, settlement, rate, par, frequency, basis, [calc_method])`
- Google Sheets: `ACCRINT(issue, first_interest, settlement, rate, par, frequency, basis, [method])`

### Behavior
- Issue date, first coupon date, settlement, rate, par, frequency, and basis are required.
- Frequency is one of 1, 2, 4 (annual, semiannual, quarterly).
- The optional method controls whether actual/actual interest is rounded.
- Errors are returned if the settlement date is before issue or if parameters are invalid.

### Examples
- `ACCRINT(DATE(2024,1,1), DATE(2024,6,30), DATE(2024,3,15), 0.08, 1000, 2, 0)` -> `42.5`

### Error Cases
- Returns an error when required date order or frequency is invalid.

### Notes
Not implemented in IronCalc. Planned as a financial function for bond-like schedules.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ACCRINT.md


---

## ACCRINTM — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the accrued interest for a security that pays interest at maturity.

### Syntax
- Excel: `ACCRINTM(issue, maturity, rate, par, basis, [day_count])`
- Google Sheets: `ACCRINTM(issue, maturity, rate, par, basis, [day_count])`

### Behavior
- Calculates accrued interest between issue and maturity.
- Basis controls day-count behavior.

### Examples
- `ACCRINTM(DATE(2024,1,1), DATE(2025,1,1), 0.05, 1000, 0)` -> accrual amount

### Error Cases
- Returns an error when dates are invalid or maturity is before issue.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ACCRINTM.md


---

## ACOS — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_acos
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Return the arccosine (inverse cosine) of a number in radians.

### Syntax
- Excel: `ACOS(number)`
- Google Sheets: `ACOS(value)`

### Behavior
- Input must be between -1 and 1 (inclusive).
- Result is in radians, range 0 to PI.

### Examples
- `ACOS(-0.5)` -> `2.094395102`

### Error Cases
- Input outside [-1, 1] returns an error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_acos`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ACOS.md


---

## ACOSH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_acosh
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Return the inverse hyperbolic cosine of a number.

### Syntax
- Excel: `ACOSH(number)`
- Google Sheets: `ACOSH(value)`

### Behavior
- Input must be >= 1.

### Examples
- `ACOSH(1)` -> `0`
- `ACOSH(10)` -> `2.9932228`

### Error Cases
- Input < 1 returns an error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_acosh`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ACOSH.md


---

## ACOT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: N
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_acot
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Return the inverse cotangent of a number in radians.

### Syntax
- Excel: `ACOT(number)`
- Google Sheets: `ACOT(value)`

### Behavior
- Result is in radians, range 0 to PI.

### Examples
- `ACOT(2)` -> `0.4636`

### Error Cases
- Non-numeric input returns an error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_acot`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ACOT.md


---

## ACOTH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_acoth
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Return the inverse hyperbolic cotangent of a number.

### Syntax
- Excel: `ACOTH(number)`
- Google Sheets: `ACOTH(value)`

### Behavior
- Absolute value of input must be > 1.

### Examples
- `ACOTH(6)` -> `0.168`

### Error Cases
- If absolute value <= 1, returns an error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_acoth`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ACOTH.md


---

## ADD — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Adds numbers (legacy alias to arithmetic addition in formula workflows).

### Syntax
- Excel: `ADD(number1, number2, ...)`
- Google Sheets: `ADD(number1, number2, ...)`

### Behavior
- Normal numeric addition with implicit coercion of numeric strings where supported by parser.
- A variadic form is expected to sum at least two values.

### Examples
- `ADD(1,2,3)` -> `6`

### Error Cases
- Non-numeric arguments return an error consistent with host behavior.

### Notes
Not implemented in IronCalc. Prefer native `+` and `SUM` operator/function patterns.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ADD.md


---

## ADDRESS — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts row and column numbers into a cell reference string.

### Syntax
- Excel: `ADDRESS(row_num, column_num, [abs_num], [a1], [sheet_text])`
- Google Sheets: `ADDRESS(row, column, [abs_num], [A1], [sheet])`

### Behavior
- Row and column must be positive integers.
- Supports absolute/relative styles through `abs_num` and optional A1 flag.
- Optional sheet_text prefixes sheet name.

### Examples
- `ADDRESS(2, 3)` -> `$C$2`
- `ADDRESS(2, 3, 4)` -> `C2`

### Error Cases
- Out-of-range row/column or invalid style flag returns an error.

### Notes
Not implemented in IronCalc. Required for formula output generation and interoperability.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ADDRESS.md


---

## AGGREGATE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns an aggregate over data with optional options to ignore errors or hidden values.

### Syntax
- Excel: `AGGREGATE(function_num, options, array, [k])`
- Google Sheets: `AGGREGATE(function_num, options, array, [k])`

### Behavior
- Supports function selector in `function_num` and option flags in `options`.
- Can be used to produce stats like SUM, AVERAGE, MAX while ignoring filtered rows/errors.

### Examples
- `AGGREGATE(9, 6, {1,2,#N/A,4}, 0)` -> `7`

### Error Cases
- Invalid `function_num` or unsupported options should return an argument error.
Error propagation depends on ignore options.

### Notes
Not implemented in IronCalc. Planned as a combined aggregate with compatibility layer.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/AGGREGATE.md


---

## AMORDEGRC — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Calculates depreciation using French accounting with coefficient and full/partial period handling.

### Syntax
- Excel: `AMORDEGRC(cost, date_purchased, first_period, salvage, period, rate, basis)`
- Google Sheets: `AMORDEGRC(cost, date_purchased, first_period, salvage, period, rate, basis)`

### Behavior
- Uses declining balance variant for French tax-style depreciation.
- Requires valid dates and positive cost basis.

### Examples
- `AMORDEGRC(100000, DATE(2024,1,1), 1, 10000, 1, 0.3, 0)` -> depreciation amount

### Error Cases
- Returns an error if depreciation period values are inconsistent or negative.

### Notes
Not implemented in IronCalc. Planned with date-aware accrual logic.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/AMORDEGRC.md


---

## AMORLINC — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Calculates linear depreciation for assets over fixed life cycles.

### Syntax
- Excel: `AMORLINC(cost, date_purchased, first_period, salvage, period, rate, basis)`
- Google Sheets: `AMORLINC(cost, date_purchased, first_period, salvage, period, rate, basis)`

### Behavior
- Uses linear method over useful life.
- Uses dates and basis to compute time fraction for period-level depreciation.

### Examples
- `AMORLINC(100000, DATE(2024,1,1), 1, 10000, 1, 0.2, 0)` -> depreciation amount

### Error Cases
- Invalid life period inputs return errors.

### Notes
Not implemented in IronCalc. Planned as a dedicated depreciation implementation.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/AMORLINC.md


---

## AND — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_and
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/logical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns TRUE if all arguments evaluate to TRUE.

### Syntax
- Excel: `AND(logical1, [logical2], ...)`
- Google Sheets: `AND(logical1, [logical2], ...)`

### Behavior
- All arguments are evaluated as booleans using standard truthy rules.
- If any argument is FALSE, result is FALSE.

### Examples
- `AND(TRUE, 1>0, 2=2)` -> `TRUE`
- `AND(TRUE, FALSE)` -> `FALSE`

### Error Cases
- Errors in any argument propagate unless host-specific short-circuit rules suppress them for non-boolean inputs.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_and`
- File: `base/src/functions/logical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/AND.md


---

## ARABIC — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_arabic
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts a Roman numeral string to an Arabic numeral.

### Syntax
- Excel: `ARABIC(text)`
- Google Sheets: `ARABIC(text)`

### Behavior
- Accepts Roman numeral input and returns decimal value.
- Input is case-insensitive and validated for syntax.

### Examples
- `ARABIC("IV")` -> `4`
- `ARABIC("MCXLV")` -> `1145`

### Error Cases
- Invalid roman text returns error.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_arabic`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ARABIC.md


---

## AREAS — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the number of areas (used in sheet layout context) for a range.

### Syntax
- Excel: `AREAS(reference)`
- Google Sheets: `AREAS(reference)`

### Behavior
- Given a multi-area reference, returns the count of areas.
- Single references return 1.

### Examples
- `AREAS("A1:C3,A5:B7")` -> `2`

### Error Cases
- Invalid reference format returns an argument error.

### Notes
Not implemented in IronCalc. Targeted for area-aware reference validation and API parity.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/AREAS.md


---

## ARRAYFORMULA — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Allows a formula to return an array result that spills across adjacent cells.

### Syntax
- Excel: no direct equivalent; Excel uses dynamic arrays
- Google Sheets: `=ARRAYFORMULA(formula)`

### Behavior
- In Sheets, forces array evaluation over ranges when entering formula in a single cell.
- Requires result expansion behavior for spill arrays.

### Examples
- `=ARRAYFORMULA(A1:A3*2)` -> doubles each value in `A1:A3`

### Error Cases
- Misaligned input/output sizes can produce overflow/spill errors in sheet implementations.

### Notes
Not implemented in IronCalc. Sheets-specific behavior; map to dynamic array engine semantics.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ARRAYFORMULA.md


---

## ARRAY_CONSTRAIN — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Limits array output to a specified row/column size.

### Syntax
- Excel: no direct function (use dynamic array helpers)
- Google Sheets: `ARRAY_CONSTRAIN(array, rows, columns)`

### Behavior
- Returns top-left `rows x columns` slice of an array.
- Excess values are discarded.

### Examples
- `ARRAY_CONSTRAIN({1,2;3,4;5,6},2,1)` -> `{1;3}`

### Error Cases
- Non-positive row/column limits result in an error.

### Notes
Not implemented in IronCalc. Planned as array shaping operator.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ARRAY_CONSTRAIN.md


---

## ASC — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts full-width (double-byte) text to half-width (single-byte) forms.

### Syntax
- Excel: `ASC(text)`
- Google Sheets: `ASC(text)`

### Behavior
- Transforms full-width alphanumeric and punctuation into ASCII-compatible forms.
- Leaves non-applicable characters unchanged.

### Examples
- `ASC("")` -> `ABC`

- Note: Non-ASCII characters omitted. See spec for full text.

### Error Cases
- Returns error for malformed UTF-8-like input sequences.

### Notes
Not implemented in IronCalc. Planned Unicode normalization utility.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ASC.md


---

## ASIN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_asin
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Return the arcsine (inverse sine) of a number in radians.

### Syntax
- Excel: `ASIN(number)`
- Google Sheets: `ASIN(value)`

### Behavior
- Input must be between -1 and 1 (inclusive).
- Result is in radians, range -PI/2 to PI/2.

### Examples
- `ASIN(-0.5)` -> `-0.523598776`

### Error Cases
- Input outside [-1, 1] returns an error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_asin`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ASIN.md


---

## ASINH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_asinh
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Return the inverse hyperbolic sine of a number.

### Syntax
- Excel: `ASINH(number)`
- Google Sheets: `ASINH(value)`

### Behavior
- Accepts any real number.

### Examples
- `ASINH(-2.5)` -> `-1.647231146`
- `ASINH(10)` -> `2.99822295`

### Error Cases
- Non-numeric input returns an error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_asinh`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ASINH.md


---

## ATAN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_atan
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Return the arctangent (inverse tangent) of a number in radians.

### Syntax
- Excel: `ATAN(number)`
- Google Sheets: `ATAN(value)`

### Behavior
- Result is in radians, range -PI/2 to PI/2.

### Examples
- `ATAN(1)` -> `0.785398163`

### Error Cases
- Non-numeric input returns an error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_atan`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ATAN.md


---

## ATAN2 — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_atan2
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Return the arctangent of the specified x- and y-coordinates in radians.

### Syntax
- Excel: `ATAN2(x_num, y_num)`
- Google Sheets: `ATAN2(x, y)`

### Behavior
- Result is in radians, range -PI to PI (excluding -PI).
- If both inputs are 0, returns `#DIV/0!`.

### Examples
- `ATAN2(1,1)` -> `0.785398163`
- `ATAN2(-1,-1)` -> `-2.35619449`

### Error Cases
- If both inputs are 0, returns `#DIV/0!`.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_atan2`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ATAN2.md


---

## ATANH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_atanh
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Return the inverse hyperbolic tangent of a number.

### Syntax
- Excel: `ATANH(number)`
- Google Sheets: `ATANH(value)`

### Behavior
- Input must be between -1 and 1, exclusive.

### Examples
- `ATANH(0.76159416)` -> `1.00000001`

### Error Cases
- Input outside (-1, 1) returns an error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_atanh`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ATANH.md


---

## AVEDEV — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_avedev
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the average of the absolute deviations from the mean.

### Syntax
- Excel: `AVEDEV(number1, [number2], ...)`
- Google Sheets: `AVEDEV(number1, [number2], ...)`

### Behavior
- Ignores non-numeric values based on engine rules.
- Computes absolute difference from arithmetic mean for all included values.

### Examples
- `AVEDEV(1,2,3,4)` -> `1`

### Error Cases
- Fewer than one valid numeric argument yields error.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_avedev`
- File: `base/src/functions/statistical/count_and_average.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/AVEDEV.md


---

## AVERAGE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_average
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns arithmetic mean of numeric values.

### Syntax
- Excel: `AVERAGE(number1, [number2], ...)`
- Google Sheets: `AVERAGE(value1, value2, ...)`

### Behavior
- Averages numeric arguments, ignoring empty cells and non-numeric where defined by host semantics.
- Text numeric coercion may apply when explicit in parser context.

### Examples
- `AVERAGE(1,2,3)` -> `2`

### Error Cases
- All arguments non-numeric and non-coercible return an error.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_average`
- File: `base/src/functions/statistical/count_and_average.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/AVERAGE.md


---

## AVERAGE.WEIGHTED — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns weighted average of values with corresponding weights.

### Syntax
- Excel: `AVERAGE.WEIGHTED(avg_range, weight_range, [additional_pairs...], [ignore_text])`
- Google Sheets: not native; emulate with `SUMPRODUCT/ SUM` patterns

### Behavior
- Each value is multiplied by weight and divided by sum(weights).
- Optional extra ranges and include-logic can alter matching behavior.

### Examples
- `AVERAGE.WEIGHTED({10,20,30},{1,2,3})` -> `23.3333333333`

### Error Cases
- Zero or negative total weight in supported modes may return divide-by-zero style error.

### Notes
Not implemented in IronCalc. Planned as dedicated weighted average function.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/AVERAGE.WEIGHTED.md


---

## AVERAGEA — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_averagea
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns average of arguments, counting TRUE as 1 and FALSE as 0, and including text-numeric per host rules.

### Syntax
- Excel: `AVERAGEA(value1, [value2], ...)`
- Google Sheets: `AVERAGEA(value1, [value2], ...)`

### Behavior
- Includes logical and text values according to host conversion policy.
- Numeric text may be included or excluded based on context.

### Examples
- `AVERAGEA(1, TRUE, FALSE)` -> `1`

### Error Cases
- If no valid operands remain, returns an error.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_averagea`
- File: `base/src/functions/statistical/count_and_average.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/AVERAGEA.md


---

## AVERAGEIF — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_averageif
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/if_ifs.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the average of values that match a condition.

### Syntax
- Excel: `AVERAGEIF(range, criteria, [average_range])`
- Google Sheets: `AVERAGEIF(range, criterion, [average_range])`

### Behavior
- Applies criteria to each item in `range` and averages corresponding items from `average_range` if provided.

### Examples
- `AVERAGEIF(A1:A4, ">10", B1:B4)` -> average of B where A>10

### Error Cases
- Criteria parse failures and mismatched ranges return an error.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_averageif`
- File: `base/src/functions/statistical/if_ifs.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/AVERAGEIF.md


---

## AVERAGEIFS — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_averageifs
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/if_ifs.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the average of values that meet multiple criteria.

### Syntax
- Excel: `AVERAGEIFS(average_range, criteria_range1, criteria1, ...)`
- Google Sheets: `AVERAGEIFS(average_range, criteria_range1, criterion1, ...)`

### Behavior
- Supports multiple criteria pairs.
- All criteria conditions are combined with AND.

### Examples
- `AVERAGEIFS(C1:C4,A1:A4,">10",B1:B4,"A*")`

### Error Cases
- Range length mismatch or malformed criteria returns an error.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_averageifs`
- File: `base/src/functions/statistical/if_ifs.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/AVERAGEIFS.md


---

## BAHTTEXT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts a number to Thai Baht text representation.

### Syntax
- Excel: `BAHTTEXT(number)`
- Google Sheets: `BAHTTEXT(number)`

### Behavior
- Produces Thai currency textual form.
- Useful for checks and invoice-style documents.

### Examples
- `BAHTTEXT(1234.56)` -> Thai text equivalent

### Error Cases
- Non-positive/invalid numeric input may return conversion error.

### Notes
Not implemented in IronCalc. Requires locale-sensitive number-to-text module.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BAHTTEXT.md


---

## BASE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_base
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts a number to text using a chosen base and minimum digits.

### Syntax
- Excel: `BASE(number, radix, [min_length])`
- Google Sheets: `BASE(number, radix, [min_length])`

### Behavior
- Number is converted to base between 2 and 36.
- Optional minimum length pads with leading zeros to requested width.

### Examples
- `BASE(10,2,8)` -> `00001010`

### Error Cases
- Radix out of range or invalid number causes error.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_base`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BASE.md


---

## BESSELI — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: N
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_besseli
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/bessel.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the modified Bessel function I(n, x).

### Syntax
- Excel: `BESSELI(x, order)`
- Google Sheets: `BESSELI(x, order)`

### Behavior
- Computes I-variant Bessel function for scalar x and order.
- Uses numeric evaluation with domain checks used by IronCalc implementation.

### Examples
- `BESSELI(1,0)` -> `1.266065877`

### Error Cases
- Invalid order or domain errors propagate to value errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_besseli`
- File: `base/src/functions/engineering/bessel.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BESSELI.md


---

## BESSELJ — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: N
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_besselj
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/bessel.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the Bessel function of the first kind J(n, x).

### Syntax
- Excel: `BESSELJ(x, order)`
- Google Sheets: `BESSELJ(x, order)`

### Behavior
- Computes Bessel J function for given arguments.
- Returns numeric output for real input ranges used in engineering use-cases.

### Examples
- `BESSELJ(0.5,1)` -> `0.242268457`

### Error Cases
- Invalid numeric domains return argument errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_besselj`
- File: `base/src/functions/engineering/bessel.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BESSELJ.md


---

## BESSELK — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: N
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_besselk
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/bessel.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the modified Bessel function of the second kind K(n, x).

### Syntax
- Excel: `BESSELK(x, order)`
- Google Sheets: `BESSELK(x, order)`

### Behavior
- Computes K-variant Bessel function for specified parameters.

### Examples
- `BESSELK(1,0.5)` -> numeric result

### Error Cases
- Invalid argument combinations may return domain error.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_besselk`
- File: `base/src/functions/engineering/bessel.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BESSELK.md


---

## BESSELY — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: N
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_bessely
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/bessel.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns Bessel function of the second kind of order x and x.

### Syntax
- Excel: `BESSELY(x, order)`
- Google Sheets: `BESSELY(x, order)`

### Behavior
- Computes Y-like behavior for real arguments where defined.
- Useful for wave-like analytic calculations.

### Examples
- `BESSELY(1,0)` -> `0.088256964`

### Error Cases
- Singular/invalid argument combinations produce domain errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_bessely`
- File: `base/src/functions/engineering/bessel.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BESSELY.md


---

## BETA.DIST — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the cumulative beta distribution or density function depending on parameters.

### Syntax
- Excel: `BETA.DIST(x, alpha, beta, cumulative, A, B, [C], [D])`
- Google Sheets: `BETA.DIST(x, alpha, beta, cumulative, lower, upper)`

### Behavior
- Supports cumulative flag and optional bounds.
- For cumulative=TRUE returns CDF, else PDF.

### Examples
- `BETA.DIST(0.5, 2, 3, TRUE, 0, 1)` -> value between 0 and 1

### Error Cases
- Invalid alpha/beta or bounds outside domain return error.

### Notes
Not implemented in IronCalc. Planned through dedicated statistical distribution module.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BETA.DIST.md


---

## BETA.INV — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the inverse of `BETA.DIST` for a given probability.

### Syntax
- Excel: `BETA.INV(probability, alpha, beta, [A], [B])`
- Google Sheets: `BETA.INV(probability, alpha, beta, [A], [B])`

### Behavior
- Inverts cumulative beta distribution.
- Works only on valid cumulative probability in [0,1].

### Examples
- `BETA.INV(0.5, 2, 2, 0, 1)` -> median-like quantile

### Error Cases
- Probability outside [0,1] or invalid parameters returns an error.

### Notes
Not implemented in IronCalc. Planned distribution inversion support.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BETA.INV.md


---

## BETA.INVN — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Alias-style inverse beta distribution function for legacy naming.

### Syntax
- Excel: `BETA.INVN(probability, alpha, beta, A, B)`
- Google Sheets: `BETA.INV(probability, alpha, beta, A, B)`

### Behavior
- Same intent as `BETA.INV` with older naming variant.

### Examples
- `BETA.INVN(0.5, 2, 2, 0, 1)` -> same domain as BETA.INV

### Error Cases
- Same validation rules as `BETA.INV`.

### Notes
Not implemented in IronCalc. Planned compatibility alias implementation.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BETA.INVN.md


---

## BIN2DEC — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_bin2dec
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/number_basis.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts a binary text representation to decimal.

### Syntax
- Excel: `BIN2DEC(number)`
- Google Sheets: `BIN2DEC(number)`

### Behavior
- Accepts up to 10-bit signed twos-complement binary text in many host modes.
- Returns decimal integer string conversion.

- Note: Non-ASCII characters omitted. See spec for full text.

### Examples
- `BIN2DEC("1010")` -> `10`

### Error Cases
- Non-binary characters or out-of-range bit-width return an error.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_bin2dec`
- File: `base/src/functions/engineering/number_basis.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BIN2DEC.md


---

## BIN2HEX — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_bin2hex
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/number_basis.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts a binary number to hexadecimal representation.

### Syntax
- Excel: `BIN2HEX(number, [places])`
- Google Sheets: `BIN2HEX(number, [places])`

### Behavior
- Converts binary text to hex string with optional minimum width.
- Padding/truncation follows host conversion rules.

### Examples
- `BIN2HEX("1111")` -> `F`

### Error Cases
- Invalid binary input or unsupported precision returns error.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_bin2hex`
- File: `base/src/functions/engineering/number_basis.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BIN2HEX.md


---

## BIN2OCT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_bin2oct
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/number_basis.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts a binary value to an octal text representation.

### Syntax
- Excel: `BIN2OCT(number, [places])`
- Google Sheets: `BIN2OCT(number, [places])`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `BIN2OCT(10,4)` -> `12`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_bin2oct`
- File: `base/src/functions/engineering/number_basis.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BIN2OCT.md


---

## BINOM.DIST — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the binomial distribution.

### Syntax
- Excel: `BINOM.DIST(number, trials, probability_s, cumulative)`
- Google Sheets: `BINOM.DIST(number_s, trials, probability_s, cumulative)`

### Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

### Examples
- `BINOM.DIST(1, 2, 0.5, FALSE)` -> `0.5`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Not implemented in IronCalc.

### Code Location
- Handler: `fn_binom_dist`
- File: `base/src/functions/statistical/binom.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BINOM.DIST.md


---

## BINOM.DIST.RANGE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns probability for a range of successes in a binomial experiment.

### Syntax
- Excel: `BINOM.DIST.RANGE(trials, prob_s, number_s, number_s2)`
- Google Sheets: `BINOM.DIST.RANGE(trials, probability_s, successes, [successes2])`

### Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

### Examples
- `BINOM.DIST.RANGE(10, 0.5, 3, 5)` -> `0.5`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Not implemented in IronCalc.

### Code Location
- Handler: `fn_binom_dist_range`
- File: `base/src/functions/statistical/binom.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BINOM.DIST.RANGE.md


---

## BINOM.INV — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns smallest integer satisfying cumulative binomial probability.

### Syntax
- Excel: `BINOM.INV(number, trials, probability_s)`
- Google Sheets: `BINOM.INV(number, trials, probability_s)`

### Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

### Examples
- `BINOM.INV(0.5, 10, 0.5)` -> `5`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Not implemented in IronCalc.

### Code Location
- Handler: `fn_binom_inv`
- File: `base/src/functions/statistical/binom.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BINOM.INV.md


---

## BITAND — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_bitand
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/bit_operations.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns bitwise AND of two integers.

### Syntax
- Excel: `BITAND(number1, number2)`
- Google Sheets: `BITAND(number1, number2)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `BITAND(6,3)` -> `2`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_bitand`
- File: `base/src/functions/engineering/bit_operations.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BITAND.md


---

## BITLSHIFT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_bitlshift
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/bit_operations.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Shifts bits left by a specified amount.

### Syntax
- Excel: `BITLSHIFT(number, shift_amount)`
- Google Sheets: `BITLSHIFT(number, shift)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `BITLSHIFT(5,2)` -> `20`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_bitlshift`
- File: `base/src/functions/engineering/bit_operations.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BITLSHIFT.md


---

## BITOR — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_bitor
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/bit_operations.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns bitwise OR of two integers.

### Syntax
- Excel: `BITOR(number1, number2)`
- Google Sheets: `BITOR(number1, number2)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `BITOR(6,3)` -> `7`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_bitor`
- File: `base/src/functions/engineering/bit_operations.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BITOR.md


---

## BITRSHIFT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_bitrshift
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/bit_operations.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Shifts bits right by a specified amount.

### Syntax
- Excel: `BITRSHIFT(number, shift_amount)`
- Google Sheets: `BITRSHIFT(number, shift)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `BITRSHIFT(20,2)` -> `5`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_bitrshift`
- File: `base/src/functions/engineering/bit_operations.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BITRSHIFT.md


---

## BITXOR — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_bitxor
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/bit_operations.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns bitwise exclusive OR of two integers.

### Syntax
- Excel: `BITXOR(number1, number2)`
- Google Sheets: `BITXOR(number1, number2)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `BITXOR(6,3)` -> `5`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_bitxor`
- File: `base/src/functions/engineering/bit_operations.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BITXOR.md


---

## BYCOL — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Applies a lambda across each column in an array.

### Syntax
- Excel: `BYCOL(array, lambda)`
- Google Sheets: `BYCOL(array, lambda)`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `BYCOL({{1,2},{3,4}}, LAMBDA(c, SUM(c))) -> {3,7}`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_bycol`
- Pseudocode: deterministic parsing, coercion, and computation.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BYCOL.md


---

## BYROW — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Applies a lambda across each row in an array.

### Syntax
- Excel: `BYROW(array, lambda)`
- Google Sheets: `BYROW(array, lambda)`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `BYROW({{1,2},{3,4}}, LAMBDA(r, SUM(r))) -> {3,7}`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_byrow`
- Pseudocode: deterministic parsing, coercion, and computation.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/BYROW.md


---

## CALL — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Calls an external routine in legacy workbook-compatible models.

### Syntax
- Excel: `CALL(program, arg1, [arg2], ...)`
- Google Sheets: not supported natively

### Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

### Examples
- `CALL("lib", 1, 2)` -> environment-specific

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CALL.md


---

## CEILING — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_ceiling
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Rounds a number up to nearest multiple of significance.

### Syntax
- Excel: `CEILING(number, significance)`
- Google Sheets: `CEILING(number, significance)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `CEILING(2.3,1)` -> `3`

### Error Cases
- Returns `#VALUE!` when significance is zero or invalid.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_ceiling`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CEILING.md


---

## CEILING.MATH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Rounds up toward zero-aware ceiling behavior with optional mode.

### Syntax
- Excel: `CEILING.MATH(number, [significance], [mode])`
- Google Sheets: `CEILING.MATH(number, [significance], [mode])`

### Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

### Examples
- `CEILING.MATH(-2.3, 0.5)` -> `-2`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Not implemented in IronCalc.

### Code Location
- Handler: `fn_ceiling_math`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CEILING.MATH.md


---

## CEILING.PRECISE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Rounds a number up to nearest multiple of significance, always positive direction.

### Syntax
- Excel: `CEILING.PRECISE(number, [significance])`
- Google Sheets: `CEILING.PRECISE(number, [significance])`

### Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

### Examples
- `CEILING.PRECISE(-2.3)` -> `-2`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Not implemented in IronCalc.

### Code Location
- Handler: `fn_ceiling_precise`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CEILING.PRECISE.md


---

## CELL — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_cell
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns metadata for a cell using a type keyword.

### Syntax
- Excel: `CELL(type_num, [reference])`
- Google Sheets: `CELL(info_type, reference)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `CELL("type", A1)` -> `"v"`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_cell`
- File: `base/src/functions/information.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CELL.md


---

## CHAR — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the character represented by a numeric code point.

### Syntax
- Excel: `CHAR(number)`
- Google Sheets: `CHAR(number)`

### Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

### Examples
- `CHAR(65)` -> `A`

### Error Cases
- Invalid numeric input outside supported codepoint range returns an error.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CHAR.md


---

## CHISQ.DIST — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the chi-square distribution value.

### Syntax
- Excel: `CHISQ.DIST(x, degrees_freedom, cumulative)`
- Google Sheets: `CHISQ.DIST(x, degrees_freedom, cumulative)`

### Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

### Examples
- `CHISQ.DIST(1, 2, TRUE)` -> `0.3935...`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Not implemented in IronCalc.

### Code Location
- Handler: `fn_chisq_dist`
- File: `base/src/functions/statistical/chisq.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CHISQ.DIST.md


---

## CHISQ.DIST.RT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns right-tail probability of chi-square.

### Syntax
- Excel: `CHISQ.DIST.RT(x, degrees_freedom)`
- Google Sheets: `CHISQ.DIST.RT(x, degrees_freedom)`

### Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

### Examples
- `CHISQ.DIST.RT(1, 2)` -> `0.6065...`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Not implemented in IronCalc.

### Code Location
- Handler: `fn_chisq_dist_rt`
- File: `base/src/functions/statistical/chisq.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CHISQ.DIST.RT.md


---

## CHISQ.INV — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns inverse chi-square for a given probability.

### Syntax
- Excel: `CHISQ.INV(probability, degrees_freedom)`
- Google Sheets: `CHISQ.INV(probability, degrees_freedom)`

### Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

### Examples
- `CHISQ.INV(0.95, 2)` -> numeric

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Not implemented in IronCalc.

### Code Location
- Handler: `fn_chisq_inv`
- File: `base/src/functions/statistical/chisq.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CHISQ.INV.md


---

## CHISQ.INV.RT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns inverse right-tail chi-square value.

### Syntax
- Excel: `CHISQ.INV.RT(probability, degrees_freedom)`
- Google Sheets: `CHISQ.INV.RT(probability, degrees_freedom)`

### Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

### Examples
- `CHISQ.INV.RT(0.05, 2)` -> numeric

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Not implemented in IronCalc.

### Code Location
- Handler: `fn_chisq_inv_rt`
- File: `base/src/functions/statistical/chisq.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CHISQ.INV.RT.md


---

## CHISQ.TEST — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns chi-square goodness-of-fit test statistic/result.

### Syntax
- Excel: `CHISQ.TEST(actual_range, expected_range)`
- Google Sheets: `CHISQ.TEST(actual_range, expected_range)`

### Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

### Examples
- `CHISQ.TEST({1,2;3,4},{2,2;2,4})` -> `0.123`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Not implemented in IronCalc.

### Code Location
- Handler: `fn_chisq_test`
- File: `base/src/functions/statistical/chisq.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CHISQ.TEST.md


---

## CHOOSE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_choose
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns a value from a list by index.

### Syntax
- Excel: `CHOOSE(index_num, value1, [value2], ...)`
- Google Sheets: `CHOOSE(index, value1, [value2], ...)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `CHOOSE(2,"A","B","C")` -> `B`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_choose`
- File: `base/src/functions/lookup_and_reference.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CHOOSE.md


---

## CHOOSECOLS — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Returns selected columns from an array.

### Syntax
- Excel: `CHOOSECOLS(array, col_num1, ...)`
- Google Sheets: `CHOOSECOLS(array, col_num1, ...)`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `CHOOSECOLS({{1,2,3},{4,5,6}},2) -> {2,5}`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_choosecols`
- Pseudocode: deterministic parsing, coercion, and computation.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CHOOSECOLS.md


---

## CHOOSEROWS — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Returns selected rows from an array.

### Syntax
- Excel: `CHOOSEROWS(array, row_num1, ...)`
- Google Sheets: `CHOOSEROWS(array, row_num1, ...)`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `CHOOSEROWS({{1,2,3},{4,5,6}},2) -> {4,5,6}`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_chooserows`
- Pseudocode: deterministic parsing, coercion, and computation.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CHOOSEROWS.md


---

## CLEAN — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Removes non-printable characters from text.

### Syntax
- Excel: `CLEAN(text)`
- Google Sheets: `CLEAN(text)`

### Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

### Examples
- `CLEAN("a
")` -> `a`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CLEAN.md


---

## CODE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns numeric code for the first character in text.

### Syntax
- Excel: `CODE(text)`
- Google Sheets: `CODE(text)`

### Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

### Examples
- `CODE("A")` -> `65`

### Error Cases
- Empty input or invalid UTF sequence returns an error.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CODE.md


---

## COLUMN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_column
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns column number of a reference.

### Syntax
- Excel: `COLUMN([reference])`
- Google Sheets: `COLUMN([reference])`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `COLUMN(B5)` -> `2`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_column`
- File: `base/src/functions/lookup_and_reference.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COLUMN.md


---

## COLUMNS — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_columns
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns count of columns in array or reference.

### Syntax
- Excel: `COLUMNS(array)`
- Google Sheets: `COLUMNS(array)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `COLUMNS({1,2,3;4,5,6})` -> `3`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_columns`
- File: `base/src/functions/lookup_and_reference.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COLUMNS.md


---

## COMBIN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_combin
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns number of combinations (n choose k).

### Syntax
- Excel: `COMBIN(number, number_chosen)`
- Google Sheets: `COMBIN(number, number_chosen)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `COMBIN(5,2)` -> `10`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_combin`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COMBIN.md


---

## COMBINA — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_combina
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns combinations with repetition.

### Syntax
- Excel: `COMBINA(number, number_chosen)`
- Google Sheets: `COMBINA(number, number_chosen)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `COMBINA(5,2)` -> `15`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_combina`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COMBINA.md


---

## COMPLEX — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_complex
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Constructs a complex number from real and imaginary parts.

### Syntax
- Excel: `COMPLEX(real_num, i_num, [suffix])`
- Google Sheets: `COMPLEX(real_num, i_num, [suffix])`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `COMPLEX(3,4)` -> `3+4i`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_complex`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COMPLEX.md


---

## CONCAT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_concat
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Joins text strings without separators.

### Syntax
- Excel: `CONCAT(text1, [text2], ...)`
- Google Sheets: `CONCAT(text1, [text2], ...)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `CONCAT("A","B")` -> `AB`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_concat`
- File: `base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CONCAT.md


---

## CONCATENATE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_concatenate
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Joins text arguments into a single text.

### Syntax
- Excel: `CONCATENATE(text1, [text2], ...)`
- Google Sheets: `CONCATENATE(text1, [text2], ...)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `CONCATENATE("A","B")` -> `AB`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_concatenate`
- File: `base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CONCATENATE.md


---

## CONFIDENCE.NORM — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns confidence interval half-width for normal distribution.

### Syntax
- Excel: `CONFIDENCE.NORM(alpha, standard_dev, size)`
- Google Sheets: `CONFIDENCE.NORM(alpha, standard_dev, size)`

### Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

### Examples
- `CONFIDENCE.NORM(0.05, 1.2, 10)` -> numeric

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Not implemented in IronCalc.

### Code Location
- Handler: `fn_confidence_norm`
- File: `base/src/functions/statistical/normal.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CONFIDENCE.NORM.md


---

## CONFIDENCE.T — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns confidence interval half-width for t distribution.

### Syntax
- Excel: `CONFIDENCE.T(alpha, standard_dev, size)`
- Google Sheets: `CONFIDENCE.T(alpha, standard_dev, size)`

### Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

### Examples
- `CONFIDENCE.T(0.05, 1.2, 10)` -> numeric

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Not implemented in IronCalc.

### Code Location
- Handler: `fn_confidence_t`
- File: `base/src/functions/statistical/normal.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CONFIDENCE.T.md


---

## CONVERT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_convert
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/convert.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts numeric value between unit systems.

### Syntax
- Excel: `CONVERT(number, from_unit, to_unit)`
- Google Sheets: `CONVERT(number, from_unit, to_unit)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `CONVERT(1, "m", "cm")` -> `100`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_convert`
- File: `base/src/functions/engineering/convert.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CONVERT.md


---

## COPILOT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Reserved/housekeeping function for assistant integrations in some editions.

### Syntax
- Excel: no equivalent
- Google Sheets: no equivalent

### Behavior
- Not implemented in IronCalc yet; behavior must match Excel and Google Sheets parity expectations.
- Argument validation and numeric/text coercion should mirror host behavior.

### Examples
- `COPILOT("status")` -> host-defined or error

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COPILOT.md


---

## CORREL — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_correl
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/correl.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns Pearson correlation coefficient.

### Syntax
- Excel: `CORREL(array1, array2)`
- Google Sheets: `CORREL(array1, array2)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `CORREL({1,2,3},{2,4,6})` -> `1`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_correl`
- File: `base/src/functions/statistical/correl.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CORREL.md


---

## COS — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_cos
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns cosine of an angle in radians.

### Syntax
- Excel: `COS(number)`
- Google Sheets: `COS(number)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `COS(0)` -> `1`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_cos`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COS.md


---

## COSH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_cosh
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns hyperbolic cosine.

### Syntax
- Excel: `COSH(number)`
- Google Sheets: `COSH(number)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `COSH(0)` -> `1`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_cosh`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COSH.md


---

## COT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_cot
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns cotangent of an angle in radians.

### Syntax
- Excel: `COT(number)`
- Google Sheets: `COT(number)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `COT(1)` -> `0.6420926159`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_cot`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COT.md


---

## COTH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_coth
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns hyperbolic cotangent.

### Syntax
- Excel: `COTH(number)`
- Google Sheets: `COTH(number)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `COTH(1)` -> `1.3130352855`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_coth`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COTH.md


---

## COUNT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_count
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Counts numeric entries in arguments.

### Syntax
- Excel: `COUNT(value1, [value2], ...)`
- Google Sheets: `COUNT(value1, [value2], ...)`

### Behavior
- Inputs are validated against expected arity and type requirements.
- Computation follows IronCalc semantics for determinism and error propagation.

### Examples
- `COUNT(1,2,"3",FALSE)` -> `2`

### Error Cases
- Invalid argument count or type yields an error.
- Domain violations return host-style function errors.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_count`
- File: `base/src/functions/statistical/count_and_average.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COUNT.md


---

## COUNTA — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_counta
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns count of non-empty values in references.

### Syntax
- Excel: `COUNTA(value1, [value2], ...)`
- Google Sheets: `COUNTA(value1, [value2], ...)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `COUNTA(1, "x", FALSE, "") -> 3`

### Error Cases
- Empty argument list returns 0.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_counta`
- File: `base/src/functions/statistical/count_and_average.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COUNTA.md


---

## COUNTBLANK — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_countblank
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns count of empty cells in a range.

### Syntax
- Excel: `COUNTBLANK(range)`
- Google Sheets: `COUNTBLANK(range)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `COUNTBLANK({"A",, "", "B"}) -> 2`

### Error Cases
- Non-range inputs may return argument error in strict mode.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_countblank`
- File: `base/src/functions/statistical/count_and_average.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COUNTBLANK.md


---

## COUNTIF — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_countif
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/if_ifs.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Counts cells that meet a single criteria.

### Syntax
- Excel: `COUNTIF(range, criteria)`
- Google Sheets: `COUNTIF(range, criterion)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `COUNTIF({1,2,3}, 2) -> 1`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_countif`
- File: `base/src/functions/statistical/if_ifs.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COUNTIF.md


---

## COUNTIFS — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_countifs
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/if_ifs.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Counts cells that meet multiple criteria.

### Syntax
- Excel: `COUNTIFS(criteria_range1, criteria1, ...)`
- Google Sheets: `COUNTIFS(criteria_range1, criteria1, ...)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `COUNTIFS({1,2,3},{">1"}, {"A","B","A"}) -> 0`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_countifs`
- File: `base/src/functions/statistical/if_ifs.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COUNTIFS.md


---

## COUNTUNIQUE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Counts unique values in supplied arguments.

### Syntax
- Excel: `COUNTUNIQUE(value1, [value2], ...)`
- Google Sheets: `COUNTUNIQUE(value1, [value2], ...)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.
- - Uniqueness determined by normalized text/value comparison.

### Examples
- `COUNTUNIQUE(1,1,2,3) -> 3`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COUNTUNIQUE.md


---

## COUPDAYBS — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns coupon days from settlement to next interest period start.

### Syntax
- Excel: `COUPDAYBS(settlement, maturity, frequency, [basis])`
- Google Sheets: `COUPDAYBS(settlement, maturity, frequency, [basis])`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.
- - Counts coupon interval length in fractional days as documented by host.

### Examples
- `COUPDAYBS(45234, 45600, 2, 0) -> integer`

### Error Cases
- Settlement after maturity returns error.
- Invalid `frequency` returns error.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COUPDAYBS.md


---

## COUPDAYS — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns number of days from settlement to maturity based on frequency and basis.

### Syntax
- Excel: `COUPDAYS(settlement, maturity, frequency, [basis])`
- Google Sheets: `COUPDAYS(settlement, maturity, frequency, [basis])`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.
- - Counts coupon period duration with basis-dependent day-count rules.

### Examples
- `COUPDAYS(45234, 45600, 2, 0) -> integer`

### Error Cases
- Settlement after maturity returns error.
- Invalid `basis` returns error.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COUPDAYS.md


---

## COUPDAYSNC — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns number of days from settlement to next coupon date.

### Syntax
- Excel: `COUPDAYSNC(settlement, maturity, frequency, [basis])`
- Google Sheets: `COUPDAYSNC(settlement, maturity, frequency, [basis])`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `COUPDAYSNC(45234, 45600, 2, 0) -> integer`

### Error Cases
- Invalid schedule results return error.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COUPDAYSNC.md


---

## COUPNCD — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns next coupon date after settlement date.

### Syntax
- Excel: `COUPNCD(settlement, maturity, frequency, [basis])`
- Google Sheets: `COUPNCD(settlement, maturity, frequency, [basis])`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `COUPNCD(45234, 45600, 2, 0) -> date`

### Error Cases
- Missing schedule yields error.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COUPNCD.md


---

## COUPNUM — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns number of coupon payments between dates.

### Syntax
- Excel: `COUPNUM(settlement, maturity, frequency, [basis])`
- Google Sheets: `COUPNUM(settlement, maturity, frequency, [basis])`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `COUPNUM(45234, 45600, 2, 0) -> 4`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COUPNUM.md


---

## COUPPCD — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns previous coupon date before settlement.

### Syntax
- Excel: `COUPPCD(settlement, maturity, frequency, [basis])`
- Google Sheets: `COUPPCD(settlement, maturity, frequency, [basis])`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `COUPPCD(45234, 45600, 2, 0) -> date`

### Error Cases
- Missing schedule yields error.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COUPPCD.md


---

## COVARIANCE.P — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns population covariance.

### Syntax
- Excel: `COVARIANCE.P(array1, array2)`
- Google Sheets: `COVARIANCE.P(array1, array2)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `COVARIANCE.P({1,2,3},{2,4,6}) -> 1`

### Error Cases
- Non-numeric values are ignored where required or return error based on host mode.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_covariance_p`
- File: `base/src/functions/statistical/covariance.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COVARIANCE.P.md


---

## COVARIANCE.S — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns sample covariance.

### Syntax
- Excel: `COVARIANCE.S(array1, array2)`
- Google Sheets: `COVARIANCE.S(array1, array2)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `COVARIANCE.S({1,2,3},{2,4,6}) -> 1`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_covariance_s`
- File: `base/src/functions/statistical/covariance.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/COVARIANCE.S.md


---

## CRITBINOM — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns threshold value for binomial distribution by cumulative probability.

### Syntax
- Excel: `CRITBINOM(number_s, trials, probability_s)`
- Google Sheets: `CRITBINOM(number_s, trials, probability_s)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `CRITBINOM(0.75, 10, 0.5) -> 6`

### Error Cases
- If probability outside 0-1, returns error.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CRITBINOM.md


---

## CSC — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_csc
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns cosecant of radian angle.

### Syntax
- Excel: `CSC(number)`
- Google Sheets: `CSC(number)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `CSC(0.5) -> 2.085829642`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_csc`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CSC.md


---

## CSCH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_csch
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns hyperbolic cosecant of a value.

### Syntax
- Excel: `CSCH(number)`
- Google Sheets: `CSCH(number)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `CSCH(1) -> 0.850918128`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_csch`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CSCH.md


---

## CUBEKPIMEMBER — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns a cube key member for OLAP metadata.

### Syntax
- Excel: `CUBEKPIMEMBER(connection, dimension_expression, hierarchy_unique_name, [property], [caption], [set_expression])`
- Google Sheets: no direct equivalent

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `CUBEKPIMEMBER("conn","dim","name") -> value`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CUBEKPIMEMBER.md


---

## CUBEMEMBER — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns member from cube hierarchy.

### Syntax
- Excel: `CUBEMEMBER(connection, member_expression, [caption], [unique_name], [property])`
- Google Sheets: no direct equivalent

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `CUBEMEMBER("conn","[Geography].[Country].[USA]") -> member`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CUBEMEMBER.md


---

## CUBEMEMBERPROPERTY — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns cube member metadata property.

### Syntax
- Excel: `CUBEMEMBERPROPERTY(cube_name, member_expression, property_name)`
- Google Sheets: no direct equivalent

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `CUBEMEMBERPROPERTY("conn","[Member]","CAPTION") -> text`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CUBEMEMBERPROPERTY.md


---

## CUBERANKEDMEMBER — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns ranked member from a cube set.

### Syntax
- Excel: `CUBERANKEDMEMBER(connection, set_expression, rank, [order], [tie]...)`
- Google Sheets: no direct equivalent

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.
- - Relies on cube engine metadata and ordering semantics.

### Examples
- `CUBERANKEDMEMBER("conn","{set}",1) -> member`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CUBERANKEDMEMBER.md


---

## CUBESET — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns a cube set object.

### Syntax
- Excel: `CUBESET(connection, set_expression, [caption], [sort_order])`
- Google Sheets: no direct equivalent

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `CUBESET("conn","{set expr}") -> set`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CUBESET.md


---

## CUBESETCOUNT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns count of members in cube set.

### Syntax
- Excel: `CUBESETCOUNT(cube_set)`
- Google Sheets: no direct equivalent

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `CUBESETCOUNT({set}) -> 2`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CUBESETCOUNT.md


---

## CUBEVALUE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns value from a cube expression.

### Syntax
- Excel: `CUBEVALUE(connection, member1, member2, ...)`
- Google Sheets: no direct equivalent

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `CUBEVALUE("conn","[Measure]","[Member]") -> 10`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CUBEVALUE.md


---

## CUMIPMT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_cumipmt
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns cumulative interest paid between periods.

### Syntax
- Excel: `CUMIPMT(rate, nper, pv, start_period, end_period, type)`
- Google Sheets: `CUMIPMT(rate, nper, pv, start_period, end_period, type)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `CUMIPMT(0.05, 12, 10000, 1, 3, 0) -> -1234`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_cumipmt`
- File: `base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CUMIPMT.md


---

## CUMPRINC — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_cumprinc
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns cumulative principal paid between periods.

### Syntax
- Excel: `CUMPRINC(rate, nper, pv, start_period, end_period, type)`
- Google Sheets: `CUMPRINC(rate, nper, pv, start_period, end_period, type)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `CUMPRINC(0.05, 12, 10000, 1, 3, 0) -> 500`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_cumprinc`
- File: `base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/CUMPRINC.md


---

## DATE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_date
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns serial date from year month day values.

### Syntax
- Excel: `DATE(year, month, day)`
- Google Sheets: `DATE(year, month, day)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.

### Examples
- `DATE(2026, 2, 19) -> serial date`

### Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible date arithmetic.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_date`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DATE.md


---

## DATEDIF — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_datedif
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns difference between two dates by unit.

### Syntax
- Excel: `DATEDIF(start_date, end_date, unit)`
- Google Sheets: `DATEDIF(start_date, end_date, unit)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.

### Examples
- `DATEDIF("2026-01-01","2026-12-31","y") -> 0`

### Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible date arithmetic.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_datedif`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DATEDIF.md


---

## DATEVALUE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_datevalue
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts text date to date serial.

### Syntax
- Excel: `DATEVALUE(date_text)`
- Google Sheets: `DATEVALUE(date_text)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.

### Examples
- `DATEVALUE("2026-02-19") -> serial date`

### Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible date arithmetic.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_datevalue`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DATEVALUE.md


---

## DAVERAGE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_daverage
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/database.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns average from records matching database criteria.

### Syntax
- Excel: `DAVERAGE(database, field, criteria)`
- Google Sheets: `DAVERAGE(database, field, criteria)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `DAVERAGE(database, "Amount", criteria) -> 120`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_daverage`
- File: `base/src/functions/database.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DAVERAGE.md


---

## DAY — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_day
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns day-of-month from date input.

### Syntax
- Excel: `DAY(serial_number)`
- Google Sheets: `DAY(date)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `DAY(DATE(2026,3,15)) -> 15`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_day`
- File: `base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DAY.md


---

## DAYS — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_days
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns difference in days between two dates.

### Syntax
- Excel: `DAYS(end_date, start_date)`
- Google Sheets: `DAYS(end_date, start_date)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `DAYS(DATE(2026,3,1), DATE(2026,1,1)) -> 59`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_days`
- File: `base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DAYS.md


---

## DAYS360 — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_days360
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns day count using 360-day year convention.

### Syntax
- Excel: `DAYS360(start_date, end_date, [method])`
- Google Sheets: `DAYS360(start_date, end_date, [method])`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `DAYS360(DATE(2026,1,1), DATE(2026,12,31), FALSE) -> 360`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_days360`
- File: `base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DAYS360.md


---

## DB — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_db
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns fixed declining balance depreciation for period.

### Syntax
- Excel: `DB(cost, salvage, life, period, [month])`
- Google Sheets: `DB(cost, salvage, life, period, [month])`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.
- - Uses declining balance and periodic schedule assumptions.

### Examples
- `DB(10000,1000,5,1) -> 1860`

### Error Cases
- Invalid `life` or `period` returns error.
- Cost values must be non-negative.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_db`
- File: `base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DB.md


---

## DBCS — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts single-byte text to double-byte string.

### Syntax
- Excel: `DBCS(text)`
- Google Sheets: `DBCS(text)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `DBCS("ABC") -> fullwidth-ABC`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/<category>.rs`
- Handler: `fn_...` (to be added)

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DBCS.md


---

## DCOUNT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_dcount
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/database.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Counts numbers in database field meeting criteria.

### Syntax
- Excel: `DCOUNT(database, field, criteria)`
- Google Sheets: `DCOUNT(database, field, criteria)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `DCOUNT(database, "Qty", criteria) -> 3`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_dcount`
- File: `base/src/functions/database.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DCOUNT.md


---

## DCOUNTA — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_dcounta
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/database.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Counts non-empty values in database field meeting criteria.

### Syntax
- Excel: `DCOUNTA(database, field, criteria)`
- Google Sheets: `DCOUNTA(database, field, criteria)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `DCOUNTA(database, "Qty", criteria) -> 5`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_dcounta`
- File: `base/src/functions/database.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DCOUNTA.md


---

## DDB — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_ddb
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns double declining balance depreciation for period.

### Syntax
- Excel: `DDB(cost, salvage, life, period, [factor])`
- Google Sheets: `DDB(cost, salvage, life, period, [factor])`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `DDB(10000,1000,5,1) -> 2000`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_ddb`
- File: `base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DDB.md


---

## DEC2BIN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_dec2bin
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/number_basis.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts decimal to binary text.

### Syntax
- Excel: `DEC2BIN(number, [places])`
- Google Sheets: `DEC2BIN(number, [places])`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `DEC2BIN(255, 8) -> 11111111`

### Error Cases
- Number out of range returns error.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_dec2bin`
- File: `base/src/functions/engineering/number_basis.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DEC2BIN.md


---

## DEC2HEX — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_dec2hex
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/number_basis.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts decimal to hexadecimal text.

### Syntax
- Excel: `DEC2HEX(number, [places])`
- Google Sheets: `DEC2HEX(number, [places])`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `DEC2HEX(255,2) -> FF`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_dec2hex`
- File: `base/src/functions/engineering/number_basis.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DEC2HEX.md


---

## DEC2OCT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_dec2oct
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/number_basis.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts decimal to octal text.

### Syntax
- Excel: `DEC2OCT(number, [places])`
- Google Sheets: `DEC2OCT(number, [places])`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `DEC2OCT(8,2) -> 10`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_dec2oct`
- File: `base/src/functions/engineering/number_basis.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DEC2OCT.md


---

## DECIMAL — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_decimal
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts base-N text into decimal number.

### Syntax
- Excel: `DECIMAL(text, radix)`
- Google Sheets: `DECIMAL(number, radix)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `DECIMAL("FF", 16) -> 255`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_decimal`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DECIMAL.md


---

## DEGREES — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_degrees
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts radians to degrees.

### Syntax
- Excel: `DEGREES(angle)`
- Google Sheets: `DEGREES(angle)`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `DEGREES(PI()) -> 180`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_degrees`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DEGREES.md


---

## DELTA — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_delta
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/misc.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns 1 when two values equal else 0.

### Syntax
- Excel: `DELTA(number1, [number2])`
- Google Sheets: `DELTA(number1, [number2])`

### Behavior
- Input values follow host-compatible coercion rules for each argument.
- Function output is deterministic for identical inputs.

### Examples
- `DELTA(10,10) -> 1`

### Error Cases
- Invalid argument count or malformed arguments return a calculation error.
- Domain violations return errors compatible with host semantics.

### Notes
Implemented in IronCalc.

### Code Location
- Handler: `fn_delta`
- File: `base/src/functions/engineering/misc.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DELTA.md


---

## DETECTLANGUAGE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Detects the probable language of text and returns a language code.

### Syntax
- Excel: `DETECTLANGUAGE(text)`
- Google Sheets: `DETECTLANGUAGE(text)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `DETECTLANGUAGE("bonjour") -> "fr"`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/information.rs`
- Pseudocode:
  1. `determine language code from text and return locale identifier`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DETECTLANGUAGE.md


---

## DEVSQ — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_devsq
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/devsq.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the sum of squares of deviations from the mean.

### Syntax
- Excel: `DEVSQ(number1, [number2], ...)`
- Google Sheets: `DEVSQ(number1, [number2], ...)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `DEVSQ(2,4,4,4,5,5,7,9) -> 32`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_devsq`
- File: `base/src/functions/statistical/devsq.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DEVSQ.md


---

## DGET — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_dget
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/database.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns one matching value from a database-like table filtered by criteria.

### Syntax
- Excel: `DGET(database, field, criteria)`
- Google Sheets: `DGET(database, field, criteria)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `DGET({"A1:A4"},"field","criteria") -> 100`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_dget`
- File: `base/src/functions/database.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DGET.md


---

## DISC — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the discount for a security at settlement and maturity.

### Syntax
- Excel: `DISC(settlement, maturity, pr, redemption, [basis])`
- Google Sheets: `DISC(settlement, maturity, pr, redemption, [basis])`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `DISC("01/01/2026", "01/01/2027", 95, 100, 0) -> 0.0526`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/financial.rs`
- Pseudocode:
  1. `derive discount = (redemption - pr) / (maturity - settlement) * basisAdjusted`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DISC.md


---

## DIVIDE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Divides one number by another.

### Syntax
- Excel: `DIVIDE(dividend, divisor)`
- Google Sheets: `DIVIDE(dividend, divisor)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `DIVIDE(10,4) -> 2.5`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/mathematical.rs`
- Pseudocode:
  1. `if divisor is 0, return #DIV/0!, else numerator/denominator with exact IEEE checks`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DIVIDE.md


---

## DMAX — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_dmax
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/database.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the maximum value in a database field matching criteria.

### Syntax
- Excel: `DMAX(database, field, criteria)`
- Google Sheets: `DMAX(database, field, criteria)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `DMAX(db, "Sales", criteria) -> 45000`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_dmax`
- File: `base/src/functions/database.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DMAX.md


---

## DMIN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_dmin
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/database.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the minimum value in a database field matching criteria.

### Syntax
- Excel: `DMIN(database, field, criteria)`
- Google Sheets: `DMIN(database, field, criteria)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `DMIN(db, "Sales", criteria) -> 12000`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_dmin`
- File: `base/src/functions/database.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DMIN.md


---

## DOLLAR — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts a number to currency-format text with a fixed decimal count.

### Syntax
- Excel: `DOLLAR(number, [decimals])`
- Google Sheets: `DOLLAR(number, [decimals])`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `DOLLAR(1234.567, 2) -> "$1,234.57"`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/text.rs`
- Pseudocode:
  1. `format number with currency symbol, decimals, negatives and locale`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DOLLAR.md


---

## DOLLARDE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_dollarde
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts a fractional dollar price to decimal representation.

### Syntax
- Excel: `DOLLARDE(fractional_dollar, fraction)`
- Google Sheets: `DOLLARDE(fractional_dollar, fraction)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `DOLLARDE(1,8) -> 1.375`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_dollarde`
- File: `base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DOLLARDE.md


---

## DOLLARFR — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_dollarfr
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts a decimal number to dollar-fractions format.

### Syntax
- Excel: `DOLLARFR(decimal_dollar, fraction)`
- Google Sheets: `DOLLARFR(decimal_dollar, fraction)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `DOLLARFR(1.5,16) -> 1.8`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_dollarfr`
- File: `base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DOLLARFR.md


---

## DPRODUCT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_dproduct
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/database.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Multiplies selected database field values after applying criteria.

### Syntax
- Excel: `DPRODUCT(database, field, criteria)`
- Google Sheets: `DPRODUCT(database, field, criteria)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `DPRODUCT(db, "Qty", criteria) -> 240`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_dproduct`
- File: `base/src/functions/database.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DPRODUCT.md


---

## DROP — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Returns a range/array with rows and/or columns removed.

### Syntax
- Excel: `DROP(array, rows, [columns])`
- Google Sheets: `DROP(array, rows, [columns])`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `DROP({1,2,3,4}, 1, 1) -> {2,3}`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Pseudocode:
  1. `slice array after removing requested rows/cols and fill truncation rules`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DROP.md


---

## DSTDEV — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_dstdev
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/database.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the sample standard deviation of database values matching criteria.

### Syntax
- Excel: `DSTDEV(database, field, criteria)`
- Google Sheets: `DSTDEV(database, field, criteria)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `DSTDEV(db, "Qty", criteria) -> 12.34`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_dstdev`
- File: `base/src/functions/database.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DSTDEV.md


---

## DSTDEVP — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_dstdevp
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/database.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the population standard deviation of database values matching criteria.

### Syntax
- Excel: `DSTDEVP(database, field, criteria)`
- Google Sheets: `DSTDEVP(database, field, criteria)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `DSTDEVP(db, "Qty", criteria) -> 10.01`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_dstdevp`
- File: `base/src/functions/database.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DSTDEVP.md


---

## DSUM — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_dsum
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/database.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Sums database field values matching criteria.

### Syntax
- Excel: `DSUM(database, field, criteria)`
- Google Sheets: `DSUM(database, field, criteria)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `DSUM(db, "Qty", criteria) -> 720`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_dsum`
- File: `base/src/functions/database.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DSUM.md


---

## DURATION — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns a bond duration-style time-weighted metric.

### Syntax
- Excel: `DURATION(settlement, maturity, coupon, yld, frequency, [basis])`
- Google Sheets: `DURATION(settlement, maturity, coupon, yld, frequency, [basis])`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `DURATION("01/01/2026", "01/01/2027", 0.05, 0.045, 1, 0) -> 7`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/financial.rs`
- Pseudocode:
  1. `compute duration formula using settlement/maturity/coupon/yield/frequency/basis`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DURATION.md


---

## DVAR — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_dvar
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/database.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the sample variance of database values matching criteria.

### Syntax
- Excel: `DVAR(database, field, criteria)`
- Google Sheets: `DVAR(database, field, criteria)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `DVAR(db, "Score", criteria) -> 48.2`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_dvar`
- File: `base/src/functions/database.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DVAR.md


---

## DVARP — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_dvarp
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/database.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the population variance of database values matching criteria.

### Syntax
- Excel: `DVARP(database, field, criteria)`
- Google Sheets: `DVARP(database, field, criteria)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `DVARP(db, "Score", criteria) -> 41.8`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_dvarp`
- File: `base/src/functions/database.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/DVARP.md


---

## EDATE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_edate
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns a date shifted by a number of months.

### Syntax
- Excel: `EDATE(start_date, months)`
- Google Sheets: `EDATE(start_date, months)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `EDATE("1/31/2026", 2) -> "3/31/2026"`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_edate`
- File: `base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/EDATE.md


---

## EFFECT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_effect
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts nominal interest rate to effective annual rate.

### Syntax
- Excel: `EFFECT(nominal_rate, npery)`
- Google Sheets: `EFFECT(nominal_rate, npery)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `EFFECT(0.05, 12) -> 0.0512`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_effect`
- File: `base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/EFFECT.md


---

## ENCODEURL — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Percent-encodes a text string for safe URL use.

### Syntax
- Excel: `ENCODEURL(url)`
- Google Sheets: `ENCODEURL(url)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `ENCODEURL("A B") -> "A%20B"`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/text.rs`
- Pseudocode:
  1. `percent-encode characters outside RFC3986 unreserved set`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ENCODEURL.md


---

## EOMONTH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_eomonth
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the last day of the month offset from a start date.

### Syntax
- Excel: `EOMONTH(start_date, months)`
- Google Sheets: `EOMONTH(start_date, months)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `EOMONTH("2/1/2026", 1) -> "3/31/2026"`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_eomonth`
- File: `base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/EOMONTH.md


---

## EPOCHTODATE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts Unix epoch seconds to a serial date value.

### Syntax
- Excel: `EPOCHTODATE(epoch, [unit])`
- Google Sheets: `EPOCHTODATE(epoch, [unit])`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `EPOCHTODATE(1700000000) -> 45146`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/date_and_time.rs`
- Pseudocode:
  1. `convert Unix seconds to date serial with timezone-neutral baseline`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/EPOCHTODATE.md


---

## EQ — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns TRUE when two values are equal.

### Syntax
- Excel: `EQ(value1, value2)`
- Google Sheets: `EQ(value1, value2)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `EQ(1,1) -> TRUE`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/logical.rs`
- Pseudocode:
  1. `strict comparison returning BOOLEAN with null-safe matching`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/EQ.md


---

## ERF — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_erf
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/bessel.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the Gauss error function.

### Syntax
- Excel: `ERF(lower_bound, [upper_bound])`
- Google Sheets: `ERF(lower_bound, [upper_bound])`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `ERF(1) -> 0.8427`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_erf`
- File: `base/src/functions/engineering/bessel.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ERF.md


---

## ERF.PRECISE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the Gauss error function with higher precision behavior.

### Syntax
- Excel: `ERF.PRECISE(x)`
- Google Sheets: `ERF.PRECISE(x)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `ERF.PRECISE(1) -> 0.84270079295`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/engineering/bessel.rs`
- Pseudocode:
  1. `delegate to erf implementation with strict precision mode`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ERF.PRECISE.md


---

## ERFC — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_erfc
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/bessel.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the complementary error function.

### Syntax
- Excel: `ERFC(lower_bound)`
- Google Sheets: `ERFC(lower_bound)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `ERFC(1) -> 0.1573`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_erfc`
- File: `base/src/functions/engineering/bessel.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ERFC.md


---

## ERFC.PRECISE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the complementary error function with higher precision behavior.

### Syntax
- Excel: `ERFC.PRECISE(x)`
- Google Sheets: `ERFC.PRECISE(x)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `ERFC.PRECISE(1) -> 0.15729920705`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/engineering/bessel.rs`
- Pseudocode:
  1. `delegate to erfc implementation with strict precision mode`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ERFC.PRECISE.md


---

## ERROR.TYPE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns an integer code describing the last error type.

### Syntax
- Excel: `ERROR.TYPE(error_val)`
- Google Sheets: `ERROR.TYPE(error_val)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `ERROR.TYPE(#N/A) -> 7`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/information.rs`
- Pseudocode:
  1. `map each error variant to spreadsheet error code integer`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ERROR.TYPE.md


---

## EUROCONVERT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts a numeric value between historical currencies.

### Syntax
- Excel: `EUROCONVERT(number, source_currency, target_currency)`
- Google Sheets: `EUROCONVERT(number, source_currency, target_currency)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `EUROCONVERT(100, "EUR", "USD") -> 110`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/financial.rs`
- Pseudocode:
  1. `convert units via static conversion table and optional full_conversion flag`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/EUROCONVERT.md


---

## EVEN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_even
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Rounds a number up to the nearest even integer.

### Syntax
- Excel: `EVEN(number)`
- Google Sheets: `EVEN(number)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `EVEN(2.3) -> 4`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_even`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/EVEN.md


---

## EXACT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_exact
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Checks if two text values are identical including case.

### Syntax
- Excel: `EXACT(text1, text2)`
- Google Sheets: `EXACT(text1, text2)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `EXACT("A","a") -> FALSE`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_exact`
- File: `base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/EXACT.md


---

## EXP — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_exp
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns e raised to the power of a number.

### Syntax
- Excel: `EXP(number)`
- Google Sheets: `EXP(number)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `EXP(1) -> 2.7182818`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Implemented in IronCalc.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_exp`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/EXP.md


---

## EXPAND — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Expands input to a larger array with fill values.

### Syntax
- Excel: `EXPAND(array, rows, [columns], [pad_with])`
- Google Sheets: `EXPAND(array, rows, [columns], [pad_with])`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `EXPAND({1,2}, 2, 3, 0) -> {{1,2,0},{1,2,0}}`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Pseudocode:
  1. `expand matrix shape and preserve input dimension semantics`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/EXPAND.md


---

## EXPON.DIST — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Calculates exponential distribution cumulative or density values.

### Syntax
- Excel: `EXPON.DIST(x, lambda, cumulative)`
- Google Sheets: `EXPON.DIST(x, lambda, cumulative)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `EXPON.DIST(1, 0.5, TRUE) -> 0.39347`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/statistical/exponential.rs`
- Pseudocode:
  1. `compute pdf/cdf with branch for cumulative flag`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/EXPON.DIST.md


---

## F.DIST — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns values of the F distribution CDF and inverse behavior via variant args.

### Syntax
- Excel: `F.DIST(x, d1, d2, cumulative)`
- Google Sheets: `F.DIST(x, d1, d2, cumulative)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `F.DIST(1.5, 5, 10, TRUE) -> 0.72`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/statistical/fisher.rs`
- Pseudocode:
  1. `compute F CDF using beta regularized path`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/F.DIST.md


---

## F.DIST.RT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the right-tail probability of the F distribution.

### Syntax
- Excel: `F.DIST.RT(x, d1, d2)`
- Google Sheets: `F.DIST.RT(x, d1, d2)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `F.DIST.RT(1.5, 5, 10) -> 0.28`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/statistical/fisher.rs`
- Pseudocode:
  1. `compute 1 - CDF tail with stable numerics`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/F.DIST.RT.md


---

## F.INV — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns inverse of F distribution CDF (given cumulative probability).

### Syntax
- Excel: `F.INV(probability, d1, d2)`
- Google Sheets: `F.INV(probability, d1, d2)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `F.INV(0.05, 5, 10) -> 0.42`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/statistical/fisher.rs`
- Pseudocode:
  1. `invert F CDF with monotonic search and precision limits`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/F.INV.md


---

## F.INV.RT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns inverse right-tail value of the F distribution.

### Syntax
- Excel: `F.INV.RT(probability, d1, d2)`
- Google Sheets: `F.INV.RT(probability, d1, d2)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `F.INV.RT(0.05, 5, 10) -> 3.35`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/statistical/fisher.rs`
- Pseudocode:
  1. `invert right-tail probability for F distribution`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/F.INV.RT.md


---

## F.TEST — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns right-tailed F-test probability for two variances.

### Syntax
- Excel: `F.TEST(array1, array2)`
- Google Sheets: `F.TEST(array1, array2)`

### Behavior
- Inputs are coerced using spreadsheet-compatible rules for numeric/text values.
- Function output is deterministic for identical inputs and environments.

### Examples
- `F.TEST({1,2,3},{4,5,6}) -> 0.12`

### Error Cases
- Invalid argument count returns an evaluation error.
- Domain violations return spreadsheet-compatible errors where required.

### Notes
Function behavior and implementation details to be added as part of batch implementation.

### Code Location
- Not yet implemented in IronCalc.
- Proposed handler: `TBD`
- Proposed file: `base/src/functions/statistical/fisher.rs`
- Pseudocode:
  1. `compute F statistic and lookup right-tail significance`
  2. Validate input arity and numeric/text constraints.
  3. Return exact error code on invalid argument domains.
  4. Return host-compatible behavior for edge cases.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/F.TEST.md


---

## FACT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_fact
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the factorial of an integer argument.

### Syntax
- Excel: `FACT(number)`
- Google Sheets: `FACT(number)`

### Behavior
- Returns 1 for 0, returns #NUM! for negative values, and rounds down non-integers to integer input domain.

### Examples
- `FACT(5) -> 120`
- `FACT(0) -> 1`

### Error Cases
- Errors on negative or fractional inputs outside allowed domain per host behavior.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_fact`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FACT.md


---

## FACTDOUBLE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_factdouble
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the double factorial of a number.

### Syntax
- Excel: `FACTDOUBLE(number)`
- Google Sheets: `FACTDOUBLE(number)`

### Behavior
- Multiplies numbers with step 2 using 1/2! base cases; deterministic for integer inputs.

### Examples
- `FACTDOUBLE(7) -> 105`
- `FACTDOUBLE(4) -> 8`

### Error Cases
- Returns domain error for negative inputs and non-numeric values.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_factdouble`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FACTDOUBLE.md


---

## FALSE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_false
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/logical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the FALSE logical constant.

### Syntax
- Excel: `FALSE()`
- Google Sheets: `FALSE()`

### Behavior
- Returns boolean FALSE with no arguments.

### Examples
- `FALSE() -> FALSE`

### Error Cases
- Argument count mismatches should return a function arity error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_false`
- File: `base/src/functions/logical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FALSE.md


---

## FILTER — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Filters array values by condition.

### Syntax
- Excel: `FILTER(array, include, [if_empty])`
- Google Sheets: `FILTER(array, include, [if_empty])`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `FILTER({1,2,3},{TRUE,FALSE,TRUE}) -> {1,3}`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_filter`
- Pseudocode: deterministic parsing, coercion, and computation.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FILTER.md


---

## FILTERXML — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Parses XML text and returns queried content using a path expression.

### Syntax
- Excel: `FILTERXML(xml, xpath)`
- Google Sheets: `FILTERXML(xml, xpath)`

### Behavior
- XML parser evaluates XPath-like path over a static XML string and returns textual/value extraction.

### Examples
- `FILTERXML("<a><b>1</b></a>", "//b") -> 1`

### Error Cases
- Invalid XML, invalid path, or unsupported expressions return parse/runtime errors.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_filterxml`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FILTERXML.md


---

## FIND — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: N
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_find
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the position of a substring inside text (case-sensitive).

### Syntax
- Excel: `FIND(find_text, within_text, [start_num])`
- Google Sheets: `FIND(find_text, within_text, [start_num])`

### Behavior
- 1-based indexing, supports start offset, empty or out-of-range inputs trigger errors, case-sensitive.

### Examples
- `FIND("b", "abc") -> 2`

### Error Cases
- Returns #VALUE! when text is not found or start position is invalid.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_find`
- File: `base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FIND.md


---

## FINDB — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Byte-level text search equivalent to FIND.

### Syntax
- Excel: `FINDB(find_text, within_text, [start_num])`
- Google Sheets: `FINDB(find_text, within_text, [start_num])`

### Behavior
- Uses byte-aware indexing and otherwise mirrors FIND domain behavior.

### Examples
- `FINDB("b", "abc") -> 2`

### Error Cases
- Returns value/domain errors when search text is missing or index is invalid.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_findb`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FINDB.md


---

## FISHER — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_fisher
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/fisher.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the hyperbolic arctangent-like Fisher transform.

### Syntax
- Excel: `FISHER(x)`
- Google Sheets: `FISHER(x)`

### Behavior
- Domain is unrestricted real input; deterministic transform with stable numeric path.

### Examples
- `FISHER(1) -> 0.868591`

### Error Cases
- Non-numeric values return calculation error; overflow handled deterministically.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_fisher`
- File: `base/src/functions/statistical/fisher.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FISHER.md


---

## FISHERINV — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_fisher_inv
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/fisher.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the inverse Fisher transform.

### Syntax
- Excel: `FISHERINV(y)`
- Google Sheets: `FISHERINV(y)`

### Behavior
- Inverse mapping of FISHER, deterministic and stable for real inputs.

### Examples
- `FISHERINV(0.5) -> 0.462117`

### Error Cases
- Invalid numeric domain returns error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_fisher_inv`
- File: `base/src/functions/statistical/fisher.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FISHERINV.md


---

## FIXED — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Formats a number to fixed decimals as text with optional thousands separators and rounding.

### Syntax
- Excel: `FIXED(number, [decimals], [no_commas])`
- Google Sheets: `FIXED(number, [decimals], [no_commas])`

### Behavior
- Applies host numeric rounding and returns text-formatted output.

### Examples
- `FIXED(1234.567, 2, TRUE) -> "1234.57"`

### Error Cases
- Invalid decimal precision or non-numeric input returns error.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_fixed`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FIXED.md


---

## FLATTEN — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Flattens nested arrays into a single-column array.

### Syntax
- Excel: `FLATTEN(value1, [value2], ...)`
- Google Sheets: `FLATTEN(value1, [value2], ...)`

### Behavior
- Recursively traverses array-like inputs and concatenates in stable row-major order.

### Examples
- `FLATTEN({{1,2},{3,4}}) -> {1;2;3;4}`

### Error Cases
- Invalid nested values and circular references are rejected.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_flatten`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FLATTEN.md


---

## FLOOR — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_floor
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Rounds a number down to nearest multiple of significance.

### Syntax
- Excel: `FLOOR(number, [significance], [mode])`
- Google Sheets: `FLOOR(number, [significance], [mode])`

### Behavior
- Uses significance and optional mode for negative numbers and host-compatible behavior.

### Examples
- `FLOOR(12.7, 1) -> 12`
- `FLOOR(-12.7, 1) -> -13`

### Error Cases
- Invalid significance or unsupported mode returns error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_floor`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FLOOR.md


---

## FLOOR.MATH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Rounds a number down to nearest multiple with explicit precision mode.

### Syntax
- Excel: `FLOOR.MATH(number,[significance],[mode],[step])`
- Google Sheets: `FLOOR.MATH(number,[significance],[mode],[step])`

### Behavior
- Supports mode and step overrides for negative rounding behavior with deterministic output.

### Examples
- `FLOOR.MATH(-3.7,1,1) -> -3`

### Error Cases
- Invalid significance and invalid mode values trigger errors.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_floor_math`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FLOOR.MATH.md


---

## FLOOR.PRECISE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Rounds number down to nearest multiple with precise semantics.

### Syntax
- Excel: `FLOOR.PRECISE(number, [significance])`
- Google Sheets: `FLOOR.PRECISE(number, [significance])`

### Behavior
- Precision variant of FLOOR without mode effects.

### Examples
- `FLOOR.PRECISE(12.7, 1) -> 12`

### Error Cases
- Domain errors for zero significance or non-numeric inputs.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_floor_precise`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FLOOR.PRECISE.md


---

## FORECAST — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Predicts a value using linear trend from known data pairs.

### Syntax
- Excel: `FORECAST(x, known_ys, known_xs)`
- Google Sheets: `FORECAST(x, known_ys, known_xs)`

### Behavior
- Requires equal-length numeric arrays; computes slope and intercept and applies to x.

### Examples
- `FORECAST(6, {20,25,30}, {1,2,3}) -> 35`

### Error Cases
- Mismatched array lengths or invalid regression input returns error.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/statistical/forecast.rs`
- Proposed handler: `fn_forecast`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FORECAST.md


---

## FORECAST.ETS — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Forecasts values using exponential smoothing.

### Syntax
- Excel: `FORECAST.ETS(target_date, values, timeline, ...)`
- Google Sheets: `FORECAST.ETS(target_date, values, timeline, ...)`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `FORECAST.ETS("2026-02-28", {1,2,3}, {1,2,3}) -> value`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Proposed file: `base/src/functions/statistical/forecast.rs`
- Proposed handler: `fn_forecast.ets`
- Pseudocode: deterministic parsing, coercion, and computation.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FORECAST.ETS.md


---

## FORECAST.ETS.CONFINT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns confidence interval for ETS forecast.

### Syntax
- Excel: `FORECAST.ETS.CONFINT(target_date, values, timeline, [statistic], [confidence])`
- Google Sheets: `FORECAST.ETS.CONFINT(target_date, values, timeline, [statistic], [confidence])`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `FORECAST.ETS.CONFINT("2026-02-28",{1,2,3},{1,2,3},1,0.95) -> {low,high}`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Proposed file: `base/src/functions/statistical/forecast.rs`
- Proposed handler: `fn_forecast.ets.confint`
- Pseudocode: deterministic parsing, coercion, and computation.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FORECAST.ETS.CONFINT.md


---

## FORECAST.ETS.SEASONALITY — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns seasonality period for ETS forecast data.

### Syntax
- Excel: `FORECAST.ETS.SEASONALITY(values, timeline, [data_completion], [aggregation])`
- Google Sheets: `FORECAST.ETS.SEASONALITY(values, timeline, [data_completion], [aggregation])`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `FORECAST.ETS.SEASONALITY({1,2,3},{1,2,3}) -> 1`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Proposed file: `base/src/functions/statistical/forecast.rs`
- Proposed handler: `fn_forecast.ets.seasonality`
- Pseudocode: deterministic parsing, coercion, and computation.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FORECAST.ETS.SEASONALITY.md


---

## FORECAST.ETS.STAT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns regression statistic for ETS forecast.

### Syntax
- Excel: `FORECAST.ETS.STAT(values, timeline, stat_type)`
- Google Sheets: `FORECAST.ETS.STAT(values, timeline, stat_type)`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `FORECAST.ETS.STAT({1,2,3},{1,2,3},1) -> value`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Proposed file: `base/src/functions/statistical/forecast.rs`
- Proposed handler: `fn_forecast.ets.stat`
- Pseudocode: deterministic parsing, coercion, and computation.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FORECAST.ETS.STAT.md


---

## FORECAST.LINEAR — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns linear trend forecast.

### Syntax
- Excel: `FORECAST.LINEAR(x, known_ys, known_xs)`
- Google Sheets: `FORECAST.LINEAR(x, known_ys, known_xs)`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `FORECAST.LINEAR(4,{3,5,7},{1,2,3}) -> 9`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Proposed file: `base/src/functions/statistical/forecast.rs`
- Proposed handler: `fn_forecast.linear`
- Pseudocode: deterministic parsing, coercion, and computation.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FORECAST.LINEAR.md


---

## FORMULATEXT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_formulatext
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the formula text of a referenced cell.

### Syntax
- Excel: `FORMULATEXT(reference)`
- Google Sheets: `FORMULATEXT(reference)`

### Behavior
- Returns formula string if target cell contains formula, otherwise errors or blank as host semantics.

### Examples
- `FORMULATEXT(A1) -> "=SUM(A1:A3)"`

### Error Cases
- Non-formula references and inaccessible cells return error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_formulatext`
- File: `base/src/functions/lookup_and_reference.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FORMULATEXT.md


---

## FREQUENCY — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: matrix

## Spec Summary
### Purpose
Returns frequency counts for values across bins.

### Syntax
- Excel: `FREQUENCY(data_array, bins_array)`
- Google Sheets: `FREQUENCY(data_array, bins_array)`

### Behavior
- Returns a vertical array with one extra bin for values above last threshold.

### Examples
- `FREQUENCY({1,2,3}, {2}) -> {2,1}`

### Error Cases
- Empty bins or non-numeric data produce errors.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/statistical/frequency.rs`
- Proposed handler: `fn_frequency`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FREQUENCY.md


---

## FTEST — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: fn_f_test
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/fisher.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Performs two-variable F-test variance comparison.

### Syntax
- Excel: `FTEST(array1, array2)`
- Google Sheets: `FTEST(array1, array2)`

### Behavior
- Calculates significance probability for variance ratio between two samples.

### Examples
- `FTEST({1,2,3}, {4,5,6}) -> 0.74`

### Error Cases
- Too few values or invalid numeric input returns error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_f_test`
- File: `base/src/functions/statistical/fisher.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FTEST.md


---

## FV — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_fv
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Calculates future value of annuity streams.

### Syntax
- Excel: `FV(rate, nper, pmt, [pv], [type])`
- Google Sheets: `FV(rate, nper, pmt, [pv], [type])`

### Behavior
- Uses constant-rate compounding and optional payment timing flag.

### Examples
- `FV(0.05, 10, -100, 0, 0) -> 1257.79`

### Error Cases
- Invalid nper/rate/type inputs produce error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_fv`
- File: `base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FV.md


---

## FVSCHEDULE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Future value after applying a schedule of interest rates.

### Syntax
- Excel: `FVSCHEDULE(principal, schedule)`
- Google Sheets: `FVSCHEDULE(principal, schedule)`

### Behavior
- Sequentially compounds principal by each scheduled rate.

### Examples
- `FVSCHEDULE(1000, {0.02, 0.03}) -> 1060.6`

### Error Cases
- Invalid array shape or non-numeric rates returns error.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/financial.rs`
- Proposed handler: `fn_fvschedule`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/FVSCHEDULE.md


---

## GAMMA — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_gamma
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/gamma.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the gamma function value.

### Syntax
- Excel: `GAMMA(number)`
- Google Sheets: `GAMMA(number)`

### Behavior
- Uses numeric approximation for defined input domains, deterministic by input and environment flags.

### Examples
- `GAMMA(5) -> 24`

### Error Cases
- Invalid domain values return function error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_gamma`
- File: `base/src/functions/statistical/gamma.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/GAMMA.md


---

## GAMMA.DIST — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns gamma distribution cumulative or density values.

### Syntax
- Excel: `GAMMA.DIST(x, alpha, beta, cumulative)`
- Google Sheets: `GAMMA.DIST(x, alpha, beta, cumulative)`

### Behavior
- Returns CDF when cumulative=TRUE, otherwise PDF.

### Examples
- `GAMMA.DIST(2, 2, 1, FALSE) -> 0.3679`

### Error Cases
- Alpha/beta must be positive; out-of-domain probability returns error.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/statistical/gamma.rs`
- Proposed handler: `fn_gamma_dist`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/GAMMA.DIST.md


---

## GAMMA.INV — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns inverse gamma distribution quantile.

### Syntax
- Excel: `GAMMA.INV(probability, alpha, beta)`
- Google Sheets: `GAMMA.INV(probability, alpha, beta)`

### Behavior
- Inverts GAMMA.DIST with deterministic numeric solving behavior.

### Examples
- `GAMMA.INV(0.5, 2, 1) -> 1.678`

### Error Cases
- Probability outside 0-1 returns error.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/statistical/gamma.rs`
- Proposed handler: `fn_gamma_inv`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/GAMMA.INV.md


---

## GAMMADIST — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: fn_gamma_dist
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/gamma.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Legacy alias for Gamma distribution cumulative/density behavior.

### Syntax
- Excel: `GAMMADIST(x, alpha, beta, cumulative)`
- Google Sheets: `GAMMADIST(x, alpha, beta, cumulative)`

### Behavior
- Compatibility wrapper with the same semantics as modern GAMMA.DIST form.

### Examples
- `GAMMADIST(2, 2, 1, FALSE) -> 0.3679`

### Error Cases
- Invalid shape/scale or x values return errors.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_gamma_dist`
- File: `base/src/functions/statistical/gamma.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/GAMMADIST.md


---

## GAMMAINV — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: fn_gamma_inv
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/gamma.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns inverse of gamma cumulative distribution.

### Syntax
- Excel: `GAMMAINV(probability, alpha, beta)`
- Google Sheets: `GAMMAINV(probability, alpha, beta)`

### Behavior
- Computes x such that GAMMA.DIST(x, alpha, beta, TRUE)=probability.

### Examples
- `GAMMAINV(0.5, 2, 1) -> 1.678`

### Error Cases
- Probability outside [0,1] returns error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_gamma_inv`
- File: `base/src/functions/statistical/gamma.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/GAMMAINV.md


---

## GAMMALN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_gamma_ln
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/gamma.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the natural logarithm of the Gamma function.

### Syntax
- Excel: `GAMMALN(x)`
- Google Sheets: `GAMMALN(x)`

### Behavior
- Uses stable log-gamma algorithm and deterministic rounding policy.

### Examples
- `GAMMALN(5) -> 3.178053`

### Error Cases
- Domain invalid for non-positive x.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_gamma_ln`
- File: `base/src/functions/statistical/gamma.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/GAMMALN.md


---

## GAMMALN.PRECISE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the natural logarithm of Gamma with precision emphasis.

### Syntax
- Excel: `GAMMALN.PRECISE(x)`
- Google Sheets: `GAMMALN.PRECISE(x)`

### Behavior
- Precision-oriented variant of GAMMALN with stricter numeric pathway.

### Examples
- `GAMMALN.PRECISE(5) -> 3.178053830`

### Error Cases
- Domain invalid for non-positive x.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/statistical/gamma.rs`
- Proposed handler: `fn_gammaln_precise`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/GAMMALN.PRECISE.md


---

## GAUSS — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_gauss
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/gauss.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the standard normal cumulative distribution value shifted around mean 0.

### Syntax
- Excel: `GAUSS(z)`
- Google Sheets: `GAUSS(z)`

### Behavior
- Deterministic CDF-like normal transform for real inputs.

### Examples
- `GAUSS(0) -> 0.5`

### Error Cases
- Non-numeric input returns error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_gauss`
- File: `base/src/functions/statistical/gauss.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/GAUSS.md


---

## GCD — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_gcd
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns greatest common divisor of one or more integers.

### Syntax
- Excel: `GCD(number1, [number2], ...)`
- Google Sheets: `GCD(number1, [number2], ...)`

### Behavior
- Computes gcd across all arguments with deterministic integer math.

### Examples
- `GCD(48, 18) -> 6`

### Error Cases
- Non-numeric input raises domain error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_gcd`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/GCD.md


---

## GEOMEAN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_geomean
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/geomean.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns geometric mean of numeric values.

### Syntax
- Excel: `GEOMEAN(number1, [number2], ...)`
- Google Sheets: `GEOMEAN(number1, [number2], ...)`

### Behavior
- Uses only positive values where required by geometric mean definition.

### Examples
- `GEOMEAN(1, 2, 4) -> 2`

### Error Cases
- Non-positive inputs cause domain error in strict mode.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_geomean`
- File: `base/src/functions/statistical/geomean.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/GEOMEAN.md


---

## GESTEP — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_gestep
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/misc.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns 1 if number >= step, else 0.

### Syntax
- Excel: `GESTEP(number, [step])`
- Google Sheets: `GESTEP(number, [step])`

### Behavior
- Compares number to threshold.

### Examples
- `GESTEP(1.5, 2) -> 0`
- `GESTEP(2.5, 2) -> 1`

### Error Cases
- Invalid step or non-numeric input returns error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_gestep`
- File: `base/src/functions/engineering/misc.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/GESTEP.md


---

## GETPIVOTDATA — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Extracts data from a pivot table structure by field/item pairs.

### Syntax
- Excel: `GETPIVOTDATA(data_field, pivot_table, [field, item, ...])`
- Google Sheets: `GETPIVOTDATA(data_field, pivot_table, [field, item, ...])`

### Behavior
- Locates pivot field combinations deterministically and returns aggregate value.

### Examples
- `GETPIVOTDATA("Sum", A1:F10, "Month", "Jan") -> 125`

### Error Cases
- Invalid pivot reference or missing field returns reference error.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_getpivotdata`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/GETPIVOTDATA.md


---

## GOOGLEFINANCE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Fetches finance data from online provider for ticker and attributes.

### Syntax
- Excel: `GOOGLEFINANCE(ticker, [attribute], [start_date], [end_date], [interval])`
- Google Sheets: `GOOGLEFINANCE(ticker, [attribute], [start_date], [end_date], [interval])`

### Behavior
- Performs remote data fetch and returns scalar or array output.

### Examples
- `GOOGLEFINANCE("NASDAQ:GOOGL", "price") -> 1800.45`

### Error Cases
- Missing network/backend or invalid ticker returns service error.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/integrations.rs`
- Proposed handler: `fn_googlefinance`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/GOOGLEFINANCE.md


---

## GOOGLETRANSLATE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Translates text between languages via service integration.

### Syntax
- Excel: `GOOGLETRANSLATE(text, source_language, target_language)`
- Google Sheets: `GOOGLETRANSLATE(text, source_language, target_language)`

### Behavior
- Returns translated text with deterministic handling of language codes.

### Examples
- `GOOGLETRANSLATE("hello", "en", "es") -> "hola"`

### Error Cases
- Missing backend/language codes returns service error.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/integrations.rs`
- Proposed handler: `fn_googletranslate`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/GOOGLETRANSLATE.md


---

## GROUPBY — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Groups rows by key(s) and applies aggregation.

### Syntax
- Excel: `GROUPBY(array, by_array, col_by_array, function)`
- Google Sheets: `GROUPBY(array, by_array, col_by_array, function)`

### Behavior
- Groups input by stable key ordering and computes requested aggregate per group.

### Examples
- `GROUPBY({1,2,1}, {"a","b","a"}, , SUM) -> {{"a",2},{"b",2}}`

### Error Cases
- Mismatched sizes or invalid function token returns error.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/statistical/groupby.rs`
- Proposed handler: `fn_groupby`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/GROUPBY.md


---

## GROWTH — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Fits exponential trend and projects values for x inputs.

### Syntax
- Excel: `GROWTH(known_ys, [known_xs], [new_x], [const])`
- Google Sheets: `GROWTH(known_ys, [known_xs], [new_x], [const])`

### Behavior
- Computes log-space regression and returns predicted y values; deterministic fit path.

### Examples
- `GROWTH({2,4,8}, {1,2,3}, {4}) -> {16}`

### Error Cases
- Non-positive known_ys or invalid args return error.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/statistical/forecast.rs`
- Proposed handler: `fn_growth`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/GROWTH.md


---

## GT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns TRUE when first argument is greater than the second.

### Syntax
- Excel: `GT(value1, value2)`
- Google Sheets: `GT(value1, value2)`

### Behavior
- Strict comparison with coercion semantics consistent with logical operators.

### Examples
- `GT(5, 3) -> TRUE`

### Error Cases
- Uncomparable types may return error.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/logical.rs`
- Proposed handler: `fn_gt`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/GT.md


---

## GTE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns TRUE when first argument is greater than or equal to second.

### Syntax
- Excel: `GTE(value1, value2)`
- Google Sheets: `GTE(value1, value2)`

### Behavior
- Deterministic comparison with type-coercion rules equivalent to comparison operators.

### Examples
- `GTE(5, 5) -> TRUE`

### Error Cases
- Uncomparable types may return error.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/logical.rs`
- Proposed handler: `fn_gte`
- Pseudocode:
-   1. Parse and validate argument count/types.
-   2. Apply deterministic coercion and ordering rules.
-   3. Compute against Excel/Sheets-compatible semantics.
-   4. Return stable numeric/text/error result.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/GTE.md


---

## HARMEAN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_harmean
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns harmonic mean of values.

### Syntax
- Excel: `HARMEAN(number1, [number2], ...)`
- Google Sheets: `HARMEAN(number1, [number2], ...)`

### Behavior
- Requires positive data and computes reciprocal-mean formula deterministically.

### Examples
- `HARMEAN(1, 2, 4) -> 1.7142857`

### Error Cases
- Zero or negative values produce domain error.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_harmean`
- File: `base/src/functions/statistical/count_and_average.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/HARMEAN.md


---

## HEX2BIN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_hex2bin
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/number_basis.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts a hexadecimal number to binary format.

### Syntax
- Excel: `HEX2BIN(number, [places])`
- Google Sheets: `HEX2BIN(number, [places])`

### Behavior
- Converts hex digits to binary and applies optional zero-padding.

### Examples
- `HEX2BIN("1A") -> "11010"`

### Error Cases
- Invalid hex digits or overflow return errors.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_hex2bin`
- File: `base/src/functions/engineering/number_basis.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/HEX2BIN.md


---

## HEX2DEC — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_hex2dec
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/number_basis.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts a hexadecimal number to decimal.

### Syntax
- Excel: `HEX2DEC(number)`
- Google Sheets: `HEX2DEC(number)`

### Behavior
- Converts hex input to decimal with signed/unsigned interpretation rules as configured.

### Examples
- `HEX2DEC("A") -> 10`

### Error Cases
- Invalid hex characters or range overflow return errors.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_hex2dec`
- File: `base/src/functions/engineering/number_basis.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/HEX2DEC.md


---

## HEX2OCT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_hex2oct
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/number_basis.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts a hexadecimal number to an octal number.

### Syntax
- Excel: `HEX2OCT(number, [places])`
- Google Sheets: `HEX2OCT(number, [places])`

### Behavior
- Converts each hex digit to octal representation and applies optional zero padding.

### Examples
- `HEX2OCT("1A") -> "032"`

### Error Cases
Invalid hex input or overflow returns a function/domain error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_hex2oct`
- File: `base/src/functions/engineering/number_basis.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_hex2oct`
- File: `base/src/functions/engineering/number_basis.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/HEX2OCT.md


---

## HLOOKUP — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_hlookup
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Looks up a value in the first row of a table and returns matching value from a specified row.

### Syntax
- Excel: `HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])`
- Google Sheets: `HLOOKUP(lookup_value, table_array, row_index, [is_sorted])`

### Behavior
- Performs row-oriented lookup with optional approximate matching.

### Examples
- `HLOOKUP(2, {1,2,3;4,5,6}, 2, FALSE) -> 5`

### Error Cases
Invalid row index or unresolved key returns #N/A-like error behavior.

### Notes
- Implemented in IronCalc.
- Handler: `fn_hlookup`
- File: `base/src/functions/lookup_and_reference.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_hlookup`
- File: `base/src/functions/lookup_and_reference.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/HLOOKUP.md


---

## HOUR — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_hour
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Extracts the hour component of a time/date serial value.

### Syntax
- Excel: `HOUR(serial_number)`
- Google Sheets: `HOUR(time)`

### Behavior
- Returns integer hour from 0 to 23 using spreadsheet date-time conversion rules.

### Examples
- `HOUR("2026-02-19 14:30") -> 14`

### Error Cases
Invalid datetime values return an argument error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_hour`
- File: `base/src/functions/date_and_time.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_hour`
- File: `base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/HOUR.md


---

## HSTACK — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Horizontally stacks arrays/values into a single array.

### Syntax
- Excel: `HSTACK(value1, [value2], ...)`
- Google Sheets: `HSTACK(value1, [value2], ...)`

### Behavior
- Concatenates arguments by column, normalizing scalar values into rows as needed.

### Examples
- `HSTACK({1,2},{3,4}) -> {1,2,3,4}`

### Error Cases
Mismatched array dimensions or invalid arguments return an error.

### Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_hstack`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_hstack`
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/HSTACK.md


---

## HYPERLINK — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns a hyperlink formula value linking display text to a target URL.

### Syntax
- Excel: `HYPERLINK(link_location, [friendly_name])`
- Google Sheets: `HYPERLINK(url, [label])`

### Behavior
- Represents link metadata and optional display label; evaluation is backend neutral in pure compute engines.

### Examples
- `HYPERLINK("https://example.com", "Open") -> "Open"`

### Error Cases
Invalid URL/text arguments return a value error.

### Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/information.rs`
- Proposed handler: `fn_hyperlink`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_hyperlink`
- Proposed file: `base/src/functions/information.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/HYPERLINK.md


---

## HYPGEOM.DIST — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the hypergeometric distribution probability.

### Syntax
- Excel: `HYPGEOM.DIST(sample_s, number_sample, population_s, number_pop, cumulative)`
- Google Sheets: `HYPGEOM.DIST(sample_s, number_sample, population_s, number_pop, cumulative)`

### Behavior
- Computes PMF or CDF based on cumulative flag.

### Examples
- `HYPGEOM.DIST(2, 3, 5, 10, FALSE) -> 0.238`

### Error Cases
Invalid draw/sample ranges return a domain error.

### Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/statistical/hypegeom.rs`
- Proposed handler: `fn_hypgeom_dist`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_hypgeom_dist`
- Proposed file: `base/src/functions/statistical/hypegeom.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/HYPGEOM.DIST.md


---

## HYPGEOMDIST — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: fn_hyp_geom_dist
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/hypegeom.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Legacy alias for the hypergeometric distribution.

### Syntax
- Excel: `HYPGEOMDIST(sample_s, number_sample, number_pop, population_s)`
- Google Sheets: `HYPGEOMDIST(sample_s, number_sample, number_pop, population_s)`

### Behavior
- Legacy argument order mapped to equivalent HYPGEOM.DIST cumulative behavior.

### Examples
- `HYPGEOMDIST(2, 3, 10, 5) -> 0.238`

### Error Cases
Invalid range values and inconsistent parameters return domain errors.

### Notes
- Implemented in IronCalc.
- Handler: `fn_hyp_geom_dist`
- File: `base/src/functions/statistical/hypegeom.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_hyp_geom_dist`
- File: `base/src/functions/statistical/hypegeom.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/HYPGEOMDIST.md


---

## IF — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_if
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/logical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns one of two values depending on logical test result.

### Syntax
- Excel: `IF(logical_test, value_if_true, value_if_false)`
- Google Sheets: `IF(condition, value_if_true, value_if_false)`

### Behavior
- Evaluates test with short-circuit branch semantics.

### Examples
- `IF(1=1, "Y", "N") -> "Y"`

### Error Cases
Invalid argument count returns arity error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_if`
- File: `base/src/functions/logical.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_if`
- File: `base/src/functions/logical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IF.md


---

## IFERROR — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_iferror
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/logical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns a fallback value when a formula evaluates to an error.

### Syntax
- Excel: `IFERROR(value, value_if_error)`
- Google Sheets: `IFERROR(value, value_if_error)`

### Behavior
- Catches error values and returns fallback; propagates non-error values.

### Examples
- `IFERROR(1/0, 0) -> 0`

### Error Cases
Non-error values pass through unchanged.

### Notes
- Implemented in IronCalc.
- Handler: `fn_iferror`
- File: `base/src/functions/logical.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_iferror`
- File: `base/src/functions/logical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IFERROR.md


---

## IFNA — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_ifna
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/logical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns fallback when value is #N/A, otherwise returns the value.

### Syntax
- Excel: `IFNA(value, value_if_na)`
- Google Sheets: `IFNA(value, value_if_na)`

### Behavior
- Special-cases only #N/A-like errors.

### Examples
- `IFNA(NA(), "missing") -> "missing"`

### Error Cases
Only #N/A is intercepted; other errors pass through.

### Notes
- Implemented in IronCalc.
- Handler: `fn_ifna`
- File: `base/src/functions/logical.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_ifna`
- File: `base/src/functions/logical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IFNA.md


---

## IFS — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_ifs
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/logical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns value corresponding to first true condition in a list.

### Syntax
- Excel: `IFS(condition1, value1, [condition2, value2], ...)`
- Google Sheets: `IFS(condition1, value1, [condition2, value2], ...)`

### Behavior
- Evaluates pairs in order and returns matching branch result.

### Examples
- `IFS(1>2, "no", 2>1, "yes") -> "yes"`

### Error Cases
No matching condition or odd argument count returns error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_ifs`
- File: `base/src/functions/logical.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_ifs`
- File: `base/src/functions/logical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IFS.md


---

## IMABS — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imabs
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the absolute value of a complex number.

### Syntax
- Excel: `IMABS(inumber)`
- Google Sheets: `IMABS(inumber)`

### Behavior
- Computes magnitude of the input complex number.

### Examples
- `IMABS("3+4i") -> 5`

### Error Cases
Invalid complex notation returns parser error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_imabs`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imabs`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMABS.md


---

## IMAGE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Returns an image function reference from a URL or local source.

### Syntax
- Excel: `IMAGE(url, [mode], [height], [width], [top], [left], [bottom], [right])`
- Google Sheets: `IMAGE(url, [mode], [height], [width], [top], [left], [bottom], [right])`

### Behavior
- Represents image placement instruction in spreadsheet UIs; not a numeric transform function.

### Examples
- `IMAGE("https://example.com/logo.png") -> image://https://example.com/logo.png`

### Error Cases
Invalid source URL/path should raise a value/runtime error in rendering mode.

### Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/information.rs`
- Proposed handler: `fn_image`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_image`
- Proposed file: `base/src/functions/information.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMAGE.md


---

## IMAGINARY — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imaginary
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the imaginary coefficient of a complex number.

### Syntax
- Excel: `IMAGINARY(inumber)`
- Google Sheets: `IMAGINARY(inumber)`

### Behavior
- Parses input and returns the imaginary part as numeric scalar.

### Examples
- `IMAGINARY("3+4i") -> 4`

### Error Cases
Invalid complex input returns #VALUE!-style error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_imaginary`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imaginary`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMAGINARY.md


---

## IMARGUMENT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imargument
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the argument (angle) of a complex number in radians.

### Syntax
- Excel: `IMARGUMENT(inumber)`
- Google Sheets: `IMARGUMENT(inumber)`

### Behavior
- Computes principal argument on the complex plane.

### Examples
- `IMARGUMENT("1+i") -> 0.7854`

### Error Cases
Zero-length vector or invalid input produces error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_imargument`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imargument`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMARGUMENT.md


---

## IMCONJUGATE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imconjugate
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns complex conjugate.

### Syntax
- Excel: `IMCONJUGATE(inumber)`
- Google Sheets: `IMCONJUGATE(inumber)`

### Behavior
- Negates imaginary sign component while preserving real part.

### Examples
- `IMCONJUGATE("3+4i") -> "3-4i"`

### Error Cases
Malformed input returns parse error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_imconjugate`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imconjugate`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMCONJUGATE.md


---

## IMCOS — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imcos
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns cosine of a complex number.

### Syntax
- Excel: `IMCOS(inumber)`
- Google Sheets: `IMCOS(inumber)`

### Behavior
- Applies complex cosine function with real-imaginary output formatting.

### Examples
- `IMCOS("i") -> 1.543080635i`

### Error Cases
Non-complex input returns a parser/domain error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_imcos`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imcos`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMCOS.md


---

## IMCOSH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imcosh
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns hyperbolic cosine of a complex number.

### Syntax
- Excel: `IMCOSH(inumber)`
- Google Sheets: `IMCOSH(inumber)`

### Behavior
- Computes cosh over complex values.

### Examples
- `IMCOSH("1") -> 1.543080635`

### Error Cases
Invalid complex input returns error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_imcosh`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imcosh`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMCOSH.md


---

## IMCOT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imcot
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns cotangent of a complex number.

### Syntax
- Excel: `IMCOT(inumber)`
- Google Sheets: `IMCOT(inumber)`

### Behavior
- Returns complex cotangent using 1/tan with branch handling for zero/near-zero denominators.

### Examples
- `IMCOT("1") -> 0.6420926159`

### Error Cases
Zero denominator or invalid input returns error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_imcot`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imcot`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMCOT.md


---

## IMCOTH — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns hyperbolic cotangent of a complex number.

### Syntax
- Excel: `IMCOTH(inumber)`
- Google Sheets: `IMCOTH(inumber)`

### Behavior
- Returns hyperbolic cotangent with deterministic complex handling.

### Examples
- `IMCOTH("1") -> 1.313035285`

### Error Cases
Zero denominator or invalid format returns error.

### Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/engineering/complex.rs`
- Proposed handler: `fn_imcoth`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_imcoth`
- Proposed file: `base/src/functions/engineering/complex.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMCOTH.md


---

## IMCSC — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imcsc
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns cosecant of a complex number.

### Syntax
- Excel: `IMCSC(inumber)`
- Google Sheets: `IMCSC(inumber)`

### Behavior
- Computes reciprocal of sine in complex domain.

### Examples
- `IMCSC("1") -> 1.188395105`

### Error Cases
Invalid complex input or undefined poles return errors.

### Notes
- Implemented in IronCalc.
- Handler: `fn_imcsc`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imcsc`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMCSC.md


---

## IMCSCH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imcsch
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns hyperbolic cosecant of a complex number.

### Syntax
- Excel: `IMCSCH(inumber)`
- Google Sheets: `IMCSCH(inumber)`

### Behavior
- Computes reciprocal of hyperbolic sine with complex arithmetic.

### Examples
- `IMCSCH("1") -> 0.850918128`

### Error Cases
Invalid complex input returns error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_imcsch`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imcsch`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMCSCH.md


---

## IMDIV — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imdiv
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Divides two complex numbers.

### Syntax
- Excel: `IMDIV(inumber1, inumber2)`
- Google Sheets: `IMDIV(inumber1, inumber2)`

### Behavior
- Performs complex division with deterministic normalization.

### Examples
- `IMDIV("4+2i", "1+i") -> 3`

### Error Cases
Division by zero or malformed complex numbers returns error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_imdiv`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imdiv`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMDIV.md


---

## IMEXP — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imexp
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns complex exponential.

### Syntax
- Excel: `IMEXP(inumber)`
- Google Sheets: `IMEXP(inumber)`

### Behavior
- Applies e^(z) in complex plane and returns normalized complex string.

### Examples
- `IMEXP("1") -> 2.718281828`

### Error Cases
Invalid complex input returns error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_imexp`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imexp`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMEXP.md


---

## IMLN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imln
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns natural logarithm of a complex number.

### Syntax
- Excel: `IMLN(inumber)`
- Google Sheets: `IMLN(inumber)`

### Behavior
- Uses principal complex logarithm with deterministic branch behavior.

### Examples
- `IMLN("1") -> 0`

### Error Cases
Non-complex/invalid input returns error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_imln`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imln`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMLN.md


---

## IMLOG — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns logarithm of a complex number with specified base.

### Syntax
- Excel: `IMLOG(inumber, [base])`
- Google Sheets: `IMLOG(inumber, [base])`

### Behavior
- Divides IMLN(inumber) by IMLN(base) when base is provided.

### Examples
- `IMLOG("10", 10) -> 1`

### Error Cases
Invalid base (<=0, 1) or invalid complex input returns error.

### Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/engineering/complex.rs`
- Proposed handler: `fn_imlog`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_imlog`
- Proposed file: `base/src/functions/engineering/complex.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMLOG.md


---

## IMLOG10 — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imlog10
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns base-10 logarithm of a complex number.

### Syntax
- Excel: `IMLOG10(inumber)`
- Google Sheets: `IMLOG10(inumber)`

### Behavior
- Computes log base 10 on complex input.

### Examples
- `IMLOG10("10") -> 1`

### Error Cases
Invalid complex input returns error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_imlog10`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imlog10`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMLOG10.md


---

## IMLOG2 — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imlog2
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns base-2 logarithm of a complex number.

### Syntax
- Excel: `IMLOG2(inumber)`
- Google Sheets: `IMLOG2(inumber)`

### Behavior
- Computes log base 2 on complex input.

### Examples
- `IMLOG2("4") -> 2`

### Error Cases
Invalid complex input returns error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_imlog2`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imlog2`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMLOG2.md


---

## IMPORTDATA — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Imports data from a URL-delivered CSV or TSV.

### Syntax
- Excel: `IMPORTDATA(url, [delimiter], [separator])`
- Google Sheets: `IMPORTDATA(url)`

### Behavior
- Retrieves remote file content and parses into tabular array.

### Examples
- `IMPORTDATA("https://example.com/data.csv") -> table`

### Error Cases
Network or URL errors return fetch/runtime error.

### Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/integrations.rs`
- Proposed handler: `fn_importdata`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_importdata`
- Proposed file: `base/src/functions/integrations.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMPORTDATA.md


---

## IMPORTFEED — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Imports a feed (e.g., RSS/ATOM) into table form.

### Syntax
- Excel: `IMPORTFEED(url, [query], [headers], [num_items], [sort], [sort_ascending])`
- Google Sheets: `IMPORTFEED(url, [query], [headers], [num_items], [sort], [sort_ascending])`

### Behavior
- Fetches and transforms feed format into tabular arrays.

### Examples
- `IMPORTFEED("https://example.com/feed") -> data table`

### Error Cases
Malformed feed URLs and connectivity issues return errors.

### Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/integrations.rs`
- Proposed handler: `fn_importfeed`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_importfeed`
- Proposed file: `base/src/functions/integrations.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMPORTFEED.md


---

## IMPORTHTML — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Imports data from HTML tables or lists.

### Syntax
- Excel: `IMPORTHTML(url, query, index)`
- Google Sheets: `IMPORTHTML(url, query, index)`

### Behavior
- Parses DOM and extracts requested table/list block as array.

### Examples
- `IMPORTHTML("https://example.com", "table", 1) -> table data`

### Error Cases
Invalid selector or network failures return errors.

### Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/integrations.rs`
- Proposed handler: `fn_importhtml`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_importhtml`
- Proposed file: `base/src/functions/integrations.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMPORTHTML.md


---

## IMPORTRANGE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Imports a range from another spreadsheet.

### Syntax
- Excel: `IMPORTRANGE(url, range_string)`
- Google Sheets: `IMPORTRANGE(spreadsheet_url, range_string)`

### Behavior
- Resolves external workbook reference and returns range values.

### Examples
- `IMPORTRANGE("id","A1:B2") -> {1,2;3,4}`

### Error Cases
Invalid permissions or external access failures return errors.

### Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/integrations.rs`
- Proposed handler: `fn_importrange`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_importrange`
- Proposed file: `base/src/functions/integrations.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMPORTRANGE.md


---

## IMPORTXML — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Imports data from XML by XPath expressions.

### Syntax
- Excel: `IMPORTXML(url, xpath_query)`
- Google Sheets: `IMPORTXML(url, xpath_query)`

### Behavior
- Downloads XML and applies XPath to produce result array.

### Examples
- `IMPORTXML("https://example.com/feed.xml", "//title") -> {"title"}`

### Error Cases
Invalid XML/XPath or fetch errors return error.

### Notes
- Not implemented in IronCalc.
- Proposed file: `base/src/functions/integrations.rs`
- Proposed handler: `fn_importxml`
- Pseudocode:
  1. Validate arguments and count.
  2. Parse complex/text/input according to host semantics.
  3. Apply deterministic computation and coercion rules.
  4. Return stable error/boolean/numeric/text result.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_importxml`
- Proposed file: `base/src/functions/integrations.rs`
- Pseudocode:
  - Validate argument count and argument types.
  - Apply deterministic coercion and ordering rules.
  - Compute per Excel/Sheets semantics.
  - Return stable error/value output.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMPORTXML.md


---

## IMPOWER — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_impower
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Raises a complex number to a complex power.

### Syntax
- Excel: `IMPOWER(inumber, number)`
- Google Sheets: `IMPOWER(inumber, number)`

### Behavior
- Computes principal complex power with deterministic branch handling.

### Examples
- `IMPOWER("1+i", 2) -> 0+2i`

### Error Cases
Invalid exponentiation for poles or malformed inputs returns error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_impower`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_impower`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMPOWER.md


---

## IMPRODUCT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_improduct
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Multiplies complex numbers.

### Syntax
- Excel: `IMPRODUCT(inumber1, [inumber2], ...)`
- Google Sheets: `IMPRODUCT(inumber1, [inumber2], ...)`

### Behavior
- Performs iterative complex multiplication across arguments.

### Examples
- `IMPRODUCT("1+i", "1-i") -> 2`

### Error Cases
Invalid complex input returns error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_improduct`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_improduct`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMPRODUCT.md


---

## IMREAL — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imreal
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the real coefficient of a complex number.

### Syntax
- Excel: `IMREAL(inumber)`
- Google Sheets: `IMREAL(inumber)`

### Behavior
- Parses and returns numeric real part.

### Examples
- `IMREAL("3+4i") -> 3`

### Error Cases
Malformed complex input returns #VALUE!-style error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_imreal`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imreal`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMREAL.md


---

## IMSEC — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imsec
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns secant of a complex number.

### Syntax
- Excel: `IMSEC(inumber)`
- Google Sheets: `IMSEC(inumber)`

### Behavior
- Computes secant in complex domain as reciprocal cosine.

### Examples
- `IMSEC("1") -> 1.850815718`

### Error Cases
Invalid complex input returns error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_imsec`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imsec`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMSEC.md


---

## IMSECH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imsech
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns hyperbolic secant of a complex number.

### Syntax
- Excel: `IMSECH(inumber)`
- Google Sheets: `IMSECH(inumber)`

### Behavior
- Computes hyperbolic secant in complex domain.

### Examples
- `IMSECH("1") -> 0.648054273`

### Error Cases
Invalid complex input returns error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_imsech`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imsech`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMSECH.md


---

## IMSIN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imsin
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns sine of a complex number.

### Syntax
- Excel: `IMSIN(inumber)`
- Google Sheets: `IMSIN(inumber)`

### Behavior
- Computes sine for complex input with deterministic complex format.

### Examples
- `IMSIN("1") -> 0.841470985`

### Error Cases
Invalid complex input returns error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_imsin`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imsin`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMSIN.md


---

## IMSINH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imsinh
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns hyperbolic sine of a complex number.

### Syntax
- Excel: `IMSINH(inumber)`
- Google Sheets: `IMSINH(inumber)`

### Behavior
- Computes sinh in complex domain.

### Examples
- `IMSINH("1") -> 1.175201194`

### Error Cases
Invalid complex input returns error.

### Notes
- Implemented in IronCalc.
- Handler: `fn_imsinh`
- File: `base/src/functions/engineering/complex.rs`

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imsinh`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMSINH.md


---

## IMSQRT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imsqrt
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the square root of a complex number.

### Syntax
- Excel: `IMSQRT(inumber)`
- Google Sheets: `IMSQRT(inumber)`

### Behavior
- Computes principal complex square root with deterministic branch handling.

### Examples
- `IMSQRT("-4") -> 0+2i`

### Error Cases
- Invalid complex input returns an error.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imsqrt`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMSQRT.md


---

## IMSUB — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imsub
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the difference of two complex numbers.

### Syntax
- Excel: `IMSUB(inumber1, inumber2)`
- Google Sheets: `IMSUB(inumber1, inumber2)`

### Behavior
- Subtracts term-wise in complex plane and returns normalized complex form.

### Examples
- `IMSUB("5+3i","2+1i") -> 3+2i`

### Error Cases
- Invalid complex inputs return error.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imsub`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMSUB.md


---

## IMSUM — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imsum
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the sum of multiple complex numbers.

### Syntax
- Excel: `IMSUM(inumber1, [inumber2], ...)`
- Google Sheets: `IMSUM(inumber1, [inumber2], ...)`

### Behavior
- Adds all inputs using deterministic complex arithmetic.

### Examples
- `IMSUM("1+i","2+3i") -> 3+4i`

### Error Cases
- Empty input list or malformed values return errors.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imsum`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMSUM.md


---

## IMTAN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_imtan
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/complex.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns tangent of a complex number.

### Syntax
- Excel: `IMTAN(inumber)`
- Google Sheets: `IMTAN(inumber)`

### Behavior
- Computes tan for complex input using sine/cosine ratio semantics.

### Examples
- `IMTAN("1") -> 1.5574`

### Error Cases
- Invalid input returns error.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_imtan`
- File: `base/src/functions/engineering/complex.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMTAN.md


---

## IMTANH — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns hyperbolic tangent of a complex number.

### Syntax
- Excel: `IMTANH(inumber)`
- Google Sheets: `IMTANH(inumber)`

### Behavior
- Computes tanh in complex domain deterministically.

### Examples
- `IMTANH("1") -> 0.7616`

### Error Cases
- Invalid input returns error.

### Notes
- Not specified in spec.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_imtanh`
- Proposed file: `base/src/functions/engineering/complex.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IMTANH.md


---

## INDEX — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_index
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns value at row/column in array.

### Syntax
- Excel: `INDEX(array, row_num, [column_num])`
- Google Sheets: `INDEX(array, row_num, [column_num])`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.

### Examples
- `INDEX({1,2;3,4},2,1) -> 3`

### Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible date arithmetic.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_index`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/INDEX.md


---

## INDIRECT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_indirect
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns range reference from text.

### Syntax
- Excel: `INDIRECT(ref_text, [a1])`
- Google Sheets: `INDIRECT(ref_text, [a1])`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.

### Examples
- `INDIRECT("A1")` resolves reference

### Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible date arithmetic.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_indirect`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/INDIRECT.md


---

## INFO — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_info
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns metadata information about a formula or environment (where supported).

### Syntax
- Excel: `INFO(type_text)`
- Google Sheets: `INFO(type_text)`

### Behavior
- Accepts an info type and returns corresponding metadata in compatible output type.

### Examples
- `INFO("system") -> "Windows"`

### Error Cases
- Unknown info type returns a value error.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_info`
- File: `base/src/functions/information.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/INFO.md


---

## INT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_int
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Rounds number down to nearest integer toward negative infinity.

### Syntax
- Excel: `INT(number)`
- Google Sheets: `INT(number)`

### Behavior
- Performs integer conversion with host-compatible flooring semantics.

### Examples
- `INT(3.8) -> 3`
- `INT(-3.8) -> -4`

### Error Cases
- Non-numeric input returns error.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_int`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/INT.md


---

## INTERCEPT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_intercept
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/correl.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the y-axis intercept from linear regression of known points.

### Syntax
- Excel: `INTERCEPT(known_ys, known_xs)`
- Google Sheets: `INTERCEPT(known_ys, known_xs)`

- Note: Non-ASCII characters omitted. See spec for full text.

### Behavior
- Computes slope and intercept from regression formula deterministically.

### Examples
- `INTERCEPT({1,2,3},{1,2,3}) -> 0`

### Error Cases
- Mismatched arrays or insufficient data returns error.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_intercept`
- File: `base/src/functions/statistical/correl.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/INTERCEPT.md


---

## INTRATE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the interest rate for an investment over a period.

### Syntax
- Excel: `INTRATE(settlement, maturity, investment, redemption, [basis])`
- Google Sheets: `INTRATE(settlement, maturity, investment, redemption, [basis])`

### Behavior
- Uses discount method and compounding basis to derive annualized rate.

### Examples
- `INTRATE("01/01/2026","01/01/2027",900,1000,0) -> 0.111111`

### Error Cases
- Settlement after maturity or invalid basis returns error.

### Notes
- Not specified in spec.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_intrate`
- Proposed file: `base/src/functions/financial.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/INTRATE.md


---

## IPMT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_ipmt
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns interest payment for a specific period.

### Syntax
- Excel: `IPMT(rate, per, nper, pv, [fv], [type])`
- Google Sheets: `IPMT(rate, per, nper, pv, [fv], [type])`

### Behavior
- Computes interest component of a payment with period index and schedule flags.

### Examples
- `IPMT(0.08/12, 1, 12, -1000) -> -6.22`

### Error Cases
- Invalid period or sign combinations return error.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_ipmt`
- File: `base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IPMT.md


---

## IRR — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_irr
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: column
- Output: scalar

## Spec Summary
### Purpose
Returns internal rate of return for periodic cash flows.

### Syntax
- Excel: `IRR(values, [guess])`
- Google Sheets: `IRR(values, [guess])`

### Behavior
- Uses iterative root solving on net present value equation.

### Examples
- `IRR({-1000,300,300,300,300}) -> 0.193`

### Error Cases
- No convergence or invalid cash flow signs return error.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_irr`
- File: `base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/IRR.md


---

## ISBETWEEN — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns TRUE if value is between two bounds.

### Syntax
- Excel: `ISBETWEEN(value, lower, upper)`
- Google Sheets: `ISBETWEEN(value, lower, upper)`

### Behavior
- Compares with inclusive or deterministic comparison rules against numeric/text inputs.

### Examples
- `ISBETWEEN(5, 1, 10) -> TRUE`

### Error Cases
- Invalid argument count returns arity error.

### Notes
- Not specified in spec.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_isbetween`
- Proposed file: `base/src/functions/information.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISBETWEEN.md


---

## ISBLANK — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_isblank
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Checks whether a reference is empty.

### Syntax
- Excel: `ISBLANK(value)`
- Google Sheets: `ISBLANK(value)`

### Behavior
- Returns TRUE if input represents an empty cell/range value.

### Examples
- `ISBLANK("") -> TRUE`

### Error Cases
- Unsupported references return #REF! behavior.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_isblank`
- File: `base/src/functions/information.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISBLANK.md


---

## ISDATE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns TRUE if value is a valid date.

### Syntax
- Excel: `ISDATE(value)`
- Google Sheets: `ISDATE(value)`

### Behavior
- Recognizes serial dates and parseable date tokens under deterministic locale rules.

### Examples
- `ISDATE("2026-02-19") -> TRUE`

### Error Cases
- Non-date values return FALSE, not an error.

### Notes
- Not specified in spec.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_isdate`
- Proposed file: `base/src/functions/date_and_time.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISDATE.md


---

## ISEMAIL — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Validates whether text is an email-like address.

### Syntax
- Excel: `ISEMAIL(value)`
- Google Sheets: `ISEMAIL(value)`

### Behavior
- Uses syntax-based validation without external network checks.

### Examples
- `ISEMAIL("a@b.com") -> TRUE`

### Error Cases
- Non-text values return FALSE.

### Notes
- Not specified in spec.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_isemail`
- Proposed file: `base/src/functions/text.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISEMAIL.md


---

## ISERR — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_iserr
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns TRUE if value is any error except #N/A.

### Syntax
- Excel: `ISERR(value)`
- Google Sheets: `ISERR(value)`

### Behavior
- Checks error type class and excludes NA-class errors.

### Examples
- `ISERR(#DIV/0!) -> TRUE`

### Error Cases
- Non-error values return FALSE.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_iserr`
- File: `base/src/functions/information.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISERR.md


---

## ISERROR — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_iserror
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns TRUE if value is any error.

### Syntax
- Excel: `ISERROR(value)`
- Google Sheets: `ISERROR(value)`

### Behavior
- Detects generic error class values.

### Examples
- `ISERROR(#N/A) -> TRUE`

### Error Cases
- Non-error values return FALSE.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_iserror`
- File: `base/src/functions/information.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISERROR.md


---

## ISEVEN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_iseven
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns TRUE when number is even.

### Syntax
- Excel: `ISEVEN(number)`
- Google Sheets: `ISEVEN(number)`

### Behavior
- Evaluates parity on integer equivalent of input as supported by host coercion.

### Examples
- `ISEVEN(4) -> TRUE`

### Error Cases
- Non-numeric inputs return error.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_iseven`
- File: `base/src/functions/information.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISEVEN.md


---

## ISFORMULA — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_isformula
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Checks whether referenced cell contains a formula.

### Syntax
- Excel: `ISFORMULA(reference)`
- Google Sheets: `ISFORMULA(reference)`

### Behavior
- For static evaluator, determines formula-flag metadata for the reference.

### Examples
- `ISFORMULA(A1) -> TRUE`

### Error Cases
- Invalid reference returns #REF! style error.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_isformula`
- File: `base/src/functions/information.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISFORMULA.md


---

## ISLOGICAL — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_islogical
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns TRUE if value is logical TRUE/FALSE.

### Syntax
- Excel: `ISLOGICAL(value)`
- Google Sheets: `ISLOGICAL(value)`

### Behavior
- Type check for boolean values only.

### Examples
- `ISLOGICAL(TRUE) -> TRUE`

### Error Cases
- Non-boolean values return FALSE.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_islogical`
- File: `base/src/functions/information.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISLOGICAL.md


---

## ISNA — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_isna
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Checks if value is #N/A error.

### Syntax
- Excel: `ISNA(value)`
- Google Sheets: `ISNA(value)`

### Behavior
- Returns TRUE only for #N/A variant and FALSE otherwise.

### Examples
- `ISNA(#N/A) -> TRUE`

### Error Cases
- Non-errors return FALSE.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_isna`
- File: `base/src/functions/information.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISNA.md


---

## ISNONTEXT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_isnontext
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns TRUE if value is not text.

### Syntax
- Excel: `ISNONTEXT(value)`
- Google Sheets: `ISNONTEXT(value)`

### Behavior
- Performs strict type test for text values.

### Examples
- `ISNONTEXT(5) -> TRUE`

### Error Cases
- No error conditions; returns FALSE for text.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_isnontext`
- File: `base/src/functions/information.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISNONTEXT.md


---

## ISNUMBER — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_isnumber
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Checks whether value is numeric.

### Syntax
- Excel: `ISNUMBER(value)`
- Google Sheets: `ISNUMBER(value)`

### Behavior
- Recognizes numeric scalars/serials after deterministic coercion.

### Examples
- `ISNUMBER("3") -> TRUE`

### Error Cases
- No errors; returns FALSE for non-numeric.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_isnumber`
- File: `base/src/functions/information.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISNUMBER.md


---

## ISO.CEILING — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Rounds value up to nearest multiple using ISO week-compatible numeric behavior.

### Syntax
- Excel: `ISO.CEILING(number, [significance], [mode])`
- Google Sheets: `ISO.CEILING(number, [significance], [mode])`

### Behavior
- Applies ISO-compatible ceiling behavior for number/significance/mode.

### Examples
- `ISO.CEILING(12.2) -> 13`

### Error Cases
- Invalid significance or mode returns error.

### Notes
- Not specified in spec.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_iso_ceiling`
- Proposed file: `base/src/functions/mathematical.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISO.CEILING.md


---

## ISODD — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_isodd
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns TRUE if number is odd.

### Syntax
- Excel: `ISODD(number)`
- Google Sheets: `ISODD(number)`

### Behavior
- Checks parity after numeric coercion.

### Examples
- `ISODD(3) -> TRUE`

### Error Cases
- Non-numeric input returns error.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_isodd`
- File: `base/src/functions/information.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISODD.md


---

## ISOMITTED — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns TRUE for omitted arguments in array formulas or omitted value contexts.

### Syntax
- Excel: `ISOMITTED(value)`
- Google Sheets: `ISOMITTED(value)`

### Behavior
- Detects omitted optional arguments in function call context.

### Examples
- `ISOMITTED(, ) -> TRUE`

### Error Cases
- Standalone invocation may always return FALSE in non-array contexts.

### Notes
- Not specified in spec.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_isomitted`
- Proposed file: `base/src/functions/information.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISOMITTED.md


---

## ISOWEEKNUM — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_isoweeknum
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the ISO week number for a date.

### Syntax
- Excel: `ISOWEEKNUM(date)`
- Google Sheets: `ISOWEEKNUM(date)`

### Behavior
- Computes ISO-8601 week number deterministically.

### Examples
- `ISOWEEKNUM("2026-02-19") -> 8`

### Error Cases
- Invalid date returns error.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_isoweeknum`
- File: `base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISOWEEKNUM.md


---

## ISPMT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_ispmt
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns interest paid during a payment period on an interest-only loan.

### Syntax
- Excel: `ISPMT(rate, per, nper, pv, fv, [type])`
- Google Sheets: `ISPMT(rate, per, nper, pv, [fv], [type])`

### Behavior
- Calculates principal-only reduction component per period with deterministic ordering.

### Examples
- `ISPMT(0.08/12, 1, 12, -1000) -> -6.22`

### Error Cases
- Invalid terms produce domain errors.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_ispmt`
- File: `base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISPMT.md


---

## ISREF — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_isref
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns TRUE if value is a reference.

### Syntax
- Excel: `ISREF(value)`
- Google Sheets: `ISREF(value)`

### Behavior
- Validates reference type and range validity.

### Examples
- `ISREF(A1) -> TRUE`

### Error Cases
- Non-reference inputs return FALSE unless invalid reference error.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_isref`
- File: `base/src/functions/information.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISREF.md


---

## ISTEXT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_istext
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns TRUE when value is text.

### Syntax
- Excel: `ISTEXT(value)`
- Google Sheets: `ISTEXT(value)`

### Behavior
- Type-checks text semantics strictly.

### Examples
- `ISTEXT("abc") -> TRUE`

### Error Cases
- No errors; FALSE for non-text values.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_istext`
- File: `base/src/functions/information.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISTEXT.md


---

## ISURL — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Checks whether text resembles a URL.

### Syntax
- Excel: `ISURL(value)`
- Google Sheets: `ISURL(value)`

### Behavior
- Validates URL-like structure (scheme/host/path) without dereferencing.

### Examples
- `ISURL("https://example.com") -> TRUE`

### Error Cases
- Non-text values return FALSE.

### Notes
- Not specified in spec.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_isurl`
- Proposed file: `base/src/functions/information.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ISURL.md


---

## JIS — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts text to Japanese Industrial Standards character set representation.

### Syntax
- Excel: `JIS(text)`
- Google Sheets: `JIS(text)`

### Behavior
- Character set conversion helper with deterministic encoding behavior.

### Examples
- `JIS("abc") -> "abc"`

### Error Cases
- Unrepresentable values may return conversion error.

### Notes
- Not specified in spec.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_jis`
- Proposed file: `base/src/functions/text.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/JIS.md


---

## JOIN — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Concatenates strings with a delimiter.

### Syntax
- Excel: `JOIN(delimiter, value1, [value2], ...)`
- Google Sheets: `JOIN(delimiter, value1, [value2], ...)`

### Behavior
- Joins values in order with delimiter, skipping empty values where host-defined.

### Examples
- `JOIN(",", "a", "b", "c") -> "a,b,c"`

### Error Cases
- Invalid delimiter types return errors.

### Notes
- Not specified in spec.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_join`
- Proposed file: `base/src/functions/text.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/JOIN.md


---

## KURT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_kurt
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the kurtosis of a data set.

### Syntax
- Excel: `KURT(number1, [number2], ...)`
- Google Sheets: `KURT(number1, [number2], ...)`

### Behavior
- Computes fourth central moment standardized by variance^2.

### Examples
- `KURT(1,2,3,4) -> -1.36`

### Error Cases
- Insufficient samples return error.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_kurt`
- File: `base/src/functions/statistical/count_and_average.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/KURT.md


---

## LAMBDA — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Defines reusable inline function.

### Syntax
- Excel: `LAMBDA(parameters, calculation)`
- Google Sheets: `LAMBDA(parameters, calculation)`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `LAMBDA(x, x+1)`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_lambda`
- Pseudocode: deterministic parsing, coercion, and computation.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/LAMBDA.md


---

## LARGE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_large
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the k-th largest value in dataset.

### Syntax
- Excel: `LARGE(array, k)`
- Google Sheets: `LARGE(array, k)`

### Behavior
- Sorts values deterministically and returns k-th index from high end.

### Examples
- `LARGE({1,2,3},2) -> 2`

### Error Cases
- Invalid k or insufficient entries returns error.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_large`
- File: `base/src/functions/statistical/count_and_average.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/LARGE.md


---

## LCM — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_lcm
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns least common multiple of integers.

### Syntax
- Excel: `LCM(number1, [number2], ...)`
- Google Sheets: `LCM(number1, [number2], ...)`

### Behavior
- Computes LCM across normalized integers with deterministic overflow behavior.

### Examples
- `LCM(4,6) -> 12`

### Error Cases
- Non-numeric inputs return error.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_lcm`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/LCM.md


---

## LEFT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: N
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_left
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns leftmost characters from a text string.

### Syntax
- Excel: `LEFT(text, [num_chars])`
- Google Sheets: `LEFT(text, [num_chars])`

### Behavior
- Returns prefix string of requested length with default 1.

### Examples
- `LEFT("hello", 2) -> "he"`

### Error Cases
- Negative count returns error.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_left`
- File: `base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/LEFT.md


---

## LEFTB — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns leftmost bytes from a text string.

### Syntax
- Excel: `LEFTB(text, [num_bytes])`
- Google Sheets: `LEFTB(text, [num_bytes])`

### Behavior
- Uses byte-length semantics for multi-byte encodings.

### Examples
- `LEFTB("hello", 2) -> "he"`

### Error Cases
- Invalid count returns error.

### Notes
- Not specified in spec.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_leftb`
- Proposed file: `base/src/functions/text.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/LEFTB.md


---

## LEN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: N
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_len
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns character count of text.

### Syntax
- Excel: `LEN(text)`
- Google Sheets: `LEN(text)`

### Behavior
- Counts characters after deterministic normalization.

### Examples
- `LEN("hello") -> 5`

### Error Cases
- Non-text values are coerced by host rules or return 0 depending on context.

### Notes
- Not specified in spec.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_len`
- File: `base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/LEN.md


---

## LENB — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns byte length of a text string.

### Syntax
- Excel: `LENB(text)`
- Google Sheets: `LENB(text)`

### Behavior
- Counts bytes according to default encoding rules.

### Examples
- `LENB("hello") -> 5`

### Error Cases
- Non-text values are coerced or return 0 by type policy.

### Notes
- Not specified in spec.

### Code Location
- Not implemented in IronCalc.
- Proposed handler: `fn_lenb`
- Proposed file: `base/src/functions/text.rs`
- Pseudocode:
  - Validate argument count and coercion rules.
  - Execute deterministic Excel/Sheets-compatible operation.
  - Return stable output including errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/LENB.md


---

## LET — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Assigns names to intermediate values in formulas.

### Syntax
- Excel: `LET(name1, value1, ... , calculation)`
- Google Sheets: `LET(name1, value1, ... , calculation)`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `LET(x,1,y,2,x+y)`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_let`
- Pseudocode: deterministic parsing, coercion, and computation.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/LET.md


---

## LINEST — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: matrix

## Spec Summary
### Purpose
Returns regression statistics for x/y data.

### Syntax
- Excel: `LINEST(known_ys, known_xs, [const], [stats])`
- Google Sheets: `LINEST(known_ys, known_xs, [const], [stats])`

### Behavior
- Linear regression fit with optional statistics output.

### Examples
- `LINEST({1,2,3},{1,2,3}) -> {1,0}`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/statistical/regression.rs`
- Proposed handler: `fn_linest`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/LINEST.md


---

## LN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_ln
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns natural logarithm of a number.

### Syntax
- Excel: `LN(number)`
- Google Sheets: `LN(number)`

### Behavior
- Logarithm base e with domain checks.

### Examples
- `LN(10) -> 2.302585

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_ln`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/LN.md


---

## LOG — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_log
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns logarithm of a number to a base.

### Syntax
- Excel: `LOG(number, [base])`
- Google Sheets: `LOG(number, [base])`

### Behavior
- Base-10 unless base is provided.

### Examples
- `LOG(100,10) -> 2

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_log`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/LOG.md


---

## LOG10 — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_log10
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns base-10 logarithm.

### Syntax
- Excel: `LOG10(number)`
- Google Sheets: `LOG10(number)`

### Behavior
- Computes log10 with host-defined error behavior.

### Examples
- `LOG10(1000) -> 3

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_log10`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/LOG10.md


---

## LOGEST — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: matrix

## Spec Summary
### Purpose
Returns coefficients/statistics for log-linear fit.

### Syntax
- Excel: `LOGEST(known_ys, known_xs, [const], [stats])`
- Google Sheets: `LOGEST(known_ys, known_xs, [const], [stats])`

### Behavior
- Fits exponential trend in linearized form.

### Examples
- `LOGEST({1,10,100},{1,2,3}) -> {10,0}`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/statistical/regression.rs`
- Proposed handler: `fn_logest`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/LOGEST.md


---

## LOGNORM.DIST — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the lognormal distribution value.

### Syntax
- Excel: `LOGNORM.DIST(x, mean, standard_dev, cumulative)`
- Google Sheets: `LOGNORM.DIST(x, mean, standard_dev, cumulative)`

### Behavior
- PDF/CDF based on cumulative flag.

### Examples
- `LOGNORM.DIST(10,0,1,TRUE) -> 0.8413

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/statistical/log_normal.rs`
- Proposed handler: `fn_lognorm_dist`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/LOGNORM.DIST.md


---

## LOGNORM.INV — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns inverse lognormal value.

### Syntax
- Excel: `LOGNORM.INV(probability, mean, standard_dev)`
- Google Sheets: `LOGNORM.INV(probability, mean, standard_dev)`

### Behavior
- Inverts lognormal CDF for target probability.

### Examples
- `LOGNORM.INV(0.5,0,1) -> 1.6487

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/statistical/log_normal.rs`
- Proposed handler: `fn_lognorm_inv`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/LOGNORM.INV.md


---

## LOOKUP — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_lookup
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Looks up value in one-row or one-column array.

### Syntax
- Excel: `LOOKUP(lookup_value, lookup_array, [result_array])`
- Google Sheets: `LOOKUP(lookup_value, lookup_array, [result_array])`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.

### Examples
- `LOOKUP(2,{1,2,3},{10,20,30}) -> 20`

### Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible date arithmetic.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_lookup`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/LOOKUP.md


---

## LOWER — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_lower
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts text to lowercase.

### Syntax
- Excel: `LOWER(text)`
- Google Sheets: `LOWER(text)`

### Behavior
- Performs deterministic case conversion.

### Examples
- `LOWER("ABC") -> "abc"`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_lower`
- File: `base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/LOWER.md


---

## LT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns TRUE if value1 < value2.

### Syntax
- Excel: `LT(value1, value2)`
- Google Sheets: `LT(value1, value2)`

### Behavior
- Compares two values with host semantics.

### Examples
- `LT(2,5) -> TRUE`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/logical.rs`
- Proposed handler: `fn_lt`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/LT.md


---

## LTE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns TRUE if value1 <= value2.

### Syntax
- Excel: `LTE(value1, value2)`
- Google Sheets: `LTE(value1, value2)`

### Behavior
- Less-or-equal comparison.

### Examples
- `LTE(2,2) -> TRUE`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/logical.rs`
- Proposed handler: `fn_lte`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/LTE.md


---

## MAKEARRAY — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Creates an array with lambda-generated values.

### Syntax
- Excel: `MAKEARRAY(rows, cols, lambda)`
- Google Sheets: `MAKEARRAY(rows, cols, lambda)`

### Behavior
- Calls lambda for each row/col index.

### Examples
- `MAKEARRAY(2,2,LAMBDA(r,c,r+c)) -> {{2,3},{3,4}}`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_makearray`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MAKEARRAY.md


---

## MAP — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Applies lambda across arrays.

### Syntax
- Excel: `MAP(array1, [array2, ...], lambda)`
- Google Sheets: `MAP(array1, [array2, ...], lambda)`

### Behavior
- Per-element mapping with deterministic argument alignment.

### Examples
- `MAP({1,2,3}, LAMBDA(x,x*2)) -> {2,4,6}`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_map`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MAP.md


---

## MARGINOFERROR — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns margin of error for estimate.

### Syntax
- Excel: `MARGINOFERROR(range, confidence, [stddev], [population])`
- Google Sheets: `MARGINOFERROR(range, confidence, [stddev], [population])`

### Behavior
- Uses mean and dispersion to compute interval margin.

### Examples
- `MARGINOFERROR({1,2,3},0.95) -> 0.58`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/statistical/standardize.rs`
- Proposed handler: `fn_marginoferror`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MARGINOFERROR.md


---

## MATCH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_match
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns position of value within array.

### Syntax
- Excel: `MATCH(lookup_value, lookup_array, [match_type])`
- Google Sheets: `MATCH(lookup_value, lookup_array, [match_type])`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.

### Examples
- `MATCH("b",{"a","b","c"},0) -> 2`

### Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible date arithmetic.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_match`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MATCH.md


---

## MAX — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_max
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns maximum value.

### Syntax
- Excel: `MAX(number1, [number2], ...)`
- Google Sheets: `MAX(number1, [number2], ...)`

### Behavior
- Returns largest scalar in inputs.

### Examples
- `MAX(1,5,3) -> 5`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_max`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MAX.md


---

## MAXA — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_maxa
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns maximum supporting text/logicals.

### Syntax
- Excel: `MAXA(value1, [value2], ...)`
- Google Sheets: `MAXA(value1, [value2], ...)`

### Behavior
- Includes text/logical conversion rules.

### Examples
- `MAXA(1,TRUE,"2") -> 2`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_maxa`
- File: `base/src/functions/statistical/count_and_average.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MAXA.md


---

## MAXIFS — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_maxifs
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/if_ifs.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns max with criteria conditions.

### Syntax
- Excel: `MAXIFS(max_range, criteria_range1, criteria1, ...)`
- Google Sheets: `MAXIFS(max_range, criteria_range1, criteria1, ...)`

### Behavior
- Filters then returns highest match.

### Examples
- `MAXIFS({1,2,3},{1,2,3},{">1"}) -> 2`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_maxifs`
- File: `base/src/functions/statistical/if_ifs.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MAXIFS.md


---

## MDETERM — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns determinant of a square matrix.

### Syntax
- Excel: `MDETERM(array)`
- Google Sheets: `MDETERM(array)`

### Behavior
- Deterministic determinant calculation.

### Examples
- `MDETERM({{1,2},{3,4}}) -> -2`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_mdeterm`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MDETERM.md


---

## MDURATION — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns modified bond duration.

### Syntax
- Excel: `MDURATION(settlement, maturity, coupon, yield, frequency, [basis])`
- Google Sheets: `MDURATION(settlement, maturity, coupon, yield, frequency, [basis])`

### Behavior
- Duration metric under given bond assumptions.

### Examples
- `MDURATION("1/1/26","1/1/27",0.05,0.04,2) -> 0.95`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/financial.rs`
- Proposed handler: `fn_mduration`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MDURATION.md


---

## MEDIAN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_median
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns median value.

### Syntax
- Excel: `MEDIAN(number1, [number2], ...)`
- Google Sheets: `MEDIAN(number1, [number2], ...)`

### Behavior
- Middle value in sorted list (or average of two).

### Examples
- `MEDIAN({1,3,3,6,7,8,9}) -> 6`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_median`
- File: `base/src/functions/statistical/count_and_average.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MEDIAN.md


---

## MID — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: N
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_mid
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns substring from text.

### Syntax
- Excel: `MID(text, start_num, num_chars)`
- Google Sheets: `MID(text, start_num, num_chars)`

### Behavior
- 1-based positional extraction.

### Examples
- `MID("hello",2,2) -> "el"`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_mid`
- File: `base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MID.md


---

## MIDB — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns byte-based substring.

### Syntax
- Excel: `MIDB(text, start_num, num_chars)`
- Google Sheets: `MIDB(text, start_num, num_chars)`

### Behavior
- Byte-position extraction rules.

### Examples
- `MIDB("hello",2,2) -> "el"`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_midb`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MIDB.md


---

## MIN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_min
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns minimum value.

### Syntax
- Excel: `MIN(number1, [number2], ...)`
- Google Sheets: `MIN(number1, [number2], ...)`

### Behavior
- Returns smallest scalar in inputs.

### Examples
- `MIN(1,5,3) -> 1`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_min`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MIN.md


---

## MINA — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_mina
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns minimum including text/logicals.

### Syntax
- Excel: `MINA(value1, [value2], ...)`
- Google Sheets: `MINA(value1, [value2], ...)`

### Behavior
- Considers special numeric coercion for text/logical values.

### Examples
- `MINA(1,TRUE,"2") -> 0`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_mina`
- File: `base/src/functions/statistical/count_and_average.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MINA.md


---

## MINIFS — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_minifs
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/if_ifs.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns min with criteria conditions.

### Syntax
- Excel: `MINIFS(min_range, criteria_range1, criteria1, ...)`
- Google Sheets: `MINIFS(min_range, criteria_range1, criteria1, ...)`

### Behavior
- Filters then returns lowest match.

### Examples
- `MINIFS({1,2,3},{1,2,3},{">1"}) -> 2`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_minifs`
- File: `base/src/functions/statistical/if_ifs.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MINIFS.md


---

## MINUS — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Subtracts numbers.

### Syntax
- Excel: `MINUS(number1, number2)`
- Google Sheets: `MINUS(number1, number2)`

### Behavior
- Arithmetic subtraction.

### Examples
- `MINUS(10,4) -> 6`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_minus`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MINUS.md


---

## MINUTE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_minute
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns minute from time/date.

### Syntax
- Excel: `MINUTE(serial_number)`
- Google Sheets: `MINUTE(time)`

### Behavior
- 0-59 minute component.

### Examples
- `MINUTE("12:34:56") -> 34`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_minute`
- File: `base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MINUTE.md


---

## MINVERSE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns inverse of matrix.

### Syntax
- Excel: `MINVERSE(array)`
- Google Sheets: `MINVERSE(array)`

### Behavior
- Returns matrix inverse for square matrices.

### Examples
- `MINVERSE({{1,2},{3,4}}) -> {{-2,1},{1.5,-0.5}}`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_minverse`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MINVERSE.md


---

## MIRR — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_mirr
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Modified internal rate of return.

### Syntax
- Excel: `MIRR(values, finance_rate, reinvest_rate)`
- Google Sheets: `MIRR(values, finance_rate, reinvest_rate)`

### Behavior
- IRR variant using separate rates.

### Examples
- `MIRR({-100,100,100},0.1,0.12) -> 0.1097`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_mirr`
- File: `base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MIRR.md


---

## MMULT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: matrix

## Spec Summary
### Purpose
Returns matrix product.

### Syntax
- Excel: `MMULT(array1, array2)`
- Google Sheets: `MMULT(array1, array2)`

### Behavior
- Row-column multiplication rules for matrices.

### Examples
- `MMULT({{1,2},{3,4}},{{1,0},{0,1}}) -> {{1,2},{3,4}}`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_mmult`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MMULT.md


---

## MOD — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_mod
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns remainder after division.

### Syntax
- Excel: `MOD(number, divisor)`
- Google Sheets: `MOD(number, divisor)`

### Behavior
- Remainder with deterministic negative number handling.

### Examples
- `MOD(5,2) -> 1`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_mod`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MOD.md


---

## MODE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns most frequent value.

### Syntax
- Excel: `MODE(number1, [number2], ...)`
- Google Sheets: `MODE(number1, [number2], ...)`

### Behavior
- Single-mode return behavior.

### Examples
- `MODE({1,2,2,3}) -> 2`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_mode`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MODE.md


---

## MODE.MULT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns all most frequent values.

### Syntax
- Excel: `MODE.MULT(number1, [number2], ...)`
- Google Sheets: `MODE.MULT(number1, [number2], ...)`

### Behavior
- Returns all modal values.

### Examples
- `MODE.MULT({1,2,2,3,3}) -> {2,3}`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_mode_mult`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MODE.MULT.md


---

## MODE.SNGL — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns single mode.

### Syntax
- Excel: `MODE.SNGL(number1, [number2], ...)`
- Google Sheets: `MODE.SNGL(number1, [number2], ...)`

### Behavior
- Returns one mode with deterministic tie rules.

### Examples
- `MODE.SNGL({1,2,2,3,3}) -> 2`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_mode_sngl`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MODE.SNGL.md


---

## MONTH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_month
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns month number.

### Syntax
- Excel: `MONTH(serial_number)`
- Google Sheets: `MONTH(date)`

### Behavior
- Returns 1-12.

### Examples
- `MONTH("2026-02-19") -> 2`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_month`
- File: `base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MONTH.md


---

## MROUND — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_mround
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Rounds to nearest multiple.

### Syntax
- Excel: `MROUND(number, multiple)`
- Google Sheets: `MROUND(number, multiple)`

### Behavior
- Rounds to nearest integer multiple.

### Examples
- `MROUND(10,3) -> 9`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_mround`
- File: `base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MROUND.md


---

## MULTINOMIAL — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns multinomial coefficient.

### Syntax
- Excel: `MULTINOMIAL(number1, [number2], ...)`
- Google Sheets: `MULTINOMIAL(number1, [number2], ...)`

### Behavior
- Factorial ratio coefficient.

### Examples
- `MULTINOMIAL(1,2,3) -> 60`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_multinomial`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MULTINOMIAL.md


---

## MULTIPLY — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns product of two numbers.

### Syntax
- Excel: `MULTIPLY(number1, number2)`
- Google Sheets: `MULTIPLY(number1, number2)`

### Behavior
- Arithmetic multiplication.

### Examples
- `MULTIPLY(6,7) -> 42`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_multiply`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MULTIPLY.md


---

## MUNIT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns unit (identity) matrix.

### Syntax
- Excel: `MUNIT(dimension)`
- Google Sheets: `MUNIT(dimension)`

### Behavior
- Produces identity matrix.

### Examples
- `MUNIT(2) -> {{1,0},{0,1}}`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_munit`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/MUNIT.md


---

## N — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_n
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts input to numeric value.

### Syntax
- Excel: `N(value)`
- Google Sheets: `N(value)`

### Behavior
- Boolean/text conversion to number.

### Examples
- `N(TRUE) -> 1`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Implemented in IronCalc.

### Code Location
- Handler: `fn_n`
- File: `base/src/functions/information.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/N.md


---

## NA — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: <inline>
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mod.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns #N/A error.

### Syntax
- Excel: `NA()`
- Google Sheets: `NA()`

### Behavior
- Dedicated missing-value error constructor.

### Examples
- `NA() -> #N/A`

### Error Cases
- Invalid argument count or input values return errors per host semantics.

### Notes
- Not implemented in IronCalc.

### Code Location
- Proposed file: `base/src/functions/information.rs`
- Proposed handler: `fn_na`
- Pseudocode:
  - Validate arguments and coerce inputs.
  - Apply deterministic engine-compatible rules.
  - Compute and return deterministic results.
  - Return standardized error on invalid domain.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/NA.md


---

## NE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Tests whether two values are not equal.

### Syntax
- Excel: `NE(a, b)`
- Google Sheets: `NE(a, b)`

### Behavior
Returns TRUE when values differ, FALSE when they are equal.

### Examples
- `NE(1,2)` -> `TRUE`
- `NE("A","A")` -> `FALSE`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/logical.rs`
- Proposed handler: `fn_ne`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/NE.md


---

## NEGBINOM.DIST — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns negative binomial distribution probabilities.

### Syntax
- Excel: `NEGBINOM.DIST(number, number_s, probability_s, cumulative)`
- Google Sheets: `NEGBINOM.DIST(number, number_s, probability_s, cumulative)`

### Behavior
Computes the negative binomial PMF/CDF depending on `cumulative`.

### Examples
- `NEGBINOM.DIST(1, 5, 0.5, TRUE)` -> `0.03125`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/statistical/binom.rs`
- Proposed handler: `fn_negbinom.dist`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/NEGBINOM.DIST.md


---

## NEGBINOMDIST — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: fn_negbinom_dist
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/binom.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Legacy Excel negative binomial distribution function.

### Syntax
- Excel: `NEGBINOMDIST(f, r, p)`
- Google Sheets: `NEGBINOMDIST(f, r, p)`

### Behavior
Returns the probability of a fixed number of failures before `r` successes.

### Examples
- `NEGBINOMDIST(2, 5, 0.5)` -> `0.05859375`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_negbinom_dist`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/binom.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/NEGBINOMDIST.md


---

## NETWORKDAYS — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_networkdays
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns business days between dates.

### Syntax
- Excel: `NETWORKDAYS(start_date,end_date,[holidays])`
- Google Sheets: `NETWORKDAYS(start_date,end_date,[holidays])`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.

### Examples
- `NETWORKDAYS("2026-01-01","2026-01-10") -> n`

### Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible date arithmetic.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_networkdays`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/NETWORKDAYS.md


---

## NETWORKDAYS.INTL — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns business days with custom weekend mask.

### Syntax
- Excel: `NETWORKDAYS.INTL(start_date,end_date,[weekend],[holidays])`
- Google Sheets: `NETWORKDAYS.INTL(start_date,end_date,[weekend],[holidays])`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.

### Examples
- `NETWORKDAYS.INTL("2026-01-01","2026-01-10",16) -> n`

### Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible date arithmetic.

### Code Location
- Proposed file: `base/src/functions/date_and_time.rs`
- Proposed handler: `fn_networkdays.intl`
- Pseudocode: validate date arguments, apply calendar/business-day logic, return standardized errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/NETWORKDAYS.INTL.md


---

## NOMINAL — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_nominal
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts effective annual rate to nominal interest rate.

### Syntax
- Excel: `NOMINAL(effect_rate, periods)`
- Google Sheets: `NOMINAL(effect_rate, periods)`

### Behavior
Calculates nominal rate by scaling effective rate for compounding periods.

### Examples
- `NOMINAL(0.08, 12)` -> `0.0766`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_nominal`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/NOMINAL.md


---

## NORM.DIST — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns normal distribution values.

### Syntax
- Excel: `NORM.DIST(x, mean, standard_dev, cumulative)`
- Google Sheets: `NORM.DIST(x, mean, standard_dev, cumulative)`

### Behavior
Returns density or cumulative probability for normal distribution.

### Examples
- `NORM.DIST(0, 0, 1, TRUE)` -> `0.5`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/statistical/normal.rs`
- Proposed handler: `fn_norm.dist`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/NORM.DIST.md


---

## NORM.INV — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns inverse of normal CDF.

### Syntax
- Excel: `NORM.INV(probability, mean, standard_dev)`
- Google Sheets: `NORM.INV(probability, mean, standard_dev)`

### Behavior
Returns x such that `NORM.DIST(x, mean, stdev, TRUE)=probability`.

### Examples
- `NORM.INV(0.5, 0, 1)` -> `0`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/statistical/normal.rs`
- Proposed handler: `fn_norm.inv`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/NORM.INV.md


---

## NORM.S.DIST — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Standard normal distribution function.

### Syntax
- Excel: `NORM.S.DIST(z, cumulative)`
- Google Sheets: `NORM.S.DIST(z, cumulative)`

### Behavior
Computes distribution values for mean 0 and standard deviation 1.

### Examples
- `NORM.S.DIST(0, TRUE)` -> `0.5`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/statistical/normal.rs`
- Proposed handler: `fn_norm.s.dist`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/NORM.S.DIST.md


---

## NORM.S.INV — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Inverse of standard normal CDF.

### Syntax
- Excel: `NORM.S.INV(probability)`
- Google Sheets: `NORM.S.INV(probability)`

### Behavior
Returns z-score for the cumulative standard normal probability.

### Examples
- `NORM.S.INV(0.5)` -> `0`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/statistical/normal.rs`
- Proposed handler: `fn_norm.s.inv`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/NORM.S.INV.md


---

## NOT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_not
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/logical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Logical negation.

### Syntax
- Excel: `NOT(logical)`
- Google Sheets: `NOT(logical)`

### Behavior
Returns TRUE when input is FALSE and FALSE when input is TRUE.

### Examples
- `NOT(TRUE)` -> `FALSE`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_not`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/logical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/NOT.md


---

## NOW — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_now
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns current date-time.

### Syntax
- Excel: `NOW()`
- Google Sheets: `NOW()`

### Behavior
Returns the engine current timestamp at deterministic evaluation time.

### Examples
- `NOW()` -> serial date-time

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_now`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/NOW.md


---

## NPER — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_nper
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns number of payment periods for a loan.

### Syntax
- Excel: `NPER(rate, pmt, pv, [fv], [type], [guess])`
- Google Sheets: `NPER(rate, pmt, pv, [fv], [type], [guess])`

### Behavior
Solves for number of periodic payments given rates and values.

### Examples
- `NPER(0.05/12, -1000, 20000)` -> `23.45`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_nper`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/NPER.md


---

## NPV — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_npv
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes net present value of a cash flow stream.

### Syntax
- Excel: `NPV(rate, value1, [value2], ...)`
- Google Sheets: `NPV(rate, value1, [value2], ...)`

### Behavior
Discounts future payments with constant rate and sums present value.

### Examples
- `NPV(0.1, 100, 110)` -> `199.09`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_npv`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/NPV.md


---

## NUMBERVALUE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts localized text into numeric value.

### Syntax
- Excel: `NUMBERVALUE(text, [decimal_separator], [group_separator])`
- Google Sheets: `NUMBERVALUE(text, [decimal_separator], [group_separator])`

### Behavior
Parses numeric text using explicit decimal and thousands separators.

### Examples
- `NUMBERVALUE("1,234.56", ".", ",")` -> `1234.56`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_numbervalue`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/NUMBERVALUE.md


---

## OCT2BIN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_oct2bin
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/number_basis.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts octal to binary.

### Syntax
- Excel: `OCT2BIN(number, [places])`
- Google Sheets: `OCT2BIN(number, [places])`

### Behavior
Converts signed octal string into binary representation.

### Examples
- `OCT2BIN(10)` -> `1010`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_oct2bin`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/number_basis.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/OCT2BIN.md


---

## OCT2DEC — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_oct2dec
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/number_basis.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts octal to decimal.

### Syntax
- Excel: `OCT2DEC(number)`
- Google Sheets: `OCT2DEC(number)`

### Behavior
Converts octal value to base-10 number.

### Examples
- `OCT2DEC(10)` -> `8`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_oct2dec`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/number_basis.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/OCT2DEC.md


---

## OCT2HEX — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_oct2hex
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/number_basis.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts octal to hexadecimal.

### Syntax
- Excel: `OCT2HEX(number, [places])`
- Google Sheets: `OCT2HEX(number, [places])`

### Behavior
Converts octal value to hexadecimal notation.

### Examples
- `OCT2HEX(10)` -> `8`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_oct2hex`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/engineering/number_basis.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/OCT2HEX.md


---

## ODD — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_odd
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Rounds away from zero to nearest odd integer.

### Syntax
- Excel: `ODD(number)`
- Google Sheets: `ODD(number)`

### Behavior
Returns the nearest odd integer with magnitude >= input absolute value.

### Examples
- `ODD(2.5)` -> `3`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_odd`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ODD.md


---

## ODDFPRICE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns odd-first-period bond price.

### Syntax
- Excel: `ODDFPRICE(settlement, maturity, issue, first_coupon, rate, yld, redemption, frequency, [basis])`
- Google Sheets: `ODDFPRICE(settlement, maturity, issue, first_coupon, rate, yld, redemption, frequency, [basis])`

### Behavior
Uses odd first coupon period conventions to calculate full-price bond value.

### Examples
- `ODDFPRICE("2026-01-01","2027-01-01","2025-01-01","2025-10-31",0.05,0.04,100,2,0)` -> `100+`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/financial.rs`
- Proposed handler: `fn_oddfprice`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ODDFPRICE.md


---

## ODDFYIELD — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns odd-first-period bond yield.

### Syntax
- Excel: `ODDFYIELD(settlement, maturity, issue, first_coupon, rate, pr, redemption, frequency, [basis])`
- Google Sheets: `ODDFYIELD(settlement, maturity, issue, first_coupon, rate, pr, redemption, frequency, [basis])`

### Behavior
Computes yield for bonds with odd first period.

### Examples
- `ODDFYIELD("2026-01-01","2027-01-01","2025-01-01","2025-10-31",0.05,100,100,2,0)` -> `0.04`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/financial.rs`
- Proposed handler: `fn_oddfyield`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ODDFYIELD.md


---

## ODDLPRICE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns odd-last-period bond price.

### Syntax
- Excel: `ODDLPRICE(settlement, maturity, last_interest, rate, yld, redemption, frequency, [basis])`
- Google Sheets: `ODDLPRICE(settlement, maturity, last_interest, rate, yld, redemption, frequency, [basis])`

### Behavior
Prices bonds where last period is not standard length.

### Examples
- `ODDLPRICE("2026-01-01","2027-01-01","2026-12-31",0.05,0.04,100,2,0)` -> `100+`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/financial.rs`
- Proposed handler: `fn_oddlprice`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ODDLPRICE.md


---

## ODDLYIELD — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns odd-last-period bond yield.

### Syntax
- Excel: `ODDLYIELD(settlement, maturity, last_coupon, rate, pr, redemption, frequency, [basis])`
- Google Sheets: `ODDLYIELD(settlement, maturity, last_coupon, rate, pr, redemption, frequency, [basis])`

### Behavior
Computes yield for odd-last bond schedules.

### Examples
- `ODDLYIELD("2026-01-01","2027-01-01","2026-12-31",0.05,100,100,2,0)` -> `0.04`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/financial.rs`
- Proposed handler: `fn_oddlyield`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ODDLYIELD.md


---

## OFFSET — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_offset
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns range offset from a reference.

### Syntax
- Excel: `OFFSET(reference, rows, cols, [height], [width])`
- Google Sheets: `OFFSET(reference, rows, cols, [height], [width])`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.

### Examples
- `OFFSET(A1,1,1,2,1)`

### Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible date arithmetic.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_offset`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/OFFSET.md


---

## OR — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_or
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/logical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Logical OR across arguments.

### Syntax
- Excel: `OR(logical1, [logical2], ...)`
- Google Sheets: `OR(logical1, [logical2], ...)`

### Behavior
Returns TRUE if any argument evaluates to TRUE.

### Examples
- `OR(FALSE, TRUE)` -> `TRUE`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_or`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/logical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/OR.md


---

## PDURATION — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_pduration
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns Macauley modified duration for a security.

### Syntax
- Excel: `PDURATION(rate, pv, fv, nper)`
- Google Sheets: `PDURATION(rate, pv, fv, nper)`

### Behavior
Computes weighted average time to receive cash flows for a zero-coupon bond approximation.

### Examples
- `PDURATION(0.08, 95, 100, 10)` -> `6.2`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_pduration`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PDURATION.md


---

## PEARSON — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_pearson
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/pearson.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns Pearson product-moment correlation coefficient.

### Syntax
- Excel: `PEARSON(array1, array2)`
- Google Sheets: `PEARSON(array1, array2)`

### Behavior
Calculates linear correlation between paired data ranges.

### Examples
- `PEARSON({1,2,3},{2,4,6})` -> `1`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_pearson`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/pearson.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PEARSON.md


---

## PERCENTILE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the k-th percentile of data.

### Syntax
- Excel: `PERCENTILE(array, k)`
- Google Sheets: `PERCENTILE(array, k)`

### Behavior
Computes percentile by Excel interpolation variant.

### Examples
- `PERCENTILE({1,2,3,4},0.5)` -> `2.5`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_percentile`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PERCENTILE.md


---

## PERCENTILE.EXC — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns percentile using exclusive interpolation.

### Syntax
- Excel: `PERCENTILE.EXC(array, k)`
- Google Sheets: `PERCENTILE.EXC(array, k)`

### Behavior
Computes exclusive percentile excluding min/max endpoints.

### Examples
- `PERCENTILE.EXC({1,2,3,4},0.5)` -> `2.5`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_percentile.exc`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PERCENTILE.EXC.md


---

## PERCENTILE.INC — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns percentile with inclusive interpolation.

### Syntax
- Excel: `PERCENTILE.INC(array, k)`
- Google Sheets: `PERCENTILE.INC(array, k)`

### Behavior
Computes inclusive percentile including min/max.

### Examples
- `PERCENTILE.INC({1,2,3,4},0.5)` -> `2.5`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_percentile.inc`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PERCENTILE.INC.md


---

## PERCENTRANK — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns rank percentile of a value in a data set.

### Syntax
- Excel: `PERCENTRANK(array, x, [significance])`
- Google Sheets: `PERCENTRANK(array, x, [significance])`

### Behavior
Finds percentile position of `x` with optional significance.

### Examples
- `PERCENTRANK({1,2,3,4},3)` -> `0.6666667`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_percentrank`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PERCENTRANK.md


---

## PERCENTRANK.EXC — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns exclusive percentile rank.

### Syntax
- Excel: `PERCENTRANK.EXC(array, x, [significance])`
- Google Sheets: `PERCENTRANK.EXC(array, x, [significance])`

### Behavior
Calculates percentile with exclusive interpolation constraints.

### Examples
- `PERCENTRANK.EXC({1,2,3,4},3)` -> `0.6667`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_percentrank.exc`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PERCENTRANK.EXC.md


---

## PERCENTRANK.INC — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns inclusive percentile rank.

### Syntax
- Excel: `PERCENTRANK.INC(array, x, [significance])`
- Google Sheets: `PERCENTRANK.INC(array, x, [significance])`

### Behavior
Calculates percentile with inclusive interpolation constraints.

### Examples
- `PERCENTRANK.INC({1,2,3,4},3)` -> `0.6667`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_percentrank.inc`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PERCENTRANK.INC.md


---

## PERMUT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns number of permutations of items.

### Syntax
- Excel: `PERMUT(number, number_chosen)`
- Google Sheets: `PERMUT(number, number_chosen)`

### Behavior
Counts ordered selections without repetition.

### Examples
- `PERMUT(5,3)` -> `60`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_permut`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PERMUT.md


---

## PERMUTATIONA — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns number of permutations with repetition.

### Syntax
- Excel: `PERMUTATIONA(number, number_chosen)`
- Google Sheets: `PERMUTATIONA(number, number_chosen)`

### Behavior
Counts ordered selections with repetition.

### Examples
- `PERMUTATIONA(5,3)` -> `125`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_permutationa`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PERMUTATIONA.md


---

## PHI — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_phi
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/phi.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the density of standard normal distribution.

### Syntax
- Excel: `PHI(x)`
- Google Sheets: `PHI(x)`

### Behavior
Computes standard normal PDF at x.

### Examples
- `PHI(0)` -> `0.3989422804`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_phi`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/phi.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PHI.md


---

## PHONETIC — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts text to phonetic reading.

### Syntax
- Excel: `PHONETIC(text)`
- Google Sheets: `PHONETIC(text)`

### Behavior
Returns phonetic transcription for Japanese text.

### Examples
- `PHONETIC("")` -> ``

- Note: Non-ASCII characters omitted. See spec for full text.

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_phonetic`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PHONETIC.md


---

## PI — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_pi
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the value of .

- Note: Non-ASCII characters omitted. See spec for full text.

### Syntax
- Excel: `PI()`
- Google Sheets: `PI()`

### Behavior
Returns the mathematical constant pi.

### Examples
- `PI()` -> `3.14159265358979`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_pi`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PI.md


---

## PIVOTBY — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Applies reduction to data and returns reshaped output.

### Syntax
- Excel: `PIVOTBY(data, pivot_column, pivot_value, data_column, function)`
- Google Sheets: `PIVOTBY(data, pivot_column, pivot_value, data_column, function)`

### Behavior
Groups and reduces input data into a pivot table structure.

### Examples
- `PIVOTBY(A1:C4,"Type","Value",SUM)` -> `table`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/table.rs`
- Proposed handler: `fn_pivotby`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PIVOTBY.md


---

## PMT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_pmt
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns periodic loan payment.

### Syntax
- Excel: `PMT(rate, nper, pv, [fv], [type])`
- Google Sheets: `PMT(rate, nper, pv, [fv], [type])`

### Behavior
Calculates payment amount using amortization formula.

### Examples
- `PMT(0.05/12, 60, 10000)` -> `-188.71`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_pmt`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PMT.md


---

## POISSON.DIST — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns Poisson distribution values.

### Syntax
- Excel: `POISSON.DIST(x, mean, cumulative)`
- Google Sheets: `POISSON.DIST(x, mean, cumulative)`

### Behavior
Computes Poisson probability mass or cumulative probability.

### Examples
- `POISSON.DIST(2,3,TRUE)` -> `0.42319008`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/statistical/distribution.rs`
- Proposed handler: `fn_poisson.dist`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/POISSON.DIST.md


---

## POW — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Raises base to a power.

### Syntax
- Excel: `POW(number, power)`
- Google Sheets: `POW(number, power)`

### Behavior
Equivalent to exponentiation operator.

### Examples
- `POW(2,3)` -> `8`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_pow`
- Pseudocode: validate args, parse coercions, compute deterministic result, return formula errors on invalid inputs.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/POW.md


---

## POWER — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_power
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Raises base to a power.

### Syntax
- Excel: `POWER(number, power)`
- Google Sheets: `POWER(number, power)`

### Behavior
Computes number raised to an exponent.

### Examples
- `POWER(2,3)` -> `8`

### Error Cases
- Invalid argument types, arity, or domain values return standardized spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_power`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/POWER.md


---

## PPMT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_ppmt
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns payment for a loan interest and principal with constant payments.

### Syntax
- Excel: `PPMT(rate, per, nper, pv, [fv], [type])`
- Google Sheets: `PPMT(rate, per, nper, pv, [fv], [type])`

### Behavior
Computes principal portion of payment at period `per`.

### Examples
- `PPMT(0.08/12,1,36,10000,0,0)` -> negative number

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_ppmt`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PPMT.md


---

## PRICE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns price of a bond per $100 face value.

### Syntax
- Excel: `PRICE(settlement, maturity, rate, yld, redemption, frequency, [basis])`
- Google Sheets: `PRICE(settlement, maturity, rate, yld, redemption, frequency, [basis])`

### Behavior
Computes clean/dirty price depending on schedule assumptions.

### Examples
- `PRICE("2026-01-01","2027-01-01",0.05,0.04,100,2,0)` -> approx

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_price`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PRICE.md


---

## PRICEDISC — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns discounted security price.

### Syntax
- Excel: `PRICEDISC(settlement, maturity, discount, redemption, [basis])`
- Google Sheets: `PRICEDISC(settlement, maturity, discount, redemption, [basis])`

### Behavior
Prices bond with discount rate and redemption value.

### Examples
- `PRICEDISC("2026-01-01","2027-01-01",0.06,100)` -> approx

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_pricedisc`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PRICEDISC.md


---

## PRICEMAT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns security price with maturity interest.

### Syntax
- Excel: `PRICEMAT(settlement, maturity, issue, rate, yld, [basis])`
- Google Sheets: `PRICEMAT(settlement, maturity, issue, rate, yld, [basis])`

### Behavior
Calculates price using issue date and annual rate context.

### Examples
- `PRICEMAT("2026-01-01","2027-01-01","2025-01-01",0.05,0.04)` -> approx

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_pricemat`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PRICEMAT.md


---

## PROB — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns cumulative probability from a list, given bounds.

### Syntax
- Excel: `PROB(x_range, prob_range, [lower_limit], [upper_limit])`
- Google Sheets: `PROB(x_range, prob_range, [lower_limit], [upper_limit])`

### Behavior
Integrates discrete probabilities within optional limits.

### Examples
- `PROB({0,1,2},{0.2,0.5,0.3},0,1)` -> `0.7`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_prob`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PROB.md


---

## PRODUCT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_product
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Multiplies all numeric arguments.

### Syntax
- Excel: `PRODUCT(number1, [number2], ...)`
- Google Sheets: `PRODUCT(number1, [number2], ...)`

### Behavior
Returns product of all numbers after coercion.

### Examples
- `PRODUCT(2,3,4)` -> `24`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_product`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PRODUCT.md


---

## PROPER — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts text to proper case (title case).

### Syntax
- Excel: `PROPER(text)`
- Google Sheets: `PROPER(text)`

### Behavior
Capitalizes each word in text; other characters become lower-case.

### Examples
- `PROPER("john smith")` -> `John Smith`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_proper`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PROPER.md


---

## PV — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_pv
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns present value of an investment.

### Syntax
- Excel: `PV(rate, nper, pmt, [fv], [type])`
- Google Sheets: `PV(rate, nper, pmt, [fv], [type])`

### Behavior
Discounts future payments and optional future value to current value.

### Examples
- `PV(0.05/12, 60, -100, 0)` -> positive amount

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_pv`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/PV.md


---

## QUARTILE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns quartile of a data set.

### Syntax
- Excel: `QUARTILE(array, quart)`
- Google Sheets: `QUARTILE(array, quart)`

### Behavior
Returns one of 1st, 2nd, 3rd, or 4th quartiles.

### Examples
- `QUARTILE({1,2,3,4},1)` -> `1.75`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/statistical/percentile.rs`
- Proposed handler: `fn_quartile`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/QUARTILE.md


---

## QUARTILE.EXC — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns exclusive quartile value.

### Syntax
- Excel: `QUARTILE.EXC(array, quartile)`
- Google Sheets: `QUARTILE.EXC(array, quartile)`

### Behavior
Uses percentile method excluding dataset endpoints.

### Examples
- `QUARTILE.EXC({1,2,3,4,5,6,7,8},2)` -> `3`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/statistical/percentile.rs`
- Proposed handler: `fn_quartile.exc`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/QUARTILE.EXC.md


---

## QUARTILE.INC — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns inclusive quartile value.

### Syntax
- Excel: `QUARTILE.INC(array, quartile)`
- Google Sheets: `QUARTILE.INC(array, quartile)`

### Behavior
Uses percentile method including dataset endpoints.

### Examples
- `QUARTILE.INC({1,2,3,4,5,6,7,8},2)` -> `4`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/statistical/percentile.rs`
- Proposed handler: `fn_quartile.inc`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/QUARTILE.INC.md


---

## QUERY — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Runs SQL-like query on arrays.

### Syntax
- Excel: `QUERY(data, query, [headers])`
- Google Sheets: `QUERY(data, query, [headers])`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `QUERY({{1,2};{3,4}}, "select Col1")`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_query`
- Pseudocode: deterministic parsing, coercion, and computation.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/QUERY.md


---

## QUOTIENT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_quotient
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns integer quotient after division.

### Syntax
- Excel: `QUOTIENT(numerator, denominator)`
- Google Sheets: `QUOTIENT(numerator, denominator)`

### Behavior
Truncates fractional part toward zero.

### Examples
- `QUOTIENT(10,3)` -> `3`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_quotient`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/QUOTIENT.md


---

## RADIANS — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_radians
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts degrees to radians.

### Syntax
- Excel: `RADIANS(angle)`
- Google Sheets: `RADIANS(angle)`

### Behavior
Applies constant /180 conversion.

- Note: Non-ASCII characters omitted. See spec for full text.

### Examples
- `RADIANS(180)` -> `3.14159`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_radians`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/RADIANS.md


---

## RAND — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_rand
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns random number between 0 and 1.

### Syntax
- Excel: `RAND()`
- Google Sheets: `RAND()`

### Behavior
Volatile function; implementation should be deterministic in seeded context.

### Examples
- `RAND()` -> `0.123456`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_rand`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/RAND.md


---

## RANDARRAY — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Returns array of random numbers.

### Syntax
- Excel: `RANDARRAY([rows], [columns], [min], [max], [integer])`
- Google Sheets: `RANDARRAY([rows], [columns], [min], [max], [integer])`

### Behavior
Generates deterministic pseudo-random grid when context is seeded.

### Examples
- `RANDARRAY(2,2,1,10,TRUE)` -> `[[1,2],[3,4]]`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_randarray`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/RANDARRAY.md


---

## RANDBETWEEN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_randbetween
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns random integer within a range.

### Syntax
- Excel: `RANDBETWEEN(bottom, top)`
- Google Sheets: `RANDBETWEEN(bottom, top)`

### Behavior
Volatile integer generation with inclusive bounds.

### Examples
- `RANDBETWEEN(1,10)` -> `5`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_randbetween`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/RANDBETWEEN.md


---

## RANK — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns rank of a number in a dataset.

### Syntax
- Excel: `RANK(number, ref, [order])`
- Google Sheets: `RANK(number, ref, [order])`

### Behavior
Supports ascending or descending rank logic.

### Examples
- `RANK(3,{1,2,3,4})` -> `2`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/statistical/statistics.rs`
- Proposed handler: `fn_rank`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/RANK.md


---

## RANK.AVG — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns average rank for ties.

### Syntax
- Excel: `RANK.AVG(number, ref, [order])`
- Google Sheets: `RANK.AVG(number, ref, [order])`

### Behavior
When ties occur, average rank is returned.

### Examples
- `RANK.AVG(3,{1,3,3,4})` -> `2.5`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/statistical/statistics.rs`
- Proposed handler: `fn_rank.avg`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/RANK.AVG.md


---

## RANK.EQ — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns standard ranked order with ties equal.

### Syntax
- Excel: `RANK.EQ(number, ref, [order])`
- Google Sheets: `RANK.EQ(number, ref, [order])`

### Behavior
Equivalent to classic Excel/Sheets rank where tied values share same rank.

### Examples
- `RANK.EQ(3,{1,3,3,4})` -> `3`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/statistical/statistics.rs`
- Proposed handler: `fn_rank.eq`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/RANK.EQ.md


---

## RATE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_rate
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns interest rate per period for an annuity.

### Syntax
- Excel: `RATE(nper, pmt, pv, [fv], [type], [guess])`
- Google Sheets: `RATE(nper, pmt, pv, [fv], [type], [guess])`

### Behavior
Solves for periodic rate using iterative method.

### Examples
- `RATE(10,-1000,10000,0,0,0.1)` -> `-0.053`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_rate`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/RATE.md


---

## RECEIVED — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns amount received from an investment at periodic settlement.

### Syntax
- Excel: `RECEIVED(settlement, maturity, investment, discount, basis)`
- Google Sheets: `RECEIVED(settlement, maturity, investment, discount, basis)`

### Behavior
Computes redemption amount from investment and discount rate.

### Examples
- `RECEIVED("2026-01-01","2027-01-01",100,0.05,0)` -> approx

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/financial.rs`
- Proposed handler: `fn_received`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/RECEIVED.md


---

## REDUCE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Accumulates values from an array with a lambda-like reducer.

### Syntax
- Excel: `REDUCE(initial_value, array, reducer, [initial_value2], ...)`
- Google Sheets: `REDUCE(initial_value, array, reducer, ...)`

### Behavior
Runs reducer left-to-right across array values.

### Examples
- `REDUCE(0,{1,2,3},LAMBDA(a,b,a+b))` -> `6`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_reduce`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/REDUCE.md


---

## REGEXEXTRACT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Extracts first substring matching regex.

### Syntax
- Excel: `REGEXEXTRACT(text, regular_expression)`
- Google Sheets: `REGEXEXTRACT(text, regular_expression)`

### Behavior
Returns first match string; errors if no match.

### Examples
- `REGEXEXTRACT("abc123","\d+")` -> `123`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_regexextract`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/REGEXEXTRACT.md


---

## REGEXMATCH — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Tests whether text matches regex pattern.

### Syntax
- Excel: `REGEXMATCH(text, regular_expression)`
- Google Sheets: `REGEXMATCH(text, regular_expression)`

### Behavior
Returns TRUE when a match exists.

### Examples
- `REGEXMATCH("abc123","\d+")` -> `TRUE`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_regexmatch`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/REGEXMATCH.md


---

## REGEXREPLACE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Replaces text based on regex match.

### Syntax
- Excel: `REGEXREPLACE(text, regular_expression, replacement)`
- Google Sheets: `REGEXREPLACE(text, regular_expression, replacement)`

### Behavior
Substitutes first/all matches according to replacement text.

### Examples
- `REGEXREPLACE("abc123","\d+","")` -> `abc`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_regexreplace`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/REGEXREPLACE.md


---

## REGISTER.ID — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts account names to identifier format in financial contexts.

### Syntax
- Excel: `REGISTER.ID(text)`
- Google Sheets: `REGISTER.ID(text)`

### Behavior
Reserved extension-like compatibility function.

### Examples
- `REGISTER.ID("AAPL")` -> `#N/A`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_register.id`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/REGISTER.ID.md


---

## REPLACE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Replaces part of text by position.

### Syntax
- Excel: `REPLACE(old_text, start_num, num_chars, new_text)`
- Google Sheets: `REPLACE(old_text, start_num, num_chars, new_text)`

### Behavior
Returns resulting text after segment replacement.

### Examples
- `REPLACE("abcdef",2,3,"ZZ")` -> `aZZf`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_replace`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/REPLACE.md


---

## REPLACEB — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Byte-length variant of REPLACE.

### Syntax
- Excel: `REPLACEB(old_text, start_num, num_chars, new_text)`
- Google Sheets: `REPLACEB(old_text, start_num, num_chars, new_text)`

### Behavior
Uses byte counts instead of character counts.

### Examples
- `REPLACEB("abcdef",2,2,"ZZ")` -> `aZZef`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_replaceb`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/REPLACEB.md


---

## REPT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_rept
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Repeats text a number of times.

### Syntax
- Excel: `REPT(text, number_times)`
- Google Sheets: `REPT(text, number_times)`

### Behavior
Concatenates repeated text segments.

### Examples
- `REPT("A",3)` -> `AAA`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_rept`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/REPT.md


---

## RIGHT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: N
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_right
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns rightmost characters from text.

### Syntax
- Excel: `RIGHT(text, [num_chars])`
- Google Sheets: `RIGHT(text, [num_chars])`

### Behavior
Returns trailing characters up to requested length.

### Examples
- `RIGHT("hello",2)` -> `lo`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_right`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/RIGHT.md


---

## RIGHTB — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Byte-length variant of RIGHT.

### Syntax
- Excel: `RIGHTB(text, [num_bytes])`
- Google Sheets: `RIGHTB(text, [num_bytes])`

### Behavior
Uses byte count and supports multibyte text variants.

### Examples
- `RIGHTB("hello",3)` -> `llo`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_rightb`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/RIGHTB.md


---

## ROMAN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_roman
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts number to Roman numeral.

### Syntax
- Excel: `ROMAN(number, [form])`
- Google Sheets: `ROMAN(number, [form])`

### Behavior
Converts Arabic number to Roman numeric string with optional compact form.

### Examples
- `ROMAN(1987)` -> `MCMLXXXVII`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_roman`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ROMAN.md


---

## ROUND — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_round
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Rounds number to fixed decimal places.

### Syntax
- Excel: `ROUND(number, num_digits)`
- Google Sheets: `ROUND(number, num_digits)`

### Behavior
Rounds halfway cases away from zero.

### Examples
- `ROUND(1.6,0)` -> `2`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_round`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ROUND.md


---

## ROUNDDOWN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_rounddown
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Rounds number toward zero.

### Syntax
- Excel: `ROUNDDOWN(number, num_digits)`
- Google Sheets: `ROUNDDOWN(number, num_digits)`

### Behavior
For negative and positive, moves magnitude down.

### Examples
- `ROUNDDOWN(1.9,0)` -> `1`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_rounddown`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ROUNDDOWN.md


---

## ROUNDUP — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_roundup
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Rounds number away from zero.

### Syntax
- Excel: `ROUNDUP(number, num_digits)`
- Google Sheets: `ROUNDUP(number, num_digits)`

### Behavior
Rounds magnitude up in magnitude direction.

### Examples
- `ROUNDUP(1.1,0)` -> `2`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_roundup`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ROUNDUP.md


---

## ROW — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_row
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns row number of reference.

### Syntax
- Excel: `ROW([reference])`
- Google Sheets: `ROW([reference])`

### Behavior
Default returns current row when reference omitted.

### Examples
- `ROW(A5)` -> `5`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_row`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ROW.md


---

## ROWS — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_rows
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns count of rows in range.

### Syntax
- Excel: `ROWS(array)`
- Google Sheets: `ROWS(array)`

### Behavior
Counts rows in array or range.

### Examples
- `ROWS({{1,2},{3,4}})` -> `2`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_rows`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/ROWS.md


---

## RRI — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_rri
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns equivalent periodic interest rate for an investment.

### Syntax
- Excel: `RRI(nper, pv, fv)`
- Google Sheets: `RRI(nper, pv, fv)`

### Behavior
Derives growth rate per period from present to future value.

### Examples
- `RRI(10,100,200)` -> `0.0718`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_rri`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/RRI.md


---

## RSQ — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_rsq
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/pearson.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns square of Pearson correlation coefficient.

### Syntax
- Excel: `RSQ(known_y, known_x)`
- Google Sheets: `RSQ(known_y, known_x)`

### Behavior
Equivalent to `PEARSON(y,x)^2`.

### Examples
- `RSQ({1,2,3},{2,4,6})` -> `1`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_rsq`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/pearson.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/RSQ.md


---

## RTD — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Gets data from DDE/real-time data servers.

### Syntax
- Excel: `RTD(prog_id, server, topic1, topic2, ...)`
- Google Sheets: `RTD(prog_id, server, topic1, topic2, ...)`

### Behavior
Not supported in deterministic offline engine; treat as external data dependency.

### Examples
- `RTD("ProgID","",1)` -> `#N/A`

### Error Cases
- Invalid argument count/type/range yields errors per host semantics.

### Notes
- Deterministic and ordered input handling required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_rtd`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/RTD.md


---

## SCAN — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Scan/reduce across array values using a reducer.

### Syntax
- Excel: `SCAN(initial_value, array, lambda)`
- Google Sheets: `SCAN(initial_value, array, lambda)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `SCAN(0,{1,2,3},LAMBDA(a,b,a+b)) -> {0,1,3,6}

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_scan`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SCAN.md


---

## SEARCH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: N
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_search
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Find substring position within text.

### Syntax
- Excel: `SEARCH(find_text, within_text, [start_num])`
- Google Sheets: `SEARCH(find_text, within_text, [start_num])`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `SEARCH("b","abc") -> 2`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_search`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SEARCH.md


---

## SEARCHB — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Find byte-wise substring position within text.

### Syntax
- Excel: `SEARCHB(find_text, within_text, [start_num])`
- Google Sheets: `SEARCHB(find_text, within_text, [start_num])`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `SEARCHB("b","abc") -> 2`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_searchb`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SEARCHB.md


---

## SEC — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_sec
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Return secant of angle.

### Syntax
- Excel: `SEC(number)`
- Google Sheets: `SEC(number)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `SEC(0) -> 1`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_sec`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SEC.md


---

## SECH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_sech
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Return hyperbolic secant of value.

### Syntax
- Excel: `SECH(number)`
- Google Sheets: `SECH(number)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `SECH(0) -> 1`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_sech`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SECH.md


---

## SECOND — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_second
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Return second component of time.

### Syntax
- Excel: `SECOND(serial_number)`
- Google Sheets: `SECOND(serial_number)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `SECOND("00:00:59") -> 59`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_second`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SECOND.md


---

## SEQUENCE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Generates sequential numeric array.

### Syntax
- Excel: `SEQUENCE(rows, [columns], [start], [step])`
- Google Sheets: `SEQUENCE(rows, [columns], [start], [step])`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `SEQUENCE(3,1) -> {1,2,3}`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_sequence`
- Pseudocode: deterministic parsing, coercion, and computation.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SEQUENCE.md


---

## SERIESSUM — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Sum terms of a power series.

### Syntax
- Excel: `SERIESSUM(x, n, m, coefficients)`
- Google Sheets: `SERIESSUM(x, n, m, coefficients)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `SERIESSUM(1,1,1,{1,2}) -> 3`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/financial.rs`
- Proposed handler: `fn_seriessum`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SERIESSUM.md


---

## SHEET — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: N
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_sheet
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Return worksheet index or name context.

### Syntax
- Excel: `SHEET([reference])`
- Google Sheets: `SHEET([reference])`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `SHEET() -> 1`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_sheet`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SHEET.md


---

## SHEETS — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: N
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_sheets
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Return number/list of sheets.

### Syntax
- Excel: `SHEETS([reference])`
- Google Sheets: `SHEETS([reference])`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `SHEETS() -> 1`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_sheets`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SHEETS.md


---

## SIGN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_sign
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the sign of a numeric value: 1 if positive, 0 if zero, and -1 if negative.

### Syntax
- Excel: `SIGN(number)`
- Google Sheets: `SIGN(number)`

### Behavior
SIGN is deterministic and only depends on numeric coercion of number. Empty cells resolve through normal engine coercion rules; if a coercion path is not defined, return an error.

### Examples
- `=SIGN(-7)` -> `-1`
- `=SIGN(0)` -> `0`
- `=SIGN(7)` -> `1`

### Error Cases
- `SIGN("text")` -> `#VALUE!`
- Extra or missing arguments -> `#VALUE!`

### Notes
Single-argument utility function used in branching and normalization logic.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_sign`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SIGN.md


---

## SIN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_sin
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the sine of an angle measured in radians.

### Syntax
- Excel: `SIN(number)`
- Google Sheets: `SIN(number)`

### Behavior
SIN uses radians for input and standard floating-point math, with deterministic IEEE-754 result ordering and formatting.

### Examples
- `=SIN(0)` -> `0`
- `=SIN(PI()/2)` -> `1`
- `=SIN(PI())` -> `0`

### Error Cases
- `SIN("abc")` -> `#VALUE!`
- Missing/extra arguments -> `#VALUE!`

### Notes
Core trigonometric function for geometry and modeling formulas.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_sin`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SIN.md


---

## SINH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_sinh
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the hyperbolic sine of a real number.

### Syntax
- Excel: `SINH(number)`
- Google Sheets: `SINH(number)`

### Behavior
Input is evaluated as a real number and the output uses stable mathematical hyperbolic sine computation.

### Examples
- `=SINH(0)` -> `0`
- `=SINH(1)` -> `1.1752011936438`

### Error Cases
- `SINH("abc")` -> `#VALUE!`
- Wrong argument count -> `#VALUE!`

### Notes
Used in engineering and growth modeling contexts.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_sinh`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SINH.md


---

## SKEW — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_skew
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the skewness of a data set, assuming sample skewness.

### Syntax
- Excel: `SKEW(number1, [number2], ...)`
- Google Sheets: `SKEW(number1, [number2], ...)`

### Behavior
Calculates sample skewness by flattening arguments and applying numeric coercion before evaluation.

### Examples
- `=SKEW({1,2,3,4,5})` -> `0`
- `=SKEW({2,2,2})` -> `0`

### Error Cases
- Requires at least 3 numeric entries after coercion.
- Zero variance output conditions produce `#DIV/0!`/`#NUM!` depending on engine rules.

### Notes
Use for distribution-shape analysis where sample interpretation is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_skew`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SKEW.md


---

## SKEW.P — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes the population skewness of a data set.

### Syntax
- Excel: `SKEW.P(number1, [number2], ...)`
- Google Sheets: `SKEW.P(number1, [number2], ...)`

### Behavior
Calculates population skewness for an entire data set after flattening ranges and applying numeric coercion semantics.

### Examples
- `=SKEW.P({1,2,3,4,5})` -> `0`
- `=SKEW.P({1,1,1,1})` -> `0`

### Error Cases
- Requires at least 3 numeric entries after coercion.
- Zero variance output conditions produce `#DIV/0!`/`#NUM!` depending on engine rules.

### Notes
Use for distribution-shape analysis in population mode.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_skew_p`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SKEW.P.md


---

## SLN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_sln
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the periodic straight-line depreciation amount.

### Syntax
- Excel: `SLN(cost, salvage_value, life)`
- Google Sheets: `SLN(cost, salvage_value, life)`

### Behavior
Returns a constant depreciation amount for each period: (cost - salvage_value) / life.

### Examples
- `=SLN(30000, 0, 10)` -> `3000`
- `=SLN(5000, 500, 5)` -> `900`

### Error Cases
- Negative or zero life -> `#NUM!`.
- Missing/invalid numeric inputs -> `#VALUE!`

### Notes
Used for linear fixed depreciation schedules.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_sln`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SLN.md


---

## SLOPE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_slope
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/correl.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns the slope of the linear regression line through known data points.

### Syntax
- Excel: `SLOPE(known_ys, known_xs)`
- Google Sheets: `SLOPE(known_ys, known_xs)`

### Behavior
Computes covariance of y and x divided by variance of x using deterministic numeric arithmetic.

### Examples
- `=SLOPE({2,4,6}, {1,2,3})` -> `2`
- `=SLOPE({5,7,9}, {1,2,3})` -> `2`

### Error Cases
- Mismatched range sizes -> `#N/A`.
- Zero variance in x -> `#DIV/0!`.

### Notes
Equivalent to LINEST slope for simple linear regression.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_slope`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/correl.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SLOPE.md


---

## SMALL — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_small
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes SMALL semantics for spreadsheet formulas.

### Syntax
- Excel: `SMALL(...)`
- Google Sheets: `SMALL(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_small`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/count_and_average.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SMALL.md


---

## SORT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Sorts array by columns and order.

### Syntax
- Excel: `SORT(range, sort_index, [sort_order])`
- Google Sheets: `SORT(range, sort_index, [sort_order])`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `SORT({{3,1},{2,0}}, 1, TRUE)`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_sort`
- Pseudocode: deterministic parsing, coercion, and computation.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SORT.md


---

## SORTBY — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Sorts range by sort keys.

### Syntax
- Excel: `SORTBY(range, sort_key1, [sort_order1], ...)`
- Google Sheets: `SORTBY(range, sort_key1, [sort_order1], ...)`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `SORTBY({{3,1},{2,0}}, {2,1})`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_sortby`
- Pseudocode: deterministic parsing, coercion, and computation.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SORTBY.md


---

## SORTN — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Computes SORTN semantics for spreadsheet formulas.

### Syntax
- Excel: `SORTN(...)`
- Google Sheets: `SORTN(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_sortn`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SORTN.md


---

## SPARKLINE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Computes SPARKLINE semantics for spreadsheet formulas.

### Syntax
- Excel: `SPARKLINE(...)`
- Google Sheets: `SPARKLINE(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_sparkline`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SPARKLINE.md


---

## SPLIT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Computes SPLIT semantics for spreadsheet formulas.

### Syntax
- Excel: `SPLIT(...)`
- Google Sheets: `SPLIT(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_split`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SPLIT.md


---

## SQRT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_sqrt
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Return square root.

### Syntax
- Excel: `SQRT(number)`
- Google Sheets: `SQRT(number)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `SQRT(9) -> 3`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_sqrt`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SQRT.md


---

## SQRTPI — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_sqrtpi
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes SQRTPI semantics for spreadsheet formulas.

### Syntax
- Excel: `SQRTPI(...)`
- Google Sheets: `SQRTPI(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_sqrtpi`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SQRTPI.md


---

## STANDARDIZE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_standardize
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/standardize.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes STANDARDIZE semantics for spreadsheet formulas.

### Syntax
- Excel: `STANDARDIZE(...)`
- Google Sheets: `STANDARDIZE(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_standardize`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/standardize.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/STANDARDIZE.md


---

## STDEV.P — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes STDEV.P semantics for spreadsheet formulas.

### Syntax
- Excel: `STDEV.P(...)`
- Google Sheets: `STDEV.P(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_stdev.p`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/STDEV.P.md


---

## STDEV.S — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes STDEV.S semantics for spreadsheet formulas.

### Syntax
- Excel: `STDEV.S(...)`
- Google Sheets: `STDEV.S(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_stdev.s`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/STDEV.S.md


---

## STDEVA — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_stdeva
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/standard_dev.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes STDEVA semantics for spreadsheet formulas.

### Syntax
- Excel: `STDEVA(...)`
- Google Sheets: `STDEVA(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_stdeva`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/standard_dev.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/STDEVA.md


---

## STDEVPA — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_stdevpa
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/standard_dev.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes STDEVPA semantics for spreadsheet formulas.

### Syntax
- Excel: `STDEVPA(...)`
- Google Sheets: `STDEVPA(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_stdevpa`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/standard_dev.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/STDEVPA.md


---

## STEYX — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_steyx
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/correl.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes STEYX semantics for spreadsheet formulas.

### Syntax
- Excel: `STEYX(...)`
- Google Sheets: `STEYX(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_steyx`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/correl.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/STEYX.md


---

## STOCKHISTORY — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes STOCKHISTORY semantics for spreadsheet formulas.

### Syntax
- Excel: `STOCKHISTORY(...)`
- Google Sheets: `STOCKHISTORY(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_stockhistory`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/STOCKHISTORY.md


---

## SUBSTITUTE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_substitute
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes SUBSTITUTE semantics for spreadsheet formulas.

### Syntax
- Excel: `SUBSTITUTE(...)`
- Google Sheets: `SUBSTITUTE(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_substitute`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SUBSTITUTE.md


---

## SUBTOTAL — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_subtotal
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/subtotal.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes SUBTOTAL semantics for spreadsheet formulas.

### Syntax
- Excel: `SUBTOTAL(...)`
- Google Sheets: `SUBTOTAL(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_subtotal`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/subtotal.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SUBTOTAL.md


---

## SUM — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_sum
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes SUM semantics for spreadsheet formulas.

### Syntax
- Excel: `SUM(...)`
- Google Sheets: `SUM(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_sum`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SUM.md


---

## SUMIF — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_sumif
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes SUMIF semantics for spreadsheet formulas.

### Syntax
- Excel: `SUMIF(...)`
- Google Sheets: `SUMIF(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_sumif`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SUMIF.md


---

## SUMIFS — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_sumifs
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes SUMIFS semantics for spreadsheet formulas.

### Syntax
- Excel: `SUMIFS(...)`
- Google Sheets: `SUMIFS(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_sumifs`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SUMIFS.md


---

## SUMPRODUCT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes SUMPRODUCT semantics for spreadsheet formulas.

### Syntax
- Excel: `SUMPRODUCT(...)`
- Google Sheets: `SUMPRODUCT(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_sumproduct`
- Pseudocode: validate inputs, apply deterministic coercion and return standardized errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SUMPRODUCT.md


---

## SUMSQ — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_sumsq
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes SUMSQ semantics for spreadsheet formulas.

### Syntax
- Excel: `SUMSQ(...)`
- Google Sheets: `SUMSQ(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_sumsq`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SUMSQ.md


---

## SUMX2MY2 — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_sumx2my2
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical_sum.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes SUMX2MY2 semantics for spreadsheet formulas.

### Syntax
- Excel: `SUMX2MY2(...)`
- Google Sheets: `SUMX2MY2(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_sumx2my2`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical_sum.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SUMX2MY2.md


---

## SUMX2PY2 — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_sumx2py2
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical_sum.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes SUMX2PY2 semantics for spreadsheet formulas.

### Syntax
- Excel: `SUMX2PY2(...)`
- Google Sheets: `SUMX2PY2(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_sumx2py2`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical_sum.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SUMX2PY2.md


---

## SUMXMY2 — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_sumxmy2
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical_sum.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes SUMXMY2 semantics for spreadsheet formulas.

### Syntax
- Excel: `SUMXMY2(...)`
- Google Sheets: `SUMXMY2(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_sumxmy2`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical_sum.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SUMXMY2.md


---

## SWITCH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_switch
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/logical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes SWITCH semantics for spreadsheet formulas.

### Syntax
- Excel: `SWITCH(...)`
- Google Sheets: `SWITCH(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit coercion rules.

### Examples
- `...`

### Error Cases
- Invalid argument count, types, and impossible domains return a spreadsheet error.

### Notes
- Deterministic and version-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_switch`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/logical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SWITCH.md


---

## SYD — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_syd
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Sum-of-years-digits depreciation calculation for an asset period.

### Syntax
- Excel: `SYD(cost, salvage, life, period)`
- Google Sheets: `SYD(cost, salvage, life, period)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- SYD(3000,1000,10,1) -> 266.67

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_syd`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/SYD.md


---

## T — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_t
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns text argument as text or empty string.

### Syntax
- Excel: `T(value)`
- Google Sheets: `T(value)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- T("x") -> ""

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_t`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/T.md


---

## T.DIST — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes T.DIST semantics for spreadsheet formulas.

### Syntax
- Excel: `T.DIST(...)`
- Google Sheets: `T.DIST(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_t.dist`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/T.DIST.md


---

## T.DIST.2T — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes T.DIST.2T semantics for spreadsheet formulas.

### Syntax
- Excel: `T.DIST.2T(...)`
- Google Sheets: `T.DIST.2T(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_t.dist.2t`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/T.DIST.2T.md


---

## T.DIST.RT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes T.DIST.RT semantics for spreadsheet formulas.

### Syntax
- Excel: `T.DIST.RT(...)`
- Google Sheets: `T.DIST.RT(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_t.dist.rt`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/T.DIST.RT.md


---

## T.INV — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes T.INV semantics for spreadsheet formulas.

### Syntax
- Excel: `T.INV(...)`
- Google Sheets: `T.INV(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_t.inv`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/T.INV.md


---

## T.INV.2T — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes T.INV.2T semantics for spreadsheet formulas.

### Syntax
- Excel: `T.INV.2T(...)`
- Google Sheets: `T.INV.2T(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_t.inv.2t`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/T.INV.2T.md


---

## T.TEST — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes T.TEST semantics for spreadsheet formulas.

### Syntax
- Excel: `T.TEST(...)`
- Google Sheets: `T.TEST(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_t.test`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/T.TEST.md


---

## TAKE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Computes TAKE semantics for spreadsheet formulas.

### Syntax
- Excel: `TAKE(...)`
- Google Sheets: `TAKE(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_take`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TAKE.md


---

## TAN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_tan
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns tangent of angle.

### Syntax
- Excel: `TAN(number)`
- Google Sheets: `TAN(number)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- TAN(0) -> 0

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_tan`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TAN.md


---

## TANH — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_tanh
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns hyperbolic tangent.

### Syntax
- Excel: `TANH(number)`
- Google Sheets: `TANH(number)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- TANH(0) -> 0

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_tanh`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TANH.md


---

## TBILLEQ — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_tbilleq
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns treasury bill discount-equivalent yield.

### Syntax
- Excel: `TBILLEQ(settlement, maturity, discount)`
- Google Sheets: `TBILLEQ(settlement, maturity, discount)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- TBILLEQ("2026-01-01","2026-07-01",0.05) -> 0.06

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_tbilleq`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TBILLEQ.md


---

## TBILLPRICE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_tbillprice
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns treasury bill price.

### Syntax
- Excel: `TBILLPRICE(settlement,maturity,discount)`
- Google Sheets: `TBILLPRICE(settlement,maturity,discount)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- TBILLPRICE("2026-01-01","2026-07-01",0.05) -> 100

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_tbillprice`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TBILLPRICE.md


---

## TBILLYIELD — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_tbillyield
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns treasury bill annual yield.

### Syntax
- Excel: `TBILLYIELD(settlement,maturity,price)`
- Google Sheets: `TBILLYIELD(settlement,maturity,price)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- TBILLYIELD("2026-01-01","2026-07-01",98) -> 0.055

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_tbillyield`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TBILLYIELD.md


---

## TEXT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_text
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Formats values as text using number format string.

### Syntax
- Excel: `TEXT(value, format_text)`
- Google Sheets: `TEXT(value, format_text)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- TEXT(123.45,"0.00") -> "123.45"

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_text`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TEXT.md


---

## TEXTAFTER — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_textafter
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns text after a delimiter.

### Syntax
- Excel: `TEXTAFTER(text, delimiter, [instance_num], [match_mode], [match_end])`
- Google Sheets: `TEXTAFTER(text, delimiter, [instance_num], [match_mode], [match_end])`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `TEXTAFTER("a,b,c",",") -> "b,c"`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_textafter`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TEXTAFTER.md


---

## TEXTBEFORE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_textbefore
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns text before a delimiter.

### Syntax
- Excel: `TEXTBEFORE(text, delimiter, [instance_num], [match_mode], [match_end])`
- Google Sheets: `TEXTBEFORE(text, delimiter, [instance_num], [match_mode], [match_end])`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `TEXTBEFORE("a,b,c",",") -> "a"`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_textbefore`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TEXTBEFORE.md


---

## TEXTJOIN — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_textjoin
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Concatenates values with delimiter.

### Syntax
- Excel: `TEXTJOIN(delimiter, ignore_empty, text1, ...)`
- Google Sheets: `TEXTJOIN(delimiter, ignore_empty, text1, ...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- TEXTJOIN(",",TRUE,"a","b") -> "a,b"

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_textjoin`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TEXTJOIN.md


---

## TEXTSPLIT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Splits text into array by delimiter.

### Syntax
- Excel: `TEXTSPLIT(text, delimiter)`
- Google Sheets: `TEXTSPLIT(text, delimiter)`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `TEXTSPLIT("a,b,c",",") -> {a,b,c}`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_textsplit`
- Pseudocode: deterministic parsing, coercion, and computation.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TEXTSPLIT.md


---

## TIME — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_time
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts hour minute second to serial time.

### Syntax
- Excel: `TIME(hour, minute, second)`
- Google Sheets: `TIME(hour, minute, second)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.

### Examples
- `TIME(1,30,0) -> 0.0625`

### Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible date arithmetic.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_time`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TIME.md


---

## TIMEVALUE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_timevalue
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts time text to serial time.

### Syntax
- Excel: `TIMEVALUE(time_text)`
- Google Sheets: `TIMEVALUE(time_text)`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.

### Examples
- `TIMEVALUE("13:30") -> 0.5625`

### Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible date arithmetic.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_timevalue`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TIMEVALUE.md


---

## TOCOL — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Computes TOCOL semantics for spreadsheet formulas.

### Syntax
- Excel: `TOCOL(...)`
- Google Sheets: `TOCOL(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_tocol`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TOCOL.md


---

## TODAY — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_today
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns current date.

### Syntax
- Excel: `TODAY()`
- Google Sheets: `TODAY()`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- TODAY() -> serial date

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_today`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TODAY.md


---

## TOROW — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Computes TOROW semantics for spreadsheet formulas.

### Syntax
- Excel: `TOROW(...)`
- Google Sheets: `TOROW(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_torow`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TOROW.md


---

## TO_DATE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes TO_DATE semantics for spreadsheet formulas.

### Syntax
- Excel: `TO_DATE(...)`
- Google Sheets: `TO_DATE(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_to_date`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TO_DATE.md


---

## TO_DOLLARS — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes TO_DOLLARS semantics for spreadsheet formulas.

### Syntax
- Excel: `TO_DOLLARS(...)`
- Google Sheets: `TO_DOLLARS(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_to_dollars`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TO_DOLLARS.md


---

## TO_PERCENT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes TO_PERCENT semantics for spreadsheet formulas.

### Syntax
- Excel: `TO_PERCENT(...)`
- Google Sheets: `TO_PERCENT(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_to_percent`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TO_PERCENT.md


---

## TO_PURE_NUMBER — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes TO_PURE_NUMBER semantics for spreadsheet formulas.

### Syntax
- Excel: `TO_PURE_NUMBER(...)`
- Google Sheets: `TO_PURE_NUMBER(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_to_pure_number`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TO_PURE_NUMBER.md


---

## TO_TEXT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes TO_TEXT semantics for spreadsheet formulas.

### Syntax
- Excel: `TO_TEXT(...)`
- Google Sheets: `TO_TEXT(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_to_text`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TO_TEXT.md


---

## TRANSPOSE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: matrix

## Spec Summary
### Purpose
Computes TRANSPOSE semantics for spreadsheet formulas.

### Syntax
- Excel: `TRANSPOSE(...)`
- Google Sheets: `TRANSPOSE(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_transpose`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TRANSPOSE.md


---

## TREND — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: matrix

## Spec Summary
### Purpose
Computes TREND semantics for spreadsheet formulas.

### Syntax
- Excel: `TREND(...)`
- Google Sheets: `TREND(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_trend`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TREND.md


---

## TRIM — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_trim
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Removes extra spaces from text.

### Syntax
- Excel: `TRIM(text)`
- Google Sheets: `TRIM(text)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- TRIM(" a  b ") -> "a b"

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_trim`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TRIM.md


---

## TRIMMEAN — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes TRIMMEAN semantics for spreadsheet formulas.

### Syntax
- Excel: `TRIMMEAN(...)`
- Google Sheets: `TRIMMEAN(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_trimmean`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TRIMMEAN.md


---

## TRIMRANGE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes TRIMRANGE semantics for spreadsheet formulas.

### Syntax
- Excel: `TRIMRANGE(...)`
- Google Sheets: `TRIMRANGE(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_trimrange`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TRIMRANGE.md


---

## TRUE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_true
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/logical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Logical true constant.

### Syntax
- Excel: `TRUE()`
- Google Sheets: `TRUE()`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- TRUE() -> TRUE

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_true`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/logical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TRUE.md


---

## TRUNC — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_trunc
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Truncates number to integer/decimal places.

### Syntax
- Excel: `TRUNC(number, [num_digits])`
- Google Sheets: `TRUNC(number, [num_digits])`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- TRUNC(1.9) -> 1

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_trunc`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/mathematical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TRUNC.md


---

## TTEST — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: fn_t_test
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/t_dist.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes TTEST semantics for spreadsheet formulas.

### Syntax
- Excel: `TTEST(...)`
- Google Sheets: `TTEST(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_t_test`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/t_dist.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TTEST.md


---

## TYPE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_type
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes TYPE semantics for spreadsheet formulas.

### Syntax
- Excel: `TYPE(...)`
- Google Sheets: `TYPE(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_type`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/information.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/TYPE.md


---

## UMINUS — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes UMINUS semantics for spreadsheet formulas.

### Syntax
- Excel: `UMINUS(...)`
- Google Sheets: `UMINUS(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_uminus`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/UMINUS.md


---

## UNARY_PERCENT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes UNARY_PERCENT semantics for spreadsheet formulas.

### Syntax
- Excel: `UNARY_PERCENT(...)`
- Google Sheets: `UNARY_PERCENT(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_unary_percent`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/UNARY_PERCENT.md


---

## UNICHAR — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes UNICHAR semantics for spreadsheet formulas.

### Syntax
- Excel: `UNICHAR(...)`
- Google Sheets: `UNICHAR(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_unichar`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/UNICHAR.md


---

## UNICODE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_unicode
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns numeric codepoint for first character.

### Syntax
- Excel: `UNICODE(text)`
- Google Sheets: `UNICODE(text)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- UNICODE("A") -> 65

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_unicode`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/UNICODE.md


---

## UNIQUE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Returns unique values from array.

### Syntax
- Excel: `UNIQUE(range_or_array, [by_col], [exactly_once])`
- Google Sheets: `UNIQUE(range_or_array, [by_col], [exactly_once])`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `UNIQUE({1,2,1}) -> {1,2}`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_unique`
- Pseudocode: deterministic parsing, coercion, and computation.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/UNIQUE.md


---

## UPLUS — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: N
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes UPLUS semantics for spreadsheet formulas.

### Syntax
- Excel: `UPLUS(...)`
- Google Sheets: `UPLUS(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Proposed file: `base/src/functions/mathematical.rs`
- Proposed handler: `fn_uplus`
- Pseudocode: validate input shape/types, apply deterministic coercion and return spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/UPLUS.md


---

## UPPER — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_upper
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts text to upper case.

### Syntax
- Excel: `UPPER(text)`
- Google Sheets: `UPPER(text)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- UPPER("abc") -> "ABC"

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_upper`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/UPPER.md


---

## VALUE — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_value
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Converts text to numeric value.

### Syntax
- Excel: `VALUE(text)`
- Google Sheets: `VALUE(text)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- VALUE("123") -> 123

### Error Cases
- Invalid argument count or invalid domains return spreadsheet errors.

### Notes
- Deterministic and platform-stable behavior is required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_value`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/VALUE.md


---

## VALUETOTEXT — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: N
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_valuetotext
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes VALUETOTEXT behavior for spreadsheet formulas.

### Syntax
- Excel: `VALUETOTEXT(...)`
- Google Sheets: `VALUETOTEXT(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_valuetotext`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/text.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/VALUETOTEXT.md


---

## VAR.P — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns population variance.

### Syntax
- Excel: `VAR.P(number1,...)`
- Google Sheets: `VAR.P(number1,...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- VAR.P({1,2,3}) -> 2/3

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_var.p`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/VAR.P.md


---

## VAR.S — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns sample variance.

### Syntax
- Excel: `VAR.S(number1,...)`
- Google Sheets: `VAR.S(number1,...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- VAR.S({1,2,3}) -> 1

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Proposed file: `base/src/functions/statistical/count_and_average.rs`
- Proposed handler: `fn_var.s`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/VAR.S.md


---

## VARA — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_vara
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/variance.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes VARA behavior for spreadsheet formulas.

### Syntax
- Excel: `VARA(...)`
- Google Sheets: `VARA(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_vara`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/variance.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/VARA.md


---

## VARPA — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_varpa
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/variance.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes VARPA behavior for spreadsheet formulas.

### Syntax
- Excel: `VARPA(...)`
- Google Sheets: `VARPA(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_varpa`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/statistical/variance.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/VARPA.md


---

## VDB — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Depreciation by declining-balance method with period schedules.

### Syntax
- Excel: `VDB(cost, salvage, life, start_period, end_period, factor, [no_switch])`
- Google Sheets: `VDB(cost, salvage, life, start_period, end_period, factor, [no_switch])`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- VDB(2400,300,10,0,1,1.5,TRUE) -> value

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_vdb`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/VDB.md


---

## VLOOKUP — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_vlookup
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes VLOOKUP behavior for spreadsheet formulas.

### Syntax
- Excel: `VLOOKUP(...)`
- Google Sheets: `VLOOKUP(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_vlookup`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/lookup_and_reference.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/VLOOKUP.md


---

## VSTACK — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Stacks arrays vertically.

### Syntax
- Excel: `VSTACK(value1, value2, ...)`
- Google Sheets: `VSTACK(value1, value2, ...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- VSTACK({1,2},{3,4}) -> {{1,2},{3,4}}

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Proposed file: `base/src/functions/extensions.rs`
- Proposed handler: `fn_vstack`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/VSTACK.md


---

## WEBSERVICE — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Fetches content from a URL.

### Syntax
- Excel: `WEBSERVICE(url)`
- Google Sheets: `WEBSERVICE(url)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- WEBSERVICE("https://...") -> response text

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Proposed file: `base/src/functions/integration.rs`
- Proposed handler: `fn_webservice`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/WEBSERVICE.md


---

## WEEKDAY — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_weekday
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes WEEKDAY behavior for spreadsheet formulas.

### Syntax
- Excel: `WEEKDAY(...)`
- Google Sheets: `WEEKDAY(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_weekday`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/WEEKDAY.md


---

## WEEKNUM — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_weeknum
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes WEEKNUM behavior for spreadsheet formulas.

### Syntax
- Excel: `WEEKNUM(...)`
- Google Sheets: `WEEKNUM(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_weeknum`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/WEEKNUM.md


---

## WEIBULL.DIST — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns Weibull distribution values.

### Syntax
- Excel: `WEIBULL.DIST(x, alpha, beta, cumulative)`
- Google Sheets: `WEIBULL.DIST(x, alpha, beta, cumulative)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- WEIBULL.DIST(2,1,1,TRUE) -> 0.8647

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Proposed file: `base/src/functions/statistical/distribution.rs`
- Proposed handler: `fn_weibull.dist`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/WEIBULL.DIST.md


---

## WORKDAY — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_workday
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns workday date after specified days.

### Syntax
- Excel: `WORKDAY(start_date, days, [holidays])`
- Google Sheets: `WORKDAY(start_date, days, [holidays])`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.

### Examples
- `WORKDAY("2026-01-01",10) -> date`

### Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible date arithmetic.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_workday`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/WORKDAY.md


---

## WORKDAY.INTL — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns workday date with custom weekend schedule.

### Syntax
- Excel: `WORKDAY.INTL(start_date, days, [weekend], [holidays])`
- Google Sheets: `WORKDAY.INTL(start_date, days, [weekend], [holidays])`

### Behavior
Deterministic spreadsheet-compatible behavior with explicit date handling.

### Examples
- `WORKDAY.INTL("2026-01-01",10,1) -> date`

### Error Cases
- Invalid dates or impossible ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible date arithmetic.

### Code Location
- Proposed file: `base/src/functions/date_and_time.rs`
- Proposed handler: `fn_workday.intl`
- Pseudocode: validate date arguments, apply calendar/business-day logic, return standardized errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/WORKDAY.INTL.md


---

## WRAPCOLS — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Wraps a one-dimensional array into columns.

### Syntax
- Excel: `WRAPCOLS(array, wrap_count, [pad_with])`
- Google Sheets: `WRAPCOLS(array, wrap_count, [pad_with])`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- WRAPCOLS({1,2,3},2) -> {{1,2},{3}}

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_wrapcols`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/WRAPCOLS.md


---

## WRAPROWS — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: spill

## Spec Summary
### Purpose
Wraps a one-dimensional array into rows.

### Syntax
- Excel: `WRAPROWS(array, wrap_count, [pad_with])`
- Google Sheets: `WRAPROWS(array, wrap_count, [pad_with])`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- WRAPROWS({1,2,3},2) -> {{1,3},{2}}

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_wraprows`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/WRAPROWS.md


---

## XIRR — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: No
- IronCalc Handler: fn_xirr
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: column
- Output: scalar

## Spec Summary
### Purpose
Computes XIRR behavior for spreadsheet formulas.

### Syntax
- Excel: `XIRR(...)`
- Google Sheets: `XIRR(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_xirr`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/XIRR.md


---

## XLOOKUP — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_xlookup
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/xlookup.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Searches a range for a match and returns corresponding value.

### Syntax
- Excel: `XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found])`
- Google Sheets: `XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found])`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `XLOOKUP("B", {"A","B","C"}, {1,2,3}) -> 2`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_xlookup`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/xlookup.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/XLOOKUP.md


---

## XMATCH — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: N
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns relative position of item in array.

### Syntax
- Excel: `XMATCH(lookup_value, lookup_array, [match_mode], [search_mode])`
- Google Sheets: `XMATCH(lookup_value, lookup_array, [match_mode], [search_mode])`

### Behavior
Deterministic behavior is required with explicit evaluation order.

### Examples
- `XMATCH("B", {"A","B","C"}) -> 2`

### Error Cases
- Invalid argument types or malformed ranges return spreadsheet errors.

### Notes
- Deterministic and reproducible under seeded execution context.

### Code Location
- Proposed file: `base/src/functions/lookup_and_reference.rs`
- Proposed handler: `fn_xmatch`
- Pseudocode: deterministic parsing, coercion, and computation.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/XMATCH.md


---

## XNPV — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_xnpv
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes XNPV behavior for spreadsheet formulas.

### Syntax
- Excel: `XNPV(...)`
- Google Sheets: `XNPV(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_xnpv`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/financial.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/XNPV.md


---

## XOR — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_xor
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/logical.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes XOR behavior for spreadsheet formulas.

### Syntax
- Excel: `XOR(...)`
- Google Sheets: `XOR(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_xor`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/logical.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/XOR.md


---

## YEAR — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_year
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes YEAR behavior for spreadsheet formulas.

### Syntax
- Excel: `YEAR(...)`
- Google Sheets: `YEAR(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_year`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/YEAR.md


---

## YEARFRAC — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: fn_yearfrac
- IronCalc File: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Computes YEARFRAC behavior for spreadsheet formulas.

### Syntax
- Excel: `YEARFRAC(...)`
- Google Sheets: `YEARFRAC(...)`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- `...`

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Implemented in IronCalc.
- Handler: `fn_yearfrac`
- File: `/Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/base/src/functions/date_and_time.rs`

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/YEARFRAC.md


---

## YIELD — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns bond yield based on price and terms.

### Syntax
- Excel: `YIELD(settlement,maturity,rate,pr,redemption,frequency,[basis])`
- Google Sheets: `YIELD(settlement,maturity,rate,pr,redemption,frequency,[basis])`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- YIELD("2026-01-01","2027-01-01",0.05,95,100,2) -> value

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Proposed file: `base/src/functions/statistical/distribution.rs`
- Proposed handler: `fn_yield`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/YIELD.md


---

## YIELDDISC — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns discounted bond yield.

### Syntax
- Excel: `YIELDDISC(settlement,maturity,pr,redemption,[basis])`
- Google Sheets: `YIELDDISC(settlement,maturity,pr,redemption,[basis])`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- YIELDDISC("2026-01-01","2027-01-01",98,100,0) -> value

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Proposed file: `base/src/functions/statistical/distribution.rs`
- Proposed handler: `fn_yielddisc`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/YIELDDISC.md


---

## YIELDMAT — Lua Implementation Prompt

## Status
- IronCalc: N
- Excel: Y
- Google Sheets: Y
- HyperFormula: N
- Missing in HyperFormula: Yes
- Missing in IronCalc: Yes
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns annual yield of bond with maturity date.

### Syntax
- Excel: `YIELDMAT(settlement,maturity,issue,first_coupon,rate,yield,redemption,frequency,[basis])`
- Google Sheets: `YIELDMAT(settlement,maturity,issue,first_coupon,rate,yield,redemption,frequency,[basis])`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- YIELDMAT("2026-01-01","2027-01-01","2025-01-01",0.5,0.05,100,100,2) -> value

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Proposed file: `base/src/functions/statistical/distribution.rs`
- Proposed handler: `fn_yieldmat`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/YIELDMAT.md


---

## Z.TEST — Lua Implementation Prompt

## Status
- IronCalc: Y
- Excel: Y
- Google Sheets: Y
- HyperFormula: Y
- Missing in HyperFormula: No
- Missing in IronCalc: No
- IronCalc Handler: n/a
- IronCalc File: n/a

## IO Shape
- Input: scalar
- Output: scalar

## Spec Summary
### Purpose
Returns z-test p-value.

### Syntax
- Excel: `Z.TEST(array, x, [sigma])`
- Google Sheets: `Z.TEST(array, x, [sigma])`

### Behavior
Deterministic spreadsheet-compatible behavior with stable coercion.

### Examples
- Z.TEST({1,2,3},2) -> 0.5

### Error Cases
- Invalid argument count/types and impossible domain values return spreadsheet errors.

### Notes
- Deterministic and reproducible behavior required.

### Code Location
- Proposed file: `base/src/functions/text.rs`
- Proposed handler: `fn_z.test`
- Pseudocode: validate input shape/types, apply deterministic computation, return standard spreadsheet errors.

## Implementation Checklist (Lua)
- Parse and coerce arguments per Excel/Sheets semantics.
- Implement error propagation and return codes exactly.
- Respect array/range inputs based on IO shape.
- Match numeric precision and rounding behavior.
- Add tests that mirror spec examples and error cases.

## Reference
- Spec file: /Users/maxwittenberg/Desktop/dagger_excel/excel_thorobid/Dagger_IronCalc/specs/functions/Z.TEST.md


---
