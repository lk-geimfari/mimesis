#!/usr/bin/env bash

poetry run mypy mimesis
poetry run pytest --cov=mimesis --cov=pytest_plugin --cov-report=xml --randomly-seed=$RANDOM
