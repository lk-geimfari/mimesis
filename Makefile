SHELL:=/usr/bin/env bash


.PHONY: help
help:
	@echo "Available options:"
	@echo "........................................................"
	@echo "clean-pyc    - remove Python file artifacts"
	@echo "clean-build  - remove build artifacts"
	@echo "clean        - remove build and Python file artifacts"
	@echo "docs         - build Sphinx HTML documentation and open in browser"
	@echo "test         - run tests quickly with the default Python"
	@echo "type-check   - run mypy for checking types"
	@echo "benchmarks   - run benchmark tests for providers"
	@echo "publish      - create dist and upload package to PyPI"
	@echo "version      - update __version__ file"
	@echo "install      - install the package to the active Python's site-packages"
	@echo "........................................................"


.PHONY: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +


.PHONY: docs
docs:
	cd docs && make html


.PHONY: clean-build
clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf .cache/
	rm -rf .mypy_cache/
	rm -rf mimesis.egg-info/
	rm -rf .benchmarks/
	rm -rf .pytest_cache/


.PHONY: clean
clean: clean-pyc clean-build


.PHONY: test
test:
	py.test --benchmark-skip --color=yes ./
	mypy mimesis/ tests/


.PHONY: type-check
type-check:
	mypy mimesis/ tests/


.PHONY: benchmarks
benchmarks:
	py.test -rf --benchmark-only --benchmark-sort=MEAN ./benchmarks


.PHONY: publish
publish:
	python3 setup.py sdist bdist_wheel && twine upload dist/*
	clean


.PHONY: version
version:
	python3 setup.py version


.PHONY: minify
minify:
	python3 setup.py minify


.PHONY: install
install:
	python3 setup.py install
