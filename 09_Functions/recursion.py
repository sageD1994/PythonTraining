#!/usr/bin/env python3

def faculty(n):
    if n <= 1: return 1
    else: return n * (faculty(n-1))

result = faculty(6)
print(result)