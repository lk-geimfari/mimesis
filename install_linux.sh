#!/usr/bin/env bash

SUPPORTED_PYTHON=python3

function install {
  virtualenv -p $SUPPORTED_PYTHON venv
  source venv/bin/activate

  # Install stable release.
  pip install elizabeth
}

install
