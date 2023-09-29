#!/bin/bash
#  This script takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
