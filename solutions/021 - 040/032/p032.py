from eulerlib import time, isPandig
initial = time()

"""
2398 is the greatest m such that 4 x m has four digits and
79 is the greatest n such that 123 x n has four digits
"""

pands = set()
for a in range(4, 80):
    for b in range(123, 2399): 
        n = a*b
        if len(str(n)) == 4:
            string = str(a) + str(b) + str(n)
            if isPandig(string):
                pands.add(n)
print(sum(pands))

final = time()
print(f"Time: {final-initial}")