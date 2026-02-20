# RECEIVED

## RECEIVED

## Purpose
Returns amount received from an investment at periodic settlement.

## Syntax
- Excel: `RECEIVED(settlement, maturity, investment, discount, basis)`
- Google Sheets: `RECEIVED(settlement, maturity, investment, discount, basis)`

## Behavior
Computes redemption amount from investment and discount rate.

## Examples (expected outputs)
- `RECEIVED("2026-01-01","2027-01-01",100,0.05,0)` -> approx

## Error Cases
- Invalid argument count/type/range yields errors per host semantics.

## Notes
- Deterministic and ordered input handling required.

## Code Location
- Proposed file: `base/src/functions/financial.rs`
- Proposed handler: `fn_received`
- Pseudocode: validate args, coerce numeric/text inputs, apply deterministic calculations, return standard errors. 

## Documentation (Microsoft)



- Source URL: https://support.microsoft.com/en-us/office/received-function-7a3f8b93-6611-4f81-8576-828312c9b5e5

- Summary: Returns amount received from an investment at periodic settlement.

- Signatures:

  - `RECEIVED(settlement, maturity, investment, discount, [basis])`

- Examples: Copy the example data in the following table, and paste it in cell A1 of a new Excel worksheet. For formulas to show results, select them, press F2, and then press Enter. If you need to, you can adjust the column widths to see all the data. Data Description 15-Feb-08 Settlement (issue) date 15-May-08 Maturity date $ 1,000,000.00 Investment 5.75% Percent discount rate 2 Actual/360 basis Formula Description Result =RECEIVED(A2,A3,A4,A5,A6) The total amount to be received at maturity, for the bond with the terms in A2:A6. $ 1,014,584.65

- Notes: - Microsoft Excel stores dates as sequential serial numbers so they can be used in calculations. By default, January 1, 1900 is serial number 1, and January 1, 2008 is serial number 39448 because it is 39,448 days after January 1, 1900. - The settlement date is the date a buyer purchases a coupon, such as a bond. The maturity date is the date when a coupon expires. For example, suppose a 30-year bond is issued on January 1, 2008, and is purchased by a buyer six months later. The issue date would be January 1, 2008, the settlement date would be July 1, 2008, and the maturity date would be January 1, 2038, which is 30 years after the January 1,…

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Documentation (Google Sheets)



- Source URL: https://support.google.com/docs/answer/3093244

- Summary: Calculates the amount received at maturity for an investment in fixed-income securities purchased on a given date. Sample Usage RECEIVED(DATE(2010,02,01),DATE(2019,12,31),1000,0.05) RECEIVED(A2,A3,

- Signatures:

  - `RECEIVED(settlement, maturity, investment, discount, [day_count_convention])`

- Examples:

  - RECEIVED(DATE(2010,02,01)

  - RECEIVED(A2,A3,A4,A5,1)

  - RECEIVED(settlement, maturity, investment, discount, [day_count_convention])

- Notes: - settlement and maturity should be entered using DATE, TO_DATE or other date parsing functions rather than by entering text.

- Error behavior: Invalid argument count/type/range yields errors per host semantics.



## Sources
- Excel: https://support.microsoft.com/en-us/office/received-function-7a3f8b93-6611-4f81-8576-828312c9b5e5
- Google Sheets: https://support.google.com/docs/answer/3093244
