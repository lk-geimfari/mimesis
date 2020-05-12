SHELL:=/usr/bin/env bash

SEED = unspecified

ifneq ("$(SEED)", "unspecified")
RANDOM_SEED = --randomly-seed=$(SEED)
endif

.PHONY: help
help:
	@echo "Available options:"
	@echo "........................................................"
	@echo "clean-pyc      - remove Python file artifacts"
	@echo "clean-build    - remove build artifacts"
	@echo "clean          - remove build and Python file artifacts"
	@echo "docs           - build Sphinx HTML documentation and open in browser"
	@echo "test           - run tests quickly with the default Python"
	@echo "test SEED=last - rerun tests with identical seed for pytest-randomly"
	@echo "test SEED=1234 - run tests with specified seed for pytest-randomly"
	@echo "type-check     - run mypy for checking types"
	@echo "publish        - create dist and upload package to PyPI"
	@echo "install        - install the package to the active Python's site-packages"
	@echo "........................................................"


.PHONY: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +


.PHONY: clean-build
clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf .cache/
	rm -rf .mypy_cache/
	rm -rf .benchmarks/
	rm -rf .pytest_cache/
	rm -rf docs/_build
	rm -rf mimesis.egg-info/


.PHONY: clean
clean: clean-pyc clean-build


.PHONY: test
test:
	pytest --color=yes $(RANDOM_SEED) ./
	mypy mimesis/ tests/
	make clean


.PHONY: docs
docs:
	cd docs && make html


.PHONY: type-check
type-check:
	mypy mimesis/ tests/


.PHONY: publish
publish:
	python3 setup.py sdist bdist_wheel && twine upload dist/*
	clean


.PHONY: minify
minify:
	python3 setup.py minify


.PHONY: install
install:
	python3 setup.py install