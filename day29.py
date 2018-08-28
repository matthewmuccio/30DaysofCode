#!/usr/bin/env python3


if __name__ == '__main__':
    n = int(input().strip())
    for _ in range(n):
        i, k = map(int, input().split())
        print(k - 1 if ((k - 1) | k) <= i else k - 2)
