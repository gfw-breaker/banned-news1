#!/bin/bash
# author: gfw-breaker

channels="nf4514 nsc415 nsc412 nsc413 nsc418 nsc423 nsc422 nsc993 nsc424"

## create dirs
for channel in $channels ; do
	mkdir -p ../pages/$channel
done
	
## get feeds files
for channel in $channels ; do
	url="https://www.epochtimes.com/gb/$channel.xml"
	wget -q --no-check-certificate $url -O $channel.xml
	sed -i 's/content:encoded/content/g' $channel.xml
	echo "getting channel: $url"
	python parse_epoch.py $channel
done


