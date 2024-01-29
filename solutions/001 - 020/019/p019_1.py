from eulerlib import time
initial = time()

months = []
for year in range(1901, 2001):
    if (year%4 == 0 and year%100 != 0) or year%400 == 0: # Conditions for a leap year
        months.extend((31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))
    else:
        months.extend((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))
        
day = 2 # Tuesday (1 Jan 1900)
sundays = 0
for i in months:
    day = (day + i)%7
    if day == 0:
        sundays += 1
print(sundays)

final = time()
print(f"Time: {final-initial}")