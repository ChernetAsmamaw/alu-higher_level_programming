#!/usr/bin/python3
""" Scrip that takes URL, sends request and displays\ value X-Request-Id variable found in the header of the response"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as request:
            print(request.info().get('X-Request-Id'))
