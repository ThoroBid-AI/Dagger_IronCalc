#!/usr/bin/env bash
set -euo pipefail

BACKLOG_FILE="specs/planning/lua_implementation_backlog.md"
SPEC_DIR="specs/functions"

if command -v rg >/dev/null 2>&1; then
  SEARCH_BIN="rg"
else
  SEARCH_BIN="grep"
fi

FUNCTIONS=()
while IFS= read -r fn; do
  FUNCTIONS+=("$fn")
done < <(
  awk '
    /^## Backlog \(Grouped\)/ { in_backlog = 1; next }
    /^## Execution Checklist/ { in_backlog = 0 }
    in_backlog && /^- `/ {
      line = $0
      sub(/^- `/, "", line)
      sub(/`.*/, "", line)
      print line
    }
  ' "$BACKLOG_FILE"
)

if [[ ${#FUNCTIONS[@]} -eq 0 ]]; then
  echo "error: no backlog functions found in $BACKLOG_FILE"
  exit 1
fi

failures=0

for fn in "${FUNCTIONS[@]}"; do
  spec_file="$SPEC_DIR/$fn.md"
  if [[ ! -f "$spec_file" ]]; then
    echo "missing spec file: $spec_file"
    failures=1
    continue
  fi

  if [[ "$SEARCH_BIN" == "rg" ]]; then
    hits=$(rg -n "TBD|<category>" "$spec_file" || true)
  else
    hits=$(grep -nE "TBD|<category>" "$spec_file" || true)
  fi
  if [[ -n "$hits" ]]; then
    echo "placeholder metadata found: $spec_file"
    echo "$hits"
    failures=1
  fi
done

if [[ $failures -ne 0 ]]; then
  echo "backlog spec validation failed"
  exit 1
fi

echo "backlog spec validation passed (${#FUNCTIONS[@]} functions checked)"
