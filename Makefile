ROOT=./

help:
	@echo "Project and maintainer:"
	@echo "\033[93m::::::::::::::::::::::::::::::::::::::::::::::::::::::::\033[0m"
	@echo "\033[92mAuthor:     Likid Geimfari <likid.geimfari@gmail.com>\033[0m"
	@echo "\033[92mPackage:    Mimesis\\033[0m"
	@echo "\033[92mRepository: https://github.com/lk-geimfari/mimesis\033[0m"
	@echo "\033[92mLicense:    MIT License\033[0m"
	@echo "\033[93m::::::::::::::::::::::::::::::::::::::::::::::::::::::::\033[0m"
	@echo ""
	@echo "Available options:"
	@echo "\033[93m::::::::::::::::::::::::::::::::::::::::::::::::::::::::\033[0m"
	@echo "\033[92mclean-pyc    - remove Python file artifacts\033[0m"
	@echo "\033[92mclean-build  - remove build artifacts\033[0m"
	@echo "\033[92mclean        - remove build and Python file artifacts\033[0m"
	@echo "\033[92mtest         - run tests quickly with the default Python\033[0m"
	@echo "\033[92mflake        - run py.test with flake8\033[0m"
	@echo "\033[92mrelease      - package and upload a release to PyPI\033[0m"
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
	py.test --verbose --color=yes $(ROOT)

flake:
	py.test --flake8

release:
	python3 setup.py register sdist upload -r pypi

install:
	python3 setup.py install
