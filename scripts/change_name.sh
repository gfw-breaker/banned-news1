#!/bin/bash

oldRepo="$1"
newRepo="$2"

if [ $# -ne 2 ]; then
	echo "exiting..."
	exit 1
fi


mds=$(ls ../pages/*/*.md)
for md in $mds; do
	echo $md
	sed -i "s#$oldRepo#$newRepo#g" $md
done

mds=$(ls ../indexes/*.md)
for md in $mds; do
	echo $md
	sed -i "s#$oldRepo#$newRepo#g" $md
done

sed -i "s#$oldRepo#$newRepo#g" macros.py

ln -s "/$oldRepo" "/$newRepo"

