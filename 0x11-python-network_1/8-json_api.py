#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    res = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        res = res.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
