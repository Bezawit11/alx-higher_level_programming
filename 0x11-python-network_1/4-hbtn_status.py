#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import requests
    r = requests.get('https://alx-intranet.hbtn.io/status')
    a = r.text
    print("Body response:")
    print("\t- type: {}".format(type(a)))
    print("\t- content: {}".format(a))
