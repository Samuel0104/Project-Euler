from eulerlib import time, isPrime
initial = time()

count = 1
n = 1
while count < 10001:
    n += 2
    if isPrime(n):
        count += 1
print(n)

final = time()
print(f"\nTime: {final-initial}")