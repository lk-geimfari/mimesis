#!/usr/bin/env bash

set -e

# Pass `CHECK=1' to use this file in CI.
: ${CHECK:=''}

if [[ "$CHECK" == '0' ]]; then
  CHECK=''  # 0 is semantically equivalent to ''
fi

TARGETS=(mimesis tests tasks/minifier.py)

if [[ -n "$CHECK" ]]; then
  echo 'Running lint check'
  uv run ruff check "${TARGETS[@]}"
  uv run ruff format --check "${TARGETS[@]}"
else
  uv run ruff check --fix "${TARGETS[@]}"
  uv run ruff format "${TARGETS[@]}"
fi
