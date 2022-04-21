#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL
curl -I "$1" 2>/dev/null | cut -d ' ' -f2 | tail -2
