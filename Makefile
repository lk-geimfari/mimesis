LINT_CHECK=0

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  release    to create a release"
	@echo "  docs       to build documentations"
	@echo "  clean      to remove build artifacts"
	@echo "  format     to format code using autoformatters"
	@echo "  lint       to check code using autoformatters"
	@echo "  test       to run tests"
	@echo "  all        run pipeline format -> test -> docs -> clean"

.PHONY: all
all: format test docs clean

.PHONY: format
format:
	CHECK=$(LINT_CHECK) bash scripts/format.sh

.PHONY: docs
docs:
	bash scripts/docs.sh

.PHONY: clean
clean:
	bash scripts/clean.sh

.PHONY: release
release:
	uv build && uv publish

.PHONY: lint
lint: LINT_CHECK=1
lint: format
	@echo 'Lint finished'

.PHONY: test
test:
	bash scripts/test.sh

.PHONY: update-deps
update-deps:
	uv pip compile --group dev --upgrade
