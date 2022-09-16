from eulerlib import time, isPrime
initial = time()

ans = 2
for i in range(3, 2000000, 2):
    if isPrime(i):
        ans += i
print(ans)

final = time()
print(f"\nTime: {final-initial}")