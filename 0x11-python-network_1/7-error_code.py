#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the 
URL and displays the body of the response.
"""

if __name__ == '__main__':
    import requests
    import sys
    try:
        r = requests.get(sys.argv[1])
        print(r.text)
    except requests.exceptions.RequestException as e:
        print(f"Error code: {e.status_code}")
