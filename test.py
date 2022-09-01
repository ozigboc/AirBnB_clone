#!/usr/bin/python3
import math


def binary_search(f, domain, MAX=1000):
    start, end = domain
    if start >= end:
        raise ValueError("Domain is empty")
    mid = (start + end) / 2
    fmid = f(mid)
    step = 0
    while abs(fmid) > 0.0001 and step < MAX:
        if fmid < 0:
            start = mid
        else:
            end = mid
        mid = (start + end) / 2
        fmid = f(mid)
        step += 1
        MAX -= 1
    return round(mid, 2)


def f(x): return (math.sin(x)**2)*(x**2)-2


domain = (2, 3)
x = binary_search(f, domain)
print(x)
