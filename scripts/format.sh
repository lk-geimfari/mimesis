#!/usr/bin/env bash

poetry run black mimesis tests
poetry run isort mimesis tests
poetry run autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place mimesis tests --exclude=__init__.py
