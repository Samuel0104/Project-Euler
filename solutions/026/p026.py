from eulerlib import time, nextPrime
initial = time()

"""
If p is a prime other than 2 or 5, the length of the
recurring cycle of 1/p is equal to the multiplicative
order of 10 modulo p.
"""

p = 7
maxLen = 0
while p < 1000:
    k = 1
    while (10**k)%p != 1:
        k += 1
    if k > maxLen:
        maxLen = k
        ans = p
    p = nextPrime(p)
print(ans)

final = time()
print(f"Time: {final-initial}")