.PHONY: help
help:
	@echo "Available options:"
	@echo "........................................................"
	@echo "clean          - remove artefacts"
	@echo "test           - run tests quickly with the default Python"
	@echo "test SEED=last - rerun tests with identical seed for pytest-randomly"
	@echo "test SEED=1234 - run tests with specified seed for pytest-randomly"
	@echo "type-check     - run mypy for checking types"
	@echo "release        - create dist and upload package to PyPI"
	@echo "........................................................"


.PHONY: clean
clean: bash scripts/clean.sh

.PHONY: test
test: bash scripts/test.sh

.PHONY: publish
publish: bash scripts/release.sh

