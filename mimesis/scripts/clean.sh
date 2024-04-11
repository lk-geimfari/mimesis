#!/usr/bin/env bash

find . -name '*.pyc' -exec rm -f {} +
find . -name '*.pyo' -exec rm -f {} +
find . -name '*~' -exec rm -f {} +
find . -name '__pycache__' -exec rm -fr {} +
rm -rf build/ dist/ .cache/ .mypy_cache/ .pytest_cache/ .benchmarks/ docs/_build mimesis.egg-info/ .ipynb_checkpoints/ .ruff_cache/
rm -f .coverage coverage.xml
