#!/usr/bin/env python3


# Completes the solve function.
# n is the number of input strings, l is the list of input strings.
def solve(l):
    # For each string in the list of input strings.
    for s in l:
        l1 = []
        l2 = []
        # For each index of the current input string.
        for i in range(len(s)):
            l1.append(s[i]) if i % 2 == 0 else l2.append(s[i])
        print("{0} {1}".format("".join(l1), "".join(l2)))


if __name__ == "__main__":
    n = int(input())
    l = []
    for i in range(n):
        l.append(input())
    solve(l)
