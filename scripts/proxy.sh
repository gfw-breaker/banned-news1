#!/bin/bash

if [ $# -ne 1 ]; then
	echo "Please specify channel..."
	exit 1
fi

pages=$(ls ../indexes/$1*.md)

for p in $pages; do
	cat template.md > $p
done

