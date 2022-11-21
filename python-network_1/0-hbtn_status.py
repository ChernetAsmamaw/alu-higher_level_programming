#!/usr/bin/python3
""" Python script that fetches https://alu-intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status')\ as request:
        information = request.read()
        print("Body response:")
        print("\t- type:", type(information))
        print("\t- content:", information)
        print("\t- utf8 content:", str(information)[2:-1])
