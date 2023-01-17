#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the 
URL and displays the body of the response.
"""

if __name__ == '__main__':
    import requests
    import sys
    r = requests.get(sys.argv[1])
    a =  r.status_code
    if a >= 400:
        print(f"Error code: {a}")
    else:
        print(r.text)
