#!/usr/bin/python

import math
from prettytable import PrettyTable

# method to return Tserial
def Tserial(n):
    return pow(n, 2)

# method to return Tparallel
def Tparallel(n, p):
    return pow(n, 2)/p + math.log(p, 2)

# method to calculate speedup
def speedup(n, p):
    return round(Tserial(n)/Tparallel(n, p), 4)

# method to calculate efficiency
def efficiency(n, p):
    return round(Tserial(n)/(p * Tparallel(n, p)), 4)

# init the values used for the problem
n_values = [10, 20, 40, 80, 160, 320]
p_values = [1, 2, 4, 8, 16, 32, 64, 128]

# init the pretty tables that will output the data
speed = PrettyTable(['p\\n', '10', '20', '40', '80', '160', '320'])
eff = PrettyTable(['p\\n', '10', '20', '40', '80', '160', '320'])

# create the tables
for p in p_values:
    # init the rows with the current p value
    speed_row = [p]
    eff_row = [p]

    # calculate all speed/eff values for each n and current p and add them to row
    for n in n_values:
        speed_row.append(speedup(n, p))
        eff_row.append(efficiency(n, p))

    # add the completed rows to the table
    speed.add_row(speed_row)
    eff.add_row(eff_row)

# print the completed tables
print("Speed table:")
print(speed)
print("\nEfficiency table:")
print(eff)
