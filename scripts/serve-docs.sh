#!/usr/bin/env bash

open_url() {
  open http://localhost:8888
}

serve_docs() {
  open_url & # Open the URL in the background
  python3 -m http.server 8888 -d docs/_build/html
}

if [ -d "docs/_build/html" ]; then
  serve_docs
else
  make docs && serve_docs
fi
