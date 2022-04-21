#!/bin/bash
#Bash script that takes in a URL, sends a POST
curl -s "$1" POST -Hd "email=test@gmail.com&subject=I will always be here for PLD"
