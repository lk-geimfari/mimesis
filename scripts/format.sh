#!/usr/bin/env bash

set -e

# Pass `CHECK=1' to use this file in CI.
: ${CHECK:=''}

if [[ "$CHECK" == '0' ]]; then
  CHECK=''  # 0 is semantically equvivalent to ''
fi
if [[ ! -z "$CHECK" ]]; then
  CHECK='--check'
  echo 'Running lint check'
fi

poetry run isort mimesis tests $CHECK
poetry run black mimesis tests $CHECK
poetry run autoflake \
  --remove-all-unused-imports \
  --recursive \
  --remove-unused-variables \
  --in-place \
  --exclude=__init__.py \
  --quiet \
  mimesis tests $CHECK
