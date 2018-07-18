#!/usr/bin/env python3


# Declare second integer, double, and String variables.
i2 = 0
d2 = 0.0
s2 = ""

# Read and save an integer, double, and String to your variables.
i2 = int(input())
d2 = float(input())
s2 = input()

# Print the sum of both integer variables on a new line.
# Print the sum of the double variables on a new line.
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print("\n".join([str(i + i2), str(d + d2), s + s2]))
