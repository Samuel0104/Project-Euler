from eulerlib import time
initial = time()

"""
The only century in the desired range is 2000, but it's
divisible by 400 so we don't check the century condition
"""

common = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
leap = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

day = 2 # Tuesday (1 Jan 1900)
sundays = 0
for year in range(1901, 2001):
    for month in range(12):
        if year%4 != 0:
            day += common[month]
        else:
            day += leap[month]
        if day%7 == 0:
            sundays += 1
print(sundays)

final = time()
print(f"Time: {final-initial}")