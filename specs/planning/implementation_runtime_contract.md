# Implementation Runtime Contract

This contract defines where function implementations must run in this repository.

For end-to-end execution steps, use:
- `specs/planning/implementation_handoff_contract.md`

## Status
- Date: 2026-02-20
- Runtime target: Rust engine (`base` crate)
- Lua runtime: not integrated in evaluation path

## Meaning of `lua_prompts.md`
- `specs/lua_prompts.md` is a planning/spec artifact.
- It is used as implementation guidance, not as executable runtime code.

## Required Integration Path (Per Function)
1. Ensure parser lookup can resolve the function name to a `Function` enum variant in `base/src/functions/mod.rs`.
2. Ensure evaluation dispatch in `Model::evaluate_function` routes that variant to a concrete handler in `base/src/functions/mod.rs`.
3. Implement handler logic in the appropriate Rust module under `base/src/functions/`.
4. Add tests in `base/src/test/` (or relevant function test module) and verify behavior parity.
5. Update backlog tracking in `specs/reports/lua_backlog_status.csv`.

## Non-Goal
- Do not write standalone `.lua` runtime code for this repo unless a dedicated runtime integration plan is added first.
