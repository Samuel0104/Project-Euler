from eulerlib import time, divisorSum
initial = time()

ans = 0
for i in range(1, 10000):
    j = divisorSum(i)
    if divisorSum(j) == i and i < j:
        ans += i + j
print(ans)

final = time()
print(f"Time: {final-initial}")