#!/bin/bash
#Bash script that takes in a URL as an argument, sends a GET
curl -sH "$1" GET "X-School-User-Id: 98"
