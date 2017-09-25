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
	@echo "flake        - run py.test with flake8"
	@echo "publish      - create dist and upload package to PyPI"
	@echo "versioner    - update __version__ file"
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


.PHONY: clean
clean: clean-pyc clean-build


.PHONY: flake
flake:
	py.test --flake8


.PHONY: test
test:
	py.test --verbose --color=yes ./


.PHONY: publish
publish:
	python3 setup.py sdist && twine upload dist/*


.PHONY: versioner
versioner:
	python3 setup.py versioner


.PHONY: install
install:
	python3 setup.py install
