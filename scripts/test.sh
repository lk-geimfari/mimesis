#!/usr/bin/env bash

poetry run mypy mimesis
poetry run pytest --cov=mimesis --cov-report=xml --randomly-seed=$RANDOM
