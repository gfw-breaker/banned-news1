#!/bin/bash

org=$1
new=$2

mds=$(ls ../pages/*/*.md)

for md in $mds; do
	echo $md
	sed -i "s#news/tw520#blog/weihuo#g" $md
	sed -i "s#  中華民國第15任總統就職典禮#《伪火》- 天安门自焚真相#" $md
done




