#!/usr/bin/env python3


ad, am, ay = [int(x) for x in input().split(" ")]
ed, em, ey = [int(x) for x in input().split(" ")]

if (ay, am, ad) <= (ey, em, ed):
    print(0)
elif (ay, am) == (ey, em):
    print(15 * (ad - ed))
elif ay == ey:
    print(500 * (am - em))
else:
    print(10000)
