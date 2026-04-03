#!/usr/bin/env bash

set -e

# Pass `CHECK=1' to use this file in CI.
: ${CHECK:=''}

if [[ "$CHECK" == '0' ]]; then
  CHECK=''  # 0 is semantically equivalent to ''
fi
if [[ ! -z "$CHECK" ]]; then
  CHECK='--check'
  echo 'Running lint check'
fi

uv run ruff check mimesis tests $CHECK
uv run ruff format --quiet mimesis tests $CHECK
