from eulerlib import time, isPrime
initial = time()

maxPrimes = 0
for a in range(-999, 1000):
    for b in range(-999, 1000, 2): # Only prime b's produce primes for n = 0
        n = 0
        while isPrime(n**2 + a*n + b):
            n += 1
        if n > maxPrimes:
            maxPrimes = n
            ans1 = a
            ans2 = b
print(ans1*ans2)

final = time()
print(f"Time: {final-initial}")