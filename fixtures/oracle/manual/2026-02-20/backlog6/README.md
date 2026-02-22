# Oracle Capture Bundle - Backlog6

Date: 2026-02-20
Scope: ARRAYFORMULA, ARRAY_CONSTRAIN, FILTER, MMULT, SPLIT, TRANSPOSE

## Files
- Sheets workbook: `sheets/oracle_backlog6_sheets.xlsx`
- Excel workbook: `excel/oracle_backlog6_excel.xlsx`

## Process
1. Open workbook in target engine.
2. Allow formulas to calculate.
3. Save workbook.
4. Import results:

```bash
python3 scripts/import_oracle_workbook.py --batches "1,5,9,12,13" --engine sheets --fixtures fixtures --workbook fixtures/oracle/manual/2026-02-20/backlog6/sheets/oracle_backlog6_sheets.xlsx
python3 scripts/import_oracle_workbook.py --batches "1,5,9,12,13" --engine excel --fixtures fixtures --workbook fixtures/oracle/manual/2026-02-20/backlog6/excel/oracle_backlog6_excel.xlsx
```
