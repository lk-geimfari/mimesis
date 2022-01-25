
.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  release    to create a release"
	@echo "  docs       to build documentations"
	@echo "  clean      to remove build artifacts"
	@echo "  format     to format code using Black and isort"
	@echo "  test       to run tests"
	@echo "  all        run pipeline format -> test -> docs -> clean"

.PHONY: all
all:
	make format
	make test
	make docs
	make clean

.PHONY: format
format:
	bash scripts/format.sh

.PHONY: docs
docs:
	bash scripts/docs.sh

.PHONY: clean
clean:
	bash scripts/clean.sh

.PHONY: release
release:
	bash scripts/release.sh

.PHONY: test
test:
	bash scripts/test.sh

.PHONY: update-deps
update-deps:
	poetry update