#!/bin/bash

org=$1
new=$2

mds=$(ls ../pages/*/*.md)

for md in $mds; do
	echo $md
	sed -i "s/31:8000/31:8808/g" $md
done




