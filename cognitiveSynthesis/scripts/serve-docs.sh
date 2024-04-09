#!/usr/bin/env bash

PORT=8887
URL=http://localhost:${PORT}
DOCS_DIR="docs/_build/html"

open_in_browser() {
  if which gnome-open >/dev/null; then
    gnome-open ${URL}
  elif which open >/dev/null; then
    open ${URL}
  else
    echo "Could not detect the web browser."
  fi
}

serve_docs() {
  open_in_browser &
  python3 -m http.server ${PORT} -d ${DOCS_DIR}
}

if [ -d "${DOCS_DIR}" ]; then
  serve_docs
else
  make docs && serve_docs
fi
