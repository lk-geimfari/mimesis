#!/usr/bin/env bash

function install {
  virtualenv -p python3 venv
  source venv/bin/activate

  # Install stable release.
  pip install elizabeth
}

install
