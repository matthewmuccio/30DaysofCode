#!/usr/bin/env python3


import math
import os
import random
import re
import sys


# Complete the weird function below.
def weird(n):
	# If n is odd:
	if n % 2 == 1:
		print("Weird")
	# If n is even:
	else:
		if 2 <= n <= 5:
			print("Not Weird")
		elif 6 <= n <= 20:
			print("Weird")
		elif n > 20:
			print("Not Weird")
		else:
			print("Weird")


if __name__ == '__main__':
	N = int(input())
	weird(N)
