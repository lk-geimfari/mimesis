#!/usr/bin/env bash

MARKDOWN_FILES=*.md
for f in $MARKDOWN_FILES
do
  filename="${f%.*}"
  echo "Converting $f to $filename.rst"
  `pandoc $f -t rst -o $filename.rst`
done
