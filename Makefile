ROOT=./

help:
	@echo "clean-pyc    - remove Python file artifacts"
	@echo "clean-build  - remove build artifacts"
	@echo "test         - run tests quickly with the default Python"
	@echo "travis-test  - run tests for Travis CI"
	@echo "test-files   - internal files for development"
	@echo "release-test - upload package to PyPI Test"
	@echo "release      - package and upload a release to PyPI"
	@echo "install      - install the package to the active Python's site-packages"

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/

test:
	py.test --cov=elizabeth/ --cov-report=term-missing  --verbose --color=yes $(ROOT)

travis-test:
	py.test --cov=elizabeth/

test-files:
	touch file.txt file.json

release-test:
	python3 setup.py sdist upload -r pypitest

release:
	python3 setup.py register sdist upload -r pypi

install:
	python3 setup.py install
