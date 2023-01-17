#!/usr/bin/python3

"""
Python script that takes 2 arguments in order to solve the given challenge
"""

import requests
import sys

if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],sys.argv[1])
    r = requests.get(url)
    c = r.json()
    for i in c[:10]:
        print(i.get('sha'), end=': ')
        print(i.get('commit').get('author').get('name'))

