#!/usr/bin/env bash
set -euo pipefail

# Sphinx must run under the project Python (>=3.10). System Python 3.9
# cannot import mimesis because of PEP 604 union syntax (X | Y).
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

rm -rf docs/_build/

uv run sphinx-build -b html -d docs/_build/doctrees docs docs/_build/html
