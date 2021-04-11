#!/usr/bin/env bash

poetry run isort mimesis tests --force-single-line-imports
poetry run autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place mimesis tests --exclude=__init__.py
poetry run black mimesis tests
