SHELL:=/usr/bin/env bash


.PHONY: help
help:
	@echo "........................................................"
	@echo "Author:     Likid Geimfari <likid.geimfari@gmail.com>"
	@echo "Repository: https://github.com/lk-geimfari/mimesis"
	@echo "........................................................"
	@echo ""
	@echo "Available options:"
	@echo "........................................................"
	@echo "clean-pyc    - remove Python file artifacts"
	@echo "clean-build  - remove build artifacts"
	@echo "clean        - remove build and Python file artifacts"
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


.PHONY: clean-build
clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive .cache/
	rm --force --recursive .mypy_cache/
	rm --force --recursive mimesis.egg-info/
	rm --force --recursive .benchmarks/


.PHONY: clean
clean: clean-pyc clean-build


.PHONY: test
test:
	py.test --benchmark-skip --color=yes ./


.PHONY: type-check
type-check:
	mypy mimesis/


.PHONY: benchmarks
benchmarks:
	py.test -rf --benchmark-only --benchmark-sort=MEAN ./benchmarks


.PHONY: publish
publish:
	python3 setup.py sdist && twine upload dist/*


.PHONY: style-check
style-check:
	py.test --flake mimesis/


.PHONY: version
version:
	python3 setup.py version


.PHONY: minify
minify:
	python3 setup.py minify


.PHONY: install
install:
	python3 setup.py install
