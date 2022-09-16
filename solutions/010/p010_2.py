from eulerlib import time, isPrime
initial = time()

print(2 + sum(n for n in range(3, 2*10**6, 2) if isPrime(n)))

final = time()
print(f"\nTime: {final-initial}")