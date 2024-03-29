#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter
"""

if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.parse
    values = {}
    values['email'] = sys.argv[2]
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
