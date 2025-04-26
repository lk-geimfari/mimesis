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

uv run isort mimesis tests $CHECK
uv run black mimesis tests $CHECK
uv run autoflake \
  --remove-all-unused-imports \
  --recursive \
  --remove-unused-variables \
  --in-place \
  --exclude=__init__.py \
  --quiet \
  mimesis tests $CHECK
