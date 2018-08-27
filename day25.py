#!/usr/bin/env python3


import math


def is_prime(num):
    if num == 1:
        return "Not prime"
    sqrt = int(math.sqrt(num))
    for x in range(2, sqrt + 1):
        if num % x == 0:
            return "Not prime"
    return "Prime"


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        num = int(input())
        print(is_prime(num))
