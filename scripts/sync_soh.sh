#!/bin/bash
# author: gfw-breaker

channels="3 4 5 6 7 55 186 59"

## create dirs
for channel in $channels ; do
	mkdir -p ../pages/soh$channel
done
	
## get feeds files
for channel in $channels ; do
	url="https://www.soundofhope.org/rss/$channel"
	wget -q $url -O "soh$channel.xml"
	echo "getting channel: $url"
	python parse_soh.py "soh$channel"
done


