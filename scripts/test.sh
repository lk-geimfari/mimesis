#!/usr/bin/env bash

poetry run mypy mimesis
poetry run black mimesis tests --check --skip-string-normalization
poetry run pytest --cov=mimesis --cov-report=xml
poetry run pyroma -d .
