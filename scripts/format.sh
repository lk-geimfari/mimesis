#!/usr/bin/env bash

set -e

# Pass `CHECK=1' to use this file in CI.
: ${CHECK:=''}

if [[ "$CHECK" == '0' ]]; then
  FORMAT=''  # 0 is semantically equivalent to ''
  LINT=''
fi
if [[ ! -z "$CHECK" ]]; then
  FORMAT='--check'
  LINT='--diff'
  echo 'Running lint check'
fi

uv run ruff check mimesis tests $LINT
uv run ruff format --quiet mimesis tests $FORMAT
