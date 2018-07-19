#!/usr/bin/env python3


import math
import os
import random
import re
import sys


# Completes the solve function.
# arr is the array with n elements.
def solve(arr):
    print(" ".join(map(str, arr[::-1])))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    solve(arr)
