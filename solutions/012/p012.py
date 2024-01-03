from eulerlib import time, numDivisors
initial = time()

ans = 1
grow = 1
while numDivisors(ans) <= 500:
    grow += 1
    ans += grow
print(ans)

final = time()
print(f"Time: {final-initial}")