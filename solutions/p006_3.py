from eulerlib import time
initial = time()

"""
(1 + 2 + ... + n)^2 = 1^3 + 2^3 + ... + n^3
"""

sumOfSquares = sum(n**2 for n in range(101))
sumOfCubes = sum(n**3 for n in range(101))
print(sumOfCubes - sumOfSquares)

final = time()
print(f"\nTime: {final-initial}")