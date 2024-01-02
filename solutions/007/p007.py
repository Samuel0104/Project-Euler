from eulerlib import time, isPrime
initial = time()

count = 1
ans = 1
while count < 10001:
    ans += 2
    if isPrime(ans):
        count += 1
print(ans)

final = time()
print(f"\nTime: {final-initial}")
