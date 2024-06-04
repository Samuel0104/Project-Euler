from eulerlib import time, isPandig
initial = time()

"""
The concatenated product of any number in the search
range and (1, 2) always has nine digits.
"""

for n in range(9876, 9182, -1):
    p = str(n) + str(2*n)
    if isPandig(p):
        ans = int(p)
        break
print(ans)

final = time()
print(f"Time: {final-initial}")