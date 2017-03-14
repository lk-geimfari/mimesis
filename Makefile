ROOT=./

VERSION = 0.3.22
PROJECT_NAME = Elizabeth
REPOSITORY_URL = https://github.com/lk-geimfari/elizabeth

help:
	@echo "Project and maintainer:"
	@echo "\033[93m::::::::::::::::::::::::::::::::::::::::::::::::::::::::\033[0m"
	@echo "\033[92mAuthor:     Likid Geimfari <likid.geimfari@gmail.com>\033[0m"
	@echo "\033[92mPackage:    $(PROJECT_NAME) $(VERSION)\\033[0m"
	@echo "\033[92mRepository: $(REPOSITORY_URL)\033[0m"
	@echo "\033[92mLicense:    MIT License\033[0m"
	@echo "\033[93m::::::::::::::::::::::::::::::::::::::::::::::::::::::::\033[0m"
	@echo ""
	@echo "Available options:"
	@echo "\033[93m::::::::::::::::::::::::::::::::::::::::::::::::::::::::\033[0m"
	@echo "\033[92mclean-pyc    - remove Python file artifacts\033[0m"
	@echo "\033[92mclean-build  - remove build artifacts\033[0m"
	@echo "\033[92mclean        - remove build and Python file artifacts\033[0m"i
	@echo "\033[92mtest         - run tests quickly with the default Python\033[0m"
	@echo "\033[92mtest-travis  - run tests for Travis CI\033[0m"
	@echo "\033[92mtest-files   - internal files for development\033[0m"
	@echo "\033[92mrelease      - package and upload a release to PyPI\033[0m"
	@echo "\033[92mrelease-test - upload package to PyPI Test\033[0m"
	@echo "\033[92minstall      - install the package to the active Python's site-packages\033[0m"
	@echo "\033[93m::::::::::::::::::::::::::::::::::::::::::::::::::::::::\033[0m"

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive .cache/

clean: clean-pyc clean-build

test:
	py.test --cov=elizabeth/ --cov-report=term-missing  --verbose --color=yes $(ROOT)

test-travis:
	py.test --cov=elizabeth/

test-files:
	touch file.txt file.json

release:
	python3 setup.py register sdist upload -r pypi

release-test:
	python3 setup.py sdist upload -r pypitest

install:
	python3 setup.py install

minify-json:
	gulp json
