#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
"""
import sys
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as res:
        print(dict(res.headers).get("X-Request-Id"))
