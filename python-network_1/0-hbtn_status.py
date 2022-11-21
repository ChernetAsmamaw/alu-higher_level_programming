#!/usr/bin/python3
''' fetch using urlib and a with statement '''


import urllib.request
'''imports urllib to fetch for URLs '''

with urllib.request.urlopen(https://alu-intranet.hbtn.io/status) as response:
   html = response.read()
