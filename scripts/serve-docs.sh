#!/usr/bin/env bash

serve_docs() {
  python3 -m http.server 8888 -d docs/_build/html
}

if [ -d "docs/_build/html" ]; then
  serve_docs
else
  make docs && serve_docs
fi
