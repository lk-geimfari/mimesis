#!/usr/bin/env bash

uv run mypy mimesis
uv run pytest --cov=mimesis --cov-report=xml --randomly-seed=$RANDOM
