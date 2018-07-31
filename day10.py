#!/usr/bin/env python3


import math
import os
import random
import re
import sys


if __name__ == '__main__':
	n = int(input().strip())
	nums = str(bin(n)[2:]).split('0')
	lens = [len(num) for num in nums]
	print(max(lens))
