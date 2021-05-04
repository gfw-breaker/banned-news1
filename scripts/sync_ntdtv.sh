#!/bin/bash
# author: gfw-breaker

channels="prog1695 prog1138 prog204 prog203 prog202 prog424 prog647 prog1699"

## create dirs
for channel in $channels ; do
	mkdir -p ../pages/$channel
done
	
## get feeds files
for channel in $channels ; do
	url="https://www.ntdtv.com/gb/$channel"
	echo "getting channel: $url"
	python parse_ntdtv.py $channel "$url"
done


