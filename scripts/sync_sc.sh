#!/bin/bash
# author: gfw-breaker

channels="p1 p2 p3 p4 p5 p6 p7 p8 p9"

## create dirs
for channel in $channels ; do
	mkdir -p ../pages/$channel
done
	
## get feeds files
for channel in $channels ; do
	url="http://www.secretchina.com/news/gb/$channel.xml"
	echo "getting channel: $url"
	wget -q $url -O $channel.xml
	python parse_sc.py $channel

	for f in $(ls ../pages/$channel/*.md); do
		sed -i '/看中国网站 禁止建立鏡像網站/d' $f
	done
done


