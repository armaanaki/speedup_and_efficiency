#!/usr/bin/python

import math

# method to return Tserial
def Tserial(n):
    return pow(n, 2)

# method to return Tparallel
def Tparallel(n, p):
    return pow(n, 2)/p + math.log(p, 2)

# method to calculate speedup
def speedup(n, p):
    return Tserial(n)/Tparallel(n, p)

# method to calculate efficiency
def efficiency(n, p):
    return Tserial(n)/(p * Tparallel(n, p))

print("Speedup: " + str(speedup(10, 1)))
print("Speedup: " + str(speedup(10, 2)))
