#!/bin/bash

org=$1
new=$2

mds=$(ls ../pages/*/*.md)

for md in $mds; do
	echo $md
	sed -i "s#banned-news3/blob/master/pages/link4.md#links/blob/master/banned.md#g" $md
done




#sed -i "s#$org#$new#g" /nogfw/README.md

