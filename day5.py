#!/usr/bin/env python3


import math
import os
import random
import re
import sys


# Completes the solve function.
def solve(n):
    for i in range(1, 11):
        print("{0} x {1} = {2}".format(n, i, n * i))


if __name__ == '__main__':
    n = int(input())
    solve(n)
