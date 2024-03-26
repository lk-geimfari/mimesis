#!/usr/bin/env bash

poetry run mypy mimesis
poetry run pytest --cov=mimesis --cov=mimesis_pytest_plugin --cov-report=xml --randomly-seed=$RANDOM
