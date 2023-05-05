#!/usr/bin/env bash

PORT=8888
DOCS_DIR="docs/_build/html"

open_url() {
  open http://localhost:${PORT}
}

serve_docs() {
  open_url & # Open the URL in the background
  python3 -m http.server ${PORT} -d ${DOCS_DIR}
}

if [ -d "${DOCS_DIR}" ]; then
  serve_docs
else
  make docs && serve_docs
fi
