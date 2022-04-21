#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL
curl -LI "$1" -o /dev/null -w '%{size_download}\n' -s
