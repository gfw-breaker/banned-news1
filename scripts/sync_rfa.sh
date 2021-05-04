#!/bin/bash
# author: gfw-breaker

channelMap="yataibaodao:yataibaodao
zhongguoyizhou:zhuanlan/zhongguoyizhou
zhongguotoushi:zhuanlan/zhongguotoushi
guojishijiao:guojishijiao
yehuazhongnanhai:zhuanlan/yehuazhongnanhai
butongdeshengyin:zhuanlan/butongdeshengyin
pinglun:pinglun"

## get feeds files
for entry in $channelMap ; do
	channel=$(echo $entry | cut -d':' -f1)
	category=$(echo $entry | cut -d':' -f2)
	mkdir -p ../pages/$channel
	url="https://www.rfa.org/mandarin/$category/rss2.xml"
	echo "getting channel: $url"
	wget -q "$url" -O $channel.xml
	sed -i 's/content:encoded/content/g' $channel.xml
	python parse_rfa.py $channel
done



