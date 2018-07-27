#!/usr/bin/env python3


import sys


try:
    S = input().strip()
    result = int(S)
except (TypeError, ValueError):
    result = "Bad String"
print(result)
