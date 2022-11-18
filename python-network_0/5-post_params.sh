#!/bin/bash
# takes a URL, sends a POST and displays body
curl -s "$1" -X POST -d "email=c.asmamaw@alustudent.com&subject=I will always be here for PLD"
