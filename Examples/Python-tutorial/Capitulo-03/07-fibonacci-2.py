#!/usr/bin/env python3

a, b = 0, 1
while a < 10:
    print(a, end=",")
    a, b = b, a+b

print()
