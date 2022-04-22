#!/usr/bin/python3
"""Python script that fetches intranet.hbtn.io/status"""
import requests
from sys import argv


if __name__ == "__main__":
	r = requests.get(argv[1])
	print(r.headers.get("X-Request-Id"))
