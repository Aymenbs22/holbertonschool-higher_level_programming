#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods
curl -sX OPTIONS "$1" -i | grep Allow | cut -d " " -f2-
