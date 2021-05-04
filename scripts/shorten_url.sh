#!/bin/bash

url=$1

curl -i -s  https://git.io -F "url=$url" | grep Location | cut -d' ' -f2


