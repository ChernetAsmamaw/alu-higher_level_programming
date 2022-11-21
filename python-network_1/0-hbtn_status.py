#!/usr/bin/python3
"""Python script that fetches https://alu-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request as request
    with request.urlopen('https://alu-intranet.hbtn.io/status') as page:
        html = page.read()
        print('Body response:')
        print("\t- type:" type(html))
        print("\t- content:" html)
        print("\t- utf8 content:" html)
