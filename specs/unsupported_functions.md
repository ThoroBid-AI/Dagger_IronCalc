# Unsupported Functions

## Scope
This list documents functions that intentionally return `#N/IMPL!` in the current engine. They are out of scope until a customer request or product need justifies the required infrastructure work.

## Current NIMPL List
- `PIVOTBY`
- `QUERY`
- `REDUCE`
- `REGISTER.ID`
- `RTD`
- `SCAN`
- `SPARKLINE`
- `STOCKHISTORY`
- `WEBSERVICE`

## Rationale
- Query/pivot engine required: `QUERY`, `PIVOTBY`.
- LAMBDA execution required: `REDUCE`, `SCAN`.
- External I/O or registry dependencies: `WEBSERVICE`, `RTD`, `REGISTER.ID`, `STOCKHISTORY`.
- UI/rendering output: `SPARKLINE`.

## Policy
- These functions must return a deterministic `#N/IMPL!` error.
- Implementation work only starts after a confirmed customer requirement.
