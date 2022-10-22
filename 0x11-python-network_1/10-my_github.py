#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    url = f"https://api.github.com/user"
    user_data = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2])).json()
    print(user_data.get('id'))
