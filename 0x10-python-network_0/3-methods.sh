#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods
curl -sX OPTIONS www.example.org -i | grep Allow | cut -d " " -f2-
