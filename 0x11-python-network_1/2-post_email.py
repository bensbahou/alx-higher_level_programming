#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
"""


import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as res:
        print(res.read().decode("utf-8"))
